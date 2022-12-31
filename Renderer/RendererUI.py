# -*- coding: utf-8 -*-
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox
import traceback
import tkinter
from video_maker import start_rendering
from pec2json import chartify

def renderer():
    
    def init():#谱面基本信息框
        
        def infoed():#点击“下一步”后执行
        
            try:#检查数据可用性
            #if True:
                if enName.get()=="":
                    raise TypeError("input error")
                else:
                    name=enName.get()
                    
                if enLevel.get()=="":
                    raise TypeError("input error")
                else:
                    level=enLevel.get()
                    
                if enSpecs.get()=="":
                    raise TypeError("input error")
                else:
                    specs=enSpecs.get()
                    width=int(specs.split()[0].split("x")[0])
                    hight=int(specs.split()[0].split("x")[1])
                    fps=int(specs.split()[2].replace("fps",""))
                    
                if enChartPath.get()=="":
                    raise TypeError("input error")
                else:
                    chart=enChartPath.get()
                    
                if enPicturePath.get()=="":
                    raise TypeError("input error")
                else:
                    picture=enPicturePath.get()
                    
                if enSongPath.get()=="":
                    raise TypeError("input error")
                else:
                    song=enSongPath.get()
                    
                if enBlur.get()=="":
                    raise TypeError("input error")
                else:
                    blur=int(enBlur.get().split()[0])
                    
                if enHighLight.get()=="开启":
                    Highlight=True
                else:
                    Highlight=False
                    
                if enNoteSize.get()=="":
                    raise TypeError("input error")
                else:
                    notesize=float(enNoteSize.get().split()[0])
                
                setinfo.destroy()
                
                start_rendering(name,level,width,hight,fps,chart,picture,song,Highlight,blur,notesize)
                
            except :#不可用则报错
                with open("ErrorsLog.txt","a",encoding="utf_8") as t:
                    traceback.print_exc(file=t)
                    t.close()
                
        def Select(var):#文件选择框
            if var==Select1:
                filePath=filedialog.askopenfilename(filetypes=[('谱面文件','.json .pec')])
                enChartPath.insert(0,filePath)
            elif var==Select2:
                filePath=filedialog.askopenfilename(filetypes=[('图片文件','.jpg .png')])
                enPicturePath.insert(0,filePath)
            else:
                filePath=filedialog.askopenfilename(filetypes=[('音频文件','.mp3 .wav .m4a .ogg .aac')])
                enSongPath.insert(0,filePath)
          
        setinfo=tkinter.Toplevel()
        setinfo.title("Settings")
        setinfo.geometry("600x420")
        subtitle=tkinter.Label(setinfo,text="设置视频信息",font=('',12),width=30,height=1)
        subtitle.place(x=300,y=30,anchor=tkinter.CENTER)
        
        Name=tkinter.Label(setinfo, text='曲名:',font=('',10),width=10,height=1)
        Name.place(x=100,y=80,anchor="e")
        enName=tkinter.Entry(setinfo,show=None,width=22)
        enName.insert(0,"")
        enName.place(x=100,y=80,anchor="w")
        
        Level=tkinter.Label(setinfo,text='等级:',font=('',10),width=10,height=1)
        Level.place(x=100,y=130,anchor="e")
        enLevel=tkinter.Entry(setinfo,show=None,width=22)
        enLevel.insert(0,"")
        enLevel.place(x=100,y=130,anchor="w")
        
        Specs=tkinter.Label(setinfo,text='规格:',font=('',10),width=10,height=1)
        Specs.place(x=100,y=180,anchor="e")
        var1=tkinter.StringVar()
        var1.set("1920x1080 16:9 60fps")
        enSpecs=ttk.Combobox(setinfo,width=20,textvariable=var1,state="readonly")
        enSpecs['values']=("1920x1080 16:9 60fps",
                          "1440x1080 4:3  60fps",
                          "1580x1080 PE   60fps",
                          "3840x2160 16:9 60fps",
                          "2880x2160 4:3  60fps",
                          "3240x2160 PE   60fps",
                          "1920x1080 16:9 120fps",
                          "1440x1080 4:3  120fps",
                          "1620x1080 PE   120fps",
                          "3840x2160 16:9 120fps",
                          "2880x2160 4:3  120fps",
                          "3160x2160 PE   120fps")
        enSpecs.place(x=100,y=180,anchor="w") 
        
        ChartPath=tkinter.Label(setinfo,text='谱面文件:',font=('',10),width=10,height=1)
        ChartPath.place(x=100,y=230,anchor="e")
        enChartPath=tkinter.Entry(setinfo,show=None,width=46)
        enChartPath.insert(0,"")
        enChartPath.place(x=100,y=230,anchor="w")
        Select1=tkinter.Button(setinfo,text='选择谱面',font=('',10),width=15,height=1,
                            command=lambda:Select(Select1))
        Select1.place(x=560,y=230,anchor="e")
        
        PicturePath=tkinter.Label(setinfo,text='曲绘文件:',font=('',10),width=10,height=1)
        PicturePath.place(x=100,y=280,anchor="e")
        enPicturePath=tkinter.Entry(setinfo,show=None,width=46)
        enPicturePath.insert(0,"")
        enPicturePath.place(x=100,y=280,anchor="w")
        Select2=tkinter.Button(setinfo,text='选择曲绘',font=('',10),width=15,height=1,
                            command=lambda:Select(Select2))
        Select2.place(x=560,y=280,anchor="e")
        
        SongPath=tkinter.Label(setinfo,text='音频文件:',font=('',10),width=10,height=1)
        SongPath.place(x=100,y=330,anchor="e")
        enSongPath=tkinter.Entry(setinfo,show=None,width=46)
        enSongPath.insert(0,"")
        enSongPath.place(x=100,y=330,anchor="w")
        Select3=tkinter.Button(setinfo,text='选择音频',font=('',10),width=15,height=1,
                            command=lambda:Select(Select3))
        Select3.place(x=560,y=330,anchor="e")
        
        HighLight=tkinter.Label(setinfo, text='双押高亮:',font=('',10),width=10,height=1)
        HighLight.place(x=350,y=80,anchor="e")
        var2=tkinter.StringVar()
        var2.set("开启")
        enHighLight=ttk.Combobox(setinfo,width=20,textvariable=var2,state="readonly")
        enHighLight['values']=("开启",
                          "关闭")
        enHighLight.place(x=350,y=80,anchor="w")
        
        NoteSize=tkinter.Label(setinfo, text='Note大小:',font=('',10),width=10,height=1)
        NoteSize.place(x=350,y=130,anchor="e")
        enNoteSize=tkinter.Entry(setinfo,show=None,width=22)
        enNoteSize.insert(0,"1.4 #推荐值#")
        enNoteSize.place(x=350,y=130,anchor="w")
        
        Blur=tkinter.Label(setinfo, text='背景模糊度:',font=('',10),width=10,height=1)
        Blur.place(x=350,y=180,anchor="e")
        enBlur=tkinter.Entry(setinfo,show=None,width=22)
        enBlur.insert(0,"70 #推荐值#")
        enBlur.place(x=350,y=180,anchor="w")
        
        OpenZip=tkinter.Button(setinfo,text='选择Zip文件',font=('',10),width=22,height=1,
                            command=lambda:messagebox.showinfo("肥肠抱歉","这个功能还没做"))
        OpenZip.place(x=180,y=380,anchor=tkinter.CENTER)
        
        done=tkinter.Button(setinfo,text='下一步',font=('',10),width=22,height=1,
                            command=lambda:infoed())
        done.place(x=420,y=380,anchor=tkinter.CENTER)
        setinfo.mainloop()
    
    init()


root=tkinter.Tk()
root.title("PE/json Chart Renderer")
root.geometry("400x300")
title1=tkinter.Label(root, text='PE/json Chart Renderer 0.1.0',font=('',12),width=30,height=2)
title1.place(relx=0.5,rely=0.1,anchor=tkinter.CENTER)
botton1=tkinter.Button(root,text='Chart rendering',font=('',10),width=20,height=2,command=renderer)
botton1.place(relx=0.5,rely=0.33,anchor=tkinter.CENTER)
botton2=tkinter.Button(root,text='Convert pec to json',font=('',10),width=20,height=2,command=chartify)
botton2.place(relx=0.5,rely=0.55,anchor=tkinter.CENTER)
title2=tkinter.Label(root, text='注：支持PE0.1.9.2的pec格式\nformatVersion3的官谱json格式',font=('',12),width=100,height=3)
title2.place(relx=0.5,rely=0.85,anchor=tkinter.CENTER)
root.mainloop()