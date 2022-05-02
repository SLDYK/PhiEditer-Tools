#coding=utf-8
from tkinter import filedialog
import json
import os
import math
from tkinter import *
import threading

def stzpq():
    def json2pec(acc):
        def jt(time):#json time
            if time<=1:
                return "1"
            elif time>=64000:
                return "2000"
            else:
                return str(time/32+1)
        def jht(time):#json holdTime
            return time/32
        def js(speed):#json speed
            return str(round(speed,1))
        def jr(rotate):#json rotate
            return str(round(rotate*-1,3))
        def ja(alpha):#json alpha
            if alpha>=1:
                return "255"
            elif alpha<=0:
                return "0"
            else:
                return str(round(alpha*255,3))
        def f3x(pos):#json formatVersion3 positionX
            return str(round(pos*2048,3))
        def f3y(pos):#json formatVersion3 positionY
            return str(round(pos*1400,3))
        def jrx(pos):#json relative positionX
            return str(round(pos*1024/9,3))
        if acc=="":
            acc=0.125
        else:
            acc=float(acc)
        pec=[]
        filePath=filedialog.askopenfilename(filetypes=[('官谱格式','.json')])
        acc=float(acc)*32
        with open(filePath,"r") as t:
            chart=json.load(t)
            pec.append(str(chart["offset"]-150)+"\n")
            pec.append("bp 0.000 "+str(chart["judgeLineList"][0]["bpm"])+"\n")
            for i in range(0,len(chart["judgeLineList"])):
                mult=chart["judgeLineList"][0]["bpm"]/chart["judgeLineList"][i]["bpm"]
                for j in range(0,len(chart["judgeLineList"][i]["speedEvents"])):
                    chart["judgeLineList"][i]["speedEvents"][j]["startTime"]=chart["judgeLineList"][i]["speedEvents"][j]["startTime"]*mult
                    chart["judgeLineList"][i]["speedEvents"][j]["endTime"]=chart["judgeLineList"][i]["speedEvents"][j]["endTime"]*mult
                for j in range(0,len(chart["judgeLineList"][i]["notesBelow"])):
                    chart["judgeLineList"][i]["notesBelow"][j]["time"]=chart["judgeLineList"][i]["notesBelow"][j]["time"]*mult
                    chart["judgeLineList"][i]["notesBelow"][j]["holdTime"]=chart["judgeLineList"][i]["notesBelow"][j]["holdTime"]*mult
                for j in range(0,len(chart["judgeLineList"][i]["notesAbove"])):
                    chart["judgeLineList"][i]["notesAbove"][j]["time"]=chart["judgeLineList"][i]["notesAbove"][j]["time"]*mult
                    chart["judgeLineList"][i]["notesAbove"][j]["holdTime"]=chart["judgeLineList"][i]["notesAbove"][j]["holdTime"]*mult
                for j in range(0,len(chart["judgeLineList"][i]["judgeLineDisappearEvents"])):
                    chart["judgeLineList"][i]["judgeLineDisappearEvents"][j]["startTime"]=chart["judgeLineList"][i]["judgeLineDisappearEvents"][j]["startTime"]*mult
                    chart["judgeLineList"][i]["judgeLineDisappearEvents"][j]["endTime"]=chart["judgeLineList"][i]["judgeLineDisappearEvents"][j]["endTime"]*mult
                for j in range(0,len(chart["judgeLineList"][i]["judgeLineMoveEvents"])):
                    chart["judgeLineList"][i]["judgeLineMoveEvents"][j]["startTime"]=chart["judgeLineList"][i]["judgeLineMoveEvents"][j]["startTime"]*mult
                    chart["judgeLineList"][i]["judgeLineMoveEvents"][j]["endTime"]=chart["judgeLineList"][i]["judgeLineMoveEvents"][j]["endTime"]*mult
                for j in range(0,len(chart["judgeLineList"][i]["judgeLineRotateEvents"])):
                    chart["judgeLineList"][i]["judgeLineRotateEvents"][j]["startTime"]=chart["judgeLineList"][i]["judgeLineRotateEvents"][j]["startTime"]*mult
                    chart["judgeLineList"][i]["judgeLineRotateEvents"][j]["endTime"]=chart["judgeLineList"][i]["judgeLineRotateEvents"][j]["endTime"]*mult
            for i in range(0,len(chart["judgeLineList"])):
                j=0
                while j<len(chart["judgeLineList"][i]["judgeLineDisappearEvents"])-1:
                    if chart["judgeLineList"][i]["judgeLineDisappearEvents"][j]["end"]==chart["judgeLineList"][i]["judgeLineDisappearEvents"][j+1]["start"] and chart["judgeLineList"][i]["judgeLineDisappearEvents"][j+1]["endTime"]-chart["judgeLineList"][i]["judgeLineDisappearEvents"][j]["startTime"]<=acc:
                        chart["judgeLineList"][i]["judgeLineDisappearEvents"][j]["end"]=chart["judgeLineList"][i]["judgeLineDisappearEvents"][j+1]["end"]
                        chart["judgeLineList"][i]["judgeLineDisappearEvents"][j]["endTime"]=chart["judgeLineList"][i]["judgeLineDisappearEvents"][j+1]["endTime"]
                        del chart["judgeLineList"][i]["judgeLineDisappearEvents"][j+1]
                        j=j-1
                    j=j+1
                j=0
                while j<len(chart["judgeLineList"][i]["judgeLineRotateEvents"])-1:
                    if chart["judgeLineList"][i]["judgeLineRotateEvents"][j]["end"]==chart["judgeLineList"][i]["judgeLineRotateEvents"][j+1]["start"] and chart["judgeLineList"][i]["judgeLineRotateEvents"][j+1]["endTime"]-chart["judgeLineList"][i]["judgeLineRotateEvents"][j]["startTime"]<=acc:
                        chart["judgeLineList"][i]["judgeLineRotateEvents"][j]["end"]=chart["judgeLineList"][i]["judgeLineRotateEvents"][j+1]["end"]
                        chart["judgeLineList"][i]["judgeLineRotateEvents"][j]["endTime"]=chart["judgeLineList"][i]["judgeLineRotateEvents"][j+1]["endTime"]
                        del chart["judgeLineList"][i]["judgeLineRotateEvents"][j+1]
                        j=j-1
                    j=j+1
                j=0
                while j<len(chart["judgeLineList"][i]["judgeLineMoveEvents"])-1:
                    if chart["judgeLineList"][i]["judgeLineMoveEvents"][j]["end"]==chart["judgeLineList"][i]["judgeLineMoveEvents"][j+1]["start"] and chart["judgeLineList"][i]["judgeLineMoveEvents"][j]["end2"]==chart["judgeLineList"][i]["judgeLineMoveEvents"][j+1]["start2"] and chart["judgeLineList"][i]["judgeLineMoveEvents"][j+1]["endTime"]-chart["judgeLineList"][i]["judgeLineMoveEvents"][j]["startTime"]<=acc:
                        chart["judgeLineList"][i]["judgeLineMoveEvents"][j]["end"]=chart["judgeLineList"][i]["judgeLineMoveEvents"][j+1]["end"]
                        chart["judgeLineList"][i]["judgeLineMoveEvents"][j]["end2"]=chart["judgeLineList"][i]["judgeLineMoveEvents"][j+1]["end2"]
                        chart["judgeLineList"][i]["judgeLineMoveEvents"][j]["endTime"]=chart["judgeLineList"][i]["judgeLineMoveEvents"][j+1]["endTime"]
                        del chart["judgeLineList"][i]["judgeLineMoveEvents"][j+1]
                        j=j-1
                    j=j+1
            for i in range(0,len(chart["judgeLineList"])):
                speedlist=[]
                for j in range(0,len(chart["judgeLineList"][i]["speedEvents"])):
                    pec.append("cv "+str(i)+" "+jt(chart["judgeLineList"][i]["speedEvents"][j]["startTime"])+" "+str(round(float(js(chart["judgeLineList"][i]["speedEvents"][j]["value"]))*7,1))+"\n")
                    speedlist.append([chart["judgeLineList"][i]["speedEvents"][j]["startTime"],chart["judgeLineList"][i]["speedEvents"][j]["endTime"],chart["judgeLineList"][i]["speedEvents"][j]["value"]])
                for j in range(0,len(chart["judgeLineList"][i]["notesAbove"])):
                    if chart["judgeLineList"][i]["notesAbove"][j]["type"]==3:
                        for a in range(0,len(speedlist)):
                            if chart["judgeLineList"][i]["notesAbove"][j]["time"]>=speedlist[a][0] and chart["judgeLineList"][i]["notesAbove"][j]["time"]<speedlist[a][1]:
                                speednote=str(round(chart["judgeLineList"][i]["notesAbove"][j]["speed"]/speedlist[a][2],1))
                        pec.append("n2 "+str(i)+" "+jt(chart["judgeLineList"][i]["notesAbove"][j]["time"])+" "+str(float(jt(chart["judgeLineList"][i]["notesAbove"][j]["time"]))+jht(chart["judgeLineList"][i]["notesAbove"][j]["holdTime"]))+" "+jrx(chart["judgeLineList"][i]["notesAbove"][j]["positionX"])+" 1 0\n# "+speednote+"\n& 1.00\n")
                    elif chart["judgeLineList"][i]["notesAbove"][j]["type"]==1:
                        pec.append("n1 "+str(i)+" "+jt(chart["judgeLineList"][i]["notesAbove"][j]["time"])+" "+jrx(chart["judgeLineList"][i]["notesAbove"][j]["positionX"])+" 1 0\n# "+js(chart["judgeLineList"][i]["notesAbove"][j]["speed"])+"\n& 1.00\n")
                    elif chart["judgeLineList"][i]["notesAbove"][j]["type"]==2:
                        pec.append("n4 "+str(i)+" "+jt(chart["judgeLineList"][i]["notesAbove"][j]["time"])+" "+jrx(chart["judgeLineList"][i]["notesAbove"][j]["positionX"])+" 1 0\n# "+js(chart["judgeLineList"][i]["notesAbove"][j]["speed"])+"\n& 1.00\n")
                    else:
                        pec.append("n3 "+str(i)+" "+jt(chart["judgeLineList"][i]["notesAbove"][j]["time"])+" "+jrx(chart["judgeLineList"][i]["notesAbove"][j]["positionX"])+" 1 0\n# "+js(chart["judgeLineList"][i]["notesAbove"][j]["speed"])+"\n& 1.00\n")
                for j in range(0,len(chart["judgeLineList"][i]["notesBelow"])):
                    if chart["judgeLineList"][i]["notesBelow"][j]["type"]==3:
                        for a in range(0,len(speedlist)):
                            if chart["judgeLineList"][i]["notesBelow"][j]["time"]>=speedlist[a][0] and chart["judgeLineList"][i]["notesBelow"][j]["time"]<speedlist[a][1]:
                                speednote=str(round(chart["judgeLineList"][i]["notesBelow"][j]["speed"]/speedlist[a][2],1))
                        pec.append("n2 "+str(i)+" "+jt(chart["judgeLineList"][i]["notesBelow"][j]["time"])+" "+str(float(jt(chart["judgeLineList"][i]["notesBelow"][j]["time"]))+jht(chart["judgeLineList"][i]["notesBelow"][j]["holdTime"]))+" "+jrx(chart["judgeLineList"][i]["notesBelow"][j]["positionX"])+" 2 0\n# "+speednote+"\n& 1.00\n")
                    elif chart["judgeLineList"][i]["notesBelow"][j]["type"]==1:
                        pec.append("n1 "+str(i)+" "+jt(chart["judgeLineList"][i]["notesBelow"][j]["time"])+" "+jrx(chart["judgeLineList"][i]["notesBelow"][j]["positionX"])+" 2 0\n# "+js(chart["judgeLineList"][i]["notesBelow"][j]["speed"])+"\n& 1.00\n")
                    elif chart["judgeLineList"][i]["notesBelow"][j]["type"]==2:
                        pec.append("n4 "+str(i)+" "+jt(chart["judgeLineList"][i]["notesBelow"][j]["time"])+" "+jrx(chart["judgeLineList"][i]["notesBelow"][j]["positionX"])+" 2 0\n# "+js(chart["judgeLineList"][i]["notesBelow"][j]["speed"])+"\n& 1.00\n")
                    else:
                        pec.append("n3 "+str(i)+" "+jt(chart["judgeLineList"][i]["notesBelow"][j]["time"])+" "+jrx(chart["judgeLineList"][i]["notesBelow"][j]["positionX"])+" 2 0\n# "+js(chart["judgeLineList"][i]["notesBelow"][j]["speed"])+"\n& 1.00\n")
                for j in range(0,len(chart["judgeLineList"][i]["judgeLineDisappearEvents"])):
                    pec.append("ca "+str(i)+" "+jt(chart["judgeLineList"][i]["judgeLineDisappearEvents"][j]["startTime"])+" "+ja(chart["judgeLineList"][i]["judgeLineDisappearEvents"][j]["start"])+"\n")
                    pec.append("cf "+str(i)+" "+jt(chart["judgeLineList"][i]["judgeLineDisappearEvents"][j]["startTime"])+" "+jt(chart["judgeLineList"][i]["judgeLineDisappearEvents"][j]["endTime"])+" "+ja(chart["judgeLineList"][i]["judgeLineDisappearEvents"][j]["end"])+"\n")
                for j in range(0,len(chart["judgeLineList"][i]["judgeLineRotateEvents"])):
                    pec.append("cd "+str(i)+" "+jt(chart["judgeLineList"][i]["judgeLineRotateEvents"][j]["startTime"])+" "+jr(chart["judgeLineList"][i]["judgeLineRotateEvents"][j]["start"])+"\n")
                    pec.append("cr "+str(i)+" "+jt(chart["judgeLineList"][i]["judgeLineRotateEvents"][j]["startTime"])+" "+jt(chart["judgeLineList"][i]["judgeLineRotateEvents"][j]["endTime"])+" "+jr(chart["judgeLineList"][i]["judgeLineRotateEvents"][j]["end"])+" 1\n")
                for j in range(0,len(chart["judgeLineList"][i]["judgeLineMoveEvents"])):
                    if chart["formatVersion"]==1:
                        warn=Toplevel()
                        warn.title("打咩")
                        warn.geometry("300x100")
                        ta=Label(warn,text='转谱失败\n此版本开始已停止支持formatVersion:1',font=('Arial',10),width=30,height=2)
                        ta.place(relx=0.5,rely=0.5,anchor=CENTER)
                    else:
                        pec.append("cp "+str(i)+" "+jt(chart["judgeLineList"][i]["judgeLineMoveEvents"][j]["startTime"])+" "+f3x(chart["judgeLineList"][i]["judgeLineMoveEvents"][j]["start"])+" "+f3y(chart["judgeLineList"][i]["judgeLineMoveEvents"][j]["start2"])+"\n")
                        pec.append("cm "+str(i)+" "+jt(chart["judgeLineList"][i]["judgeLineMoveEvents"][j]["startTime"])+" "+jt(chart["judgeLineList"][i]["judgeLineMoveEvents"][j]["endTime"])+" "+f3x(chart["judgeLineList"][i]["judgeLineMoveEvents"][j]["end"])+" "+f3y(chart["judgeLineList"][i]["judgeLineMoveEvents"][j]["end2"])+" 1\n")
            t.close()
            chartpec=str(''.join(pec))
            if chart["formatVersion"]==3:
                savePath=filedialog.asksaveasfilename(initialfile='在此处为PEC文件命名'+'.pec',filetypes=[("PEC谱面", ".pec")])
                with open(savePath,"w") as t:
                    t.write(chartpec)
                    t.close()
        w1.destroy()
    global zpq
    zpq=True
    while zpq==True:
        zpq=False
        w1=Toplevel()
        w1.title("转谱器")
        w1.geometry("300x200")
        entry11=Entry(w1,show=None)
        entry11.place(relx=0.5,rely=0.4,anchor=CENTER)
        t11=Label(w1,text='事件精度值：\n即一个beat内的最短事件长度\n如不输入则默认0.125',font=('Arial',10),width=30,height=3)
        t11.place(relx=0.5,rely=0.2,anchor=CENTER)
        t12=Label(w1,text='输入后再选择谱面',font=('Arial',10),width=30,height=1)
        t12.place(relx=0.5,rely=0.55,anchor=CENTER)
        b11=Button(w1,text='选择谱面',font=('Arial',10),width=10,height=1,command=lambda:json2pec(entry11.get()))
        b11.place(relx=0.5,rely=0.7,anchor=CENTER)
        w1.mainloop()
def stzbpm():
    def changebpmforpec(BPM):
        def beat2sec(beat,bpm,offset):
            time=-offset
            for i in range(0,len(bpm)-1):
                if beat>=bpm[i][0] and beat>=bpm[i+1][0]:
                    time=time+(bpm[i+1][0]-bpm[i][0])/bpm[i][1]*60
                if beat>=bpm[i][0] and beat<bpm[i+1][0]:
                    time=time+(beat-bpm[i][0])/bpm[i][1]*60
            return round(time,3)
        def sec2beat(time,bpm):
            beat=time*bpm/60
            return round(beat,3)
        filePath=filedialog.askopenfilename(filetypes=[('PEC文件','.pec')])
        with open(filePath,"r") as t:
            data=t.readlines()
            offset=float(data[0])/1000
            bpmlist=[]
            pecline=[]
            for i in range(0,len(data)):
                if "bp" in data[i]:
                    bp=data[i].split()
                    bpmlist.append([float(bp[1]),float(bp[2])])
            bpmlist.append([2000.000,bpmlist[-1][1]])
            for i in range(0,len(data)):
                if "n" in data[i]:
                    if "n2" in data[i]:
                        hold=data[i].split()
                        starttime=beat2sec(float(hold[2]),bpmlist,offset)
                        endtime=beat2sec(float(hold[3]),bpmlist,offset)
                        pecline.append(hold[0]+" "+hold[1]+" "+str(starttime)+" "+str(endtime)+" "+hold[4]+" "+hold[5]+" "+hold[6]+"\n")
                        pecline.append(data[i+1])
                        pecline.append(data[i+2])
                    else:
                        note=data[i].split()
                        time=beat2sec(float(note[2]),bpmlist,offset)
                        pecline.append(note[0]+" "+note[1]+" "+str(time)+" "+note[3]+" "+note[4]+" "+note[5]+"\n")
                        pecline.append(data[i+1])
                        pecline.append(data[i+2])
                if "c" in data[i]:
                    if "cf" in data[i]:
                        event=data[i].split()
                        starttime=beat2sec(float(event[2]),bpmlist,offset)
                        endtime=beat2sec(float(event[3]),bpmlist,offset)
                        pecline.append(event[0]+" "+event[1]+" "+str(starttime)+" "+str(endtime)+" "+event[4]+"\n")
                    elif "cr" in data[i]:
                        event=data[i].split()
                        starttime=beat2sec(float(event[2]),bpmlist,offset)
                        endtime=beat2sec(float(event[3]),bpmlist,offset)
                        pecline.append(event[0]+" "+event[1]+" "+str(starttime)+" "+str(endtime)+" "+event[4]+" "+event[5]+"\n")
                    elif "cm" in data[i]:
                        event=data[i].split()
                        starttime=beat2sec(float(event[2]),bpmlist,offset)
                        endtime=beat2sec(float(event[3]),bpmlist,offset)
                        pecline.append(event[0]+" "+event[1]+" "+str(starttime)+" "+str(endtime)+" "+event[4]+" "+event[5]+" "+event[6]+"\n")
                    elif "cp" in data[i]:
                        event=data[i].split()
                        time=beat2sec(float(event[2]),bpmlist,offset)
                        pecline.append(event[0]+" "+event[1]+" "+str(time)+" "+event[3]+" "+event[4]+"\n")
                    else:
                        event=data[i].split()
                        time=beat2sec(float(event[2]),bpmlist,offset)
                        pecline.append(event[0]+" "+event[1]+" "+str(time)+" "+event[3]+"\n")
            t.close
        newbpm=BPM
        newpec=[]
        for i in range(0,len(pecline)):
            if "n" in pecline[i]:
                if "n2" in pecline[i]:
                    hold=pecline[i].split()
                    starttime=sec2beat(float(hold[2]),newbpm)
                    endtime=sec2beat(float(hold[3]),newbpm)
                    newpec.append(hold[0]+" "+hold[1]+" "+str(starttime)+" "+str(endtime)+" "+hold[4]+" "+hold[5]+" "+hold[6]+"\n")
                    newpec.append(pecline[i+1])
                    newpec.append(pecline[i+2])
                else:
                    note=pecline[i].split()
                    time=sec2beat(float(note[2]),newbpm)
                    newpec.append(note[0]+" "+note[1]+" "+str(time)+" "+note[3]+" "+note[4]+" "+note[5]+"\n")
                    newpec.append(pecline[i+1])
                    newpec.append(pecline[i+2])
            if "c" in pecline[i]:
                if "cf" in pecline[i]:
                    event=pecline[i].split()
                    starttime=sec2beat(float(event[2]),newbpm)
                    endtime=sec2beat(float(event[3]),newbpm)
                    newpec.append(event[0]+" "+event[1]+" "+str(starttime)+" "+str(endtime)+" "+event[4]+"\n")
                elif "cr" in pecline[i]:
                    event=pecline[i].split()
                    starttime=sec2beat(float(event[2]),newbpm)
                    endtime=sec2beat(float(event[3]),newbpm)
                    newpec.append(event[0]+" "+event[1]+" "+str(starttime)+" "+str(endtime)+" "+event[4]+" "+event[5]+"\n")
                elif "cm" in pecline[i]:
                    event=pecline[i].split()
                    starttime=sec2beat(float(event[2]),newbpm)
                    endtime=sec2beat(float(event[3]),newbpm)
                    newpec.append(event[0]+" "+event[1]+" "+str(starttime)+" "+str(endtime)+" "+event[4]+" "+event[5]+" "+event[6]+"\n")
                elif "cp" in pecline[i]:
                    event=pecline[i].split()
                    time=sec2beat(float(event[2]),newbpm)
                    newpec.append(event[0]+" "+event[1]+" "+str(time)+" "+event[3]+" "+event[4]+"\n")
                else:
                    event=pecline[i].split()
                    time=sec2beat(float(event[2]),newbpm)
                    newpec.append(event[0]+" "+event[1]+" "+str(time)+" "+event[3]+"\n")
        savePath=filedialog.asksaveasfilename(initialfile='在此处为PEC文件命名'+'.pec',filetypes=[("PEC谱面", ".pec")])
        with open(savePath,"w") as t:
            t.write("0\n")
            t.write("bp 0 "+str(newbpm)+"\n")
            for i in range(0,len(newpec)):
                t.write(newpec[i])
            t.close

    def changebpmforjson(BPM):
        filePath=filedialog.askopenfilename(filetypes=[('官谱格式','.json')])
        with open(filePath,"r") as t:
            chart=json.load(t)
            for i in range(0,len(chart["judgeLineList"])):
                mult=BPM/chart["judgeLineList"][i]["bpm"]
                chart["judgeLineList"][i]["bpm"]=BPM
                for j in range(0,len(chart["judgeLineList"][i]["speedEvents"])):
                    chart["judgeLineList"][i]["speedEvents"][j]["startTime"]=chart["judgeLineList"][i]["speedEvents"][j]["startTime"]*mult
                    chart["judgeLineList"][i]["speedEvents"][j]["endTime"]=chart["judgeLineList"][i]["speedEvents"][j]["endTime"]*mult
                for j in range(0,len(chart["judgeLineList"][i]["notesBelow"])):
                    chart["judgeLineList"][i]["notesBelow"][j]["time"]=chart["judgeLineList"][i]["notesBelow"][j]["time"]*mult
                    chart["judgeLineList"][i]["notesBelow"][j]["holdTime"]=chart["judgeLineList"][i]["notesBelow"][j]["holdTime"]*mult
                for j in range(0,len(chart["judgeLineList"][i]["notesAbove"])):
                    chart["judgeLineList"][i]["notesAbove"][j]["time"]=chart["judgeLineList"][i]["notesAbove"][j]["time"]*mult
                    chart["judgeLineList"][i]["notesAbove"][j]["holdTime"]=chart["judgeLineList"][i]["notesAbove"][j]["holdTime"]*mult
                for j in range(0,len(chart["judgeLineList"][i]["judgeLineDisappearEvents"])):
                    chart["judgeLineList"][i]["judgeLineDisappearEvents"][j]["startTime"]=chart["judgeLineList"][i]["judgeLineDisappearEvents"][j]["startTime"]*mult
                    chart["judgeLineList"][i]["judgeLineDisappearEvents"][j]["endTime"]=chart["judgeLineList"][i]["judgeLineDisappearEvents"][j]["endTime"]*mult
                for j in range(0,len(chart["judgeLineList"][i]["judgeLineMoveEvents"])):
                    chart["judgeLineList"][i]["judgeLineMoveEvents"][j]["startTime"]=chart["judgeLineList"][i]["judgeLineMoveEvents"][j]["startTime"]*mult
                    chart["judgeLineList"][i]["judgeLineMoveEvents"][j]["endTime"]=chart["judgeLineList"][i]["judgeLineMoveEvents"][j]["endTime"]*mult
                for j in range(0,len(chart["judgeLineList"][i]["judgeLineRotateEvents"])):
                    chart["judgeLineList"][i]["judgeLineRotateEvents"][j]["startTime"]=chart["judgeLineList"][i]["judgeLineRotateEvents"][j]["startTime"]*mult
                    chart["judgeLineList"][i]["judgeLineRotateEvents"][j]["endTime"]=chart["judgeLineList"][i]["judgeLineRotateEvents"][j]["endTime"]*mult
            t.close()
        savePath=filedialog.asksaveasfilename(initialfile='在此处为json谱面命名'+'.json',filetypes=[("json谱面", ".json")])
        with open(savePath,"w") as t:
            t.write(str(chart))
            t.close()
        w3.destroy()
    global zbpm
    zbpm=True
    while zbpm==True:
        zbpm=False
        w3=Toplevel()
        w3.title("BPM转换器")
        w3.geometry("300x200")
        entry31=Entry(w3,show=None)
        entry31.place(relx=0.5,rely=0.4,anchor=CENTER)
        t31=Label(w3,text='BPM转换改变谱面内BPM的数值\n且实际播放效果无变化\n输入新的BPM值',font=('Arial',10),width=30,height=3)
        t31.place(relx=0.5,rely=0.2,anchor=CENTER)
        t32=Label(w3,text='输入后再选择谱面',font=('Arial',10),width=30,height=1)
        t32.place(relx=0.5,rely=0.55,anchor=CENTER)
        b31=Button(w3,text='选择json',font=('Arial',10),width=10,height=1,command=lambda:changebpmforjson(float(entry31.get())))
        b31.place(relx=0.3,rely=0.7,anchor=CENTER)
        b32=Button(w3,text='选择pec',font=('Arial',10),width=10,height=1,command=lambda:changebpmforpec(float(entry31.get())))
        b32.place(relx=0.7,rely=0.7,anchor=CENTER)
        w3.mainloop()
def sthbpm():
    def sepm(var,chart):
        filePath=filedialog.askopenfilename(filetypes=[('PEC文件','.pec')])
        with open(filePath,"r") as t:
            chart.set(t.read())
            var.set(var.get()+"\n已选择："+os.path.split(filePath)[-1])
    def sedl(var,chart,output,starttime,endtime):
        newpec=[]
        bpm=[]
        var.set(var.get()+"\n第{0}beat到第{1}beat".format(starttime,endtime))
        data=chart.get().split('\n')
        for i in range(0,len(data)):
            if "c" in data[i]:
                st=float(data[i].split()[2])
                if st>=starttime and st<endtime:
                    newpec.append(data[i]+"\n")
            if "n" in data[i]:
                st=float(data[i].split()[2])
                if st>=starttime and st<endtime:
                    newpec.append(data[i]+"\n")
                    newpec.append(data[i+1]+"\n")
                    newpec.append(data[i+2]+"\n")
            if "bp" in data[i]:
                if data[i] in bpm:
                    pass
                else:
                    newpec.append(data[i]+"\n")
                    bpm.append(data[i])
        output.set(output.get()+''.join(newpec))
    def out(output):
        data=output.get().split("\n")
        savePath=filedialog.asksaveasfilename(initialfile='在此处为PEC谱面命名'+'.pec',filetypes=[("PEC谱面", ".pec")])
        with open(savePath,"w") as t:
            t.write("0\n")
            bpm=[]
            for i in range(0,len(data)):
                if "bp" in data[i]:
                    if data[i] in bpm:
                       pass
                    else:
                       t.write(data[i]+"\n")
                       bpm.append(data[i])
            for i in range(0,len(data)):
                if "c" in data[i]:
                    t.write(data[i]+"\n")
                if "n" in data[i]:
                    t.write(data[i]+"\n")
                    t.write(data[i+1]+"\n")
                    t.write(data[i+2]+"\n")
            t.close()
            w2.destroy()
    global hbpm
    hbpm=True
    while hbpm==True:
        hbpm=False
        w2=Toplevel()
        w2.title("谱面合并")
        w2.geometry("600x400")
        var=StringVar()
        chart=StringVar()
        output=StringVar()
        pm=Label(w2, textvariable=var,font=('Arial', 12),width=300, height=150)
        pm.place(relx=0.6,rely=0.5,anchor=CENTER)
        t21=Label(w2, text='逐个添加需要合并的谱面/段落\n添加完成后再导出',font=('Arial',12),width=100,height=2)
        t21.place(relx=0.5,rely=0.1,anchor=CENTER)
        b21=Button(w2,text='选择谱面',font=('Arial',10),width=10,height=1,command=lambda:sepm(var,chart))
        b21.place(relx=0.15,rely=0.2,anchor=CENTER)
        t22=Label(w2, text='设置开始和结束时间\n单位:beat',font=('Arial',12),width=15,height=2)
        t22.place(relx=0.15,rely=0.3,anchor=CENTER)
        t23=Label(w2, text='开始:',font=('Arial',12),width=10,height=1)
        t23.place(relx=0.1,rely=0.4,anchor=CENTER)
        t24=Label(w2, text='结束:',font=('Arial',12),width=10,height=1)
        t24.place(relx=0.1,rely=0.5,anchor=CENTER)
        entry21=Entry(w2,show=None,width=5)
        entry21.place(relx=0.2,rely=0.4,anchor=CENTER)
        entry22=Entry(w2,show=None,width=5)
        entry22.place(relx=0.2,rely=0.5,anchor=CENTER)
        b22=Button(w2,text='确认',font=('Arial',10),width=10,height=1,command=lambda:sedl(var,chart,output,float(entry21.get()),float(entry22.get())))
        b22.place(relx=0.15,rely=0.6,anchor=CENTER)
        t25=Label(w2, text='继续添加谱面\n全部添加完成后\n点击合并导出',font=('Arial',12),width=15,height=3)
        t25.place(relx=0.15,rely=0.75,anchor=CENTER)
        b23=Button(w2,text='合并导出',font=('Arial',10),width=10,height=1,command=lambda:out(output))
        b23.place(relx=0.15,rely=0.9,anchor=CENTER)
        w2.mainloop()
        
def stzrpe():
    def rpe2pe(lamdata):
        multdata=lamdata[0]
        var=lamdata[1]
        def cut(start,end,frequency,ease):
            mult=end-start
            final=[]
            if frequency==0:
                final.append(start)
                final.append(end)
            elif ease==0 or ease==1:
                for i in range(0,int(frequency)):
                    final.append(start+(i/int(frequency))*mult)
                final.append(end)
            elif ease==2:
                for i in range(0,int(frequency)):
                    final.append(start+math.sin((i/int(frequency))*math.pi/2)*mult)
                final.append(end)
            elif ease==3:
                trans=cut(start,end,int(frequency),2)
                for i in range(0,int(frequency)+1):
                    final.append(start+end-trans[-i-1])
            elif ease==4:
                trans=cut(start,end,int(frequency),5)
                for i in range(0,int(frequency)+1):
                    final.append(start+end-trans[-i-1])
            elif ease==5:
                for i in range(0,int(frequency)):
                    final.append(start+pow(i/int(frequency),2)*mult)
                final.append(end)
            elif ease==6:
                for i in range(0,int(frequency)):
                    final.append(start+(1-math.cos((i/int(frequency))*math.pi))/2*mult)
                final.append(end)
            elif ease==7:
                for i in range(0,int(frequency)):
                    if (i/int(frequency))<0.5:
                        final.append(start+2*(i/int(frequency))*(i/int(frequency))*mult)
                    else:
                        final.append(start+(1-pow(-2*(i/int(frequency))+2,2)/2)*mult)
                final.append(end)
            elif ease==8:
                trans=cut(start,end,int(frequency),9)
                for i in range(0,int(frequency)+1):
                    final.append(start+end-trans[-i-1])
            elif ease==9:
                for i in range(0,int(frequency)):
                    final.append(start+pow(i/int(frequency),3)*mult)
                final.append(end)
            elif ease==10:
                trans=cut(start,end,int(frequency),11)
                for i in range(0,int(frequency)+1):
                    final.append(start+end-trans[-i-1])
            elif ease==11:
                for i in range(0,int(frequency)):
                    final.append(start+pow(i/int(frequency),4)*mult)
                final.append(end)
            elif ease==12:
                for i in range(0,int(frequency)):
                    if (i/int(frequency))<0.5:
                        final.append(start+pow(i/int(frequency),3)*4*mult)
                    else:
                        final.append(start+(1-pow(-2*(i/int(frequency))+2,3)/2)*mult)
                final.append(end)
            elif ease==13:
                for i in range(0,int(frequency)):
                    if (i/int(frequency))<0.5:
                        final.append(start+pow(i/int(frequency),4)*8*mult)
                    else:
                        final.append(start+(1-pow(-2*(i/int(frequency))+2,4)/2)*mult)
                final.append(end)
            elif ease==14:
                trans=cut(start,end,int(frequency),15)
                for i in range(0,int(frequency)+1):
                    final.append(start+end-trans[-i-1])
            elif ease==15:
                for i in range(0,int(frequency)):
                    final.append(start+pow(i/int(frequency),5)*mult)
                final.append(end)
            elif ease==16:
                trans=cut(start,end,int(frequency),17)
                for i in range(0,int(frequency)+1):
                    final.append(start+end-trans[-i-1])
            elif ease==17:
                for i in range(0,int(frequency)):
                    final.append(start+pow(2,(10*(i/int(frequency)-1)))*mult)
                final.append(end)
                final[0]=start
            elif ease==19:
                trans=cut(start,end,int(frequency),18)
                for i in range(0,int(frequency)+1):
                    final.append(start+end-trans[-i-1])
            elif ease==18:
                for i in range(0,int(frequency)):
                    final.append(start+math.sqrt(1-pow((i/int(frequency)-1),2))*mult)
                final.append(end)
            elif ease==20:
                trans=cut(start,end,int(frequency),21)
                for i in range(0,int(frequency)+1):
                    final.append(start+end-trans[-i-1])
            elif ease==21:
                for i in range(0,int(frequency)):
                    final.append(start+(2.70158 *i/int(frequency)-1.70158)*pow(i/int(frequency),2)*mult)
                final.append(end)
            elif ease==22:
                for i in range(0,int(frequency)):
                    if (i/int(frequency))<0.5:
                        final.append(start+(1-math.sqrt(1-pow(2*i/int(frequency),2)))/2*mult)
                    else:
                        final.append(start+(math.sqrt(1-pow(-2*i/int(frequency)+2,2))+1)/2*mult)
                final.append(end)
            elif ease==23:
                for i in range(0,int(frequency)):
                    if (i/int(frequency))<0.5:
                        final.append(start+(14.379638*(i/int(frequency))-5.189819)*pow((i/int(frequency)),2)*mult)
                    else:
                        final.append(start+((14.379638*(i/int(frequency))-9.189819)*pow((i/int(frequency)-1),2)+1)*mult)
                final.append(end)
            elif ease==24:
                trans=cut(start,end,int(frequency),25)
                for i in range(0,int(frequency)+1):
                    final.append(start+end-trans[-i-1])
            elif ease==25:
                for i in range(0,int(frequency)):
                    final.append(start+(-pow(2,10*i/int(frequency)-10)*math.sin((i/int(frequency)*10-10.75)*2*math.pi/3))*mult)
                final.append(end)
                final[0]=start
            elif ease==26:
                frequency=int(frequency)
                for i in range(0,int(frequency)):
                    if (i/int(frequency))*11<4:
                        final.append(start+(pow((i/int(frequency))*11,2))/16*mult)
                    elif (i/int(frequency))*11<8:
                        final.append(start+(pow((i/int(frequency))*11-6,2)+12)/16*mult)
                    elif (i/int(frequency))*11<10:
                        final.append(start+(pow((i/int(frequency))*11-9,2)+15)/16*mult)
                    else:
                        final.append(start+(pow((i/int(frequency))*11-10.5,2)+15.75)/16*mult)
                final.append(end)
            elif ease==27:
                trans=cut(start,end,int(frequency),26)
                frequency=int(frequency)
                for i in range(0,int(frequency)+1):
                    final.append(start+end-trans[-i-1])
            elif ease==28:
                for i in range(0,int(frequency)):
                    if (i/int(frequency))<0.5:
                        final.append(cut(start,end/2,int(frequency)/2,27)[i])
                    else:
                        final.append(cut(end/2,end,int(frequency)/2,26)[i-50])
                final.append(end)
            elif ease==29:
                for i in range(0,int(frequency)):
                    if (i/int(frequency))<0.5:
                        final.append(start-(pow(2,20*(i/int(frequency))-10)*math.sin((20*(i/int(frequency))-11.125)*2*math.pi/4.5)/2)*mult)
                    else:
                        final.append(start+(pow(2,-20*(i/int(frequency))+10)*math.sin((20*(i/int(frequency))-11.125)*2*math.pi/4.5)/2+1)*mult)
                final.append(end)
                final[0]=start
            return final

        def beat(elem):
            return float(elem[0]+elem[1]/elem[2])

        def bp(elem):
            time=beat(elem["startTime"])
            out="bp "+str(time)+" "+str(elem["bpm"])+"\n"
            return out

        def RPEX(x):
            x=x/675*1024+1024
            return x

        def RPEY(y):
            y=y/450*700+700
            return y

        def getdata(judgeline,datalist,timepoint):
            data=[]
            base=[]
            for i in range(0,len(datalist)):
                if datalist[i][0]==judgeline:
                    data.append(datalist[i])
            if len(data)==0:
                return 0
            for i in range(0,len(data)):
                if timepoint>=data[i][1] and timepoint<data[i][2]:
                    value=data[i][3]+(timepoint-data[i][1])/(data[i][2]-data[i][1])*(data[i][4]-data[i][3])
                    return value
            for i in range(0,len(data)):
                base.append(data[i][1])
            if len(base)!=0 and timepoint<min(base):
                return 0
            if len(base)!=0 and timepoint>=max(base):
                return data[-1][4]
            for i in range(0,len(data)):
                if timepoint>=data[i][2] and timepoint<data[i+1][1]:
                    value=data[i][4]
                    return value
        def getdatam(judgeline,datalist,timepoint):
            timepoint=timepoint-0.001
            return getdata(judgeline,datalist,timepoint)
        def deal(alldata):
            pectimecut=alldata[0]
            pecdata=alldata[1]
            var=alldata[2]
            for c in range(0,len(chart["judgeLineList"])):
                list1=[[],[],[],[]]
                for i in range(0,len(pectimecut)):
                    var.set("时间较长，请耐心等待\n正在转换第 "+str(c)+" 条判定线\n进度 "+str(round(100*i/len(pectimecut),2))+"%")
                    timepoint=pectimecut[i]
                    alphadata=getdata(c,pecdata[0][0],timepoint)+getdata(c,pecdata[1][0],timepoint)+getdata(c,pecdata[2][0],timepoint)+getdata(c,pecdata[3][0],timepoint)+getdata(c,pecdata[4][0],timepoint)
                    Xdata=RPEX(getdata(c,pecdata[0][1],timepoint)+getdata(c,pecdata[1][1],timepoint)+getdata(c,pecdata[2][1],timepoint)+getdata(c,pecdata[3][1],timepoint)+getdata(c,pecdata[4][1],timepoint))
                    Ydata=RPEY(getdata(c,pecdata[0][2],timepoint)+getdata(c,pecdata[1][2],timepoint)+getdata(c,pecdata[2][2],timepoint)+getdata(c,pecdata[3][2],timepoint)+getdata(c,pecdata[4][2],timepoint))
                    rotatedata=getdata(c,pecdata[0][3],timepoint)+getdata(c,pecdata[1][3],timepoint)+getdata(c,pecdata[2][3],timepoint)+getdata(c,pecdata[3][3],timepoint)+getdata(c,pecdata[4][3],timepoint)
                    list1[0].append([c,alphadata,timepoint])
                    list1[1].append([c,Xdata,timepoint])
                    list1[2].append([c,Ydata,timepoint])
                    list1[3].append([c,rotatedata,timepoint])
                    timepoint=pectimecut[i]+1/16
                    alphadata=getdatam(c,pecdata[0][0],timepoint)+getdatam(c,pecdata[1][0],timepoint)+getdatam(c,pecdata[2][0],timepoint)+getdatam(c,pecdata[3][0],timepoint)+getdatam(c,pecdata[4][0],timepoint)
                    Xdata=RPEX(getdatam(c,pecdata[0][1],timepoint)+getdatam(c,pecdata[1][1],timepoint)+getdatam(c,pecdata[2][1],timepoint)+getdatam(c,pecdata[3][1],timepoint)+getdatam(c,pecdata[4][1],timepoint))
                    Ydata=RPEY(getdatam(c,pecdata[0][2],timepoint)+getdatam(c,pecdata[1][2],timepoint)+getdatam(c,pecdata[2][2],timepoint)+getdatam(c,pecdata[3][2],timepoint)+getdatam(c,pecdata[4][2],timepoint))
                    rotatedata=getdatam(c,pecdata[0][3],timepoint)+getdatam(c,pecdata[1][3],timepoint)+getdatam(c,pecdata[2][3],timepoint)+getdatam(c,pecdata[3][3],timepoint)+getdatam(c,pecdata[4][3],timepoint)
                    list1[0].append([c,alphadata,timepoint])
                    list1[1].append([c,Xdata,timepoint])
                    list1[2].append([c,Ydata,timepoint])
                    list1[3].append([c,rotatedata,timepoint])
                list2=[[list1[0][0]],[list1[1][0]],[list1[2][0]],[list1[3][0]]]
                singal=[0,3]
                for i in singal:
                    for j in range(2,len(list1[i])-2):
                        if j%2!=0:
                            if list1[i][j][1]!=list1[i][j-2][1] or list1[i][j][1]!=list1[i][j+2][1]:
                                list2[i].append(list1[i][j])
                                list2[i].append(list1[i][j+1])
                    list2[i].append(list1[i][-1])
                for j in range(2,len(list1[1])-2):
                    if j%2!=0:
                        if list1[1][j][1]!=list1[1][j-2][1] or list1[1][j][1]!=list1[1][j+2][1] or list1[2][j][1]!=list1[2][j-2][1] or list1[2][j][1]!=list1[2][j+2][1]:
                            list2[1].append(list1[1][j])
                            list2[2].append(list1[2][j])
                            list2[1].append(list1[1][j+1])
                            list2[2].append(list1[2][j+1])
                list2[1].append(list1[1][-1])
                list2[2].append(list1[2][-1])
                for i in range(0,len(list2)):
                    for j in range(0,len(list2[i])-1):
                        if j%2==0 and i==0:
                            pecline="ca "+str(c)+" "+str(round(list2[i][j][2],3))+" "+str(round(list2[i][j][1],3))+"\n"
                            finalpec.append(pecline)
                            pecline="cf "+str(c)+" "+str(round(list2[i][j][2],3))+" "+str(round(list2[i][j+1][2],3))+" "+str(round(list2[i][j+1][1],3))+"\n"
                            finalpec.append(pecline)
                        if j%2==0 and i==1:
                            pecline="cp "+str(c)+" "+str(round(list2[i][j][2],3))+" "+str(round(list2[i][j][1],3))+" "+str(round(list2[i+1][j][1],3))+"\n"
                            finalpec.append(pecline)
                            pecline="cm "+str(c)+" "+str(round(list2[i][j][2],3))+" "+str(round(list2[i][j+1][2],3))+" "+str(round(list2[i][j+1][1],3))+" "+str(round(list2[i+1][j+1][1],3))+" 1\n"
                            finalpec.append(pecline)
                        if j%2==0 and i==3:
                            pecline="cd "+str(c)+" "+str(round(list2[i][j][2],3))+" "+str(round(list2[i][j][1],3))+"\n"
                            finalpec.append(pecline)
                            pecline="cr "+str(c)+" "+str(round(list2[i][j][2],3))+" "+str(round(list2[i][j+1][2],3))+" "+str(round(list2[i][j+1][1],3))+" 1\n"
                            finalpec.append(pecline)
            savePath=filedialog.asksaveasfilename(initialfile='在此处为PEC谱面命名'+'.pec',filetypes=[("PEC谱面", ".pec")])
            with open(savePath,"w") as t:
                for i in range(0,len(finalpec)):
                    t.write(finalpec[i])
                t.close()
        def display(var):
            pm=Label(w4, textvariable=var,font=('Arial', 12),width=300, height=5)
            pm.place(relx=0.5,rely=0.72,anchor=CENTER)
        
        if multdata=="":
            multdata=16
        else:
            multdata=float(1/multdata)
        filePath=filedialog.askopenfilename(filetypes=[('RPE谱面','.json')])
        with open(filePath,"r") as t:
            chart=json.load(t)
            bpm=[]
            for i in range (0,len(chart["BPMList"])):
                bpm.append(bp(chart["BPMList"][i]))
            offset=str(chart["META"]["offset"]+175)+"\n"
            pecdata=[[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]],[[],[],[],[],[]]]
            note=[]
            totaltime=[]
            for i in range(0,len(chart["judgeLineList"])):
                for j in range(0,len(chart["judgeLineList"][i]["eventLayers"])):
                    data=chart["judgeLineList"][i]["eventLayers"][j]
                    if type(chart["judgeLineList"][i]["eventLayers"][j])==dict and "alphaEvents" in chart["judgeLineList"][i]["eventLayers"][j].keys():
                        for c in range(0,len(chart["judgeLineList"][i]["eventLayers"][j]["alphaEvents"])):
                            frequency=(beat(chart["judgeLineList"][i]["eventLayers"][j]["alphaEvents"][c]["endTime"])-beat(chart["judgeLineList"][i]["eventLayers"][j]["alphaEvents"][c]["startTime"]))*16
                            value=cut(chart["judgeLineList"][i]["eventLayers"][j]["alphaEvents"][c]["start"],chart["judgeLineList"][i]["eventLayers"][j]["alphaEvents"][c]["end"],int(frequency),chart["judgeLineList"][i]["eventLayers"][j]["alphaEvents"][c]["easingType"])
                            timecut=cut(beat(chart["judgeLineList"][i]["eventLayers"][j]["alphaEvents"][c]["startTime"]),beat(chart["judgeLineList"][i]["eventLayers"][j]["alphaEvents"][c]["endTime"]),int(frequency),1)
                            for d in range(0,len(timecut)-1):
                                line=[i,timecut[d],timecut[d+1],value[d],value[d+1]]
                                pecdata[j][0].append(line)
                                totaltime.append(timecut[d+1])
                    if type(chart["judgeLineList"][i]["eventLayers"][j])==dict and "moveXEvents" in chart["judgeLineList"][i]["eventLayers"][j].keys():
                        for c in range(0,len(chart["judgeLineList"][i]["eventLayers"][j]["moveXEvents"])):
                            frequency=(beat(chart["judgeLineList"][i]["eventLayers"][j]["moveXEvents"][c]["endTime"])-beat(chart["judgeLineList"][i]["eventLayers"][j]["moveXEvents"][c]["startTime"]))*16
                            value=cut(chart["judgeLineList"][i]["eventLayers"][j]["moveXEvents"][c]["start"],chart["judgeLineList"][i]["eventLayers"][j]["moveXEvents"][c]["end"],int(frequency),chart["judgeLineList"][i]["eventLayers"][j]["moveXEvents"][c]["easingType"])
                            timecut=cut(beat(chart["judgeLineList"][i]["eventLayers"][j]["moveXEvents"][c]["startTime"]),beat(chart["judgeLineList"][i]["eventLayers"][j]["moveXEvents"][c]["endTime"]),int(frequency),1)
                            for d in range(0,len(timecut)-1):
                                line=[i,timecut[d],timecut[d+1],value[d],value[d+1]]
                                pecdata[j][1].append(line)
                                totaltime.append(timecut[d+1])
                    if type(chart["judgeLineList"][i]["eventLayers"][j])==dict and "moveYEvents" in chart["judgeLineList"][i]["eventLayers"][j].keys():
                        for c in range(0,len(chart["judgeLineList"][i]["eventLayers"][j]["moveYEvents"])):
                            frequency=(beat(chart["judgeLineList"][i]["eventLayers"][j]["moveYEvents"][c]["endTime"])-beat(chart["judgeLineList"][i]["eventLayers"][j]["moveYEvents"][c]["startTime"]))*16
                            value=cut(chart["judgeLineList"][i]["eventLayers"][j]["moveYEvents"][c]["start"],chart["judgeLineList"][i]["eventLayers"][j]["moveYEvents"][c]["end"],int(frequency),chart["judgeLineList"][i]["eventLayers"][j]["moveYEvents"][c]["easingType"])
                            timecut=cut(beat(chart["judgeLineList"][i]["eventLayers"][j]["moveYEvents"][c]["startTime"]),beat(chart["judgeLineList"][i]["eventLayers"][j]["moveYEvents"][c]["endTime"]),int(frequency),1)
                            for d in range(0,len(timecut)-1):
                                line=[i,timecut[d],timecut[d+1],value[d],value[d+1]]
                                pecdata[j][2].append(line)
                                totaltime.append(timecut[d+1])
                    if type(chart["judgeLineList"][i]["eventLayers"][j])==dict and "rotateEvents" in chart["judgeLineList"][i]["eventLayers"][j].keys():
                        for c in range(0,len(chart["judgeLineList"][i]["eventLayers"][j]["rotateEvents"])):
                            frequency=(beat(chart["judgeLineList"][i]["eventLayers"][j]["rotateEvents"][c]["endTime"])-beat(chart["judgeLineList"][i]["eventLayers"][j]["rotateEvents"][c]["startTime"]))*16
                            value=cut(chart["judgeLineList"][i]["eventLayers"][j]["rotateEvents"][c]["start"],chart["judgeLineList"][i]["eventLayers"][j]["rotateEvents"][c]["end"],int(frequency),chart["judgeLineList"][i]["eventLayers"][j]["rotateEvents"][c]["easingType"])
                            timecut=cut(beat(chart["judgeLineList"][i]["eventLayers"][j]["rotateEvents"][c]["startTime"]),beat(chart["judgeLineList"][i]["eventLayers"][j]["rotateEvents"][c]["endTime"]),int(frequency),1)
                            for d in range(0,len(timecut)-1):
                                line=[i,timecut[d],timecut[d+1],value[d],value[d+1]]
                                pecdata[j][3].append(line)
                                totaltime.append(timecut[d+1])
                    if type(chart["judgeLineList"][i]["eventLayers"][j])==dict and "speedEvents" in chart["judgeLineList"][i]["eventLayers"][j].keys():
                        for c in range(0,len(chart["judgeLineList"][i]["eventLayers"][j]["speedEvents"])):
                            frequency=(beat(chart["judgeLineList"][i]["eventLayers"][j]["speedEvents"][c]["endTime"])-beat(chart["judgeLineList"][i]["eventLayers"][j]["speedEvents"][c]["startTime"]))*16
                            value=cut(chart["judgeLineList"][i]["eventLayers"][j]["speedEvents"][c]["start"],chart["judgeLineList"][i]["eventLayers"][j]["speedEvents"][c]["end"],int(frequency),1)
                            timecut=cut(beat(chart["judgeLineList"][i]["eventLayers"][j]["speedEvents"][c]["startTime"]),beat(chart["judgeLineList"][i]["eventLayers"][j]["speedEvents"][c]["endTime"]),int(frequency),1)
                            for d in range(0,len(timecut)-1):
                                line=[i,timecut[d],value[d+1]/6.43*10]
                                pecdata[j][4].append(line)
                                totaltime.append(timecut[d+1])
                if "notes" in chart["judgeLineList"][i].keys():
                    for j in range(0,len(chart["judgeLineList"][i]["notes"])):
                        above=chart["judgeLineList"][i]["notes"][j]["above"]
                        if above==0:
                            above=2
                        isFake=chart["judgeLineList"][i]["notes"][j]["isFake"]
                        positionX=RPEX(chart["judgeLineList"][i]["notes"][j]["positionX"])-1024
                        speed=chart["judgeLineList"][i]["notes"][j]["speed"]
                        if chart["judgeLineList"][i]["notes"][j]["type"]==2:
                            anote="n2 "+str(i)+" "+str(beat(chart["judgeLineList"][i]["notes"][j]["startTime"]))+" "+str(beat(chart["judgeLineList"][i]["notes"][j]["endTime"]))+" "+str(positionX)+" "+str(above)+" "+str(isFake)+"\n"
                            note.append(anote)
                            note.append("# "+str(speed)+"\n")
                            note.append("& 1.00\n")
                            totaltime.append(beat(chart["judgeLineList"][i]["notes"][j]["endTime"]))
                        else:
                            anote="n"+str(chart["judgeLineList"][i]["notes"][j]["type"])+" "+str(i)+" "+str(beat(chart["judgeLineList"][i]["notes"][j]["startTime"]))+" "+str(positionX)+" "+str(above)+" "+str(isFake)+"\n"
                            note.append(anote)
                            note.append("# "+str(speed)+"\n")
                            note.append("& 1.00\n")
                            totaltime.append(beat(chart["judgeLineList"][i]["notes"][j]["endTime"]))
            t.close()
        maxtime=max(totaltime)
        pectimecut=cut(0,maxtime,int(maxtime*16),1)
        finalpec=[str(offset)]
        for i in range(0,len(bpm)):
            finalpec.append(bpm[i])
        for i in range(0,len(pectimecut)):
            pectimecut[i]=round(pectimecut[i],4)
        speedlist=pecdata[0][4]
        for i in range(0,len(speedlist)):
            line="cv "+str(speedlist[i][0])+" "+str(speedlist[i][1])+" "+str(round(speedlist[i][2],3))+"\n"
            finalpec.append(line)
        for i in range(0,len(note)):
            finalpec.append(note[i])
        thread=threading.Thread(target=deal,args=([pectimecut,pecdata,var],))
        thread.start()
        thread2=threading.Thread(target=display,args=(var,))
        thread2.start()
        

    
    global zrpe
    zrpe=True
    while zrpe==True:
        zrpe=False
        w4=Toplevel()
        w4.title("转谱器")
        w4.geometry("300x200")
        var=StringVar()
        entry41=Entry(w4,show=None)
        entry41.place(relx=0.5,rely=0.4,anchor=CENTER)
        t41=Label(w4,text='事件精度值：\n即一个beat内的最短事件长度\n如不输入则默认0.0625',font=('Arial',10),width=30,height=3)
        t41.place(relx=0.5,rely=0.2,anchor=CENTER)
        b41=Button(w4,text='选择谱面',font=('Arial',10),width=10,height=1,command=lambda:rpe2pe([entry41.get(),var]))
        b41.place(relx=0.5,rely=0.6,anchor=CENTER)
        tip=Label(w4,text='注：此功能可保留X,Y分离和多层运动\n若未使用X,Y分离和多层运动\n可直接在RPE软件内导出为PE格式',font=('Arial', 10),width=300, height=3)
        tip.place(relx=0.5,rely=0.8,anchor=CENTER)
        w4.mainloop()

root=Tk()
root.title("1615的谱面工具箱")
root.geometry("600x400")


zpq=False
zbpm=False
hbpm=False
zrpe=False
t1=Label(root, text='谱面工具测试版0.0.5',font=('Arial',12),width=30,height=2)
t1.place(relx=0.5,rely=0.1,anchor=CENTER)
b1=Button(root,text='官谱转PE转谱器',font=('Arial',10),width=20,height=2,command=stzpq)
b1.place(relx=0.25,rely=0.25,anchor=CENTER)
b2=Button(root,text='谱面合并',font=('Arial',10),width=20,height=2,command=sthbpm)
b2.place(relx=0.25,rely=0.45,anchor=CENTER)
b3=Button(root,text='BPM换算',font=('Arial',10),width=20,height=2,command=stzbpm)
b3.place(relx=0.25,rely=0.65,anchor=CENTER)
b4=Button(root,text='RPE转PE转谱器',font=('Arial',10),width=20,height=2,command=stzrpe)
b4.place(relx=0.75,rely=0.25,anchor=CENTER)
t2=Label(root, text='注：此工具适用于\nPE的pec格式 官谱和RPE的json格式',font=('Arial',12),width=30,height=3)
t2.place(relx=0.5,rely=0.85,anchor=CENTER)

root.mainloop()
