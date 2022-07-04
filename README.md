# Tutorial on "Gene regulatory network inference from single-cell transcriptomics data" (ISMB 2022)

# Schedule

*11:00am-6:00pm, July 10, 2022*

**10:45am-11:00pm:** Arrival and coffee

**11:00am-11:30pm:** Welcome, Introduction, Plan for the day, and meet tutors/speakers

**11:30am-12:15pm:** 
    *How to Build Gene Regulatory Networks from Single-Cell RNA-seq data* (Talk, ~30min+questions)
    T. M. Murali

**12:15pm-13:00pm:** *Inferring Gene Regulatory Networks and causal regulators using Transfer Entropy NETwork (TENET)* (Talk, ~30min+questions)
    Kedar Natarajan 

**13:00pm-14:00pm:** *Lunch*

**14:00pm-15:15pm:** GRN benchmarking using BEELINE (*Hands-on*)  
  *Introduction to scRNA-seq, methods overview &amp; principles*  
  *Introduction to generating synthetic datasets using BoolODE*  
  *Beeline benchmarking on scRNA-seq datasets*  

**15:15pm-15:30pm:** *Break*

**15:30pm-16:45pm:** BEELINE contd..  
  *Visualising and interpreting BEELINE results* 

**16:45pm-17:00pm:** *Break*

**17:00pm-17:30pm:** GRN inference using TENET  
  *Applying TENET on scRNA-seq datasets*  

**17:30pm-18:00pm:** *Discussion:*  
  *Advantages, trade-offs and considerations for GRN inference methods*  
  *Perspectives and workshop feedback*  


# Instructions (Linux)
=======
# Installation and Setup
>>>>>>> main
1. [Download](https://www.virtualbox.org/wiki/Downloads) and [install](https://www.virtualbox.org/manual/ch02.html) Virtual Box.
2. [Download](https://bioinformatics.cs.vt.edu/~murali/beeline-tutorials/ISMB2022-GRN-Ubuntu20.04_final.ova) the pre-configured Virtual Machine(VM) image.
3. Create a VM by [importing](https://docs.oracle.com/cd/E26217_01/E26796/html/qs-import-vm.html) the downloaded VM image.
You would have now created a VM with the following properties - 
    - VM Name: ISMB2022-GRN-VM
    - Operating System: Ubuntu 20.04.1 LTS (64bit)
    - Memory(RAM): 2GB
    - Root access:
        - username: ismb2022-grn
        - password: root
    - VM contains:
        - Docker v20.10.7
        - Anaconda v4.12.0
        - Python v3.9.12
        - Java v11.0.15
        - Cytoscape v3.9.1
        - GraphSpace Python Client v1.0.0
        - BEELINE installation and configurations (`/home/ismb2022-grn/ISMB2022-GRN-Workshop/Beeline`)
        - TENET installation and configurations (`/home/ismb2022-grn/ISMB2022-GRN-Workshop/TENET`)


# Instructions (Mac with Intel architecture). Tested on MBP 2019, 2.4Ghz Quad-Core intel i5, 8GB OS Monterey
1. Follow the above steps 1-3
2. When starting VirtualBox on intel mac, if you encounter kernel error, try below options
    a. Go to System Preferences > Security & Privacy and then allow VirtualBox to load
    b. Restart mac in recovery mode (Command (⌘) + R), goto Utilities tab and terminal. type "spctl kext-consent add VB5E2TV963". Restart again and repeat step (a) and restart virtualbox  

# Instructions (Mac with ARM/M1/Silicon architecture). Tested on MBP 2021, Apple M1, 16GB OS Monterey
_VirtualBox is not supported on MACs with ARM architecture
1. [Download](https://www.parallels.com/blogs/parallels-desktop-apple-silicon-mac/) and [install] Parallels. Allow access to downloads folder.
2. Free Download Ubuntu 20.04.2 ARM64 (2.37GB, free) within Parallels GUI (~3-5min; ~30MB/sec)
3. Create a 15 day trial account, create password for the Ubuntu OS
4. Follow the steps 1-3 (from linux instructions). 
5. If you encounter error during virtual box installation, try below steps
    a. sudo apt-get update
	  b. sudo dpkg -i --force-architecture Downloads/virtualbox-6.1_6.1.34-150636.1~Ubuntu~eoan_amd64.deb
    c. If you see a kernel error, try below
    d. echo "deb [arch=amd64] https://download.virtualbox.org/virtualbox/debian $(lsb_release -sc) contrib" | sudo tee /etc/apt/sources.list.d/virtualbox.list
    e. wget https://www.virtualbox.org/download/oracle_vbox_2016.asc
    f. sudo apt-key add oracle_vbox_2016.asc
    g. sudo apt update
    h. sudo apt install virtualbox-6.1


### BEELINE
=======
# Running BEELINE
We will perform the following steps - 
1. Activate BEELINE 
2. Run and evaluate GRN inference algorithms using 
   1. *BLRunner*
   2. *BLEvaluator*
3. Visualize the performance of the algorithms using *BLPlotter*
### 1. Activate BEELINE
>>>>>>> main
Open a new terminal and execute following commands
```commandline
cd /home/ismb2022-grn/ISMB2022-GRN-Workshop/Beeline
conda activate BEELINE
```

### 2. Run and evaluate GRN inference algorithms
We will use three types of datasets for this step - 

#### 1. Synthetic datasets
```commandline
python BLRunner.py --config config-files/Quickstart/Synthetic/dyn-BF-quickstart.yaml
python BLEvaluator.py --config config-files/Quickstart/Synthetic/dyn-BF-quickstart.yaml --auc --jaccard --epr

python BLRunner.py --config config-files/Quickstart/Synthetic/dyn-LI-quickstart.yaml
python BLEvaluator.py --config config-files/Quickstart/Synthetic/dyn-LI-quickstart.yaml --auc --jaccard --epr

python BLRunner.py --config config-files/Quickstart/Synthetic/dyn-BFC-quickstart.yaml
python BLEvaluator.py --config config-files/Quickstart/Synthetic/dyn-BFC-quickstart.yaml --auc --jaccard --epr

python BLRunner.py --config config-files/Quickstart/Synthetic/dyn-TF-quickstart.yaml
python BLEvaluator.py --config config-files/Quickstart/Synthetic/dyn-TF-quickstart.yaml --auc --jaccard --epr
```
#### 2. Curated datasets
```commandline
python BLRunner.py --config config-files/Quickstart/Curated/GSD-quickstart.yaml
python BLEvaluator.py --config config-files/Quickstart/Curated/GSD-quickstart.yaml --auc --jaccard --epr

python BLRunner.py --config config-files/Quickstart/Curated/mCAD-quickstart.yaml
python BLEvaluator.py --config config-files/Quickstart/Curated/mCAD-quickstart.yaml --auc --jaccard --epr

python BLRunner.py --config config-files/Quickstart/Curated/HSC-quickstart.yaml
python BLEvaluator.py --config config-files/Quickstart/Curated/HSC-quickstart.yaml --auc --jaccard --epr

python BLRunner.py --config config-files/Quickstart/Curated/VSC-quickstart.yaml
python BLEvaluator.py --config config-files/Quickstart/Curated/VSC-quickstart.yaml --auc --jaccard --epr
```

#### 3. Experimental (scRNA-seq) datasets
```commandline
python BLRunner.py --config config-files/Quickstart/scRNA-seq/mTuck-quickstart.yaml
python BLEvaluator.py --config config-files/Quickstart/scRNA-seq/mTuck-quickstart.yaml --auc --jaccard --epr
```

### 3. Visualize the performance of GRN inference algorithms
```commandline
python BLPlotter.py --config config-files/Quickstart/Synthetic/dyn-BF-quickstart.yaml,config-files/Quickstart/Synthetic/dyn-LI-quickstart.yaml,config-files/Quickstart/Synthetic/dyn-BFC-quickstart.yaml,config-files/Quickstart/Synthetic/dyn-TF-quickstart.yaml,config-files/Quickstart/Curated/GSD-quickstart.yaml,config-files/Quickstart/Curated/mCAD-quickstart.yaml,config-files/Quickstart/Curated/HSC-quickstart.yaml,config-files/Quickstart/Curated/VSC-quickstart.yaml,config-files/Quickstart/scRNA-seq/mTuck-quickstart.yaml  --epr --auroc --overview
```
The following output files will be created - 
1. AUPRC: `/home/ismb2022-grn/ISMB2022-GRN-Workshop/Beeline/dyn-BF-dyn-LI-dyn-BFC-dyn-TF-GSD-mCAD-HSC-VSC-boxplot-AUROC.pdf`
2. Early Precision: `/home/ismb2022-grn/ISMB2022-GRN-Workshop/Beeline/dyn-BF-dyn-LI-dyn-BFC-dyn-TF-GSD-mCAD-HSC-VSC-boxplot-EPr.pd`
3. Overview: `/home/ismb2022-grn/ISMB2022-GRN-Workshop/Beeline/dyn-BF-dyn-LI-dyn-BFC-dyn-TF-GSD-mCAD-HSC-VSC-overview.pdf`

# Running TENET
We will perform the following steps - 
1. Activate TENET 
2. Perform GRN inference on -
   1. Synthetic dataset
   2. Experimental dataset
   3. Curated dataset
    
### 1. Activate TENET
Open terminal and execute following commands
```commandline
cd /home/ismb2022-grn/ISMB2022-GRN-Workshop/TENET
conda activate TENET
```

### 2. Perform GRN inference using different datasets

#### 1. Synthetic Dataset
```commandline
./TENET expression_data.csv 2 trajectory.txt cell_select.txt 1
```

Plotting synthetic data (FDR cutoff)
_python makeGRN.py [cutoff for FDR]_
```commandline
python makeGRN.py [cutoff for FDR]
```
Plotting synthetic data (Retaining number of links)
_python makeGRNsameNumberOfLinks.py [number of links]_
```commandline
python makeGRNsameNumberofLinks.py 500
```

=======
#### 2. Experimental(scRNA-seq)
#### Execute TENET on experimental dataset (500 highly variable genes with roles in _stem cell maintenance_ and _neuronal differentiation_)
```commandline
./TENET expression_dataTuck_500genes.csv  2 pseudotimeTuck.txt cell_selectTuck.txt 1
```
Optionally TENET can be run on higher number of highly variable genes (1725 genes)
```commandline
./TENET expression_dataTuck_1725genes.csv 2 pseudotimeTuck.txt cell_selectTuck.txt 1
```
or TENET can be run on higher number of highly variable genes (500 genes) and fewer cells (258 cells)
```commandline
./TENET expression_dataTuck_500genes.csv 2 pseudotimeTuck.txt cell_selectTuck_subset.txt 1
```

Plotting synthetic data (FDR cutoff and same number of links
_python makeGRN.py [cutoff for FDR]_
_python makeGRNsameNumberOfLinks.py [number of links]_
```commandline
python makeGRN.py [cutoff for FDR]
python makeGRNsameNumberofLinks.py 500
```
_Output Files_
```commandline
TE_results_matrix.fdr0.01.sif
TE_results_matrix.NumberOfLinks500.sif
```


# Resources
