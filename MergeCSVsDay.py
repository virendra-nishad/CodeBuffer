import os
import pandas as pd
import csv
from Dtypes import dtype_map

# This class is expecting input folder which contains csv to be merged
# and output folder where csv have to be kept
class MergeCSVs:
    def __init__(self):
        self.in_path = ""
        self.out_path = ""
        self.out_filename = ""

    def setInPath(self, in_path):
        self.in_path = in_path

    def setOutPath(self, out_path):
        self.out_path = out_path

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

    def setOutFilename(self, out_filename):
        self.out_filename = out_filename

    def getOutFilename(self):
        if self.out_filename != "":
            return self.out_filename
        else:
            raise Exception("Filename not set")

    def getFolderList(self, in_path):
        dir_list = []
        for _, dirs, _ in os.walk(in_path):
            dir_list.extend(dirs)
        return dir_list

    def getFileList(self, in_path):
        file_list = []
        for _, _, files in os.walk(in_path):
            file_list.extend(files)
        return file_list

    def mergeCSVs(self):
        if not os.path.exists(self.getOutPath()):
            os.mkdir(self.getOutPath())
        file_path_list = []
        file_list = self.getFileList(self.getInPath())
        for file_name in file_list:
            file_path_list.append(os.path.join(self.getInPath(), file_name))
    
        temp_df = pd.read_csv(file_path_list[0], index_col=False)
        cols = list(temp_df.columns)
        cols_remove = ["FLowStartTimestamp", "SrcIP", "DstIP"]
        col_names = [col for col in cols if col not in cols_remove]
        # mergeCSVs(dir_name, total_file_list, output_dir, col_names)
        # dir_name = self.getInputDir().split('/')[-1]
        with open(os.path.join(self.getOutPath(), self.getOutFilename()), 'w') as write_obj:
            csv_dict_writer = csv.DictWriter(write_obj, fieldnames=col_names, extrasaction="ignore")
            csv_dict_writer.writeheader()
            for file_path in file_path_list:
                with open(file_path, 'r') as read_obj:
                    csv_dict_reader = csv.DictReader(read_obj)
                    for row in csv_dict_reader:
                        csv_dict_writer.writerow(row)


if __name__ == "__main__":

    in_path = "/home/viren/Thesis/2018OutputCSVLabel"
    out_path = "/home/viren/Thesis/2018MergedLabeledCSVs"

    dir_list = []
    for _, dirs, _ in os.walk(in_path):
        dir_list.extend(dirs)
    # walk through each folder present in in_path
    # Do below for each folder present in in_path, i.e merge csv based on folder
    for dir_name in dir_list:

        # below are the basic setup require before using MergeCSVs class
        merge_csv = MergeCSVs()
        merge_csv.setInPath(os.path.join(in_path, dir_name))
        merge_csv.setOutPath(out_path)
        merge_csv.setOutFilename(dir_name + ".csv")

        merge_csv.mergeCSVs()