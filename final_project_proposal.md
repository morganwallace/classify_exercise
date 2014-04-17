## Final Project Proposal
---
**Morgan Wallace**
#### Datamining - Info 290T-03 Spring 2014

***Please Note:  *** 

This project supports the work I am doing for my MIMS final project. The project is called *** Hercubit *** and it is a wearable fitness device that gives users real-time feedback on their computer to help them exercise. 

## Goals
To find the most presice and accurate classifier of exercise types. For example, 20 samples of data represent 1 repitition of an unknown type of exercise (possibly bicep curl or shoulder press). Use some or all of the following classification methods and see which is best:

* svm
* naive bayes
* Neural networks
* K-nearest neighbors
* maybe others if there's time.

##Roles
I, Morgan Wallace, am not working with any other student in Info 290T-03. I have collaborators on my MIMS final project team that I work closely with, however, **the data mining related work that I submit for this class will be entirely my own**. The entirety of my data will come from this other group project but I have been responsible for creating, cleaning, and organizing the data since the beginning, many months ago.

##Resources
#####Data

My data is composed of hundreds of repititions of various free-weight exercises like:

* Bicep Curls
* Tricep Curls/Kickbacks
* Shoulder Press

Each repitition is made up of samples which are taken every 0.1 seconds and have raw values x, y, and z axes for each of the 3 sensors on the device (accelerometer, gyroscope, magnetometer)


For a much more in-depth look at my data so far, please view one of my latest iPython notebooks <http://nbviewer.ipython.org/gist/morganwallace/9966432>



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
* By April 11th:

	1. segment dataset into training, test, and holdout.
	2. research and estimate which 3 classifiers will provide the best results.
* by April 16th:
	1. Add any last data to data set
	2. Uncover preliminary feature sets through visualization and observation
	3. Take first stab at implementing code on at least 1 classification method
* by April 23rd
	1. 3 working classification tools
* by April 30th
	1. All classifiers optimized and measured.
	2. Code submitted
* by May 8th
	1. Prepare presentation
* by May 14th
	1. Write reports