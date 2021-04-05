import os                                                               #Import os module                                               
import csv                                                              #Module to read and write tabular data in CSV format 

candidate_path = os.path.join('Resources', 'election_data.csv')         #Declaring the CSV file path 

voters_count = []                                                       #Lists for each candidate 
khan_total = []
correy_total = []
li_total = []
otooley_total = []

with open(candidate_path, newline= '') as candidatesCSV:                #Naming file    
    csvreader = csv.reader(candidatesCSV, delimiter=',')                #Return a reader object which will iterate over lines in the given csvfile
    #print(csvreader)                                                   #Optional to see the csv.reader object
    csv_header = next(csvreader)                                        #Reads the header row first and then skips it to exclude from the following analysis. 
    #print(csv_header)                                                  #Just in case we want to see our header ;)

    for row in csvreader:                                               #A loop with conditionals to obtain each candidate's lists 
        voters_count.append(row[2]) 
        if row[2] == "Khan":
            khan_total.append(row[2])
        elif row[2] == "Correy": 
            correy_total.append(row[2])
        elif row[2] == "Li":
            li_total.append(row[2])
        elif row[2] == "O'Tooley":
            otooley_total.append(row[2])  

voters_count = len(voters_count)                                        #Votes count per candidate 
khan_total = len(khan_total)
correy_total = len(correy_total)
li_total = len(li_total)
otooley_total = len(otooley_total)

khan_p = "{:.3%}".format(khan_total/voters_count)                       #Votes percentage per candidate with format .000% 
correy_p = "{:.3%}".format(correy_total/voters_count)
li_p = "{:.3%}".format(li_total/voters_count)
otooley_p = "{:.3%}".format(otooley_total/voters_count)


candidates_dic ={                                                       #Dictionary for candidates and their votes count 
    "Khan": khan_total, 
    "Correy": correy_total, 
    "Li": li_total,
    "O'Tooley": otooley_total
    } 

winner = max(candidates_dic, key = candidates_dic.get)               #Find the key with max value in my dictionary. Found this function on Kite.com 


print("Election results\n------------------------")                     #Printing all results 
print(f'Total Votes: {voters_count}\n------------------------')
print(f'Khan: {khan_p} ({khan_total})')
print(f'Correy: {correy_p} ({correy_total})')
print(f'Li: {li_p} ({li_total})')
print(f"O'Tooley: {otooley_p} ({otooley_total})\n------------------------")
print(f'Winner: {winner} \n------------------------')



output_path = os.path.join("Analysis", "results.txt")                 #Writing results to a text file, using '\n' for the newline 
with open(output_path, 'w') as text_file:
 
    text_file.write("Election results\n")
    text_file.write("-----------------------------------\n")            
    text_file.write(f'Total Votes: {voters_count}\n')
    text_file.write("-----------------------------------\n")
    text_file.write(f'Khan: {khan_p} ({khan_total})\n')
    text_file.write(f'Correy: {correy_p} ({correy_total})\n')
    text_file.write(f'Li: {li_p} ({li_total})\n')
    text_file.write(f"O'Tooley: {otooley_p} ({otooley_total})\n")
    text_file.write("-----------------------------------\n")
    text_file.write(f'Winner: {winner}\n')
    text_file.write("-----------------------------------\n")
