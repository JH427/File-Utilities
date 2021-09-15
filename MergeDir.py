#Merge All PDF Documents in directory
#jeharper@uga.edu
#Python3

from PyPDF2 import PdfFileMerger, PdfFileReader
from os.path import isfile, join
from os import listdir

def merge_dir(path):

    merger = PdfFileMerger()

    files = [f for f in listdir(path) if isfile(join(path, f))]

    print(files)

    for f in files:
        if 'pdf' in f[-3:].lower():
            merger.append(PdfFileReader(path+f, 'rb'))

    merger.write(path+'summary.pdf')
            

