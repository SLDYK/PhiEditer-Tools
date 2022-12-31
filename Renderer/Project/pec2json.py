# -*- coding: utf-8 -*-
import json
from tkinter import filedialog
import tkinter
from lib_for_json import end_floor, float_range, recent_speed, cut, beat2sec, sec2beat

def pec2json(filePath):
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
        t.close()
    newbpm=bpmlist[-1][1]
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



    data=newpec

    notes=[]
    move_event=[]
    rotate_event=[]
    alpha_event=[]
    speed_event=[]
    Num_note=0
    BPM=newbpm
    new_chart={"formatVersion":3,
            "offset":0,
            "numOfNotes":int,
            "judgeLineList":[]}
    Num_judgeline=[]
    for i in range(len(data)):
        if "n" in data[i]:
            if "n1" in data[i]:
                notes.append({"type":1,
                            "line":int(data[i].split()[1]),
                            "positionX":float(data[i].split()[3])/1024*9,
                            "time":float(data[i].split()[2])*32,
                            "holdTime":0,
                            "speed":float(data[i+1].split()[1]),
                            "above":float(data[i].split()[4]),
                            "isFake":float(data[i].split()[5])})
                if float(data[i].split()[5])==0:
                    Num_note+=1
                Num_judgeline.append(int(data[i].split()[1]))
            elif "n2" in data[i]:
                notes.append({"type":3,
                            "line":int(data[i].split()[1]),
                            "positionX":float(data[i].split()[4])/1024*9,
                            "time":float(data[i].split()[2])*32,
                            "holdTime":float(data[i].split()[3])*32-float(data[i].split()[2])*32,
                            "speed":float(data[i+1].split()[1]),
                            "above":float(data[i].split()[5]),
                            "isFake":float(data[i].split()[6])})
                if float(data[i].split()[6])==0:
                    Num_note+=1
                Num_judgeline.append(int(data[i].split()[1]))
            elif "n3" in data[i]:
                notes.append({"type":4,
                            "line":int(data[i].split()[1]),
                            "positionX":float(data[i].split()[3])/1024*9,
                            "time":float(data[i].split()[2])*32,
                            "holdTime":0,
                            "speed":float(data[i+1].split()[1]),
                            "above":float(data[i].split()[4]),
                            "isFake":float(data[i].split()[5])})
                if float(data[i].split()[5])==0:
                    Num_note+=1
                Num_judgeline.append(int(data[i].split()[1]))
            elif "n4" in data[i]:
                notes.append({"type":2,
                            "line":int(data[i].split()[1]),
                            "positionX":float(data[i].split()[3])/1024*9,
                            "time":float(data[i].split()[2])*32,
                            "holdTime":0,
                            "speed":float(data[i+1].split()[1]),
                            "above":float(data[i].split()[4]),
                            "isFake":float(data[i].split()[5])})
                if float(data[i].split()[5])==0:
                    Num_note+=1
                Num_judgeline.append(int(data[i].split()[1]))
        elif "c" in data[i]:
            if "cm" in data[i]:
                move_event.append({"line":int(data[i].split()[1]),
                                "startTime":float(data[i].split()[2])*32,
                                "endTime":float(data[i].split()[3])*32,
                                "end":float(data[i].split()[4])/2048,
                                "end2":float(data[i].split()[5])/1400,
                                "easing":int(data[i].split()[6])})
                Num_judgeline.append(int(data[i].split()[1]))
            elif "cp" in data[i]:
                move_event.append({"line":int(data[i].split()[1]),
                                "startTime":float(data[i].split()[2])*32,
                                "start":float(data[i].split()[3])/2048,
                                "start2":float(data[i].split()[4])/1400})
                Num_judgeline.append(int(data[i].split()[1]))
            elif "cr" in data[i]:
                rotate_event.append({"line":int(data[i].split()[1]),
                                    "startTime":float(data[i].split()[2])*32,
                                    "endTime":float(data[i].split()[3])*32,
                                    "end":float(data[i].split()[4])*-1,
                                    "easing":int(data[i].split()[5])})
                Num_judgeline.append(int(data[i].split()[1]))
            elif "cd" in data[i]:
                rotate_event.append({"line":int(data[i].split()[1]),
                                    "startTime":float(data[i].split()[2])*32,
                                    "start":float(data[i].split()[3])*-1})
                Num_judgeline.append(int(data[i].split()[1]))
            elif "cf" in data[i]:
                alpha_event.append({"line":int(data[i].split()[1]),
                                    "startTime":float(data[i].split()[2])*32,
                                    "endTime":float(data[i].split()[3])*32,
                                    "end":float(data[i].split()[4])/255})
                Num_judgeline.append(int(data[i].split()[1]))
            elif "ca" in data[i]:
                alpha_event.append({"line":int(data[i].split()[1]),
                                    "startTime":float(data[i].split()[2])*32,
                                    "start":float(data[i].split()[3])/255})
                Num_judgeline.append(int(data[i].split()[1]))
            elif "cv" in data[i]:
                speed_event.append({"line":int(data[i].split()[1]),
                                    "startTime":float(data[i].split()[2])*32,
                                    "start":float(data[i].split()[3])/7})
                Num_judgeline.append(int(data[i].split()[1]))
    new_chart["numOfNotes"]=Num_note
    Num_judgeline=max(Num_judgeline)+1
    for i in range(Num_judgeline):
        
        a_line={"bpm":BPM,
                "notesAbove":[],
                "notesBelow":[],
                "speedEvents":[],
                "judgeLineMoveEvents":[],
                "judgeLineDisappearEvents":[],
                "judgeLineRotateEvents":[]}
        
        note_this_line=[]
        speed_this_line=[]
        move_this_line=[]
        rotate_this_line=[]
        alpha_this_line=[]
        
        for j in range(len(speed_event)):
            if speed_event[j]["line"]==i:
                speed_this_line.append(speed_event[j])
                speed_event.pop(j)
                speed_event.insert(j,"delete")
        while "delete" in speed_event:
            speed_event.remove("delete")
        
        floor=0
        speed_this_line.sort(key=lambda x:x["startTime"])
        for j in range(len(speed_this_line)):
            startTime=speed_this_line[j]["startTime"]
            try:
                endTime=speed_this_line[j+1]["startTime"]
            except:
                endTime=float("inf")
            value=speed_this_line[j]["start"]
            a_line["speedEvents"].append({"startTime":startTime,
                                        "endTime":endTime,
                                        "value":value})
            a_line["speedEvents"][-1].update({"floorPosition":floor})
            floor+=(endTime-startTime)/32/BPM*60*value
        
        a_line["speedEvents"].insert(0,{"startTime":-999999,
                                                "endTime":a_line["speedEvents"][0]["startTime"],
                                                "value":0,
                                                "floorPosotion":0})
        
        for j in range(len(notes)):
            if notes[j]["line"]==i:
                note_this_line.append(notes[j])
                notes.pop(j)
                notes.insert(j,"delete")
        while "delete" in notes:
            notes.remove("delete")
            
        for j in range(len(note_this_line)):
            tp=note_this_line[j]["type"]
            time=note_this_line[j]["time"]
            positionX=note_this_line[j]["positionX"]
            holdTime=note_this_line[j]["holdTime"]
            speed=note_this_line[j]["speed"]
            floorPostion=end_floor(time,a_line["speedEvents"],BPM)
            floorPostion2=end_floor(time+holdTime,a_line["speedEvents"],BPM)
            if note_this_line[j]["type"]==3:
                mult=recent_speed(time,a_line["speedEvents"])
                speed=speed*mult
            if note_this_line[j]["isFake"]==1:
                time+=999999
            if note_this_line[j]["above"]==1:
                a_line["notesAbove"].append({"type":tp,
                                            "time":time,
                                            "positionX":positionX,
                                            "holdTime":holdTime,
                                            "speed":speed,
                                            "floorPosition":floorPostion,
                                            "floorPosition2":floorPostion2})
            else:
                a_line["notesBelow"].append({"type":tp,
                                            "time":time,
                                            "positionX":positionX,
                                            "holdTime":holdTime,
                                            "speed":speed,
                                            "floorPosition":floorPostion,
                                            "floorPosition2":floorPostion2})
        
        time_point=[]
        for j in range(len(move_event)):
            if move_event[j]["line"]==i:
                move_this_line.append(move_event[j])
                time_point.append(move_event[j]["startTime"])
                try:
                    time_point.append(move_event[j]["endTime"])
                except:
                    pass
                move_event.pop(j)
                move_event.insert(j,"delete")
        while "delete" in move_event:
            move_event.remove("delete")
        
        time_point=list(set(time_point))
        time_point.sort()
        
        for j in range(len(time_point)):
            startTime=time_point[j]
            try:
                endTime=time_point[j+1]
            except:
                endTime=float("inf")
            a_line["judgeLineMoveEvents"].append({"startTime":startTime,
                                                "endTime":endTime})
            
        for j in range(len(move_this_line)):
            
            time=move_this_line[j]["startTime"]
            try:
                start=move_this_line[j]["start"]
                start2=move_this_line[j]["start2"]
            except:
                end=move_this_line[j]["end"]
                end2=move_this_line[j]["end2"]
                easing=move_this_line[j]["easing"]
            for k in range(len(a_line["judgeLineMoveEvents"])):
                if a_line["judgeLineMoveEvents"][k]["startTime"]==time:
                    try:
                        a_line["judgeLineMoveEvents"][k].update({"start":start,
                                                                "start2":start2})
                        break
                    except:
                        a_line["judgeLineMoveEvents"][k].update({"end":end,
                                                                "end2":end2,
                                                                "easing":easing})
                        break
            try:
                del start
                del start2
            except:
                del end
                del end2
                del easing
                
        for j in range(len(a_line["judgeLineMoveEvents"])):
            key=list(a_line["judgeLineMoveEvents"][j].keys())
            if key==['startTime','endTime']:
                start=a_line["judgeLineMoveEvents"][j-1]["end"]
                start2=a_line["judgeLineMoveEvents"][j-1]["end2"]
                end=a_line["judgeLineMoveEvents"][j-1]["end"]
                end2=a_line["judgeLineMoveEvents"][j-1]["end2"]
                easing=1
                a_line["judgeLineMoveEvents"][j].update({"start":start,
                                                        "start2":start2,
                                                        "end":end,
                                                        "end2":end2,
                                                        "easing":easing})
            elif key==['startTime','endTime','start','start2']:
                end=a_line["judgeLineMoveEvents"][j]["start"]
                end2=a_line["judgeLineMoveEvents"][j]["start2"]
                easing=1
                a_line["judgeLineMoveEvents"][j].update({"end":end,
                                                        "end2":end2,
                                                        "easing":easing})
            elif key==['startTime','endTime','end','end2','easing']:
                start=a_line["judgeLineMoveEvents"][j-1]["end"]
                start2=a_line["judgeLineMoveEvents"][j-1]["end2"]
                easing=a_line["judgeLineMoveEvents"][j]["easing"]
                a_line["judgeLineMoveEvents"][j].update({"start":start,
                                                        "start2":start2,
                                                        "easing":easing})
                
        for j in range(len(a_line["judgeLineMoveEvents"])):
            easing=a_line["judgeLineMoveEvents"][j]["easing"]
            if easing != 0 and easing != 1:
                startTime=a_line["judgeLineMoveEvents"][j]["startTime"]
                endTime=a_line["judgeLineMoveEvents"][j]["endTime"]
                start=a_line["judgeLineMoveEvents"][j]["start"]
                start2=a_line["judgeLineMoveEvents"][j]["start2"]
                end=a_line["judgeLineMoveEvents"][j]["end"]
                end2=a_line["judgeLineMoveEvents"][j]["end2"]
                time_cut=float_range(startTime,endTime,1)
                a_line["judgeLineMoveEvents"].pop(j)
                a_line["judgeLineMoveEvents"].insert(j,"delete")
                for k in range(len(time_cut)-1):
                    cut_startTime=time_cut[k]
                    cut_endTime=time_cut[k+1]
                    cut_start=cut(start,end,startTime,endTime,0,1,easing,cut_startTime)
                    cut_start2=cut(start2,end2,startTime,endTime,0,1,easing,cut_startTime)
                    cut_end=cut(start,end,startTime,endTime,0,1,easing,cut_endTime)
                    cut_end2=cut(start2,end2,startTime,endTime,0,1,easing,cut_endTime)
                    a_line["judgeLineMoveEvents"].append({"startTime":cut_startTime,
                                                        "endTime":cut_endTime,
                                                        "start":cut_start,
                                                        "end":cut_end,
                                                        "start2":cut_start2,
                                                        "end2":cut_end2,
                                                        "easing":1})
        while "delete" in a_line["judgeLineMoveEvents"]:
            a_line["judgeLineMoveEvents"].remove("delete")
        a_line["judgeLineMoveEvents"].sort(key=lambda x:x["startTime"])
        
        a_line["judgeLineMoveEvents"].insert(0,{"startTime":-999999,
                                                "endTime":a_line["judgeLineMoveEvents"][0]["startTime"],
                                                "start":a_line["judgeLineMoveEvents"][0]["start"],
                                                "end":a_line["judgeLineMoveEvents"][0]["start"],
                                                "start2":a_line["judgeLineMoveEvents"][0]["start2"],
                                                "end2":a_line["judgeLineMoveEvents"][0]["start2"]})
        
        time_point=[]
        for j in range(len(rotate_event)):
            if rotate_event[j]["line"]==i:
                rotate_this_line.append(rotate_event[j])
                time_point.append(rotate_event[j]["startTime"])
                try:
                    time_point.append(rotate_event[j]["endTime"])
                except:
                    pass
                rotate_event.pop(j)
                rotate_event.insert(j,"delete")
        while "delete" in rotate_event:
            rotate_event.remove("delete")
        
        time_point=list(set(time_point))
        time_point.sort()
        
        for j in range(len(time_point)):
            startTime=time_point[j]
            try:
                endTime=time_point[j+1]
            except:
                endTime=float("inf")
            a_line["judgeLineRotateEvents"].append({"startTime":startTime,
                                                "endTime":endTime})
        
        for j in range(len(rotate_this_line)):
            
            time=rotate_this_line[j]["startTime"]
            try:
                rstart=rotate_this_line[j]["start"]
            except:
                rend=rotate_this_line[j]["end"]
                easing=rotate_this_line[j]["easing"]
            for k in range(len(a_line["judgeLineRotateEvents"])):
                if a_line["judgeLineRotateEvents"][k]["startTime"]==time:
                    try:
                        a_line["judgeLineRotateEvents"][k].update({"start":rstart})
                        break
                    except:
                        a_line["judgeLineRotateEvents"][k].update({"end":rend,
                                                                "easing":easing})
                        break
            try:
                del rstart
            except:
                del rend
                del easing
                
        for j in range(len(a_line["judgeLineRotateEvents"])):
            key=list(a_line["judgeLineRotateEvents"][j].keys())
            if key==['startTime','endTime']:
                rstart=a_line["judgeLineRotateEvents"][j-1]["end"]
                rend=a_line["judgeLineRotateEvents"][j-1]["end"]
                easing=1
                a_line["judgeLineRotateEvents"][j].update({"start":rstart,
                                                        "end":rend,
                                                        "easing":easing})
            elif key==['startTime','endTime','start']:
                rend=a_line["judgeLineRotateEvents"][j]["start"]
                easing=1
                a_line["judgeLineRotateEvents"][j].update({"end":rend,
                                                        "easing":easing})
            elif key==['startTime','endTime','end','easing']:
                rstart=a_line["judgeLineRotateEvents"][j-1]["end"]
                easing=a_line["judgeLineRotateEvents"][j]["easing"]
                a_line["judgeLineRotateEvents"][j].update({"start":rstart,
                                                        "easing":easing})
                
        for j in range(len(a_line["judgeLineRotateEvents"])):
            easing=a_line["judgeLineRotateEvents"][j]["easing"]
            if easing != 0 and easing != 1:
                startTime=a_line["judgeLineRotateEvents"][j]["startTime"]
                endTime=a_line["judgeLineRotateEvents"][j]["endTime"]
                start=a_line["judgeLineRotateEvents"][j]["start"]
                end=a_line["judgeLineRotateEvents"][j]["end"]
                time_cut=float_range(startTime,endTime,1)
                a_line["judgeLineRotateEvents"].pop(j)
                a_line["judgeLineRotateEvents"].insert(j,"delete")
                for k in range(len(time_cut)-1):
                    cut_startTime=time_cut[k]
                    cut_endTime=time_cut[k+1]
                    cut_start=cut(start,end,startTime,endTime,0,1,easing,cut_startTime)
                    cut_end=cut(start,end,startTime,endTime,0,1,easing,cut_endTime)
                    a_line["judgeLineRotateEvents"].append({"startTime":cut_startTime,
                                                            "endTime":cut_endTime,
                                                            "start":cut_start,
                                                            "end":cut_end,
                                                            "easing":1})
        while "delete" in a_line["judgeLineRotateEvents"]:
            a_line["judgeLineRotateEvents"].remove("delete")
        a_line["judgeLineRotateEvents"].sort(key=lambda x:x["startTime"])
        
        a_line["judgeLineRotateEvents"].insert(0,{"startTime":-999999,
                                                "endTime":a_line["judgeLineRotateEvents"][0]["startTime"],
                                                "start":a_line["judgeLineRotateEvents"][0]["start"],
                                                "end":a_line["judgeLineRotateEvents"][0]["start"]})
        
        time_point=[]
        for j in range(len(alpha_event)):
            if alpha_event[j]["line"]==i:
                alpha_this_line.append(alpha_event[j])
                time_point.append(alpha_event[j]["startTime"])
                try:
                    time_point.append(alpha_event[j]["endTime"])
                except:
                    pass
                alpha_event.pop(j)
                alpha_event.insert(j,"delete")
        while "delete" in alpha_event:
            alpha_event.remove("delete")
            
        time_point=list(set(time_point))
        time_point.sort()
        
        for j in range(len(time_point)):
            startTime=time_point[j]
            try:
                endTime=time_point[j+1]
            except:
                endTime=float("inf")
            a_line["judgeLineDisappearEvents"].append({"startTime":startTime,
                                                "endTime":endTime})
            
        for j in range(len(alpha_this_line)):
            
            time=alpha_this_line[j]["startTime"]
            try:
                astart=alpha_this_line[j]["start"]
            except:
                aend=alpha_this_line[j]["end"]
            for k in range(len(a_line["judgeLineDisappearEvents"])):
                if a_line["judgeLineDisappearEvents"][k]["startTime"]==time:
                    try:
                        a_line["judgeLineDisappearEvents"][k].update({"start":astart})
                        break
                    except:
                        a_line["judgeLineDisappearEvents"][k].update({"end":aend})
                        break
            try:
                del astart
            except:
                del aend
        
        for j in range(len(a_line["judgeLineDisappearEvents"])):
            key=list(a_line["judgeLineDisappearEvents"][j].keys())
            if key==['startTime','endTime']:
                astart=a_line["judgeLineDisappearEvents"][j-1]["end"]
                aend=a_line["judgeLineDisappearEvents"][j-1]["end"]
                a_line["judgeLineDisappearEvents"][j].update({"start":astart,
                                                            "end":aend})
            elif key==['startTime','endTime','start']:
                aend=a_line["judgeLineDisappearEvents"][j]["start"]
                easing=1
                a_line["judgeLineDisappearEvents"][j].update({"end":aend})
            elif key==['startTime','endTime','end']:
                astart=a_line["judgeLineDisappearEvents"][j-1]["end"]
                a_line["judgeLineDisappearEvents"][j].update({"start":astart})
        
        a_line["judgeLineDisappearEvents"].insert(0,{"startTime":-999999,
                                                "endTime":a_line["judgeLineDisappearEvents"][0]["startTime"],
                                                "start":0,
                                                "end":a_line["judgeLineDisappearEvents"][0]["start"]})
        
        new_chart["judgeLineList"].append(a_line)            
                
    return new_chart

def chartify():
    root=tkinter.Tk()
    root.withdraw()
    filePath=filedialog.askopenfilename(filetypes=[('PE谱面','.pec')])
    new_chart=pec2json(filePath)        
    savePath=filedialog.asksaveasfilename(initialfile='Chart'+'.json',filetypes=[("json(官谱格式)", ".json")])
    with open(savePath,"w") as t:
        chart=json.dumps(new_chart)
        t.write(chart)
        t.close()
    