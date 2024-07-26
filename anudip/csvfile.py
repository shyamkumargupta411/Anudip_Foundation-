import csv
f=open("shyam.csv",'a',newline="")
wo=csv.writer(f)
data=[["a","b","c","d"],[16,15,14,13],[12,52,46,90],[36,52,75,94]]
wo.writerows(data)
f=open("shyam.csv",'r')
re=csv.reader(f)
li=list(re)
for i in li:
    print(i)
f.close()
