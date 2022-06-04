from tkinter import *
from tkinter import filedialog
import math
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
def getposx(camposdata,campospoint,time):
    if [m for m in campospoint[0] if m<=time]!=[]:
        x=campospoint[1][campospoint[0].index((max([m for m in campospoint[0] if m<=time])))]
    for i in range(0,len(camposdata[0])):
        if time>=camposdata[0][i] and time<camposdata[1][i]:
            x=camposdata[2][i]+(time-camposdata[0][i])/(camposdata[1][i]-camposdata[0][i])*(camposdata[3][i]-camposdata[2][i])
            break
    return x
def getposy(camposdata,campospoint,time):
    if [m for m in campospoint[0] if m<=time]!=[]:
        y=campospoint[2][campospoint[0].index((max([m for m in campospoint[0] if m<=time])))]
    for i in range(0,len(camposdata[0])):
        if time>=camposdata[0][i] and time<camposdata[1][i]:
            y=camposdata[4][i]+(time-camposdata[0][i])/(camposdata[1][i]-camposdata[0][i])*(camposdata[5][i]-camposdata[4][i])
            break
    return y
def getrot(camrotdata,camrotpoint,time):
    if [m for m in camrotpoint[0] if m<=time]!=[]:
        r=camrotpoint[1][camrotpoint[0].index((max([m for m in camrotpoint[0] if m<=time])))]
    for i in range(0,len(camrotdata[0])):
        if time>=camrotdata[0][i] and time<camrotdata[1][i]:
            r=camrotdata[2][i]+(time-camrotdata[0][i])/(camrotdata[1][i]-camrotdata[0][i])*(camrotdata[3][i]-camrotdata[2][i])
            break
    return r
def rot(x1,y1,x2,y2):
    if x1<x2:
        r=math.asin((y2-y1)/(math.sqrt(pow((x2-x1),2)+pow((y2-y1),2))))
    elif x1==x2 and y1<y2:
        r=math.pi/2
    elif x1==x2 and y1>y2:
        r=math.pi/2*(-1)
    elif x1>x2:
        r=math.pi-math.asin((y2-y1)/(math.sqrt(pow((x2-x1),2)+pow((y2-y1),2))))
    elif x1==x2 and y1==y2:
        r=0
    return r
root=Tk()
root.withdraw()
print("欢迎使用1615的判定线追踪动画生成器\n遇到bug请及时反馈作者哦\n")
filePath=filedialog.askopenfilename(filetypes=[('PE谱面','.pec')])
cameraline=int(input("摄像机基准线号："))
deal=["cm","cr","cp","cd"]
end=0
track=input("请输入追踪线号（如有多条用空格隔开）：")
track=track.split()
for i in range(0,len(track)):
    track[i]=int(track[i])
starttime=float(input("开始时间："))
endtime=float(input("结束时间："))
with open(filePath,"r") as t:
    data=t.readlines()
    t.close()
keep=[data[0],data[1]]
dealdata=[]
cameradata=[]
for i in range(2,len(data)):
    event=data[i].split()
    if event==[]:
        pass
    elif "n" in event[0]:
        keep.append(data[i])
        keep.append(data[i+1])
        keep.append(data[i+2])
    elif "#" in event[0]:
        pass
    elif "&" in event[0]:
        pass
    elif int(event[1])==cameraline:
        keep.append(data[i])
        if event[0] in deal:
            cameradata.append(data[i])
    elif int(event[1]) in track:
        if event[0] in deal:
            dealdata.append(data[i])
        else:
            keep.append(data[i])
    else:
        keep.append(data[i])
campospoint=[[],[],[]]
camrotpoint=[[],[]]
for i in range(0,len(cameradata)):
    event=cameradata[i].split()
    if event[0]=="cp":
        campospoint[0].append(float(event[2]))
        campospoint[1].append((float(event[3])-1024)*(-1)+1024)
        campospoint[2].append(float(event[4]))
    elif event[0]=="cd":
        camrotpoint[0].append(float(event[2]))
        camrotpoint[1].append(float(event[3]))
    elif event[0]=="cm":
        campospoint[0].append(float(event[3]))
        campospoint[1].append((float(event[4])-1024)*(-1)+1024)
        campospoint[2].append(float(event[5]))
    else:
        camrotpoint[0].append(float(event[3]))
        camrotpoint[1].append(float(event[4]))
camposdata=[[],[],[],[],[],[]]#timestart,timeend,xstart,xend,ystart,yend
camrotdata=[[],[],[],[]]#timestart,timeend,rotstart,rotend
for i in range(0,len(cameradata)):
    event=cameradata[i].split()
    if event[0]=="cm" and float(event[2])<=endtime and float(event[3])>=starttime:
        timestart=float(event[2])
        timeend=float(event[3])
        xstart=campospoint[1][campospoint[0].index((max([x for x in campospoint[0] if x<=timestart])))]
        ystart=campospoint[2][campospoint[0].index((max([x for x in campospoint[0] if x<=timestart])))]
        xend=(float(event[4])-1024)*-1+1024
        yend=float(event[5])
        mult=16*(timeend-timestart)
        if mult<1:
            mult=1
        timecut=cut(timestart,timeend,mult,1)
        xcut=cut(xstart,xend,mult,int(event[6]))
        ycut=cut(ystart,yend,mult,int(event[6]))
        for i in range(0,len(timecut)-1):
            camposdata[0].append(timecut[i])
            camposdata[1].append(timecut[i+1])
            camposdata[2].append(xcut[i])
            camposdata[3].append(xcut[i+1])
            camposdata[4].append(ycut[i])
            camposdata[5].append(ycut[i+1])
    elif event[0]=="cr" and float(event[2])<=endtime and float(event[3])>=starttime:
        timestart=float(event[2])
        timeend=float(event[3])
        rstart=camrotpoint[1][camrotpoint[0].index((max([x for x in camrotpoint[0] if x<=timestart])))]
        rend=float(event[4])
        mult=16*(timeend-timestart)
        timecut=cut(timestart,timeend,mult,1)
        rcut=cut(rstart,rend,mult,int(event[5]))
        for i in range(0,len(timecut)-1):
            camrotdata[0].append(timecut[i])
            camrotdata[1].append(timecut[i+1])
            camrotdata[2].append(rcut[i])
            camrotdata[3].append(rcut[i+1])
camstx=getposx(camposdata,campospoint,starttime)
camsty=getposy(camposdata,campospoint,starttime)
camstr=getrot(camrotdata,camrotpoint,starttime)
for j in track:
    trackpospoint=[[],[],[]]
    trackrotpoint=[[],[]]
    for i in range(0,len(dealdata)):
        event=dealdata[i].split()
        if int(event[1])==j and event[0]=="cp":
            trackpospoint[0].append(float(event[2]))
            trackpospoint[1].append((float(event[3])-1024)*(-1)+1024)
            trackpospoint[2].append(float(event[4]))
        elif int(event[1])==j and event[0]=="cd":
            trackrotpoint[0].append(float(event[2]))
            trackrotpoint[1].append(float(event[3]))
        elif int(event[1])==j and event[0]=="cm":
            trackpospoint[0].append(float(event[3]))
            trackpospoint[1].append((float(event[4])-1024)*(-1)+1024)
            trackpospoint[2].append(float(event[5]))
        elif int(event[1])==j and event[0]=="cr":
            trackrotpoint[0].append(float(event[3]))
            trackrotpoint[1].append(float(event[4]))
    for i in range(0,len(dealdata)):
        event=dealdata[i].split()
        if int(event[1])==j and event[0]=="cr" and float(event[2])<=endtime and float(event[3])>=starttime:
            timestart=float(event[2])
            timeend=float(event[3])
            rstart=trackrotpoint[1][trackrotpoint[0].index((max([x for x in trackrotpoint[0] if x<=timestart])))]
            rend=float(event[4])
            mult=16*(timeend-timestart)
            if mult<1:
                mult=1
            timecut=cut(timestart,timeend,mult,1)
            rcut=cut(rstart,rend,mult,int(event[5]))
            for m in range(0,len(timecut)-1):
                time1=timecut[m]
                time2=timecut[m+1]
                changerot=getrot(camrotdata,camrotpoint,time2)-camstr
                frot=rcut[m+1]+changerot
                pecline="cr "+str(j)+" "+str(round(time1,3))+" "+str(round(time2,3))+" "+str(round(frot,3))+" 1\n"
                keep.append(pecline)
    for i in range(0,len(dealdata)):
        event=dealdata[i].split()
        if int(event[1])==j and event[0]=="cm" and float(event[2])<=endtime and float(event[3])>=starttime:
            timestart=float(event[2])
            timeend=float(event[3])
            xstart=trackpospoint[1][trackpospoint[0].index((max([x for x in trackpospoint[0] if x<=timestart])))]
            ystart=trackpospoint[2][trackpospoint[0].index((max([x for x in trackpospoint[0] if x<=timestart])))]
            xend=(float(event[4])-1024)*-1+1024
            yend=float(event[5])
            mult=16*(timeend-timestart)
            if mult<1:
                mult=1
            timecut=cut(timestart,timeend,mult,1)
            xcut=cut(xstart,xend,mult,int(event[6]))
            ycut=cut(ystart,yend,mult,int(event[6]))
            for m in range(0,len(timecut)-1):
                time1=timecut[m]
                time2=timecut[m+1]
                pecx=xcut[m+1]
                pecy=ycut[m+1]
                changerot=getrot(camrotdata,camrotpoint,time2)-camstr
                changex=getposx(camposdata,campospoint,time2)-camstx
                changey=getposy(camposdata,campospoint,time2)-camsty
                long=math.sqrt(pow((pecx-camstx),2)+pow((pecy-camsty),2))
                newrot=rot(camstx,camsty,pecx,pecy)+changerot/180*math.pi
                rotx=(camstx-1024)*-1+1024-long*math.cos(newrot)-changex
                roty=camsty+long*math.sin(newrot)+changey
                pecline="cm "+str(j)+" "+str(round(time1,3))+" "+str(round(time2,3))+" "+str(round(rotx,3))+" "+str(round(roty,3))+" 1\n"
                keep.append(pecline)
        elif int(event[1])==j and event[0]=="cp" and float(event[2])<=endtime and float(event[2])>=starttime:
            time2=float(event[2])
            pecx=float(event[3])
            pecy=float(event[4])
            changerot=getrot(camrotdata,camrotpoint,time2)-camstr
            changex=getposx(camposdata,campospoint,time2)-camstx
            changey=getposy(camposdata,campospoint,time2)-camsty
            long=math.sqrt(pow((pecx-camstx),2)+pow((pecy-camsty),2))
            newrot=rot(camstx,camsty,pecx,pecy)+changerot/180*math.pi
            rotx=(camstx-1024)*-1+1024+long*math.cos(newrot)-changex
            roty=camsty+long*math.sin(newrot)+changey
            pecline="cp "+str(j)+" "+str(round(time2,3))+" "+str(round(rotx,3))+" "+str(round(roty,3))+"\n"
            keep.append(pecline)
        elif int(event[1])==j and event[0]=="cd" and float(event[2])<=endtime and float(event[2])>=starttime:
            time2=float(event[2])
            pecrot=float(event[3])
            changerot=getrot(camrotdata,camrotpoint,time2)-camstr
            newrot=pecrot+changerot
            pecline="cd "+str(j)+" "+str(round(time2,3))+" "+str(round(newrot,3))+"\n"
            keep.append(pecline)
    for i in range(0,len(dealdata)):
        event=dealdata[i].split()
        if int(event[1])==j and event[0]=="cr":
            if float(event[2])>endtime or float(event[3])<=starttime:
                keep.append(dealdata[i])
        if int(event[1])==j and event[0]=="cm":
            if float(event[2])>endtime or float(event[3])<=starttime:
                keep.append(dealdata[i])
        if int(event[1])==j and event[0]=="cd":
            if float(event[2])>endtime or float(event[2])<=starttime:
                keep.append(dealdata[i])
        if int(event[1])==j and event[0]=="cp":
            if float(event[2])>endtime or float(event[2])<=starttime:
                keep.append(dealdata[i])
savePath=filedialog.asksaveasfilename(initialfile='在此处为PEC谱面命名'+'.pec',filetypes=[("PEC谱面", ".pec")])
with open(savePath,"w") as t:
    for i in range(0,len(keep)):
        t.write(keep[i])
    t.close()
