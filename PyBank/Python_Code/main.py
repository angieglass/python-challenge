

import os
import csv


budgetCSV = os.path.join('..', 'Resources', 'budget_data.csv')

# Open file, it automatically sets to mode "read"
with open(budgetCSV, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")