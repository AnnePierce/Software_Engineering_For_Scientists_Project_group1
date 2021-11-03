#!/usr/bin/python3
"""
Contains a function to align the behavior start and stop times to the closest fluorescent times that exist
"""

def behavior_start_time(fTimeGreen, behav_start_time,):
    """
    Objective: Create a list that contains what will be the new start time
    for the behavior. The new start time is the value in fTimeGreen that is
    the closest to each time value in behav_start_time

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
        This list of floats contains the new start time
        for each behavior which is the time in fTimeGreen
        that is cloests to each behavior start time.
    """