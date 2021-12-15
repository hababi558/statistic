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
 
data=Counter(newData)
modeDataForRange={
    '50-60':0,
    '60-70':0,
    '70-80':0
}
for height,occurance in data.items():
    if 50<float(height)<60:
        modeDataForRange['50-60']+=occurance
    elif 60<float(height)<70:
        modeDataForRange['60-70']+=occurance
    elif 70<float(height)<80:
        modeDataForRange['70-80']+=occurance

modeRange,modeOccurance=0,0

for range,occurance in modeDataForRange.items():
    if occurance>modeOccurance:
        modeRange,modeOccurance=[int(range.split('-')[0]),int(range.split('-')[1])],occurance
        

mode=float((modeRange[0]+modeRange[1])/2)
print(f"Mode is: ->{mode:2f}")