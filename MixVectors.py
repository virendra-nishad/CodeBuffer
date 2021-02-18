import os
import csv
import pandas as pd

filename_attack = "/home/viren/Thesis/SeparatedNormalAttack/attack.csv"
filename_normal = "/home/viren/Thesis/SeparatedNormalAttack/normal.csv"

out_path = "/home/viren/Thesis/MixedNormalAttack"
if not os.path.exists(out_path):
    os.mkdir(out_path)
threshold = 10**6


with open(filename_normal, 'r') as normal_read_obj, open(filename_attack, 'r') as attack_read_obj:
    csv_normal_dict_reader = csv.DictReader(normal_read_obj)
    csv_attack_dict_reader = csv.DictReader(attack_read_obj)
    row_normal = next(csv_normal_dict_reader, None)
    row_attack = next(csv_attack_dict_reader, None)
    file_counter = 0
    file_prefix = "attack_normal_mix"
    while row_attack != None and row_normal != None:
        row_counter = 1
        with open(os.path.join(out_path, file_prefix + str(file_counter) + ".csv"), 'w') as write_obj:
            csv_dict_writer = csv.DictWriter(write_obj, fieldnames=csv_attack_dict_reader.fieldnames)
            csv_dict_writer.writeheader()
            while row_counter < 10**5 and row_attack != None:
                csv_dict_writer.writerow(row_attack)
                row_counter += 1
                row_attack = next(csv_attack_dict_reader, None)

            while row_counter < 10**6 and row_normal != None:
                csv_dict_writer.writerow(row_normal)
                row_counter += 1
                row_normal = next(csv_normal_dict_reader, None)
                
        file_counter += 1
        print(file_counter)

    file_prefix = "leftover"
    if row_normal != None:
        with open(os.path.join(out_path, file_prefix + "_normal" + ".csv"), 'w') as write_obj:
            csv_dict_writer = csv.DictWriter(write_obj, fieldnames=csv_attack_dict_reader.fieldnames)
            csv_dict_writer.writeheader()
            while row_normal != None:
                csv_dict_writer.writerow(row_normal)
                row_normal = next(csv_normal_dict_reader, None)

    if row_attack != None:
        with open(os.path.join(out_path, file_prefix + "_attack" + ".csv"), 'w') as write_obj:
            csv_dict_writer = csv.DictWriter(write_obj, fieldnames=csv_attack_dict_reader.fieldnames)
            csv_dict_writer.writeheader()
            while row_attack != None:
                csv_dict_writer.writerow(row_attack)
                row_attack = next(csv_attack_dict_reader, None)
