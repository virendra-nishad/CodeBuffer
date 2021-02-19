import os
import pandas as pd
import csv


if __name__ == "__main__":

    in_path = "/home/viren/Thesis/SeparatedNormalAttack"
    out_path = os.path.join(os.getcwd(), "DatasetInfo")

    cols_to_drop = ["FLowStartTimestamp", "SrcIP", "DstIP", "SrcPort", "DstPort", "Protocol"]

    file_list = []
    for _, _, files in os.walk()


    # dir_list = []
    # for _, dirs, _ in os.walk(in_path):
    #     dir_list.extend(dirs)
    # # walk through each folder present in in_path
    # # Do below for each folder present in in_path, i.e merge csv based on folder

    # for dir_name in dir_list:

    #     # below are the basic setup require before using MergeCSVs class
    #     merge_csv = MergeCSVs()
    #     merge_csv.setInPath(os.path.join(in_path, dir_name))
    #     merge_csv.setOutPath(out_path)
    #     merge_csv.setOutFilename("single.csv")

    #     merge_csv.mergeCSVs()