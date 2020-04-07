import os
import pandas as pd

def excel_to_csv(dir = None):
    """ Export to .csv each excel file we encounter in the directory `dir`. 
        If no directory is given, it assumes the current working directory. """

    if dir == None:
        dir = os.getcwd()

    for file in os.listdir(dir): # we read the files in our folder
        if file[-3:] in ['xls','xlsx']: # if the file is an excel
            # we read the file
            df = pd.read_excel(file,header = None)

            # and we export it again to a csv with the following line
            df.to_csv(file[:-4] + '.csv',header = None, index = None,sep = '\t',encoding='utf-8')
