def file_reader(filename): 
    # Import Data and deinterleave
    
    fdata = open(filename)
    # Load file containing florescence data
    f_time = fdata.strip().split() 
    # Pull out red and green florescence for each vole 
    ftime = f_time[0] 
    # Parse the time for each florescence 
    fgreen2 = f_time[2]
    # Parses green florescence for vole 2 (stranger or partner)
    fgreen1 = f_time[3]
    # Parses green florescence for vole 1 (subject)
    fred2 = f_time[4]
    # Parses red florescenece for vole 2 (stranger or partner)
    fred1 = f_time[5]
    # Parses red florescence for vole 1 (subject)
    
    ftime = f_time[0] / (60*1000) 
    # Converts ftime from milliseconds to minutes
    
    
    # All columns containing florescence must be the same length to plot them
    # This creates a standard length for all columns 
    
    # For each column, the true florescence data is interleaved such that every 3rd data point is the true florescence
    # We need to "deinterleave" the data by taking each 3rd data point. 
    # We have to identify what data point to start which is 25 because the first 25 data points are unreliable
    # Next, we have to identify whether the 25th data point is the red, green, or isosbestic florescent channel. 
    # Once the channel is identified, it follows a pattern of red, isosbestic, green...
    
    #Deinterleave the 3 channels for vole 1 (subject)
    
    #Deinterleave the 3 channels for vole 2 (partner or stranger) 
    
    return fdata
