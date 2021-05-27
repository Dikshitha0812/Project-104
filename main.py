import csv
with open("data.csv",newline="") as f :
    reader=csv.reader(f)
    file_data=list(reader)

# Deleting the first row in list file data that are column  names
file_data.pop(0)

# Bringing Weight data into new list
weight=[]
for i in range(len(file_data)):
    data=file_data[i][2]
    weight.append(data)

print("Mean,Median,Mode of data :")

#Calculating Mean
sum =0
for i in weight:
    sum=sum+float(i)

values=len(weight)
mean=sum/values
print("Mean of the data :",mean)

# Calculaating Median
weight.sort()
if values%2 ==0 :
    num1=float(weight[values//2])
    num2=float(weight[values//2-1])
    median=(num1+num2)/2

else :
    median=weight[values//2]

print("Median of data :",median)

# Calculating Mode
range1=0
range2=0
range3=0
range4=0
range5=0
range6=0
range7=0
range8=0
range9=0
range10=0


for i in range(len(weight)):
    if 75<float(weight[i])<85:
        range1=range1+1
    elif 85<float(weight[i])<95:
        range2=range2+1
    elif 95<float(weight[i])<105:
        range3=range3+1
    elif 105<float(weight[i])<115:
        range4=range4+1
    elif 115<float(weight[i])<125:
        range5=range5+1
    elif 125<float(weight[i])<135:
        range6=range6+1
    elif 135<float(weight[i])<145:
        range7=range7+1
    elif 145<float(weight[i])<155:
        range8=range8+1
    elif 155<float(weight[i])<165:
        range9=range9+1
    elif 165<float(weight[i])<175:
        range10=range10+1    
    

#print(range1,range2,range3,range4,range5,range6,range7,range8,range9,range10)
mode=(125+135)/2
print("Mode of the data:", mode)