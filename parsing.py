#!/usr/bin/python3
"""
Contains the function file_reader which will parse the columns in
the data file given, and deinterleave the time and fluorescence.
"""

import sys
import numpy as np


def file_reader(filename):
    """
    Objective: To deinterleave the time and fluorescence for the red,
    isosbestic, and green channels.

    Parameters
    ----------
    filename: string
        This will provide the file path needed to the raw data file.


    Returns
    -------
    fTimeRed : array
        This array holds the timestamps for the red fluorescence.

    fTimeIsosbestic : array
        This array holds the timestamps for the isosbestic fluorescence.

    fTimeGreen : array
        This array holds the timestamps for the green fluorescence.

    f1red : array
        This array holds the floats for the
        red fluorescence for the subject.

    f1isosbestic : array
        This array holds the floats for the
        isosbestic fluorescence for the subject.

    f1green : array
        This array holds the floats for the
        green fluorescence for the subject.

    f2red : array
        This array holds the floats for the
        red fluorescence for the partner or stranger.

    f2isosbestic : array
        This array holds the floats for the
        isosbestic fluorescence for the partner or stranger.

    f2green : array
        This array holds the floats for the
        green fluorescence for the partner or stranger.
    """
    data = np.loadtxt(filename)

    # time column
    ftime = data[:, [0]]  # timestamps
    ftimemin = ftime / (60*1000)

    # identifying fluorescent columns
    fgreen1 = data[:, [3]]  # green for vole 1 (subject)
    fgreen2 = data[:, [2]]  # green for vole 2 (stranger or partner)
    fred1 = data[:, [5]]  # red for vole 1
    fred2 = data[:, [4]]  # red for vole 2
    last = len(fgreen1)  # len of green vole 1

    # deinterleaving fluroescence for vole 1
    f1red = fred1[24:last-2:3]
    f1isosbestic = fgreen1[25:last-1:3]
    f1green = fgreen1[26:last-1:3]

    # deinterleaving fluroescence for vole 2
    f2red = fred2[24:last-2:3]
    f2isosbestic = fgreen2[25:last-1:3]
    f2green = fgreen2[26:last-1:3]

    # deinterleaving time
    fTimeRed = ftime[24:last-2:3]
    fTimeIsosbestic = ftime[25:last-1:3]
    fTimeGreen = ftime[26:last-1:3]

    return fTimeRed, fTimeIsosbestic, fTimeGreen, f1red, f1isosbestic, f1green, f2red, f2isosbestic, f2green


def main():
    raw_data = "/home/jovyan/swefs_group1/correct_test_data/FiberPhoSig2020-08-22T09_00_59.csv"
    fTimeRed, fTimeIsosbestic, fTimeGreen, f1red, f1isosbestic, f1green, f2red, f2isosbestic, f2green = file_reader(raw_data)


if __name__ == "__main__":
    main()
