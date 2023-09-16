import os
import struct
import zlib
from tkinter import filedialog

ask_dialogue = ""
ask_dialogue = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select BIN", filetype=(('bin file', '*.bin'),("ALL file",'*.*')))

if len(ask_dialogue) != 0:
        openfile = open(ask_dialogue, "rb")
        bin_file = openfile.read()
        openfile.close()

        n=len(ask_dialogue)-1
        solo_file_name = ""
        while n!= 0 and ask_dialogue[n] != '/':
                solo_file_name = ask_dialogue[n] + solo_file_name
                n -= 1

        out_put_folder = ""
        out_put_folder = solo_file_name + " OutPut//"

        if not os.path.exists(out_put_folder):
            os.makedirs(out_put_folder)

        line_reads=[]
        name_file =[]
        file_size = []
        file_offset = []

        i = 0
        L_name = 0

        header = bytearray()

        i = 0
        while bin_file[i:i+3] != b'PNG':
            i += 1
        header = bin_file[0:i-1]

        line_reads = header.split( b'/' )

        line_reads = line_reads[1:]

        for x in range(0, len(line_reads)):
            name_file.append(line_reads[x][:-7].decode('utf-8'))
            file_size.append(struct.unpack(">L",line_reads[x][-7:-3])[0])
            file_offset.append(struct.unpack(">L",b'\x00' + line_reads[x][-3:])[0])

        data = bytearray()
        for x in range(0, len(name_file)):
            data = bin_file[file_offset[x] : file_offset[x]+file_size[x]]
            out_file = open(out_put_folder+name_file[x], "wb+")
            out_file.write(data)
            out_file.close()

        print("Files Extracted")

