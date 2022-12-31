# -*- coding: utf-8 -*-
import math

def end_floor(beat,speed,BPM):
    for i in range(len(speed)):
        if beat>=speed[i]["startTime"] and beat<speed[i]["endTime"]:
            floorstart=speed[i]['floorPosition']
            starttime=speed[i]["startTime"]
            floor=floorstart+(beat-starttime)/32/BPM*60*speed[i]["value"]
            break
        else:
            floor=0
    return floor

def float_range(start,end,step):
    result=[start]
    while start+step < end:
        start+=step
        result.append(start)
    result.append(end)
    return result

def recent_speed(beat,speed):
    for i in range(len(speed)):
        if beat>=speed[i]["startTime"] and beat<speed[i]["endTime"]:
            return speed[i]["value"]

def cut(start,end,starttime,endtime,left,right,ease,point):
    def f(x,ease):
        if ease==0 or ease==1:
            return x
        elif ease==2:
            return math.sin((x*math.pi)/2)
        elif ease==3:
            return 1-math.cos((x*math.pi)/2)
        elif ease==4:
            return 1-(1-x)*(1-x)
        elif ease==5:
            return x*x
        elif ease==6:
            return -(math.cos(math.pi*x)-1)/2
        elif ease==7:
            if x<0.5:
                return 2*x*x
            else:
                return 1-math.pow(-2*x+2,2)/2
        elif ease==8:
            return 1-math.pow(1-x,3)
        elif ease==9:
            return x*x*x
        elif ease==10:
            return 1-math.pow(1-x,4)
        elif ease==11:
            return x*x*x*x
        elif ease==12:
            if x<0.5:
                return 4*x*x*x
            else:
                return 1-math.pow(-2*x+2,3)/2
        elif ease==13:
            if x<0.5:
                return 8*x*x*x*x
            else:
                return 1-math.pow(-2*x+2,4)/2
        elif ease==14:
            return 1-math.pow(1-x,5)
        elif ease==15:
            return x*x*x*x*x
        elif ease==16:
            if x==1:
                return 1
            else:
                return 1-math.pow(2,-10*x)
        elif ease==17:
            if x==0:
                return 0
            else:
                return math.pow(2,10*x-10)
        elif ease==18:
            return math.sqrt(1 - math.pow(x - 1, 2))
        elif ease==19:
            return 1-math.sqrt(1-math.pow(x,2))
        elif ease==20:
            c1=1.70158
            c3=c1+1
            return 1+c3*math.pow(x-1,3)+c1*math.pow(x-1,2)
        elif ease==21:
            c1=1.70158
            c3=c1+1
            return c3*x*x*x-c1*x*x
        elif ease==22:
            if x<0.5:
                return (1-math.sqrt(1-math.pow(2*x,2)))/2
            else:
                return (math.sqrt(1-math.pow(-2*x+2,2))+1)/2
        elif ease==23:
            c1=1.70158
            c2=c1*1.525
            if x<0.5:
                return (math.pow(2*x,2)*((c2+1)*2*x-c2))/2
            else:
                return (math.pow(2*x-2,2)*((c2+1)*(x*2-2)+c2)+2)/2
        elif ease==24:
            c4=(2*math.pi)/3
            if x==0:
                return 0
            elif x==1:
                return 1
            else:
                return math.pow(2,-10*x)*math.sin((x*10-0.75)*c4)+1
        elif ease==25:
            c4=(2*math.pi)/3
            if x==0:
                return 0
            elif x==1:
                return 1
            else:
                return -math.pow(2,10*x-10)*math.sin((x*10-10.75)*c4)
        elif ease==26:
            if x<4/11:
                return math.pow(x*11,2)
            elif x<8/11:
                return math.pow(x*11-6,2)+12
            elif x<10/11:
                return math.pow(x*11-9,2)+15
            else:
                return math.pow(x*11-10.5,2)+15.75
        elif ease==27:
            return 1-f(x,26)
        elif ease==28:
            if x<0.5:
                return (1-f(1-2*x,27))/2
            else:
                return (1+f(2*x-1,26))/2
        elif ease==29:
            c5=(2*math.pi)/4.5
            if x==0:
                return 0
            elif x==1:
                return 1
            elif x<0.5:
                return -(math.pow(2,20*x-10)*math.sin((20*x-11.125)*c5))/2
            else:
                return (math.pow(2,-20*x+10)*math.sin((20*x-11.125)*c5))/2+1
    aim=left+(right-left)*(point-starttime)/(endtime-starttime)
    mult=(f(aim,ease)-f(left,ease))/(f(right,ease)-f(left,ease))
    result=start+(end-start)*mult    
    return result

def beat2sec(beat,bpm,offset):
    time=-offset
    for i in range(0,len(bpm)-1):
        if beat>=bpm[i][0] and beat>=bpm[i+1][0]:
            time=time+(bpm[i+1][0]-bpm[i][0])/bpm[i][1]*60
        if beat>=bpm[i][0] and beat<bpm[i+1][0]:
            time=time+(beat-bpm[i][0])/bpm[i][1]*60
    return time

def sec2beat(time,bpm):
    beat=time*bpm/60
    return beat