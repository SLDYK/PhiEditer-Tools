from tkinter import *
from tkinter.messagebox import *
from tkinter import filedialog
from tkinter import ttk
import zipfile
import os

def load():
    with open("Settings.txt","r",encoding="utf_8") as t:
        chartdata=t.readlines()
        t.close()
    global table
    elem=table.get_children()
    for item in elem:
        table.delete(item)
    j=0
    for i in range(0,len(chartdata)):
        if chartdata[i]=="#\n":
            table.insert("",j,values=(chartdata[i+1][6:-1],chartdata[i+2][6:-1],chartdata[i+3][9:-1],chartdata[i+4][7:-1],chartdata[i+5][7:-1],chartdata[i+6][10:-1],chartdata[i+7][9:-1]))

def importchart():
    picture=["png","jpg","jpeg"]
    music=["mp3","wav","ogg"]
    filePath=filedialog.askopenfilename(filetypes=[('PE谱面','.zip')])
    fz=zipfile.ZipFile(filePath,"r")
    level="无信息"
    composer="无信息"
    charter="无信息"
    for file in fz.namelist():
        if file.split(".")[-1]=="pec":
            fz.extract(file,)
            chart=file
        elif file.split(".")[-1] in music:
            fz.extract(file,"Resources/")
            music=file
        elif file.split(".")[-1] in picture:
            fz.extract(file,"Resources/")
            picture=file
        elif file=="info.csv":
            fz.extract(file,"infodir/")
            with open("infodir/info.csv","r",encoding="utf_8") as t:
                data=t.readlines()
                level=data[-1].split(",")[7]
                charter=data[-1].split(",")[9]
                t.close()
            os.remove("infodir/info.csv")
            os.rmdir("infodir")
    fz.close()
    with open("Settings.txt","a",encoding="utf_8") as t:
        info="\n#\nName: "+filePath.split("/")[-1][:-4]+"\nSong: "+music+"\nPicture: "+picture+"\nChart: "+chart+"\nLevel: "+level+"\nComposer: "+composer+"\nCharter: "+charter+"\n"
        t.write(info)
        t.close()
    result=showinfo("导入成功","PhiEditer:啊，要进去了")
    load()

def exportchart(item):
    
    def infocsv(infolist):
        setinfo.destroy()
        item=infolist[7]
        savePath=filedialog.asksaveasfilename(initialfile=item[0]+'.zip',filetypes=[("PE谱面", ".zip")])
        with open("infodata","w",encoding="utf_8") as t:
            t.write("Chart,Music,Image,AspectRatio,ScaleRatio,GlobalAlpha,Name,Level,Illustrator,Designer\n谱面,音乐,图片,宽高比,按键缩放,背景变暗,名称,等级,曲绘,谱师\n")
            t.write(infolist[3]+","+infolist[1]+","+infolist[2]+",,,,"+infolist[0]+","+infolist[8]+","+infolist[6]+","+infolist[5])
            t.close()
        z=zipfile.ZipFile(savePath,"w",zipfile.ZIP_DEFLATED)
        z.write(item[3],item[3])
        z.write("Resources/"+item[1],item[1])
        z.write("Resources/"+item[2],item[2])
        z.write("infodata","info.csv")
        z.close()
        os.remove("infodata")
        result=showinfo("导出成功","PhiEditer:啊，导出来了")
        
    holdon=False
    global table
    if item=="":
        result=showinfo("无从下手","靠杯啦你还没有选择谱面诶")
    else:
        info=askyesno("嘿！这个试图导出谱面的家伙","如果，我是说如果，你是否需要一份info.csv在你的zip里呢")
        if info:
            setinfo=Toplevel()
            setinfo.title("既然这样伙计")
            setinfo.geometry("300x300")
            subtitle=Label(setinfo, text="那你得填填这个了",font=('', 10),width=30,height=1)
            subtitle.place(relx=0.5,rely=0.1,anchor=CENTER)
            
            name=Label(setinfo, text='名称:',font=('',10),width=10,height=1)
            name.place(relx=0.15,rely=0.19,anchor=CENTER)
            enname=Entry(setinfo,show=None,width=15)
            enname.insert(0,item[0])
            enname.place(relx=0.4,rely=0.19,anchor=CENTER)

            music=Label(setinfo, text='音频:',font=('',10),width=10,height=1)
            music.place(relx=0.15,rely=0.28,anchor=CENTER)
            enmusic=Entry(setinfo,show=None,width=15)
            enmusic.insert(0,item[1])
            enmusic.place(relx=0.4,rely=0.28,anchor=CENTER)

            photo=Label(setinfo, text='背景:',font=('',10),width=10,height=1)
            photo.place(relx=0.15,rely=0.37,anchor=CENTER)
            enphoto=Entry(setinfo,show=None,width=15)
            enphoto.insert(0,item[2])
            enphoto.place(relx=0.4,rely=0.37,anchor=CENTER)

            chart=Label(setinfo, text='谱面:',font=('',10),width=10,height=1)
            chart.place(relx=0.15,rely=0.46,anchor=CENTER)
            enchart=Entry(setinfo,show=None,width=15)
            enchart.insert(0,item[3])
            enchart.place(relx=0.4,rely=0.46,anchor=CENTER)

            level=Label(setinfo, text='难度:',font=('',10),width=10,height=1)
            level.place(relx=0.15,rely=0.55,anchor=CENTER)
            enlevel=Entry(setinfo,show=None,width=15)
            enlevel.insert(0,item[4])
            enlevel.place(relx=0.4,rely=0.55,anchor=CENTER)

            composer=Label(setinfo, text='曲师:',font=('',10),width=10,height=1)
            composer.place(relx=0.15,rely=0.64,anchor=CENTER)
            encomposer=Entry(setinfo,show=None,width=15)
            encomposer.insert(0,item[5])
            encomposer.place(relx=0.4,rely=0.64,anchor=CENTER)

            charter=Label(setinfo, text='谱师:',font=('',10),width=10,height=1)
            charter.place(relx=0.15,rely=0.73,anchor=CENTER)
            encharter=Entry(setinfo,show=None,width=15)
            encharter.insert(0,item[6])
            encharter.place(relx=0.4,rely=0.73,anchor=CENTER)

            illustrator=Label(setinfo, text='画师:',font=('',10),width=10,height=1)
            illustrator.place(relx=0.15,rely=0.82,anchor=CENTER)
            enillustrator=Entry(setinfo,show=None,width=15)
            enillustrator.insert(0,"无信息")
            enillustrator.place(relx=0.4,rely=0.82,anchor=CENTER)

            done=Button(setinfo,text='是的，当然，我都交代了',font=('',10),width=22,height=1,command=lambda:infocsv([enname.get(),enmusic.get(),enphoto.get(),enchart.get(),encomposer.get(),encharter.get(),enillustrator.get(),item,enlevel.get()]))
            done.place(relx=0.5,rely=0.92,anchor=CENTER)
            setinfo.mainloop()
        else:
            holdon=True
        while holdon:
            holdon=False
            savePath=filedialog.asksaveasfilename(initialfile=item[0]+'.zip',filetypes=[("PE谱面", ".zip")])    
            z=zipfile.ZipFile(savePath,"w",zipfile.ZIP_DEFLATED)
            z.write(item[3],item[3])
            z.write("Resources/"+item[1],item[1])
            z.write("Resources/"+item[2],item[2])
            z.close()
            result=showinfo("导出成功","PhiEditer:啊，导出来了")

def deletechart(item):
    global table
    if item=="":
        result=showinfo("无从下手","靠杯啦你还没有选择谱面诶")
    else:
        result=askyesno("看在上帝的份上","我的老伙计，我是说你真的要这么做吗")
        if result:
            os.remove(item[3])
            os.remove("Resources/"+item[1])
            os.remove("Resources/"+item[2])
            info="\n#\nName: "+item[0]+"\nSong: "+item[1]+"\nPicture: "+item[2]+"\nChart: "+item[3]+"\nLevel: "+item[4]+"\nComposer: "+item[5]+"\nCharter: "+item[6]
            with open("Settings.txt","r",encoding="utf_8") as t:
                basicset=t.read()
                t.close()
            with open("Settings.txt","w",encoding="utf_8") as t:
                t.write(basicset.replace(info,""))
                t.close
            result=showinfo("谱面已删除",item[0]+":我真的会谢")
        load()

root=Tk()
root.title("1615的PE管理器")
root.geometry("615x300")
b1=Button(root,text='导入谱面',font=('',10),width=10,height=2,command=importchart)
b1.place(relx=0.09,rely=0.1,anchor=CENTER)
b2=Button(root,text='导出谱面',font=('',10),width=10,height=2,command=lambda:exportchart(table.item(table.selection(),"values")))
b2.place(relx=0.24,rely=0.1,anchor=CENTER)
b3=Button(root,text='删除谱面',font=('',10),width=10,height=2,command=lambda:deletechart(table.item(table.selection(),"values")))
b3.place(relx=0.39,rely=0.1,anchor=CENTER)
b4=Button(root,text='加载数据',font=('',10),width=10,height=2,command=load)
b4.place(relx=0.87,rely=0.1,anchor=CENTER)
table=ttk.Treeview(root,columns=("名称","音频","背景","谱面","难度","作曲","作谱"),show="headings")
table.column("名称",width=80)
table.column("音频",width=80)
table.column("背景",width=80)
table.column("谱面",width=80)
table.column("难度",width=80)
table.column("作曲",width=80)
table.column("作谱",width=80)
table.heading("名称",text="名称")
table.heading("音频",text="音频")
table.heading("背景",text="背景")
table.heading("谱面",text="谱面")
table.heading("难度",text="难度")
table.heading("作曲",text="作曲")
table.heading("作谱",text="作谱")
table.place(relx=0.48,rely=0.57,anchor=CENTER)
ybar=ttk.Scrollbar(root,orient="vertical",command=table.yview)
table["yscroll"]=ybar.set
ybar.place(relx=0.96,rely=0.3,anchor=CENTER)
root.mainloop()
