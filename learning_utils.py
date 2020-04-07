import os
import pandas as pd
import numpy as np
from colorama import Fore, Back, Style

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


def isempty(line):
    """ Checks if a line is empty  (contains only witespaces or tabs)"""
    if len(line.replace("\n","").replace(" ","").replace("\t","")) == 0:
        return True
    else:
        return False


def format_md(line):
    """ Convert Markdown line to highlighted text in the terminal. 
    Only useful for our particular case! """
    parts = line[2:].split('*')
    for (i, part) in enumerate(parts):
        if i%2 == 1:
            parts[i] = Fore.BLACK + Back.YELLOW + part + Style.RESET_ALL

    return "* " + "".join(parts)

def keep(line):
    """ Checks if a line is relevant, i.e. it is neither a header nor an empty line """
    if ("#" not in line) and not isempty(line):
        return True
    else:
        return False

def random_grammar(file, N):
    """ Takes markdown file `file` and returns a random subset of `N` the listed (with `*`) items. 
        Also highlights text inside `*`"""

    with open(file,'r') as f:
        lines = f.readlines()

    keep_lines = [line for (i, line) in enumerate(lines) if keep(line)]

    keep_lines = [line.replace("\n","") for line in keep_lines]
    # TODO: allow decaying probability distribution
    p = np.ones(len(keep_lines))
    p = p/sum(p)

    if N > len(keep_lines):
        N = len(keep_lines)
        print("There are only {} grammar resources.".format(N))

    print("")
    print("  " + Fore.BLACK + Back.RED + "Today's random grammar:" + Style.RESET_ALL) 
    print("  -----------------------\n")


    for i in range(N):
        i = np.random.choice(range(len(keep_lines)), size = 1, p = p)[0]
        
        print(format_md(keep_lines[i]))
        
        keep_lines.pop(i)
        p = p[range(len(p)) != i]
        p = p/sum(p)
        
    print("\n")