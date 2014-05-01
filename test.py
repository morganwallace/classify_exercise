import pickle
from hercubit import device
import pandas as pd


ser,conn_type=device.connect(bluetooth_enabled=False)
print conn_type
clf=pickle.load(open('svc_model.p'))
print dir(clf)

def make_labeled_data(df_x):
    all_reps=[]
    labels=[]
    
    # Iterate through sets
    for mySet in range( 1 , max(df_x.set_id)+1 ):
        
        # get list of indexes of labeled repititions for this set
        rep_index_list=df_x[(df_x.rep_count!=0) & (df_x.set_id==mySet)].index.tolist()
        
        #use list of indexes to make slices of data for each rep
        for i in range(len(rep_index_list)):
            
            #Make sure not to use the last label because it has no rep after it
            if i==len(rep_index_list)-1: break
            
            #Make a slice of data frame just for this repitition
            rep_df=df_x.iloc[rep_index_list[i]:rep_index_list[i+1]+1]
            
            #store data about this rep
            rep_features=[]
            # Use columns with sensor data for analysis
            columns=list(df_x.columns[5:14])
            for col in columns:
                values=rep_df.loc[:,[col]].values #get raw values for each sensor
                
                # Analyze values for column
                avg=np.mean(values)
                std=np.std(values)
                rng=max(values) - min(values)
                
                #save features
                for i in (avg,std, rng[0]):
                    rep_features.append(round(i,2))
                    
            labels.append(rep_df.iloc[0].exerciseType)
            all_reps.append(rep_features)
                        
    return all_reps, labels

def main():
	gen=device.sensor_stream(ser,conn_type)
	while True:
		print gen.next()

if __name__ == '__main__':
	main()