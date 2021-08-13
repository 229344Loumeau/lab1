#!/usr/bin/env python3

#script that parses the log file and returns counts of unique events and the total number of log events

#Create List to store lines
uniquelist =[]

#Create counter
count =0

#open log file
with open("auth.log", "r") as f:
   
#iterate through log file and append unique lines
    for line in f:
         if line not in uniquelist:
                uniquelist.append(line)
                count = count + 1

#print unique lines in log file                
print(f"The number of events is: {count}")


#ToDO: Split Lines into events
