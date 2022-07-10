# Tutorial on "Gene regulatory network inference from single-cell transcriptomics data" (ISMB 2022)

# Table of Contents
**[Schedule](#schedule)**<br>
**[Virtual Box Installation and Setup](#virtual-box-installation-and-setup)**<br>
&emsp;  [Windows and Linux](#windows-and-linux)<br>
&emsp;  [OS X](#os-x)<br>
**[Creating Virtual Machine](#creating-virtual-machine)**<br>
**[Running BEELINE](#running-beeline)**<br>
**[Running TENET](#running-tenet)**<br>
**[Resources](#resources)**<br>
**[Tutorial Communication Channel](#tutorial-communication-channel)**<br>

# Schedule 

*11:00 am - 6:00 pm* (Lunch Break 1:00 pm - 2:00 pm; Coffee Breaks at 3:15 - 3:30 and 4:45 - 5:00 pm)

**10:45am-11:00pm:** Arrival and coffee  
**11:00-11:30:** Welcome, Introduction, plan for day and meet tutors/speakers

**11:30-12:15:** Talk 1: T. M. Murali ***[How to Build Gene Regulatory Networks from Single-Cell RNA-seq data](http://bioinformatics.cs.vt.edu/~murali/beeline-tutorials/2022-07-10-ismb-beeline-grns.pdf)***  
   
**12:15-13:00:** Talk 2: Kedar Natarajan ***[Inferring Gene Regulatory Networks and causal regulators using Transfer Entropy NETwork (TENET)](https://drive.google.com/file/d/12IjP2O9suir3-VF9O5S7JjUgFKP6k9VZ/view?usp=sharing)***

    

**13:00-14:00:** *Lunch*

**14:00-15:15:** GRN benchmarking using BEELINE (*_Hands-on_*)  
  *Introduction to scRNA-seq, methods overview &amp; principles*  
  *[Introduction to generating synthetic datasets using BoolODE](http://bioinformatics.cs.vt.edu/~murali/beeline-tutorials/2022-07-10-ismb-beeline-data.pdf )*  
  *Beeline benchmarking on scRNA-seq datasets* 

**15:15-15:30:** *Break*

**15:30-16:45:** BEELINE contd. (*_Hands-on_*)  
  *Visualising and interpreting BEELINE results* 

**16:45-17:00:** *Break*

**17:00-17:30:** GRN inference using TENET  (*_Hands-on_*)  
  *Applying TENET on scRNA-seq datasets and visualisation*

**17:30-18:00:** Discussions   
  *Perspectives: Advantages, trade-offs and considerations for GRN inference methods*  
  *[ISMB Tutorial feedback](https://docs.google.com/forms/d/e/1FAIpQLSftVbI5O-P6EidL-PBgmqjdVE9QX3SfsgGKqkX6DDxJzGvrfQ/viewform?usp=sf_link)* 


# Virtual Box Installation and Setup

## Windows and Linux
[Download](https://www.virtualbox.org/wiki/Downloads) and [install](https://www.virtualbox.org/manual/ch02.html) Virtual Box.

## OS X
### Instructions (Mac with Intel architecture). 
_Tested on MBP 2019, 2.4Ghz Quad-Core intel i5, 8GB OS Monterey_  
1. [Download](https://www.virtualbox.org/wiki/Downloads) and [install](https://www.virtualbox.org/manual/ch02.html) Virtual Box.
2. When starting VirtualBox on intel mac, if you encounter kernel error, try below options
    a. Go to System Preferences > Security & Privacy and then allow VirtualBox to load
    b. Restart mac in recovery mode (Command (⌘) + R), goto Utilities tab and terminal. type "spctl kext-consent add VB5E2TV963". Restart again and repeat step (a) and restart virtualbox  
3. Follow the installation instructions below (see "Creating Virtual Machine")

### Instructions (Mac with ARM/M1/Silicon architecture). 
_Tested on MBP 2021, Apple M1, 16GB OS Monterey_
_Note: VirtualBox is not supported on MACs with ARM architecture and below are some suggestions that have worked for some users. We have not exhaustively tested the tutorial material on ARM architecture, and suggest users to use a non-ARM mac for current iteration of the workshop_   

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
6. Follow the installation instructions below (see "Creating Virtual Machine")


# Creating A Virtual Machine
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

> Note: To enable full screen mode for the virtual machine, you can use the short-cut: Host (Right Ctrl + F) or use the toolbar: View > Full-screen mode

# Running BEELINE
All steps and commands to run BEELINE are in pre-configured Jupyter notebook [ISMB 2022 GRN Tutorial on BEELINE.ipynb](./notebooks/ISMB%202022%20GRN%20Tutorial%20on%20BEELINE.ipynb).
Through this notebook we will perform the following steps - 
1. Activate BEELINE 
2. Run and evaluate GRN inference algorithms using *BLRunner* and *BLEvaluator*, respectively on following datasets
   1. Synthetic datasets
   2. Curated datasets
3. Visualize the performance of the algorithms using *BLPlotter*


To start the Jupyter Notebook  - 
* Double click the shell script ```ISMB2022-BEELINE-GRN-Notebook.sh``` on the Desktop

OR

* Open a terminal and execute the command: ```. /home/ismb2022-grn/Desktop/ISMB2022-BEELINE-GRN-Notebook.sh``` 

> Please wait for 5-10 seconds for the Jupyter Notebook to load and show up in the browser.

Once the Jupyter Notebook has started, execute all the cells in the notebook sequentially.

# Running TENET

All steps and commands to run TENET are in pre-configured Jupyter notebook [ISMB 2022 GRN Tutorial on TENET.ipynb](./notebooks/ISMB%202022%20GRN%20Tutorial%20on%20TENET.ipynb).
Through this notebook we will perform the following steps - 
1. Activate TENET 
2. Perform GRN inference on -
   1. Synthetic dataset
   2. Experimental dataset

To start up the Jupyter Notebook -
* Double click the shell script ```ISMB2022-TENET-GRN-Notebook.sh``` on the Desktop

OR

* Open a terminal and execute the command: ```. /home/ismb2022-grn/Desktop/ISMB2022-TENET-GRN-Notebook.sh``` 

> Please wait for 5-10 seconds for the Jupyter Notebook to load and show up in the browser.

Once the Jupyter Notebook has started, execute all the cells in the notebook sequentially.



# Resources

### Introduction to single-cell transcriptomics data analysis  
1. [Single-cell analysis course from Wellcome Sanger Institute](https://www.singlecellcourse.org/)
2. [Single-cell analysis course from Broad Institute](https://broadinstitute.github.io/2019_scWorkshop/)

### GRN inference methods, benchmarking, and reviews
1. [TENET](https://academic.oup.com/nar/article/49/1/e1/5973444)
2. [BEELINE](https://pubmed.ncbi.nlm.nih.gov/31907445/)
3. Reviews on GRN network inference
   1. [Gene regulatory network inference in single-cell biology](https://www.sciencedirect.com/science/article/abs/pii/S2452310021000184)
   2. [Mapping gene regulatory networks from single-cell omics data](https://pubmed.ncbi.nlm.nih.gov/29342231/)

# Tutorial Communication Channel
Please use the [ISMB-2022 Tutorial: GRN inference from scRNA-seq](https://join.slack.com/t/slack-rdm6568/shared_invite/zt-1c7ckfz37-eLMTzds61pllv_Gq4NvV6g) Slack channel for technical support during the tutorial, to initiate discussions, and communicate with participants and speakers.
