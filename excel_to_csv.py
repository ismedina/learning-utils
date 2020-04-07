#!/usr/bin/env python
''' This is a small script that reads each excel file in the current directory and exports it to
    a .csv file, with utf-8 encoding and the separator between columns being a tabulator.
    The output is perfect for importing it from apps such as Anki'''

from os import listdir
import pandas as pd

# we export to .csv each excel file we encounter
for file in listdir(): # we read the files in our folder
    if file[-3:] == 'xls': # if the file is an excel
        # we read the file
        df = pd.read_excel(file,header = None)

        # and we export it again to a csv with the following line
        df.to_csv(file[:-4] + '.csv',header = None, index = None,sep = '\t',encoding='utf-8')
