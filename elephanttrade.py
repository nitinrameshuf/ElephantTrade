#Author: Nitin Ramesh
import csv, os
import db_access

#To-Do
# Implement python visualization
# Data: 
# [0] country_or_area,
# [1] year,
# [2] comm_code,
# [3] commodity,
# [4] flow,
# [5] trade_usd,
# [6] weight_kg,
# [7] quantity_name,
# [8] quantity,
# [9] category

data = []
count = 0
#Below implementation , splits even if the data has comma inside it
with open(os.path.dirname(__file__) + '/Files/mini_trade.csv') as file:
    reader = csv.reader(file) 
    for i in reader:
        print(i)



    # for i in reader:
    #     if count != 0 :
    #         print(i)
    #         #data.append(i)
