#!usr/bin/python3
"""
Uses parsing and functions
"""
import parsing
import allfunctions

def main():
    raw_data = "/home/jovyan/swefs_group1/correct_test_data/FiberPhoSig2020-08-22T09_00_59.csv"
    fTimeGreen = "/home/jovyan/swefs_group1/correct_func_test_data/fTimeGreen.txt"
    sages2ndFit1 = "/home/jovyan/swefs_group1/correct_func_test_data/sages2ndFit1.txt"
    
    parsed_data = parsing.file_reader(raw_data)

    allfunctions.statistics(fTimeGreen, "/home/jovyan/swefs_group1/test_data/givesniff_start_time.txt", "/home/jovyan/swefs_group1/test_data/givesniff_stop_time.txt", sages2ndFit1)

    allfunctions.statistics(fTimeGreen, "/home/jovyan/swefs_group1/test_data/receivesniff_start_time.txt", "/home/jovyan/swefs_group1/test_data/receivesniff_stop_time.txt", sages2ndFit1)

    allfunctions.statistics(fTimeGreen, "/home/jovyan/swefs_group1/test_data/rear_start_time.txt", "/home/jovyan/swefs_group1/test_data/rear_stop_time.txt", sages2ndFit1)

    allfunctions.statistics(fTimeGreen, "/home/jovyan/swefs_group1/test_data/push_start_time.txt", "/home/jovyan/swefs_group1/test_data/push_stop_time.txt", sages2ndFit1)

    allfunctions.statistics(fTimeGreen, "/home/jovyan/swefs_group1/test_data/groomself_start_time.txt", "/home/jovyan/swefs_group1/test_data/groomself_stop_time.txt", sages2ndFit1)


if __name__ == "__main__":
    main()

