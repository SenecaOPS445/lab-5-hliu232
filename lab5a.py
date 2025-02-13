#!/usr/bin/env python3
# Author ID: hliu232

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    filename = open(file_name,'r')
    f_str = filename.read()
    filename.close()
    return f_str

def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    filename = open(file_name,'r')
    f_str = filename.read()
    f_list = f_str.split('\n')
    if f_list[-1] == '':
        f_list = f_list[:-1]
        
    filename.close()
    return f_list

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))