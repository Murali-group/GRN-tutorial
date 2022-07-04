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

# Virtual Box Installation and  Setup

## Windows and Linux
[Download](https://www.virtualbox.org/wiki/Downloads) and [install](https://www.virtualbox.org/manual/ch02.html) Virtual Box.

## OS X
> WIP: Add instructions for MAC 

# Creating Virtual Machine
>**NOTE: The pre-configured Virtual Machine image is undergoing continuous updates. Please wait until July 06, 2022 00:00 EST to download the final version that will be used during the tutorial.**
1. [Download](https://bioinformatics.cs.vt.edu/~murali/beeline-tutorials/ISMB2022-GRN-Ubuntu20.04_final.ova) the pre-configured Virtual Machine(VM) image.
2. Create a VM by [importing](https://docs.oracle.com/cd/E26217_01/E26796/html/qs-import-vm.html) the downloaded VM image.

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

# Running BEELINE
All steps and commands to run BEELINE are in pre-configured Jupyter notebook ```ISMB 2022 GRN Tutorial on BEELINE.ipynb```.
Through this notebook we will perform the following steps - 
1. Activate BEELINE 
2. Run and evaluate GRN inference algorithms using *BLRunner* and *BLEvaluator*, respectively on following datasets
   1. Synthetic datasets
   2. Curated datasets
3. Visualize the performance of the algorithms using *BLPlotter*

To start up the Jupyter Notebook, execute the shell script ```ISMB2022-BEELINE-GRN-Notebook.sh``` on the Desktop by -
* Double clicking the shell script

OR

* Open a terminal and execute the command: ```. /home/ismb2022-grn/Desktop/ISMB2022-BEELINE-GRN-Notebook.sh``` 

> Please wait for 5-10 seconds for the Jupyter Notebook to load and show up in the browser.

Once the Jupyter Notebook has started, execute all the cells in the notebook sequentially.

# Running TENET

All steps and commands to run TENET are in pre-configured Jupyter notebook ```ISMB 2022 GRN Tutorial on TENET.ipynb```.
Through this notebook we will perform the following steps - 
1. Activate TENET 
2. Perform GRN inference on -
   1. Experimental dataset
   2. Synthetic dataset
   3. Curated dataset

To start up the Jupyter Notebook, execute the shell script ```ISMB2022-TENET-GRN-Notebook.sh``` located at the Desktop by -
* Double clicking the shell script

OR

* Open a terminal and execute the command: ```. /home/ismb2022-grn/Desktop/ISMB2022-TENET-GRN-Notebook.sh``` 

> Please wait for 5-10 seconds for the Jupyter Notebook to load and show up in the browser.

Once the Jupyter Notebook has started, execute all the cells in the notebook sequentially.

