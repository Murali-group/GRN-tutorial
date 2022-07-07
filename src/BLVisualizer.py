#!/usr/bin/env python
# coding: utf-8

import os
import sys
import yaml
import argparse
import itertools
import numpy as np
import pandas as pd
from graphspace_python.api.client import GraphSpace
from graphspace_python.graphs.classes.gsgraph import GSGraph
import uuid

# local imports
import BLEval as ev

def get_parser() -> argparse.ArgumentParser:
    '''
    :return: an argparse ArgumentParser object for parsing command
        line parameters
    '''
    parser = argparse.ArgumentParser(
        description='Generate GraphSpace networks from GRN inference results.')

    parser.add_argument('-c','--config', default='config.yaml',
        help="Configuration file containing list of datasets "
              "algorithms and output specifications.\n")

    parser.add_argument('-a', '--algorithm', default='rankedEdges.csv',
        help="Name of algorithm specified in config for which to generate GRN.\n")
    
    parser.add_argument('-d', '--dataset', default='rankedEdges.csv',
        help="Name of dataset specified in config for which to generate GRN.\n")

    parser.add_argument('-t', '--threshold', default=0.5,
        help="EdgeWeight threshold above which to add edges to GRN.\n")

    return parser

def parse_arguments():
    '''
    Initialize a parser and use it to parse the command line arguments
    :return: parsed dictionary of command line arguments
    '''
    parser = get_parser()
    opts = parser.parse_args()

    return opts

red = "#8B0000"
blue = "#4169E1"
white = "#FFFFFF"
gray = "#7f8184"
black = '#000000'


default_node_styles = {
    'background-color': white,
    'color': black,
    'border-color': black,
    'shape': 'ellipse',
    'width': 50,
    'height': 50,
    }

act_edge_style = {
    'color': blue,
    'width': 3,
    'opacity': 0.6,
    'target-arrow-shape': 'triangle',
    }

inhib_edge_style = {
    'color': red,
    'width': 3,
    'opacity': 0.6,
    }

def post_graph_to_graphspace(G, username, password, graph_name, make_public=None):
    """
    Post a graph to graphspace and perform other layout and sharing tasks
    *G*: Costructed GSGraph object
    *username*: GraphSpace username 
    *password*: GraphSpace password 
    *graph_name*: Name to give to graph when posting. If a graph with that name already exists, it will be updated
    *make_public*: Make the graph public
    """
    # post to graphspace
    gs = GraphSpace(username, password)
    #print("\nPosting graph '%s' to graphspace\n" % (graph_name))
    gs_graph = gs.get_graph(graph_name, owner_email=username)

    if gs_graph is None:
        print("\nPosting graph '%s' to graphspace\n" % (graph_name))
        G.set_name(graph_name)
        gsgraph = gs.post_graph(G)
    else:
        # "re-post" or update the graph 
        print("\nGraph '%s' already exists. Updating it\n" % (graph_name))
        gsgraph = gs.update_graph(G, graph_name=graph_name, owner_email=username)
    if make_public is True:
        print("Making graph '%s' public." % (graph_name))
        gsgraph = gs.publish_graph(graph=G)
    
    print(gsgraph.url)

def constructGraph(edges, node_labels={}, graph_attr={}, popups={}, edge_dirs={}):
    """
    Posts the set of edges to graphspace

    *edges*: set of edges to post 
    *graph_attr*: optional dictionary containing styles for nodes and edges. For example:
        n1: {color: red, border_width: 10}
        n1-n2: {line-color: blue}
    *node_labels*: optional dictionary containing the desired label for each node
    *popups*: optional dictionary containing html popups for nodes and edges 
    *edge_dirs*: optional dictionary specifying if an edge is directed (True) or not (False). Default is not directed (False)

    returns the constructed GSGraph
    """

    G = GSGraph()
    
    nodes = set([t for t,h in edges]).union(set([h for t,h in edges]))

    # GSGraph does not allow adding multiple nodes with the same name.
    # Use this set to make sure each node has a different gene name.
    labels_added = set()

    ## add GraphSpace/Cytoscape.js attributes to all nodes.
    for n in nodes:
        # this dictionary will pass along any extra parameters that are not usually handled by GraphSpace
        attr_dict = {}

        # if there is no popup, then have the popup just be the node name
        node_popup = popups.pop(n, n)
        # leave the gene name as the node ID if there are no node_labels provided
        node_label = node_labels.pop(n,n)

        node_labels[n] = node_label
        labels_added.add(node_label)

        G.add_node(node_label, attr_dict=attr_dict, popup=node_popup, label=node_label)

        
        attr_dict = default_node_styles
        
        #border_color = "#7f8184"  # slightly darker grey
        #shape = 'ellipse'
        #color = '#D8D8D8'  # grey - background-color
        #border_style = 'solid'
        #width = 45
        #height = 45
        #border_width = 2
        #bubble = None  # default is the node color
        if n in graph_attr:
            # any attribute can be set in the graph_attr dict and the defaults will be overwritten
            for style in graph_attr[n]:
                # for some reason, the text color is updated with this color... 
                if style == 'color':
                    continue
                attr_dict[style] = graph_attr[n][style]
                
        if 'border-color' not in attr_dict:
            attr_dict['border-color'] = attr_dict['color'] 
        
        # I updated the bubble function in graphspace_python gsgraph.py so it wouldn't overwrite the border color.
        #bubble = color if bubble is None else bubble

        G.add_node_style(node_label, shape=attr_dict['shape'] , attr_dict=attr_dict, color=attr_dict['color'] , width=attr_dict['width'],
                        height=attr_dict['height'])

    # Add all of the edges and their Graphspace/Cytoscape.js attributes
    for (u,v) in edges:
        # if there is no popup, then have the popup just be the edge name
        edge_popup = popups.pop((u,v), "%s-%s" % (u,v))
        directed = edge_dirs.pop((u,v), True)
        # TODO directed vs undirected edges into an option
        G.add_edge(node_labels[u],node_labels[v],directed=directed,popup=edge_popup)

        # edge style defaults:
        attr_dict = act_edge_style = {
            'color': blue,
            'width': 3,
            'opacity': 0.6,
            'target-arrow-shape': 'triangle',
        }
        #color = "#D8D8D8"  # in the attr_dict, this is 'line-color'
        if (u,v) in graph_attr:
            # any attribute can be set in the graph_attr dict and the defaults will be overwritten
            for style in graph_attr[(u,v)]:
                attr_dict[style] = graph_attr[(u,v)][style]
            if 'color' in graph_attr[(u,v)]:
                color = graph_attr[(u,v)]['color']

        #print(width, color, arrow_shape, edge_style)
        G.add_edge_style(node_labels[u], node_labels[v], attr_dict=attr_dict,
                         directed=directed, color=attr_dict['color']) 
    return G

def main():
    opts = parse_arguments()
    config_file = opts.config

    evalConfig = None

    with open(config_file, 'r') as conf:
        evalConfig = ev.ConfigParser.parse(conf)
      
    df = pd.read_csv(str(evalConfig.output_settings.base_dir) + '/' \
                              + str(evalConfig.input_settings.datadir).split("inputs")[1] + '/' \
                              + opts.dataset + '/' + opts.algorithm + '/rankedEdges.csv', sep='\t')
    
    #min max scale edge weights
    df['EdgeWeight'] = (df['EdgeWeight']-df['EdgeWeight'].min())/(df['EdgeWeight'].max()-df['EdgeWeight'].min())
    #select edges above edge weight threshold
    edges = [(e['Gene1'], e['Gene2']) for i, e in df.iterrows() if e['EdgeWeight'] > float(opts.threshold)]
    
    G = constructGraph(edges)
    graph_name = 'ISMB 2022 GRN Tutorial ' + opts.algorithm + ' ' + opts.dataset + ' Network '+ uuid.uuid4().hex
    post_graph_to_graphspace(G, "ISMB2022GRNTutorial@gmail.com", "ISMB2022GRNTutorial", graph_name, make_public=True)

if __name__ == '__main__':
  main()