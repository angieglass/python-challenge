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


#Votes per candidate 
voters_count = len(voters_count)
khan_total = len(khan_total)
correy_total = len(correy_total)
li_total = len(li_total)
otooley_total = len(otooley_total)

#Percentages per candidate 

khan_p = "{:.3%}".format(khan_total/voters_count)
correy_p = "{:.3%}".format(correy_total/voters_count)
li_p = "{:.3%}".format(li_total/voters_count)
otooley_p = "{:.3%}".format(otooley_total/voters_count)

print("Election results\n------------------------")
print(f'Total voters count: {voters_count}\n------------------------')
print(f'Khan: {khan_p} ({khan_total})')
print(f'Correy: {correy_p} ({correy_total})')
print(f'Li: {li_p} ({li_total})')
print(f"O'Tooley: {otooley_p} ({otooley_total})\n------------------------")
print(f'Winner: \n------------------------')

