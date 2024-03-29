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

5. behavior_fluor: This function will give the normalized fluorescence
values during each behavior event.

6. baseline_fluor: This function will give the normalized fluorescence
values during the baseline period.

7. base_mean: This function will give the mean value of the baseline.

8. baselinestd: This function will give the standard
deviation of the baseline period.

9. event_z: This function will give the zscore values
for each value in behavior_fluor.

10. zscpre_max: This function will give the maximum
zscore value and location of the max zscore.
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
    array: list
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
    near_loc: list
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
    near_value: list
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
    mean: float
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
def behavior_fluor(behav_start_loc, timeafter, normsig):
    """
    Objective: To find the normalized fluorescence value during the behavior.

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
    event_fluor: array
        This array contains the normalized fluorescence
        values during each behavior event.
    """
    new_list = [x+timeafter for x in behav_start_loc]
    num_events = len(behav_start_loc)
    event_fluor = []
    for i in range(num_events):
        x, y = behav_start_loc[i], new_list[i]
        event_fluor.append(normsig[x:y])
    return event_fluor


def baseline_fluor(behav_start_loc, behav_stop_loc, normsig, timeprior):
    """
    Objective: To find the normalized fluorescence value during the baseline.

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

    timeprior: int
        An interger that is the idex number of the time period the user
        wants the baseline to be. Right now its 300 which is 5 seconds.


    Returns
    -------
    baseline_fluor: array
        This array contains the normalized fluorescence
        values for the baseline.
    """
    new_list = [x-timeprior for x in behav_stop_loc]
    num_events = len(behav_start_loc)
    baseline_fluor = []
    for i in range(num_events):
        x, y = new_list[i], behav_start_loc[i]
        baseline_fluor.append(normsig[x:y])
    return baseline_fluor


def base_mean(baseline_fluor):
    """
    Objective: To find the mean of the baseline period.

    Parameters
    ----------
    baseline_fluor: array
        This array contains the normalized fluorescence
        values for the baseline.


    Returns
    -------
    baseline_mean: float
        A single float which is the mean of the baseline.
    """
    df = pd.DataFrame(baseline_fluor)
    baseline_mean = df.mean()
    baseline_mean = sum(baseline_mean)/len(baseline_mean)
    return baseline_mean


def baselinestd(baseline_fluor):
    """
    Objective: To find the mean standard deviation of the baseline.

    Parameters
    ----------
    baseline_fluor: array
        This array contains the normalized fluorescence
        values for the baseline.


    Returns
    -------
    mean_base_std: float
        A single float which is the mean standard devioation of the baseline
        This is done by getting the standard deviation of all the baseline
        events and then taking the mean of all the standard deviations.
    """
    df = pd.DataFrame(baseline_fluor)
    base_std = df.std()
    mean_base_std = base_std.mean()
    return mean_base_std


def event_z(event_fluor, baseline_mean, mean_base_std):
    """
    Objective: To find the zscores for the fluorescence during each event.

    Parameters
    ----------
    event_fluor: array
        This array contains the normalized fluorescence
        values during each behavior event.

    baseline_mean: float
        A single float which is the mean of the baseline.

    mean_base_std: float
        A single float which is the mean standard devioation of the baseline
        This is done by getting the standard deviation of all the baseline
        events and then taking the mean of all the standard deviations.


    Returns
    -------
    event_zscores: array
        This array contains the zscores for event.
    """
    event_zscores = []
    for x in event_fluor:
        event_zscores.append((x - baseline_mean) / mean_base_std)
    return event_zscores


def zscore_max(event_zscores):
    """
    Objective: To find the max zscore value and location of the max zscore.

    Parameters
    ----------
    event_zscores: array
        This array contains the zscores for event.


    Returns
    -------
    max_zscore: float
        This float is the max zscore value for the event.
    """
    df = pd.DataFrame(event_zscores)
    row_means = df.mean(axis=0)
    row_means = row_means.to_list()
    max_zscore = max(row_means)
    index = row_means.index(max_zscore)
    idx_sec = index/60
    return max_zscore, idx_sec


def main():
    fTimeGreen_path = "./fTimeGreen.txt"
    behav_start_time_path = "./push_start_time.txt"
    behav_stop_time_path = "./push_stop_time.txt"
    normsig_path = "./sages2ndFit1.txt"

    fluor_array = file2numpy(fTimeGreen_path)

    behav_start_array = file2numpy(behav_start_time_path)
    # print(behav_start_array)
    behav_stop_array = file2numpy(behav_stop_time_path)
    # print(behav_stop_array)
    sages2ndFit = file2numpy(normsig_path)
    # print(behav_stop_array)

    behav_start_loc = behavior_nearest_loc(fluor_array, behav_start_array)
    # print(behav_start_loc)
    behav_start_value = behavior_nearest_value(fluor_array, behav_start_array)
    # print(behav_start_value)

    behav_stop_loc = behavior_nearest_loc(fluor_array, behav_stop_array)
    # print(behav_stop_loc)
    behav_stop_value = behavior_nearest_value(fluor_array, behav_stop_array)
    # print(behav_stop_value)

    auc = area_under_curve(behav_start_loc, behav_stop_loc, sages2ndFit)

    behavior_fluorescence = behavior_fluor(behav_start_loc, 300,
                                           sages2ndFit)

    baseline_fluorescence = baseline_fluor(behav_start_loc, behav_stop_loc,
                                           sages2ndFit, 300)

    baseline_mean = base_mean(baseline_fluorescence)

    baseline_stdev = baselinestd(baseline_fluorescence)

    zscore = event_z(behavior_fluorescence, baseline_mean, baseline_stdev)

    max_zscore, idx_sec = zscore_max(zscore)

    # auc, z-score max value, and zscore max value location appended here
    file = open("peak_zscore_results.csv", 'a')
    file.write(f"behavior:{behav_start_time_path} auc:{auc} zscore:{max_zscore} max zscore location{idx_sec}")


if __name__ == "__main__":
    main()
