#!/usr/bin/python3
"""
Contains a function to find the green fluroescent times
that are closest to the behavior start and stop times.
"""


import sys


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
