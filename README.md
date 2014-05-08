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

My data is composed of hundreds of repititions of various free-weight exercises like:

* Bicep Curls
* Tricep Curls/Kickbacks
* Shoulder Press

Each repitition is made up of samples which are taken every 0.1 seconds and have raw values x, y, and z axes for each of the 3 sensors on the device (accelerometer, gyroscope, magnetometer)


For a much more in-depth look at my data so far, please view one of my iPython notebooks:

* notebooks/SVC.ipynb - *SVC classifier build and testing* - also online here: <http://nbviewer.ipython.org/github/morganwallace/classify_exercise/blob/master/notebooks/SVC.ipynb>
* notebooks/Machine Learning.ipynb - *Initial data prep and exploration* - also online here: <http://nbviewer.ipython.org/github/morganwallace/classify_exercise/blob/master/notebooks/Machine%20Learning%20-%20Free%20Weights.ipynb>


**rep_tracker_svc.py** implements the SVC for real-time data coming from a Hercubit device.



#####Software
GitHub, Python, iPython and the following Python libraries:

* sklearn 
* matplotlib 
* mpld3
* seaborn
* pandas
* numpy

#####Other
I will be using the wearable devices as sources of data for the test, training and holdout datasets.

##Project Plan
* By April 20th:

	1. segment dataset into training, test (holdout set will be created later with device).
	2. research and estimate which 3 classifiers will provide the best results.
* by April 21th:
	1. Uncover preliminary feature sets through visualization and observation
	2. Take first stab at implementing code on at least 1 classification method
* by April 23rd
	1. 3 working classification tools
* by April 30th
	1. All classifiers optimized and measured.
	2. Code submitted
* by May 8th
	1. Prepare presentation
* by May 14th
	1. Write reports