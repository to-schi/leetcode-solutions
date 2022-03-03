#solve with bash!
# Read from the file file.txt and output the tenth line to stdout.
# https://leetcode.com/problems/tenth-line/
sed -n '10p' < file.txt



#python version :) 
# fhand = open('tenth-line.txt', 'r')
# def tenthline():
#     count = 0
#     for line in fhand:
#         count = count + 1
#         if count == 10:
#             return line

# print(tenthline())
