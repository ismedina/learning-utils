#!/usr/bin/env python
from learning_utils import *

''' This is a small script that reads each excel file in the current directory and exports it to
    a .csv file, with utf-8 encoding and the separator between columns being a tabulator.
    The output is perfect for importing it from apps such as Anki'''
    
if __name__ == "__main__":
    excel_to_csv()