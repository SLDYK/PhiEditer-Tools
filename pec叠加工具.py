from tkinter import filedialog
from tkinter import *
import os
filePath1=filedialog.askopenfilename(filetypes=[('原谱面','.pec')])
filePath2=filedialog.askopenfilename(filetypes=[('叠加谱面','.pec')])
newpec=[]
with open(filePath2,"r") as f:
    pecline=f.readlines()
    for i in range(0,len(pecline)):
        newpec.append(pecline[i])
    f.close()
with open(filePath1,"r") as t:
    pecline=t.readlines()
    for i in range(3,len(pecline)):
        line=pecline[i].split()
        if len(line)>=1:
            if "c" in line[0] or "n" in line[0]:
                line[1]=str(int(line[1])+30)
                line.append("\n")
                line=' '.join(line)
                newpec.append(line)
            else:
                line.append("\n")
                line=' '.join(line)
                newpec.append(line)
    t.close()
savePath=filedialog.asksaveasfilename(initialfile='combine.pec',filetypes=[("PEC谱面", ".pec")])
with open("savePath","wt") as c:
    c.write(pecline[0])
    c.write(pecline[1])
    for m in range(0,len(newpec)):
            if "n" in newpec[m]:
                c.write(str(newpec[m]))
                c.write(str(newpec[m+1]))
                c.write(str(newpec[m+2]))
    for m in range(0,len(newpec)):
            if "c" in newpec[m]:
                c.write(str(newpec[m]))
    c.close()
print('done')  
