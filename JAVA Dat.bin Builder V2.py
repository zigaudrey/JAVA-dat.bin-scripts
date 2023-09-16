import os
import struct
from tkinter import filedialog

folder_name = ""
folder_name = filedialog.askdirectory(title='Select Folder')

if len(folder_name) != 0:

    n=len(folder_name)-1
    solo_folder_name = ""
    while n!= 0 and folder_name[n] != '/':
            solo_folder_name = folder_name[n] + solo_folder_name
            n -= 1

    folder_name += "//"

    file_list = os.listdir(folder_name)
    header= bytearray()
    body=bytearray()

    print(file_list)

    file_size = []
    file_offset = []

    for i in range(len(file_list)):
        header += b'/' + bytes(file_list[i].encode("utf-8")) + bytes(7)

    for i in range(len(file_list)):
        data_file = open(folder_name + file_list[i], 'rb')
        data_bin = data_file.read()
        data_file.close()
        file_offset.append(len(header)+len(body))    
        file_size.append(len(data_bin))
        body += data_bin

    header= bytearray()
    for i in range(len(file_list)):
        header += b'/' + bytes(file_list[i].encode("utf-8")) + struct.pack(">L", file_size[i]) + struct.pack(">L", file_offset[i])[1:]
        
    out_file = open(solo_folder_name + " NEW.bin", "wb+")
    out_file.write(header+body)
    out_file.close()

    print("Data.Bin Done")
