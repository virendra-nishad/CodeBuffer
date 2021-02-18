import os
import csv
import pandas as pd
from Dtypes import dtype_map

filename = "/home/viren/Thesis/SeparatedNormalAttack/attack.csv"

# chunksize = 10 ** 6
# with pd.read_csv(filename, chunksize=chunksize, dtype=dtype_map) as reader:
#     for chunk in reader:
#         print(chunk)

counter = 0
with open(filename) as csvfile:  
    data = csv.DictReader(csvfile)
    for row in data:
        counter += 1
print(counter)