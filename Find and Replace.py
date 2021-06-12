import os
import sys

filename=input("Enter a filename: ")
if ".txt" in filename:
	filename=filename.replace(".txt","")

try:
	file_in = open(filename+".txt", "rt")
except:
	input("File not found!")
	sys.exit()

old_string=input("Enter the old string to be replaced: ")
new_string=input("Enter the new string to be replaced: ")




file_out = open("out.txt", "wt")
for line in file_in:
	file_out.write(line.replace(old_string, new_string))

file_in.close()
file_out.close()
os.remove(filename+".txt")
os.rename("out.txt",filename+".txt")
input("Done!!!")