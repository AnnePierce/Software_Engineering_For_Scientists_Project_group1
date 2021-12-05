def file_reader(filename):
    fdata = open(filename)

    # time column
    f_time = fdata.strip().split()
    ftime = f_time[0]  #timestamps
    ftime = f_time[0] / (60*1000)  #converts ftime from ms to min
    last = len(fgreen1) # len of green vole 1

    # identifying fluorescent columns
    fgreen1 = f_time[3]  # green for vole 1 (subject)
    fgreen2 = f_time[2]  #green for vole 2 (stranger or partner)
    fred1 = f_time[5]  # red for vole 1
    fred2 = f_time[4]  # red for vole 2

    # deinterleaving fluroescence for vole 1
    f1red = fred1[24: 3, last-2]
    f1isosbestic = fgreen1[25: 3, last]
    f1green = fgreen1[26: 3, last-1]

    # deinterleaving fluroescence for vole 2
    f2red = fred2[24: 3, last-2]
    f2isosbestic = fgreen2[25: 3, last]
    f2green = fgreen2[26: 3, last-1]

    # deinterleaving time
    fTimeRed = ftime[24: 3, last-2]
    fTimeIsosbestic = ftime[25: 3, last]
    fTimeGreen = ftime[26: 3, last-1]


    return fTimeGreen,f1green,f2green
