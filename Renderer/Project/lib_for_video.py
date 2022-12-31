# -*- coding: utf-8 -*-
import numpy
import os
from PIL import Image, ImageFilter, ImageChops, ImageEnhance

def Trim(img,hight,width,Blur):
    scale=hight/width
    imgscale=img.height/img.width
    if scale>=imgscale:
        start=int((img.width-(img.height/scale))/2)
        end=int(start+(img.height/scale))
        Tr=img.crop((start,0,end,img.height))
    else:
        start=int((img.height-(img.width*scale))/2)
        end=int(start+(img.width*scale))
        Tr=img.crop((0,start,img.width,end))
    Tr=Tr.resize((width,hight))
    Tr=Tr.filter(ImageFilter.GaussianBlur(radius=Blur*hight/1080))
    Tr=ImageChops.multiply(Tr,Image.new("RGBA",(Tr.width,Tr.height),(200,200,200,255)))
    Tr = ImageEnhance.Brightness(Tr).enhance(0.55) #亮度调整
    return Tr

def f2b(i,fps,BPM):
    s=32*BPM*(i/fps)/60
    return s

def b2f(s,fps,BPM):
    i=60*fps*s/32/BPM
    return int(i)

def cut(start,end,starttime,endtime,point):
    aim=(point-starttime)/(endtime-starttime)
    result=start+(end-start)*aim    
    return result

def present_floor(beat,speed,BPM):
    for i in range(len(speed)):
        if beat>=speed[i]["startTime"] and beat<speed[i]["endTime"]:
            floorstart=speed[i]['floorPosition']
            starttime=speed[i]["startTime"]
            floor=floorstart+(beat-starttime)/32/BPM*60*speed[i]["value"]
            break
    return [floor,floor+5]

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

def holdhead_fix(img):
    layer=Image.new("RGBA",(img.width,int(2*img.height)),(0,0,0,0))
    layer.paste(img,(0,img.height))
    return layer

def holdend_fix(img):
    layer=Image.new("RGBA",(img.width,int(2*img.height)),(0,0,0,0))
    layer.paste(img,(0,0))
    return layer

def speed_fix(note,speed):
    value=note['speed']
    beat=note['time']
    for i in range(len(speed)):
        if beat>=speed[i]["startTime"] and beat<speed[i]["endTime"]:
            value=value/speed[i]["value"]
            break
    return value

def paste_pos(frame,note):
    x1=frame.width*note['linex']
    y1=frame.height*(1-note['liney'])
    x2=x1+320/3*note['positionX']*numpy.cos(note['rotate']/180*numpy.pi)
    y2=y1-320/3*note['positionX']*numpy.sin(note['rotate']/180*numpy.pi)
    distance=note['distance']*650*note["speed"]
    if note['Above']:
        x3=x2+distance*numpy.cos((note['rotate']+90)/180*numpy.pi)
        y3=y2-distance*numpy.sin((note['rotate']+90)/180*numpy.pi)
    else:
        x3=x2-distance*numpy.cos((note['rotate']+90)/180*numpy.pi)
        y3=y2+distance*numpy.sin((note['rotate']+90)/180*numpy.pi)
    return [x3,y3]

def effect_pos(frame,note):
    # print(note)
    x1=frame.width*note['linex']
    y1=frame.height*(1-note['liney'])
    x2=x1+320/3*note['positionX']*numpy.cos(note['rotate']/180*numpy.pi)
    y2=y1-320/3*note['positionX']*numpy.sin(note['rotate']/180*numpy.pi)
    return [x2,y2]

def paste_hold_pos(frame,hold,beat):
    x1=frame.width*hold['linex']
    y1=frame.height*(1-hold['liney'])
    x2=x1+320/3*hold['positionX']*numpy.cos(hold['rotate']/180*numpy.pi)
    y2=y1-320/3*hold['positionX']*numpy.sin(hold['rotate']/180*numpy.pi)
    distance=hold['distance']*650*hold["speed"]
    distance2=hold['distance2']*650*hold["speed"]
    if hold['Above']:
        xhead=x2+distance*numpy.cos((hold['rotate']+90)/180*numpy.pi)
        yhead=y2-distance*numpy.sin((hold['rotate']+90)/180*numpy.pi)
        xend=x2+distance2*numpy.cos((hold['rotate']+90)/180*numpy.pi)
        yend=y2-distance2*numpy.sin((hold['rotate']+90)/180*numpy.pi)
    else:
        xhead=x2-distance*numpy.cos((hold['rotate']+90)/180*numpy.pi)
        yhead=y2+distance*numpy.sin((hold['rotate']+90)/180*numpy.pi)
        xend=x2-distance2*numpy.cos((hold['rotate']+90)/180*numpy.pi)
        yend=y2+distance2*numpy.sin((hold['rotate']+90)/180*numpy.pi)
    if distance>=0 and hold['time']>=beat:
        xbody=0.5*(xhead+xend)
        ybody=0.5*(yhead+yend)
        length=distance2-distance
    else:
        xbody=0.5*(x2+xend)
        ybody=0.5*(y2+yend)
        length=distance2
    if length<=1:
        length=1
    return [[xhead,yhead],[xbody,ybody],[xend,yend],int(length)]

def p4(rotgroup,length,width,img,pos):
    length=length*width/1920*3
    x1=int(pos[0]-(numpy.cos(rotgroup[0]/180*numpy.pi)*length+0.5*img.width))
    y1=int(pos[1]-(numpy.sin(rotgroup[0]/180*numpy.pi)*length+0.5*img.height))
    x2=int(pos[0]-(numpy.cos(rotgroup[1]/180*numpy.pi)*length+0.5*img.width))
    y2=int(pos[1]-(numpy.sin(rotgroup[1]/180*numpy.pi)*length+0.5*img.height))
    x3=int(pos[0]-(numpy.cos(rotgroup[2]/180*numpy.pi)*length+0.5*img.width))
    y3=int(pos[1]-(numpy.sin(rotgroup[2]/180*numpy.pi)*length+0.5*img.height))
    x4=int(pos[0]-(numpy.cos(rotgroup[3]/180*numpy.pi)*length+0.5*img.width))
    y4=int(pos[1]-(numpy.sin(rotgroup[3]/180*numpy.pi)*length+0.5*img.height))
    return [(x1,y1),(x2,y2),(x3,y3),(x4,y4)]

def linepos(hight,width,rotate,xp,yp,aline):
    x0=0.5*width
    y0=0.5*hight
    k=numpy.tan((-rotate%180)*numpy.pi/180)
    if k==0:
        y=yp
        x=x0
    elif rotate%90==0:
        y=y0
        x=xp
    else:
        x=(x0/k+y0+k*xp-yp)/(1/k+k)
        y=k*x-k*xp+yp
    return (int(x-0.5*aline.width),int(y-0.5*aline.height),int(x),int(y))
    
def score(combo,total):
    s=int(1000000*combo/total)
    t=str(10000000+s)
    return t[1:]

def beat2msec(s, bpm, hitsoundoffset):
    return 60 * s / 32 / bpm * 1000 + hitsoundoffset

def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        return True
    else:
        return False
    
