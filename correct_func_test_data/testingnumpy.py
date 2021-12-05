#!/usr/bin/python3
"""
Contains the following functions:
1. file2numpy: This function will load a txt file and change to a numpy array.

2. behavior_nearest_loc: This function will return the
index (array location) for the value in fluor_array that
is closest in value to each row in behav_array.

3. behavior_nearest_value: This function will give the value in
fluor_array that is closest to the value for each row in behav_array.

4. area_under_curve: This function will give the mean
fluroescence for all events of a behavior.
"""


import sys
import numpy as np
import pandas as pd


def file2numpy(file_path):
    """
    Objective: To take the given file and convert to a numpy array.

    Parameters
    ----------
    file_path: str
        This will provide the file path needed.


    Returns
    -------
    array : list
        This is a numpy array.
    """
    array = np.loadtxt(file_path, dtype=float)
    return array


def behavior_nearest_loc(fluor_array, behav_array):
    """
    Objective: Find the array location for the value in fluor_array that 
    is closest in value to each row in behav_array.

    Parameters
    ----------
    fluor_array: list
        This numpy array contains of all the time
        points corresponding to the green channel.

    behav_array: list
        This numpy array contains all of the
        start times when the behavior occurred.


    Returns
    -------
    near_loc : list
        This list of integers contains the array location where the value for
        each row in behav_array is closest in value to that in fluor_array.
    """
    near_loc = []
    for x in np.nditer(behav_array):
        loc = (np.abs(fluor_array - x)).argmin()
        near_loc.append(loc)
    return near_loc
        
        
def behavior_nearest_value(fluor_array, behav_array):
    """
    Objective: To find the value in fluor_array that is
    closest to the value for each row in behav_array.

    Parameters
    ----------
    fluor_array: list
        This numpy array contains of all the time
        points corresponding to the green channel.

    behav_array: list
        This numpy array contains all of the
        start times when the behavior occurred.


    Returns
    -------
    near_value : list
        This list of floats contains the value in fluor_array
        that is cloest to each value in behav_array.
    """
    near_value = []
    for x in behav_array:
        n = [abs(i - x) for i in fluor_array]
        value = n.index(min(n))
        near_value.append(fluor_array[value])
    return near_value

def area_under_curve(behav_start_loc, behav_stop_loc, normsig):
    """
    Objective: To find the mean fluorescence value during the behavior.

    Parameters
    ----------
    behav_start_loc: list
        This list of integers contains the array location
        in norm sig for the start of a behavior event.

    behav_stop_loc: list
        This list of integers contains the array location
        in norm sig for the stop of a behavior event.
        
    normsig: list
        This numpy array contains the normalized 
        fluroescent values for the green channel.


    Returns
    -------
    mean : float
        This single float is the mean fluorescence value for the behavior.
    """
    if (len(behav_start_loc) != len(behav_stop_loc)):
        raise Error(f"behav_start_loc and behav_stop_loc should be equal")
    new_list = [x+1 for x in behav_stop_loc]
    num_events = len(behav_start_loc)
    total_len, total_sum = 0, 0
    for i in range(num_events):
        x, y = behav_start_loc[i], new_list[i]
        total_sum += sum(normsig[x:y])
        total_len += len(normsig[x:y])
        mean = total_sum / total_len
    return mean


# below functions are for zscores
def behavior_fluor(behav_start_loc, behav_stop_loc, normsig):
    new_list = [x+1 for x in behav_stop_loc]
    num_events = len(behav_start_loc)
    event_fluor = []
    for i in range(num_events):
        x, y = behav_start_loc[i], new_list[i]
        event_fluor.append(normsig[x:y])
    return event_fluor


def baseline_fluor(behav_start_loc, behav_stop_loc, normsig, timeprior):
    new_list = [x-timeprior for x in behav_stop_loc]
    num_events = len(behav_start_loc)
    baseline_fluor = []
    for i in range(num_events):
        x, y = new_list[i], behav_start_loc[i]
        baseline_fluor.append(normsig[x:y])
    return baseline_fluor


def base_mean(baseline_fluor):
    df = pd.DataFrame(baseline_fluor)
    baseline_mean = df.mean()
    baseline_mean = sum(baseline_mean)/ len(baseline_mean)
    return baseline_mean


def baselinestd(baseline_fluor):
    df = pd.DataFrame(baseline_fluor)
    base_std = df.std()
    mean_base_std = base_std.mean()
    return mean_base_std


def event_z(event_fluor, baseline_mean, mean_base_std):
    event_zscores = []
    for x in event_fluor:
        event_zscores.append((x - baseline_mean) / mean_base_std)
    return event_zscores


def zscore_max(event_zscores):
    df = pd.DataFrame(event_zscores)
    max_zscore = df.max()
    max_zscore = max(event_zscores)
    print(max_zscore)


def main():
    fTimeGreen_path = "./fTimeGreen.txt"
    behav_start_time_path = "./push_start_time.txt"
    behav_stop_time_path = "./push_stop_time.txt"
    normsig_path = "./sages2ndFit1.txt"
    
    fluor_array = file2numpy(fTimeGreen_path)
    
    behav_start_array = file2numpy(behav_start_time_path)
    #print(behav_start_array)
    behav_stop_array = file2numpy(behav_stop_time_path)
    #print(behav_stop_array)
    sages2ndFit = file2numpy(normsig_path)
    #print(behav_stop_array)
    
    behav_start_loc = behavior_nearest_loc(fluor_array, behav_start_array)
    #print(behav_start_loc)
    behav_start_value = behavior_nearest_value(fluor_array, behav_start_array)
    #print(behav_start_value)
    
    behav_stop_loc = behavior_nearest_loc(fluor_array, behav_stop_array)
    #print(behav_stop_loc)
    behav_stop_value = behavior_nearest_value(fluor_array, behav_stop_array)
    #print(behav_stop_value)
    
    auc = area_under_curve(behav_start_loc, behav_stop_loc, sages2ndFit)
    
    behavior_fluorescence = behavior_fluor(behav_start_loc, behav_stop_loc,
                                     sages2ndFit)

    baseline_fluorescence = baseline_fluor(behav_start_loc, behav_stop_loc,
                                        sages2ndFit, 300)

    baseline_mean = base_mean(baseline_fluorescence)

    baseline_stdev = baselinestd(baseline_fluorescence)
    
    zscore = event_z(behavior_fluorescence, baseline_mean, baseline_stdev)
    
    max_zscore = zscore_max(zscore)

#     with open("auc_results.csv", 'a') as file:
#         file.write(f:"{behavior_start_time} {auc}")
    
#     # add z-score function here
#     with open("peak_zscore_results.csv", 'a') as file:
#         file.write(f:"{behavior_start_time} {zscore_peak}") # second {} once zscore is integrated into main and you know the output name

#     with open("peak_zscore_latency_results.csv", 'a') as file:
#         file.write(f:"{behavior_start_time} {zscore_latency}") # second {} once zscore is integrated into main and you know the output name
                   
if __name__ == "__main__":
    main()
