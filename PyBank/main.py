
import os                                                       #Import module OS 
import csv                                                      #Module to read and write tabular data in CSV format 

budget_path = os.path.join('Resources', 'budget_data.csv')      #Declaring the CSV file path 

total_months = []                                               #Will create a new list to count the lenght of the months
total_profitloss = []                                           #Will create a new list to sum all their values with the sum function. 

with open(budget_path, newline= '') as budget_data:             #Naming file 
    csvreader = csv.reader(budget_data, delimiter=',')          #Return a reader object which will iterate over lines in the given csvfile
    #print(csvreader)                                           #Optional to see the csv.reader object. 

    csv_header = next(csvreader)                                #Reads the header row first and then skips it to exclude from the following analysis. 
    print(f"CSV Header: {csv_header}")                          #Just in case we want to see our header ;) 

    for row in csvreader:                                       #Yay! a loop to generate our new lists. 
        total_months.append(row[0])                             #Creating the Months List
        total_profitloss.append((int(row[1])))                  #Creating the Profit/Loss List 

months_count = len(total_months)                                #Counting the lenght of the months lists with the len() function 
profitTotal = sum(total_profitloss)                             #Adding the sum() function which works only with lists. 



print("Financial Analysis")                                     #Printing results!! 
print(f"Total Months: {months_count}")
print(f"Total Profit/Loss: ${profitTotal}")