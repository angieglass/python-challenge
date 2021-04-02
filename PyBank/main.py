
import os                                                       #Import module OS 
import csv                                                      #Module to read and write tabular data in CSV format 

budget_path = os.path.join('Resources', 'budget_data.csv')      #Declaring the CSV file path 

total_months = []                                               #Will create a new list to count the lenght of the months
total_profitloss = []                                           #Will create a new list to sum all their values with the sum function. 
change_profitloss = []

with open(budget_path, newline= '') as budget_data:             #Naming file 
    csvreader = csv.reader(budget_data, delimiter=',')          #Return a reader object which will iterate over lines in the given csvfile
    #print(csvreader)                                           #Optional to see the csv.reader object

    csv_header = next(csvreader)                                #Reads the header row first and then skips it to exclude from the following analysis. 
    #print(f"CSV Header: {csv_header}")                         #Just in case we want to see our header ;) 

    for row in csvreader:                                       #Yay! a loop to generate our new lists. 
        total_months.append(row[0])                             #Creating the Months List
        total_profitloss.append((int(row[1])))                  #Creating the Profit/Loss List 

months_count = len(total_months)                                #Counting the lenght of the months lists with the len() function 
profitTotal = sum(total_profitloss)                             #Adding the sum() function which works only with lists. 


#My result here was IndexError: list index out of range. So I found out I needed to add a range to my list. 
#Had to Google this: for i in range(len(a_list)) iterates through numbers (which can be used for index access of a_list).
for change in range(len(total_profitloss)-1):                     
    change_profitloss.append(total_profitloss[change+1]-total_profitloss[change])

average_change = round(sum(change_profitloss)/len(change_profitloss),2) #Obtaining the sum of my new list between its lenght and rounding to 2 decimals  

max_change_profitloss = max(change_profitloss)                  #Max function in average change list 
min_change_profitloss = min(change_profitloss)                  #Min function in average change list 



print("'Financial Analysis'")                                     #Printing results!! 
print("-----------------------------------")
print(f"Total Months: {months_count}")
print(f"Total Profit/Loss: ${profitTotal}")
print(f"Average Change: ${average_change}")
print(f"Greatest increase in Profits: (${max_change_profitloss})")
print(f"Greatest decrease in Profits: (${min_change_profitloss})")