#clean_combine.py
#Author Aedan Wells
#date 11/5/2022

import os
import pandas as pd
#read the path
goalie_path = "raw_21_goalies/"
skater_path = "raw_21_skaters/"
#list all the files from the directory
goalie_file_list = os.listdir(goalie_path)
skater_file_list = os.listdir(skater_path)

df_append = pd.DataFrame()
#get all of the goalie files together
for file in goalie_file_list:
    temp_frame = pd.read_csv(goalie_path + "/" +file)
    temp_main = pd.DataFrame(temp_frame[temp_frame['situation'] == 'all'])
    df_append = df_append.append(temp_main, ignore_index=True)

df_append.to_csv('raw_21_goalies/full_goalies.csv')

frame_append = pd.DataFrame()
#get all of the skater files together
for file in skater_file_list:
    temp_frame = pd.read_csv(skater_path + "/" +file)
    temp_main = pd.DataFrame(temp_frame[temp_frame['situation'] == 'all'])
    frame_append = frame_append.append(temp_main, ignore_index=True)

frame_append.to_csv('raw_21_skaters/full_skaters.csv')