import pickle
import pandas as pd
from pandas import read_csv
import os

def add_to_model(new_csv):
	#convert to DataFrame
	df=read_csv(new_csv)
	#find and label peaks based on exerciseType

	#add to labeled_data.csv and training_data.csv

	#Teach classifier

	#save new classifer model
	
	#Verification with testing data and hold out

	#Save model performance to model performance.csv

def main():
	add_to_model('data/test_add.csv')
if __name__ == '__main__':
	main()