
from __future__ import division

import saved_data

import pickle
import sklearn
from sklearn import datasets, svm
import pandas as pd
import numpy as np


def peakdetect(y_axis, x_axis = None, lookahead = 500, delta = 0):
    """
    Converted from/based on a MATLAB script at http://billauer.co.il/peakdet.html
    
    Algorithm for detecting local maximas and minmias in a signal.
    Discovers peaks by searching for values which are surrounded by lower
    or larger values for maximas and minimas respectively
    
    keyword arguments:
    y_axis -- A list containg the signal over which to find peaks
    x_axis -- A x-axis whose values correspond to the 'y_axis' list and is used
        in the return to specify the postion of the peaks. If omitted the index
        of the y_axis is used. (default: None)
    lookahead -- (optional) distance to look ahead from a peak candidate to
        determine if it is the actual peak (default: 500) 
        '(sample / period) / f' where '4 >= f >= 1.25' might be a good value
    delta -- (optional) this specifies a minimum difference between a peak and
        the following points, before a peak may be considered a peak. Useful
        to hinder the algorithm from picking up false peaks towards to end of
        the signal. To work well delta should be set to 'delta >= RMSnoise * 5'.
        (default: 0)
            Delta function causes a 20% decrease in speed, when omitted
            Correctly used it can double the speed of the algorithm
    
    return -- two lists [maxtab, mintab] containing the positive and negative
        peaks respectively. Each cell of the lists contains a tupple of:
        (position, peak_value) 
        to get the average peak value do 'np.mean(maxtab, 0)[1]' on the results
    """
    maxtab = []
    mintab = []
    dump = []   #Used to pop the first hit which always if false
       
    length = len(y_axis)
    if x_axis is None:
        x_axis = range(length)
    
    #perform some checks
    if length != len(x_axis):
        raise ValueError, "Input vectors y_axis and x_axis must have same length"
    if lookahead < 1:
        raise ValueError, "Lookahead must be above '1' in value"
    if not (np.isscalar(delta) and delta >= 0):
        raise ValueError, "delta must be a positive number"
    
    #needs to be a numpy array
    y_axis = np.asarray(y_axis)
    
    #maxima and minima candidates are temporarily stored in
    #mx and mn respectively
    mn, mx = np.Inf, -np.Inf
    
    #Only detect peak if there is 'lookahead' amount of points after it
    for index, (x, y) in enumerate(zip(x_axis[:-lookahead], y_axis[:-lookahead])):
        if y > mx:
            mx = y
            mxpos = x
        if y < mn:
            mn = y
            mnpos = x
        
        ####look for max####
        if y < mx-delta and mx != np.Inf:
            #Maxima peak candidate found
            #look ahead in signal to ensure that this is a peak and not jitter
            if y_axis[index:index+lookahead].max() < mx:
                maxtab.append((mxpos, mx))
                dump.append(True)
                #set algorithm to only find minima now
                mx = np.Inf
                mn = np.Inf
        ## Morgan's addition
        y    
            
        
        ####look for min####
        if y > mn+delta and mn != -np.Inf:
            #Minima peak candidate found 
            #look ahead in signal to ensure that this is a peak and not jitter
            if y_axis[index:index+lookahead].min() > mn:
                mintab.append((mnpos, mn))
                dump.append(False)
                #set algorithm to only find maxima now
                mn = -np.Inf
                mx = -np.Inf
    
    
    #Remove the false hit on the first value of the y_axis
    try:
        if dump[0]:
            maxtab.pop(0)
            #print "pop max"
        else:
            mintab.pop(0)
            #print "pop min"
        del dump
    except IndexError:
        #no peaks were found, should the function return empty lists?
        pass
    
    return maxtab, mintab
 

# <codecell>

def remap(peaks):
    """Reformat coordinates of peaks to properly feed into pyplot"""
    tabs=[]
    for tab in peaks: #mintab and maxtab
        tab=([i[1] for i in tab],[i[0] for i in tab])
        tabs.append(tab)
    return tabs

# <codecell>

### INCOMPLETE
def get_ranges(peaks):
    """Range if there is a min to max or max to min"""
    ranges={}
    both_min_max={}
#     print peaks
    for tab in peaks:
#         print 'tabs'
#         print tab
        peak=tab[0]
        for i in range(len(peak)):
#             print peak
            if ranges.get(i)==None:
                ranges[i]=[peak[i],'just one']
                
            else:
                ranges[i][0]=abs(ranges[i]-peak[i])
                ranges[i][1]='both_min_max'
            return [r[0] for r in ranges.values() if r[1]=="both_min_max"]

# <codecell>

deltas={'acc':.15,'gyro':2500,'magnet':15}

# <codecell>

def plot_peaks(df_x,fig,ax, axes,mylookahead=10, delta=""):
    global deltas
    peak_dict={}
    ranges={}
    for axis in axes:
        peaks=peakdetect(df_x[axis],df_x['t (sec)'], lookahead=mylookahead,delta=delta)
        peaks=remap(peaks)
#         r=get_ranges(peaks)
#         print r
#         ranges[axis]=sum(r)/len(r)
#         print ranges[axis]
        ax.plot(peaks[0][1],peaks[0][0], "o") # Plot dots for local maxima
        ax.plot(peaks[1][1],peaks[1][0], "o") # Plot dots for local minima
        print "%d local min, %d local max found on %s axis" % (len(peaks[1][0]),len(peaks[0][0]),axis)
    return fig, ax

# <codecell>

def plot_sensor(sensor="acc", peaks=True,lookahead=10,user="Morgan",exercise='bicep curls',delta=None):
    #setup a slice of the data frame
    global df, deltas
    df_x=df[df.exerciseType==exercise]        
    df_x=df_x[df_x.User==user]
    df_x=df_x[df_x.set_id== int(df_x.set_id.head(1))]
    
    #Make plots
    fig, ax = plt.subplots()
    if sensor=="acc": axes=list(df_x.columns[4:7])
    if sensor=="gyro": axes=list(df_x.columns[7:10])
    if sensor=="magnet": axes=list(df_x.columns[10:13])
        
    for axis in axes:
        ax.plot(df_x['t (sec)'], df_x[axis], label=axis[-1])
    
    if peaks==True:
        if delta==None:
            delta=deltas[sensor]
        plot_peaks(df_x,fig, ax, axes,mylookahead=lookahead, delta=delta)
    ax.legend()
    ax.set_title("10 reps of "+str(df_x.exerciseType.iloc[0])+": sensor="+sensor+", user="+str(df_x.User.iloc[0])+", set_id="+str(df_x.set_id.iloc[0]))
#     return fig, ax

# <codecell>

reps={}
def add_rep_count(set_id,col='acc_y',max_or_min='max',mylookahead=10):
    global reps
    reps[set_id]=0
    #prepare a slice of the dataframe for peak detection
    df_x=df[df.set_id==set_id]
    
    #find peaks
    peaks=peakdetect(df_x[col],df_x['t (sec)'], lookahead=mylookahead)
    if max_or_min=="max": i =0
    elif max_or_min=="min": i =1
    times=[peak[0] for peak in peaks[i]]
    
    #set values
    for time in times:
        reps[set_id]+=1
        rep_index=df_x[df_x['t (sec)']==time].index[0]
        df.rep_count[rep_index]=reps[set_id]
#     print df[df.set_id==set_id]

# <codecell>

def manual_add_rep(i):
    global reps
    reps[set_id]+=1
    df.rep_count[i]=reps[set_id]
