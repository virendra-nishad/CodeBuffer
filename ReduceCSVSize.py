import os
import pandas as pd
from Dtypes import dtype_map

class ReduceCSVsize:
    def __init__(self):
        self.in_path = ""
        self.out_path = ""
        self.file_name = ""

    def setInPath(self, in_path):
        self.in_path = in_path

    def setOutPath(self, out_path):
        self.out_path = out_path

    def setFilename(self, file_name):
        self.file_name = file_name

    def getInPath(self):
        if self.in_path != "":
            return self.in_path
        else:
            raise Exception("Input path not set")

    def getOutPath(self):
        if self.out_path != "":
            return self.out_path
        else:
            raise Exception("Output path not set")

    def getFilename(self):
        if self.file_name != "":
            return self.file_name
        else:
            raise Exception("File name not set")

    def reduceCSVSize(self):
        df = pd.read_csv(os.path.join(self.getInPath(), self.getFilename()), dtype=dtype_map, index_col=False)
        # df = pd.read_csv(os.path.join(input_dir, csv_file), index_col=False)
        drop_col = ["FLowStartTimestamp", "SrcIP", "DstIP"]
        df.drop(drop_col, axis = 1)
        df["Protocol"].replace({6: 0, 17: 1}, inplace=True)
        df["Protocol"] = df["Protocol"].astype('bool')
        if not os.path.exists(self.getOutPath()):
            os.mkdir(self.getOutPath())
        df.to_csv(os.path.join(self.getOutPath(), self.getFilename()) , index=False)


if __name__ == "__main__":

    in_dir = "/home/viren/Thesis/2018OutputCSVLabel"
    out_dir = "/home/viren/Thesis/2018LabeledCSVsReduced"
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

    dir_list = []
    for _, dirs, _ in os.walk(in_dir):
        dir_list.extend(dirs)

    for dir_name in dir_list:
        print(dir_name)
        csv_list = []
        for _, _, files in os.walk(os.path.join(in_dir, dir_name)):
            csv_list.extend(files)    
        reduce_csv_size = ReduceCSVsize()
        reduce_csv_size.setInPath(os.path.join(in_dir, dir_name))
        reduce_csv_size.setOutPath(os.path.join(out_dir, dir_name))
        for csv_name in csv_list:
            reduce_csv_size.setFilename(csv_name)
            reduce_csv_size.reduceCSVSize()

# if not os.path.exists("OutData"):
#     os.mkdir("OutData")
# for csv_file in csv_list:
#     df = pd.read_csv(os.path.join(input_dir, csv_file), dtype=dtype_map, index_col=False)
#     # df = pd.read_csv(os.path.join(input_dir, csv_file), index_col=False)
#     drop_col = ["FLowStartTimestamp", "SrcIP", "DstIP"]
#     df.drop(drop_col, axis = 1)
#     df["Protocol"].replace({6: 0, 17: 1}, inplace=True)
#     df["Protocol"] = df["Protocol"].astype('bool')
#     df.to_csv("OutData/" + csv_file, index=False)
