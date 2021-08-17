def triangle_pattern():
    row=20       #define how many rows
    for i in range(row): # this is for line change loop
        for j in range(row-i,1,-1):       # this is for space print in reverse order length
            print(" ",end=" ")              # print space and end is used to prevent from line break 
        for k in range(0,i+1):              # this is used for star print
            print(" * ",end=" ") 
        print()                            #used for line change 







triangle_pattern()
    