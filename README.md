# Tutorial on "Gene regulatory network inference from single-cell transcriptomics data" (ISMB 2022)

# Schedule 

*11:00 am - 6:00 pm* (Lunch Break 1:00 pm - 2:00 pm; Coffee Breaks at 3:15 - 3:30 and 4:45 - 5:00 pm)

**11:00-11:30:** Welcome, Introduction, plan for day and meet tutors/speakers

**11:30-12:15:** Talk 1 (~30min+questions)
    T. M. Murali (*Brief intro to scRNA-seq, GRN inference and BEELINE*)

**12:15-13:00:** Talk 2 (~30min+questions)
    *(tentatively AM) TENET*

**13:00-14:00:** *Lunch*

**14:00-15:15:** GRN inference method 1 (*Hands-on*)
    *PySCENIC*
    *Short introduction to scRNA-seq, methods overview &amp; principle*
    *Count matrix*
    *Jupyter notebooks with steps (~15-25min)*
    *Applying GRN inference method 1 on simulated data (workflow and let users run
themselves). Simulated data from BoolODE as well as modelled scRNA-seq
parameters*
    *Advanced users (running GRN inference on public scRNA-seq data)*

**15:15-15:30:** *Break*

**15:30-16:45:** GRN inference method 2 (Hands-on)
    *Implement TENET in BEELINE*
    *Intro to TENET and BEELINE (methods overview)*
    *Jupyter notebooks with steps (~15-25min)*
    *Inference on simulated data using BEELINE/TENET*
    *Advanced users (public scRNA-seq data; processed count matrix)*

**16:45-17:00:** *Break*

**17:00-17:30:** *Discussion:* advantages, trade-offs, considerations (scaling methods to increased features vs cells, single-cell atlases, accuracy vs sensitivity, TF-target prediction vs
edge weights etc.,)

**17:30-18:00:** Wind up, discussions, feedback and perspectives

# Instructions
1. [Download](https://www.virtualbox.org/wiki/Downloads) and [install](https://www.virtualbox.org/manual/ch02.html) Virtual Box.
2. [Download](https://drive.google.com/drive/folders/1AgKtJere3qq4URhQMQCz5_VyQ_SCVR6c?usp=sharing) the pre-configured Virtual Machine(VM) image.
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
./TENET expression_data.csv 1 trajectory.txt cell_select.txt 1
```
Execute TENET on experimental dataset
```commandline
./TENET expression_dataTuck.csv 1 pseudotimeTuck.txt cell_selectTuck.txt 1
```
# Resources
