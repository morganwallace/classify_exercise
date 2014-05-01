import csv
import pickle
import sklearn
import pandas as pd
from pandas import read_csv
import numpy as np
import pandas as pd


def add_reps(set_id,mylist):
    global df
    count=0
#     df_x=df[df.set_id==set_id]
    for t in mylist:
        count+=1
        t=round(t,3)
        indx = df[(df['t (sec)']>t-.05) & (df['t (sec)']<t+.05) &(df.set_id==set_id)].index.tolist()[0]
        df.loc[indx,'rep_count']=count

def add(new_data='',filename=''):
	if filename!='':
		with open (filename) as savedfile:
			new_data=pickle.load(savedfile)
			print new_data[0]
	#get labeled data
	with open('labeled_data.csv', 'rb') as csvfile:
		df=read_csv(csvfile)
	new_set_id=df.set_id.max()
	df.columns=['Unnamed: 0','User','exerciseType','rep_count','t (sec)','acc_x','acc_y','acc_z','gyro_x','gyro_y','gyro_z','magnet_x','magnet_y','magnet_z','set_id']
	df.drop("Unnamed: 0",1)
	df.add(new_data)
	df.head()
		


def main():
	add(filename='saved_animations_and_data/2014-04-23__16-20-43_bicep curls_lisa/2014-04-23__16-20-43_bicep curls.p')

if __name__ == '__main__':
	main()