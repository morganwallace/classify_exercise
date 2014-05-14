#classify_exercise

---

This repository contains the scripts and documents for the *UC Berkeley School of Information* [Spring 2014 Data Mining](http://www.ischool.berkeley.edu/courses/i290t-dma) class' final project.

**Author: ** Morgan Wallace

***Below is the proposal for this project***



## Final Project Proposal
---
**Morgan Wallace**
#### Datamining - Info 290T-03 Spring 2014

***Please Note:  *** 

This project supports the work I am doing for my MIMS final project. The project is called *** Hercubit *** and it is a wearable fitness device that gives users real-time feedback on their computer to help them exercise. 

## Goals
To implement and begin to optimize a SVM classifier for free-weight exercises.

##Roles
I, Morgan Wallace, am not working with any other student in Info 290T-03. I have collaborators on my MIMS final project team that I work closely with, however, **the data mining related work that I submit for this class will be entirely my own**. The entirety of my data will come from this other group project but I have been responsible for creating, cleaning, and organizing the data since the beginning, many months ago.

##Resources
#####Data

My data is composed of 784 repititions of various free-weight exercises like:

* Bicep Curls
* Tricep Curls/Kickbacks
* Shoulder Press

Each repitition is made up of samples which are taken every 0.1 seconds and have raw values x, y, and z axes for each of the 3 sensors on the device (accelerometer, gyroscope, magnetometer).

The data is in the ``data/`` directory and subdivided into 

* labeled_data.csv - all data
* training_data.csv - all_data except holdout
* holdout.csv - for testing model on new data.


For a much more in-depth look at my data so far, please view one of my iPython notebooks:

* ``notebooks/SVC.ipynb`` - *SVC classifier build and testing* - also online here: <http://nbviewer.ipython.org/github/morganwallace/classify_exercise/blob/master/notebooks/SVC.ipynb>
* ``notebooks/Machine Learning.ipynb`` - *Initial data prep and exploration* - also online here: <http://nbviewer.ipython.org/github/morganwallace/classify_exercise/blob/master/notebooks/Machine%20Learning%20-%20Free%20Weights.ipynb>


**``rep_tracker_svc.py``** implements the SVC for real-time data coming from a Hercubit device (``data/backup.csv`` will be iterated through instead of connecting to the device).

**``save_graph_and_data.py``** is the script that connects to the Hercubit device and visualizes and then saves the data for the training set. It will output the ``data/new_training.csv`` file that ``notebooks/SVC.ipynb`` uses to add new sets to the training dataset (although this output is disabled for this submission since you will not have a device - ``data/backup.csv`` will be iterated through instead).

**``hercubit/``** directory is a package of scrips used for connected to a hercubit device. *For this submission, bluetooth has been disabled;  ``data/backup.csv`` will be iterated through instead.

#####Software
GitHub, Python, iPython and the following Python libraries:

* sklearn 
* numpy
* matplotlib 
* mpld3
* seaborn
* pandas
* numpy
* pyserial

#####Other
I will be using the Hercubit wearable device as a source of data for the test, training and holdout datasets.

