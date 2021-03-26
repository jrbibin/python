import os
import sys
from subprocess import call
#source = input("Enter File Source Path:")
d = input("Enter File Destination Path:")
q = []
with open("D:/New folder/source.txt") as file:
    for source in file:
        q.append(source)
for a in q:
    n = a.strip('\n')
    call(["robocopy",n,d,"/S","/E","/XC","/XN","/XO"])
print("End")