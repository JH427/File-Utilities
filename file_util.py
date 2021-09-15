#file utilities
#jeharper@uga.edu
#Python3

from os import listdir
from os.path import isfile, join

n = '\n'

def f_listize(file, delimiter):
    """Returns the contents of a file as a list of lists, splitting each line by the delimiter."""
    return_arr = []
    arr_size = 0
    with open(file, 'r') as f:
        max_arr = []
        for l in f.readlines():
            max_arr.append(len(l.split(delimiter)))
        arr_size = max(max_arr)
    return_arr = [[] for i in range(arr_size)]
    with open(file, 'r') as f:
        temp_arr = []
        for line in f:
            line = line.split(delimiter)
            limit = len(line)
            for x in range(limit):
                return_arr[x].append(line[x])
    if return_arr:
        return return_arr
    else:
        return None

def f_search(file, search):
    results = []
    try:
        with open(file, 'r', errors='ignore') as f:
            count = 0
            for line in f:
                count += 1
                if search.lower() in line.lower():
                    results.append([count, line])
    except (FileNotFoundError, PermissionError) as e:
        return e
    if results:
        return results
    else:
        return None

def dir_search(path, search):
    files = [f for f in listdir(path) if isfile(join(path, f))]
    results = []
    for x in files:
        if f_search(path+x, search):
            results.append([x, f_search(x, search)])
    if results:
        return results
    else:
        return None

def dir_search_display(path, search):
    if dir_search(path, search):
        l = dir_search(path, search)
        for x in l:
            print('FILE '+x[0]+' CONTAINS '+'\"'+search+'\"'+' AT:')
            for z in x[1]:
                print('Line: '+str(z[0])+' -> '+'\"'+z[1].strip()+'\"')
    else:
        print('No Results')


        

            
                
