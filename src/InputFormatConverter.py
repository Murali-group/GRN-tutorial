import pandas as pd
import argparse
import os

# Usage: python InputFormatConverter.py --mode [tenet-to-beeline | beeline-to-tenet] --exprsn_data <path-to>/expression_dataTuck.csv --pseudo_time <path-to>/pseudotimeTuck.txt --output_dir <path-to>/output


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate input data files from TENET supported format in BEELINE supported format.")
    parser.add_argument("-m", "--mode", help="choose a mode from [tenet-to-beeline | beeline-to-tenet]. Only 'tenet-to-beeline' is currently supported.")
    parser.add_argument("-e", "--exprsn_data", help="absolute path to expression-data file in TENET supported format.\n")
    parser.add_argument("-p", "--pseudo_time", help="absolute path to pseudo-time data file in TENET supported format.\n")
    parser.add_argument("-o", "--output_dir", help="absolute path to output directory.\n")

    return parser


def generate_expression_data_file(expression_data_filepath, expression_data_output_filepath):
    # generate expression data file
    expression_data_df = pd.read_csv(expression_data_filepath, header=0, index_col=0)
    cell_names = list(expression_data_df.index.values)
    print(expression_data_df.head(5))
    print(f"Cell Names = {cell_names}")
    print(f"Cell Names count = {len(cell_names)}")

    expression_data_df_transpose = expression_data_df.T
    expression_data_df_transpose.index = expression_data_df_transpose.index.str.upper()
    expression_data_df_transpose.columns = expression_data_df_transpose.columns.str.upper()
    print(f"Writing expression data file at {expression_data_output_filepath}")

    expression_data_df_transpose.to_csv(expression_data_output_filepath)
    return cell_names


def generate_pseudo_time_file(pseudo_time_filepath, pseudo_time_output_filepath, cell_names):
    # generate pseudo time file
    pseudo_time_file = open(pseudo_time_filepath, "r")
    pseudo_time_list = pseudo_time_file.readlines()
    pseudo_time_list = [float(x.strip()) for x in pseudo_time_list]
    # print(pseudo_time_list)
    pseudo_time_df = pd.DataFrame(list(zip(cell_names, pseudo_time_list)), columns=["", "PseudoTime"])
    pseudo_time_df.set_index("", inplace=True)
    pseudo_time_df.index = pseudo_time_df.index.str.upper()
    print(f"Writing pseudo time file at {pseudo_time_output_filepath}")
    pseudo_time_df.to_csv(pseudo_time_output_filepath)


def tenet_to_beeline_conversion(expression_data_filepath, pseudo_time_filepath, output_dir):
    # create the mTuck directory within the output directory folder
    output_dir_path = os.path.join(output_dir)
    os.makedirs(output_dir_path, exist_ok=True)

    expression_data_output_filepath = os.path.join(output_dir_path, "ExpressionData.csv")
    cell_names = generate_expression_data_file(expression_data_filepath, expression_data_output_filepath)

    pseudo_time_output_filepath = os.path.join(output_dir_path, "PseudoTime.csv")
    generate_pseudo_time_file(pseudo_time_filepath, pseudo_time_output_filepath, cell_names)
    return


def main():
    opts = get_parser().parse_args()
    mode = opts.mode
    expression_data_filepath = opts.exprsn_data
    pseudo_time_filepath = opts.pseudo_time
    output_dir = opts.output_dir

    print(f"mode = {mode}")
    print(f"expression_data_filepath = {expression_data_filepath}")
    print(f"pseudo_time_filepath = {pseudo_time_filepath}")
    print(f"output_dir = {output_dir}")
    if mode == "tenet-to-beeline":
        tenet_to_beeline_conversion(expression_data_filepath, pseudo_time_filepath, output_dir)
    else:
        print("ERROR: Unsupported mode specified. Choose a mode from [tenet-to-beeline | beeline-to-tenet]. Only 'tenet-to-beeline' is currently supported.")


if __name__ == "__main__":
    main()
