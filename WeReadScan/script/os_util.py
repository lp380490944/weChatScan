'''
os_util.py
Copyright 2020 by Algebra-FUN
ALL RIGHTS RESERVED.
'''

import os
import shutil
import platform


def dir_check(dir):
    try:
        os.makedirs(f'{os.getcwd()}/{dir}')
    except FileExistsError:
        pass

def os_start_file(file_name):
    if platform.system() == "Windows":
        os.system(f"start {file_path}")
    elif platform.system() == "Darwin":  # macOS
        os.system(f"open {file_name}")
    else:
        print(f"Unsupported platform: {platform.system()}. Please open the file manually.")
def clear_temp(file_name):
    shutil.rmtree(file_name)
