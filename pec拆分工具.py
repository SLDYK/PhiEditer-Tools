from tkinter import filedialog
from tkinter import *
def sgn(n):
    if n==0:
        return 0
    else:
        return 1
print("选择谱面：")
filePath=filedialog.askopenfilename(filetypes=[('PE谱面','.pec')])
with open(filePath,"r") as t:
    alldata=t.readlines()
    data=[]
    head=[]
    useless=[]
    for i in range(len(alldata)):
        if "c" in alldata[i]:
            data.append(alldata[i])
        elif "n" in alldata[i]:
            data.append(alldata[i])
            data.append(alldata[i+1])
            data.append(alldata[i+2])
        elif "#" in alldata[i] or "&" in alldata[i]:
            useless.append(alldata[i])
        else:
            head.append(alldata[i])
    t.close()
num=[]
for i in range(len(data)):
    if "c" in data[i]:
        num.append(int(data[i].split()[1]))
maxline=max(num)+1
amount=int(maxline/30)+sgn(maxline%30)
print("将会拆分出 "+str(amount)+" 个文件\n")
for i in range(0,amount):
    chart=[]
    for j in range(len(data)):
        if "c" in data[j]:
            if int(data[j].split()[1]) in range(i*30,i*30+30):
                chart.append(data[j].split())
        elif "n" in data[j]:
            if int(data[j].split()[1]) in range(i*30,i*30+30):
                chart.append(data[j].split())
                chart.append(data[j+1])
                chart.append(data[j+2])
    for m in range(len(chart)):
        if type(chart[m])==list:
            chart[m][1]=str(int(chart[m][1])%30)
            chart[m]=" ".join(chart[m])+"\n"
    savePath=filedialog.asksaveasfilename(initialfile='Split '+str(i+1)+'.pec',filetypes=[("PEC谱面", ".pec")])
    with open(savePath,"w") as t:
        for k in range(0,len(head)):
            if head[k] !="\n":
                t.write(head[k])
        for k in range(0,len(chart)):
            t.write(chart[k])
        print("done")
        t.close()
