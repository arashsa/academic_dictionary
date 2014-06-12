__author__ = 'arashsaidi'

from main_functions import read_xml, read_txt
import glob

list_of_freqs = []


def read_all_files(p, ending):
    # reads all files in a folder: '/folder/*.xml'
    global list_of_freqs
    path = p
    files = glob.glob(path)
    for name in files:
        # read_current_file returns a frequency distribution
        freq_dist = read_current_file(name, ending)
        list_of_freqs.append(freq_dist)

    return list_of_freqs


def read_current_file(f, ending):
    # calls methods according to file type
    if ending == 'xml':
        return read_xml(f)
    elif ending == 'txt':
        return read_txt(f)
    else:
        print 'ERROR: Do not support type of file'

