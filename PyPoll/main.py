# To keep in mind: 
# A def could work, 
# How to add percentage format to my results? 



import os                                                      
import csv                                                      

candidate_path = os.path.join('Resources', 'election_data.csv')     

voters_count = []
khan_total = []
correy_total = []
li_total = []
otooley_total = []

with open(candidate_path, newline= '') as candidatesCSV:             
    csvreader = csv.reader(candidatesCSV, delimiter=',')         
    print(csvreader)                                           
    csv_header = next(csvreader)                             

    for row in csvreader: 
        voters_count.append(row[2]) 
        if row[2] == "Khan":
            khan_total.append(row[2])
        elif row[2] == "Correy": 
            correy_total.append(row[2])
        elif row[2] == "Li":
            li_total.append(row[2])
        elif row[2] == "O'Tooley":
            otooley_total.append(row[2])  
    
voters_count = len(voters_count)
khan_total = len(khan_total)
correy_total = len(correy_total)
li_total = len(li_total)
otooley_total = len(otooley_total)

print("Election results\n------------------")
print(f'Total voters count: {voters_count}\n-----------------')
print(f'Khan: {khan_total}')
print(f'Correy: {correy_total}')
print(f'Li: {li_total}')
print(f"O'Tooley: {otooley_total}\n------------------------")
