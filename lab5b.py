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

def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    f = open(file_name,'a')
    f.write(string_of_lines)
    f.close()

    return f


def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    f = open(file_name,'w')
    for item in list_of_lines:
        f.write(str(item) + '\n')
    f.close()

    return f

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    
    f1_read = open(file_name_read,'r')
    f_list = f1_read.read()
    tem_list = f_list.split('\n')
    if tem_list[-1] == '':
        tem_list = tem_list[:-1]

    f2_write = open(file_name_write,'w')
    number = 1
    for item in tem_list:
        f2_write.write(str(number) + ':' + str(item) + '\n')
        number = number + 1
    
    f1_read.close()
    f2_write.close()
    return f2_write
    


if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))