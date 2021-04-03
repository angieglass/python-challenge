
import os                                                       #Import module OS 
import csv                                                      #Module to read and write tabular data in CSV format 

budget_path = os.path.join('Resources', 'budget_data.csv')      #Declaring the CSV file path 

total_months = []                                               #Will create a new list to count the lenght of the months
total_profitloss = []                                           #Will create a new list to sum all their values with the sum function. 
change_profitloss = []
month_max = []
month_min = []

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


#While printing I had an error here called IndexError: list index out of range. So I found out I needed to add a range to my list. 
#Had to Google this: for i in range(len(a_list)) iterates through numbers (which can be used for index access of a_list). Life saving! 
for change in range(len(total_profitloss)-1):                     
    change_profitloss.append(total_profitloss[change+1]-total_profitloss[change])

average_change = round(sum(change_profitloss)/len(change_profitloss),2) #Obtaining the sum of my new list between its lenght and rounding to 2 decimals  

max_change_profitloss = max(change_profitloss)                  #Max function in average change list 
min_change_profitloss = min(change_profitloss)                  #Min function in average change list 

for x,y in zip(total_months[1:], change_profitloss):            #Created a new zip list between the months [1:] to exclude the first value with the change_profitloss
        if y == max_change_profitloss:                          #Looping to find the max value and obtaining the max and min value and adding to my lists to capture this values 
                month_max.append(x)
                #print(month_max)
        if y == min_change_profitloss:
                month_min.append(x)
                #print(month_min)       



print("'Financial Analysis'")                                     #Printing results!! 
print("-----------------------------------")
print(f"Total Months: {months_count}")
print(f"Total Profit/Loss: ${profitTotal}")
print(f"Average Change: ${average_change}")
print(f"Greatest increase in Profits: {month_max} (${max_change_profitloss})")
print(f"Greatest decrease in Profits: {month_min} (${min_change_profitloss})")



output_path = os.path.join("Analysis", "results.txt")            #Writing to a text file, using '\n' for the newline 
with open(output_path, 'w') as text_file:
 
    text_file.write("Financial Analysis\n")                  
    text_file.write("-----------------------------------\n")
    text_file.write(f"Total Months: {months_count}\n")
    text_file.write(f"Total Profit/Loss: ${profitTotal}\n")
    text_file.write(f"Average Change: ${average_change}\n")
    text_file.write(f"Greatest increase in Profits: {month_max} (${max_change_profitloss})\n")
    text_file.write(f"Greatest decrease in Profits: {month_min} (${min_change_profitloss})\n")
