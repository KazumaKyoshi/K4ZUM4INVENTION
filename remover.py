import glob
import os

list_of_files = glob.glob('*.gz')

latest_file = max(list_of_files, key=os.path.getctime)

print("Using scheme: backup_yyyymmdd.tar.gz")
if max(list_of_files, key=os.path.getctime):
    print("[delete]", list_of_files[0])
    print("[delete]", list_of_files[1])
    print("[keep]", latest_file)
