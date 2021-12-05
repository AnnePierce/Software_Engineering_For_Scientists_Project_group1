import sys
import numpy as np


print(array_from_file)
# function 1
def file_reader(filename, print_header=True, delimiter=','):

    # creates empty list that will be returned.
    data_list = []
    # opens and reads the file
    with open(filename, 'r') as opened_file:
        file_lines = opened_file.readlines()
        for line_number, line in enumerate(file_lines):
            data_list.append(line.split(delimiter))
        print(data_list)

def behavior_start_time(fTimeGreen, behav_start_time):
        
        
def main():
    filename = "/home/jovyan/swefs_group1/correct_func_test_data/push_start_time.txt"
    file_reader(filename)

    
# def behavior_start_time(fTimeGreen, behav_start_time):

#     minValAr = []
#     minValidx = []
#     fdata = open(filename)
#     print(behav_start_time)
    
#     for row in behav_start_time:
#         times = min(abs(fTimeGreen - row))
#         minValAr.append(times)
#         locs = minValAr.index(fTimeGreen)
#         minValidx.append(locs)
#         print(minValAr)
        

#     return minValAr, minValidx

if __name__ == "__main__":
    main()
    
#     fTimeGreen_path = "./fTimeGreen.txt"
#     behav_start_time_path = "./push_start_time.txt"
#     behavior_start_time(fTimeGreen_path, 
#                         behav_start_time_path)
