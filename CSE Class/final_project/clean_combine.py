#import the modules
import os
import pandas as pd
#read the path
goalie_path = "~/datascience/cse441/final_project/raw_21_goalies"
#list all the files from the directory
file_list = os.listdir(goalie_path)
file_list