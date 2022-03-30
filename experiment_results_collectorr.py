import glob
import os
import shutil

list_of_files = glob.glob('*.txt')
print ("Parsing experiment result files in current directory... done.")
print ("Creating directory", "aggregated", "... done.\n")

res = []
for i in list_of_files:
    split_lines = i.split("_")
    for x in split_lines:
        if x not in res:
            res.append(x)

ip_address1 = res[0]
ip_address2 = res[4]
ip_address3 = res[8]

print("IP addresses encountered: ", "\t- " + ip_address1, "\t- " + ip_address2, "\t- " + ip_address3, sep="\n")
