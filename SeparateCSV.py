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
        self.filename_normal = ""
        self.filename_attack = ""

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

    def setNormalFilename(self, filename):
        self.filename_normal = filename

    def getNormalFilename(self):
        if self.filename_normal != "":
            return self.filename_normal
        else:
            raise Exception("Filename not set")

    def setAttackFilename(self, filename):
        self.filename_attack = filename

    def getAttackFilename(self):
        if self.filename_attack != "":
            return self.filename_attack
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
        dir_list = self.getFolderList(self.in_path)
        total_file_list = []
        for dir_name in dir_list:
            files = self.getFileList(os.path.join(in_path, dir_name))
            for filename in files:
                total_file_list.append(os.path.join(in_path, dir_name, filename))
        # obtained total filename with their path

        if not os.path.exists(self.getOutPath()):
            os.mkdir(self.getOutPath())
    
        temp_df = pd.read_csv(total_file_list[0], index_col=False)
        cols = list(temp_df.columns)
        with open(self.filename_normal, 'w') as normal_write_obj, open(self.filename_attack, 'w') as attack_write_obj:
            csv_normal_dict_writer = csv.DictWriter(normal_write_obj, fieldnames=cols, extrasaction="ignore")
            csv_normal_dict_writer.writeheader()
            csv_attack_dict_writer = csv.DictWriter(attack_write_obj, fieldnames=cols, extrasaction="ignore")
            csv_attack_dict_writer.writeheader()
            for file_path in total_file_list:
                print(file_path)
                with open(file_path, 'r') as read_obj:
                    csv_dict_reader = csv.DictReader(read_obj)
                    for row in csv_dict_reader:
                        if row["Label_Normal_0"] == "False":
                            csv_normal_dict_writer.writerow(row)
                        elif row["Label_Normal_0"] == "True":
                            csv_attack_dict_writer.writerow(row)
                        else:
                            print("Neither attack nor normal")


if __name__ == "__main__":

    in_path = "/home/viren/Thesis/2018OutputCSVLabel"
    out_path = "/home/viren/Thesis/SeparatedNormalAttack"

    merge_csv = MergeCSVs()
    merge_csv.setInPath(in_path)
    merge_csv.setOutPath(out_path)
    merge_csv.setNormalFilename(os.path.join(out_path, "normal.csv"))
    merge_csv.setAttackFilename(os.path.join(out_path, "attack.csv"))

    merge_csv.mergeCSVs()