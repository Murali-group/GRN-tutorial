# Tutorial on "Gene regulatory network inference from single-cell transcriptomics data" (ISMB 2022)

# Schedule

*11:00am-6:00pm, July 10, 2022* 
**10:45am-11:00pm:** Arrival and coffee
**11:00am-11:30pm:** Welcome, Introduction, Plan for the day, and meet tutors/speakers

**11:30am-12:15pm:** 

    "How to Build Regulatory Networks from Single-Cell RNA-seq data" (Talk)  (~30min+questions)
    T. M. Murali (*BEELINE*)

**12:15pm-13:00pm:** Talk 2 (~30min+questions)
    Kedar Natarajan *TENET*

**13:00pm-14:00pm:** *Lunch*

**14:00pm-15:15pm:** BEELINE (*Hands-on*)  
  *Short introduction to scRNA-seq, methods overview &amp; principle* (KNN)  
  *Generating synthetic data using BoolODE* (KA)  
  *Running BEELINE on synthetic/toy data using pre-selected methods* (KA/BA/KNN)  
  *Plotting output from BEELINE (jupyter notebooks)* (KA/BA/KNN)  
  *Advanced users (running GRN inference on public scRNA-seq data)* (KA/BA/KNN)  

**15:15pm-15:30pm:** *Break*

**15:30pm-16:45pm:** BEELINE  
  *BEELINE on real scRNA-seq data*  
  *Plotting and interpreting output from BEELINE benchmark*  

**16:45pm-17:00pm:** *Break*

**17:00pm-17:30pm:** TENET  
  *Running TENET on terminal using BoolODE synthetic data*  
  *Running TENET on terminal using test real data/Tuck et al dataset*  
  *Visualising TENET results on Cytoscape, and interpretation*  
  *Advanced users (public scRNA-seq data; processed count matrix)*  
    
**17:30pm-18:00pm:** *Discussion:* 
                Advantages, trade-offs and considerations for GRN inference  
                Perspectives and feedback from audience  
                ISMB Feedback survey link  

# Instructions (Linux)
1. [Download](https://www.virtualbox.org/wiki/Downloads) and [install](https://www.virtualbox.org/manual/ch02.html) Virtual Box.
2. [Download](https://drive.google.com/file/d/1HRAySKr6dkljbGjwY14gHbu5PsjDPACy/view?usp=sharing) the pre-configured Virtual Machine(VM) image.
3. Create a VM by [importing](https://docs.oracle.com/cd/E26217_01/E26796/html/qs-import-vm.html) the downloaded VM image.
4. Details of the imported VM are - 
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
        - BEELINE installation and configurations (`/home/ismb2022-grn/ISMB2022-GRN-Workshop/Beeline`)
        - TENET installation and configurations (`/home/ismb2022-grn/ISMB2022-GRN-Workshop/TENET`)


# Instructions (Mac with Intel architecture). Tested on MBP 2019, 2.4Ghz Quad-Core intel i5, 8GB OS Monterey
1. [Download](https://www.virtualbox.org/wiki/Downloads) and [install](https://www.virtualbox.org/manual/ch02.html) Virtual Box.
2. [Download](https://drive.google.com/file/d/1HRAySKr6dkljbGjwY14gHbu5PsjDPACy/view?usp=sharing) the pre-configured Virtual Machine(VM) image.
3. Create a VM by [importing](https://docs.oracle.com/cd/E26217_01/E26796/html/qs-import-vm.html) the downloaded VM image.
4. If you encounter kernel error, try below options
    a. Go to System Preferences > Security & Privacy and then allow VirtualBox to load
    b. Restart mac in recovery mode (Command (⌘) + R), goto Utilities tab and terminal. type "spctl kext-consent add VB5E2TV963". Restart again and repeat step (a) and restart virtualbox
5. Details of the imported VM are - 
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
        - BEELINE installation and configurations (`/home/ismb2022-grn/ISMB2022-GRN-Workshop/Beeline`)
        - TENET installation and configurations (`/home/ismb2022-grn/ISMB2022-GRN-Workshop/TENET`)


# Instructions (Mac with ARM/M1/Silicon architecture). Tested on MBP 2021, Apple M1, 16GB OS Monterey
_VirtualBox is not supported on MACs with ARM architecture
1. [Download](https://www.parallels.com/blogs/parallels-desktop-apple-silicon-mac/) and [install] Parallels. Allow access to downloads folder.
2. Free Download Ubuntu 20.04.2 ARM64 (2.37GB, free) within Parallels GUI (~3-5min; ~30MB/sec)
3. Create a 15 day trial account, create password for the Ubuntu OS
4. [Download](https://www.virtualbox.org/wiki/Downloads) and [install](https://www.virtualbox.org/manual/ch02.html) Virtual Box within Ubuntu
5. If you encounter error during virtual box installation, try below steps
    a. sudo apt-get update
	b. sudo dpkg -i --force-architecture Downloads/virtualbox-6.1_6.1.34-150636.1~Ubuntu~eoan_amd64.deb
    c. If you see a kernel error, try below
    d. echo "deb [arch=amd64] https://download.virtualbox.org/virtualbox/debian $(lsb_release -sc) contrib" | sudo tee /etc/apt/sources.list.d/virtualbox.list
    e. wget https://www.virtualbox.org/download/oracle_vbox_2016.asc
    f. sudo apt-key add oracle_vbox_2016.asc
    g. sudo apt update
    h. sudo apt install virtualbox-6.1
6. Start virtual box
7. [Download](https://drive.google.com/file/d/1HRAySKr6dkljbGjwY14gHbu5PsjDPACy/view?usp=sharing) the pre-configured Virtual Machine(VM) image.
8. Create a VM by [importing](https://docs.oracle.com/cd/E26217_01/E26796/html/qs-import-vm.html) the downloaded VM image.
9. Details of the imported VM are - 
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
        - BEELINE installation and configurations (`/home/ismb2022-grn/ISMB2022-GRN-Workshop/Beeline`)
        - TENET installation and configurations (`/home/ismb2022-grn/ISMB2022-GRN-Workshop/TENET`)




### BEELINE
Open a new terminal and execute following commands
```commandline
cd /home/ismb2022-grn/ISMB2022-GRN-Workshop/Beeline
conda activate BEELINE
```
Execute configured algorithms and evaluate their performance on - 

1. Example dataset
```commandline
python BLRunner.py --config config-files/Quickstart/example-quickstart.yaml
python BLEvaluator.py --config config-files/Quickstart/example-quickstart.yaml --auc --jaccard --epr
```

2. Synthetic datasets
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
3. Curated datasets
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

Create visualizations
```commandline
python BLPlotter.py --config config-files/Quickstart/Synthetic/dyn-BF-quickstart.yaml,config-files/Quickstart/Synthetic/dyn-LI-quickstart.yaml,config-files/Quickstart/Synthetic/dyn-BFC-quickstart.yaml,config-files/Quickstart/Synthetic/dyn-TF-quickstart.yaml,config-files/Quickstart/Curated/GSD-quickstart.yaml,config-files/Quickstart/Curated/mCAD-quickstart.yaml,config-files/Quickstart/Curated/HSC-quickstart.yaml,config-files/Quickstart/Curated/VSC-quickstart.yaml  --epr --auroc --overview
```
The following output files will be created - 
1. AUPRC: `/home/ismb2022-grn/ISMB2022-GRN-Workshop/Beeline/outputs/Curated/VSC/VSC-boxplot-AUROC.pdf`
2. Early Precision: `/home/ismb2022-grn/ISMB2022-GRN-Workshop/Beeline/outputs/Curated/VSC/VSC-boxplot-EPr.pdf`
3. Overview: `/home/ismb2022-grn/ISMB2022-GRN-Workshop/Beeline/outputs/Curated/VSC/VSC-overview.pdf`

> **Note:** Work is in progress to configure the output file directory through the BLPlotter script.
Until then, the plots will be created as per the output settings in the last configuration file of the `--config` option.


### TENET
Open terminal and execute following commands
```commandline
cd /home/ismb2022-grn/ISMB2022-GRN-Workshop/TENET
conda activate TENET
```
Execute TENET on synthetic dataset
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

Execute TENET on experimental dataset
```commandline
./TENET expression_dataTuck.csv 2 pseudotimeTuck.txt cell_selectTuck.txt 1
```
Execute TENET on experimental dataset (1k features)
```commandline
./TENET expression_dataTuck_1kfeatures.csv 2 pseudotimeTuck.txt cell_selectTuck.txt 1
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
