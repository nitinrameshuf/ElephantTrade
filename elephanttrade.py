#Author: Nitin Ramesh
import csv, os

#To-Do
# Implement python visualization

data = []
count = 0
#Below implementation , splits even if the data has comma inside it
with open(os.path.dirname(__file__) + '/Files/export.csv') as file:
    reader = csv.reader(file)
    for i in reader:
        data.append(i)
         
for i in data:
    print(i)


