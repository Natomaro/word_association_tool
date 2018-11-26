#!/usr/bin/env python
# import sys
# print (sys.argv)

#search_string = input("Enter your word pal: ")
search_string = "east"
with open('everything.txt', mode='r') as infile:
    for line in infile:
        if search_string in line:
            with open('output.txt', mode='a') as outfile:
                outfile.writelines([line])