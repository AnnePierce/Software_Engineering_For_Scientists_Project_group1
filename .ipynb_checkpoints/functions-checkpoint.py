#!/usr/bin/python3
"""
Contains the following functions:
1. behavior_start_time: This function finds the green fluorescent times 
that are closest to the behavior start times.

2. behavior_stop_time: This function finds the green fluorescent times 
that are closest to the behavior stop times.

3. event_fluors: This function creates a list of the normalized fluorescense
during each behavior event that is present.

4. behavior_auc: This function will give the mean fluorescence 
for the behavior.

"""


import sys
import numpy as np


def behavior_start_time(fTimeGreen, behav_start_time):
    """
    Objective: Create a list that contains what will be the new start times
    for the behavior. The new start times are the values in fTimeGreen that
    are the closest to each time value in behav_start_time.

    Parameters
    ----------
    fTimeGreen: list
        This list of floats contains all the time
        points corresponding to the green channel.

    behav_start_time: list
        This list of floats contains all of the
        start times when the behavior occurred.


    Returns
    -------
    minValAr : list
        This list of floats contains the new start times
        for each occurance of the behavior, which is the time
        in fTimeGreen that is closest to each behavior start time.
    minValidx : list
        This list of integers contains the location where
        minValAr exists in fTimeGreen.
    """
    minValAr = []
    minValidx = []
    for row in behav_start_time:
        times = min(abs(fTimeGreen-row))
        minValAr.append(times)
        locs = minValAr.index(fTimeGreen)
        minValidx.append(locs)

    return minValAr, minValidx


def behavior_stop_time(fTimeGreen, behav_stop_time):
    """
    Objective: Create a list that contains what will be the new stop times
    for the behavior. The new stop times are the values in fTimeGreen that
    are the closest to each time value in behav_stop_time.

    Parameters
    ----------
    fTimeGreen: list
        This list of floats contains all the time
        points corresponding to the green channel.

    behav_stop_time: list
        This list of floats contains all of the
        stop times when the behavior occurred.


    Returns
    -------
    minValAr_s : list
        This list of floats contains the new stop times
        for each occurance of the behavior, which is the time
        in fTimeGreen that is closest to each behavior stop time.
    minValidx_s : list
        This list of integers contains the location where
        minValAr_s exists in fTimeGreen.
    """
    minValAr_s = []
    minValidx_s = []
    for row in behav_stop_time:
        times = min(abs(fTimeGreen-row))
        minValAr_s.append(times)
        locs = minValAr_s.index(fTimeGreen)
        minValidx_s.append(locs)

    return minValAr_s, minValidx_s

def event_fluors(minValidx, minValidx_s, sages2ndFit1):
    """
    Objective: Return a list containing the normalized fluorescence
    during each event for the behavior being analyzed.

    Parameters
    ----------
    minValidx : list
        This list of integers (created in the behavior_start_time function)
        contains the location of the start fluorescent time 
        for the behavior being analyzed.
        
    minValidx_s : list
       This list of integers (created in the behavior_stop_time function)
        contains the location of the start fluorescent time 
        for the behavior being analyzed.
        
    sages2ndFit1 : list
       This list of floats is the normalized fluorescence for the female.


    Returns
    -------
    behavior_fluorescence : list
        Returns a list containing the entire normalized fluorescence 
        during each event for the behavior being analyzed.
    """
    behavior_fluorescence = []
    for start in minValidx
        for stop in minValidx_s
            behavior_fluor = normsig[start:stop]
            behavior_fluorescence.append(behavior_fluor)
    return behavior_fluorescence


def behavior_auc(behavior_fluorescence):
    """
    Objective: Return a single float that is the mean fluorescence during 
    the behavior being analyzed which represents the area under the curve.

    Parameters
    ----------
    behavior_fluorescence : list
        This is a list containing the entire normalized fluorescence 
        during each event for the behavior being analyzed.


    Returns
    -------
    mean_fluor : float
        Return a single float that is the mean fluorescence during 
        the behavior being analyzed which represents the area under the curve.
    """
    mean_fluor = np.matrix.mean(axis=None, dtype=floats, out=None)[source]
    return mean_fluor