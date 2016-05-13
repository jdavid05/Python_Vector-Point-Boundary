#========================================================================================#
# Name   : Ass3_Davidson.py                                                              #
# Purpose: Check the boundaries of polygons                                              #
#            - Read the boundaries of the polygon.                                       #
#            - Calculate the number of points falling within the polygon.                #
#            - Write the results to an output file.                                      #
#                                                                                        #
# Written By: Joseph Davidson                                                            #
#========================================================================================#

Ans = "Y"
# Do you want to process a file?
while Ans[0].upper() == "Y":
    
    # Initiate a loop to retrieve the input data file.
    itworked = False
    while itworked == False:
    
        # Ask user to input the file and directory.
        FILE = raw_input("Enter the name of the file you would like to analyze: \n")
        NAME = FILE
        
        if FILE[-3:].upper() != "TXT":      
            FILE += ".txt"                                                          

        try:
            FILE = open(FILE,'r')           
            itworked = True



        # If the file cannot be opened (EXCEPTION) tell the user 
        #   and repeat the question.
        except:
            print "That file is not accepted. Please choose another..."

    # Start a loop to create the output data file.    
    itworked2 = False
    while itworked2 == False:

        # Create an output file concatenating Results with the input filename.
        OUTFILE ="Results_" + NAME
        OUTNAME = OUTFILE

        # If the user did not add .txt to the filename, add it.
        if OUTFILE[-3:].upper() != "TXT":      
            OUTFILE += ".txt"                                                          

        try:
            OUTFILE = open(OUTFILE,'w')           
            itworked2 = True

        # If .txt can not be added to the filename (EXCEPTION) create
        #   a file with the default name.
        except:
            OUTFILE = open('Results.txt','w')
            itworked2 = True

    # Produce the output screen.
    print "\nProcessing file: %s" % NAME
    OUTFILE.write("Results for file: %s\n" % NAME)
    print"Output will be written to file: %s.txt\n" % OUTNAME

    # Initiate the counters.
    linecount = 0
    inside = 0
    outside = 0

    # Read the first line.
    line = FILE.readline()

    # Initiate a loop to read the input file.
    while line != "":
        
        # Extract the three fields.
        type,x,y = line.split(',')
        
        # Clean the data
        type = type.strip('"')
        
        # Convert the x and y values to float (real) numbers.
        x = float(x)
        y = float(y)
        
        # Initiate a loop to separate the data fields.
        # Display the header and results.
        # Write the results to the output file.
        for i in line:
            if type.upper() == "LOWER LIMIT":
                llx = x
                lly = y
                xy = 1
                break
            if type.upper() == "UPPER LIMIT":
                ulx = x
                uly = y
                xyz = 1
                break
            if xyz>0 and xy>0:
                print "--------------------------------------------------"
                print "    coordinates (%4.1f, %4.1f) - are upper limits." % (ulx, uly)
                OUTFILE.write ("\n--------------------------------------------------")
                OUTFILE.write("\n    coordinates (%4.1f, %4.1f) - are upper limits." % (ulx, uly))
                print "    coordinates (%4.1f, %4.1f) - are lower limits." % (llx, lly)
                print "--------------------------------------------------"
                OUTFILE.write("\n    coordinates (%4.1f, %4.1f) - are lower limits." % (llx, lly))
                OUTFILE.write("\n--------------------------------------------------")
                xy = 0
                xyz = 0
            elif x < llx:
                print "    pair: (%4.1f, %4.1f) - x value is LOW." % (x, y)
                linecount = linecount + 1
                outside = outside + 1
                OUTFILE.write("\n    pair: (%4.1f, %4.1f) - x value is LOW." % (x, y))
                break
            elif y < lly:
                print "    pair: (%4.1f, %4.1f) - y value is LOW." % (x, y)
                linecount = linecount + 1
                outside = outside + 1
                OUTFILE.write("\n    pair: (%3.1f, %3.1f) - y value is LOW." % (x, y))
                break
            elif x > ulx:
                print "    pair: (%4.1f, %4.1f) - x value is HIGH." % (x, y)
                linecount = linecount + 1
                outside = outside + 1
                OUTFILE.write("\n    pair: (%4.1f, %4.1f) - x value is HIGH." % (x, y))
                break
            elif y > uly:
                print "    pair: (%4.1f, %4.1f) - y value is HIGH." % (x, y)
                linecount = linecount + 1
                outside = outside + 1
                OUTFILE.write("\n    pair: (%4.1f, %4.1f) - y value is HIGH." % (x, y))
                break
            else:
                print "    pair: (%4.1f, %4.1f) - is OK." % (x, y)
                linecount = linecount + 1
                inside = inside + 1
                OUTFILE.write("\n    pair: (%4.1f, %4.1f) - is OK." % (x, y))
                break
        # Read the next line in the data.
        line = FILE.readline()
    # Close the input file.
    FILE.close()

    # Print the summary header.
    print "\n\n\t\tSummary        "
    OUTFILE.write("\n\n\n\t\tSummary        ")
    print "%s" %('='*50)
    OUTFILE.write("\n%s" %('='*50))
    
    # Print the number of vertices and how many were inside and outside of the boundaries.
    print "There were %d vertices in the data." % linecount
    OUTFILE.write("\nThere were %d vertices in the data." % linecount)
    print "    - %d points were inside the boundary." % inside
    OUTFILE.write("\n    - %d points were inside the boundary." % inside)
    print "    - %d points were outside the boundary." % outside
    OUTFILE.write("\n    - %d points were outside the boundary." % outside)
    # Close the output file
    OUTFILE.close()
    # Ask the user if they would like to read another file.
    Ans = raw_input("\nWould you like to read another file? :\n")
    if len(Ans) == 0:
        Ans = "Y"
# Close the program.
print "Goodbye"
