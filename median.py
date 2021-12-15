import csv 
from collections import Counter 

with open('SOCR-HeightWeight.csv',newline='') as f:
    reader=csv.reader(f)
    fileData=list(reader)

fileData.pop(0)
newData=[]

for i in range(len(fileData)):
    num=fileData[i][1]
    newData.append(float(num))
 
n=len(newData)
newData.sort()
if n%2==0:
    median1=float(newData[n//2])
    median2=float(newData[n//2-1])
    median=(median2+median1)/2
else:
    median=newData[n//2]
print('meadian is: '+ str(median))
