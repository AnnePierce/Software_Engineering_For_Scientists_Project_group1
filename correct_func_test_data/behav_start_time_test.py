import sys
import numpy as np


def behavior_start_time(fTimeGreen, behav_start_time):

    minValAr = []
    minValidx = []
    for row in behav_start_time:
        times = min(abs(fTimeGreen - row))
        minValAr.append(times)
        locs = minValAr.index(fTimeGreen)
        minValidx.append(locs)
        print(minValAr)
        

    return minValAr, minValidx

if __name__ == "__main__":
    
    fTimeGreen_path = "./fTimeGreen.csv"
    behav_start_time_path = "./push_start_time.csv"
    behavior_start_time(fTimeGreen_path, 
                        behav_start_time_path)