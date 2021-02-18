import seaborn as sns
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Dtypes import dtype_map
import json

in_file = "/home/viren/Thesis/2018LabeledCSVsReduced/Thursday-15-02-2018/capEC2AMAZ-O4EL3NG-172.31.67.38.csv"
temp = pd.read_csv(in_file, index_col=False)

cols = temp.columns

in_dir = "/home/viren/Thesis/2018LabeledCSVsReduced"

dir_list = []
for _, dirs, _ in os.walk(in_dir):
    dir_list.extend(dirs)


corr_count = {}
for col in cols:
    corr_count[col] = 0
# print(corr_count)
with open("beforeCount.json", 'w') as outFile:
    json.dump(corr_count, outFile, indent=4)

for dir_name in dir_list:
    file_list = []
    for _,_,files in os.walk(os.path.join(in_dir, dir_name)):
        file_list.extend(files)
    for file_name in file_list:
        in_file = os.path.join(in_dir, dir_name, file_name)
        df = pd.read_csv(in_file, index_col=False)
        # drop_col = ["FLowStartTimestamp", "SrcIP", "DstIP"]
        # df.drop(drop_col, axis=1, inplace=True)
        cor_matrix = df.corr().abs()
        upper_tri = cor_matrix.where(np.triu(np.ones(cor_matrix.shape),k=1).astype(np.bool))
        corelated_cols = [column for column in upper_tri.columns if any(upper_tri[column] > 0.95)]
        for col in corelated_cols:
            if col in corr_count.keys():
                corr_count[col] += 1
            else:
                print(col)
        # print(corr_count)
        # print()
        # print()
with open("afterCount.json", 'w') as outFile:
    json.dump(corr_count, outFile, indent=4)