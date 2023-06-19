# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import tkinter
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from tkinter.ttk import Notebook, Frame
import zipfile
import os
import traceback
import shutil

def load():
    try:
        with open("PEdata","r",encoding="utf_8") as p:
            PEdata=p.read()
            p.close()
        with open(PEdata+"Chartlist.txt","r",encoding="utf_8") as t:
            chartdata=t.readlines()
            t.close()
        #global table
        elem=table.get_children()
        for item in elem:
            table.delete(item)
        for i in range(0,len(chartdata)):
            if chartdata[i]=="#\n":
                
                table.insert("",0,values=(chartdata[i+1][6:-1],
                                          chartdata[i+2][6:-1],
                                          chartdata[i+3][9:-1],
                                          chartdata[i+4][7:-1],
                                          chartdata[i+5][7:-1],
                                          chartdata[i+6][10:-1],
                                          chartdata[i+7][9:-1],
                                          chartdata[i+8][9:-1],))
    except:
        with open("ErrorsLog.txt","a",encoding="utf_8") as t:
            traceback.print_exc(file=t)
            t.close()
        messagebox.showinfo("绑定RPE","首次运行时请绑定您的Re:PhiEdit")
        PEPath=filedialog.askopenfilename(initialfile="PhiEdit.exe",filetypes=[('PhiEdit','.exe')])
        with open("PEdata","w",encoding="utf_8") as t:
            t.write(PEPath.replace("PhiEdit.exe",""))
            t.close()
        if "PhiEdit.exe" in PEPath:
            load()
            return messagebox.showinfo("Success","成功绑定 Re:PhiEdit")
        else:
            return messagebox.showinfo("Error","无效目录")
        
def load_this_page(PEdata,T):
    try:
        #with open("PEdata","r",encoding="utf_8") as p:
        #    PEdata=p.read()
        #    p.close()
        with open(PEdata.rstrip('\n')+"Chartlist.txt","r",encoding="utf_8") as t:
            chartdata=t.readlines()
            t.close()
        #global table
        elem=T.get_children()
        for item in elem:
            T.delete(item)
        for i in range(0,len(chartdata)):
            if chartdata[i]=="#\n":
                
                T.insert("",0,values=(chartdata[i+1][6:-1],
                                          chartdata[i+3][6:-1],
                                          chartdata[i+4][9:-1],
                                          chartdata[i+5][7:-1],
                                          chartdata[i+6][7:-1],
                                          chartdata[i+7][10:-1],
                                          chartdata[i+8][9:-1],
                                          chartdata[i+2][6:-1],))
    except:
        #with open("ErrorsLog.txt","a",encoding="utf_8") as t:
        #    traceback.print_exc(file=t)
        #    t.close()
        #messagebox.showinfo("绑定PE","首次运行时请绑定您的PhiEditer")
        #PEPath=filedialog.askopenfilename(initialfile="PhiEditer.exe",filetypes=[('PhiEditer','.exe')])
        #with open("PEdata","w",encoding="utf_8") as t:
        #    t.write(PEPath.replace("PhiEditer.exe",""))
        #    t.close()
        #if "PhiEditer.exe" in PEPath:
        #    load()
        #    return messagebox.showinfo("Success","成功绑定 PhiEditer")
        #else:
        #    return messagebox.showinfo("Error","无效目录")
        pass
        
def importchart(Path,T):
    PEdata=Path.rstrip('\n')
    picture=["png","jpg","jpeg"]
    music=["mp3","wav","ogg","flac"]
    filePath=filedialog.askopenfilename(filetypes=[('RPE谱面','.pez')])
    fz=zipfile.ZipFile(filePath,"r")
    level="无信息"
    composer="无信息"
    charter="无信息"
    name=filePath.split("/")[-1].replace(".pez","")
    pezpath="无信息"
    
    for file in fz.namelist():
        if ".txt" in file:
            fz.extract(file,"infodir/")
            try:
                with open("infodir/"+file,"r",encoding="utf_8") as t:
                    data=t.readlines()
                    for i in range(len(data)):
                        if "Level: " in data[i]:
                            level=data[i][7:-1]
                        elif "Charter: " in data[i]:
                            charter=data[i][9:-1]
                        elif "Composer: " in data[i]:
                            composer=data[i][10:-1]
                        elif "Name: " in data[i]:
                            name=data[i][6:-1]
                        elif "Path: " in data[i]:
                            pezpath=data[i][6:-1]
                    t.close()
                os.remove("infodir/"+file)
            except:
                with open("infodir/info.txt","r",encoding="utf_8") as t:
                    data=t.readlines()
                    for i in range(len(data)):
                        if "Level: " in data[i]:
                            level=data[i][7:-1]
                        elif "Charter: " in data[i]:
                            charter=data[i][9:-1]
                        elif "Composer: " in data[i]:
                            composer=data[i][10:-1]
                        elif "Name: " in data[i]:
                            name=data[i][6:-1]
                    t.close()
                os.remove("infodir/"+file)
            os.rmdir("infodir")
            break
        elif file=="info.csv":
            fz.extract(file,"infodir/")
            with open("infodir/info.csv","r",encoding="utf_8") as t:
                data=t.readlines()
                for i in range(len(data)):
                    if "Name" in data[i]:
                        title=data[i].replace("\n","").split(",")
                value=data[-1].replace("\n","").split(",")
                try:
                    level=value[title.index("Level")]
                except:
                    pass
                try:
                    charter=value[title.index("Charter")]
                except:
                    pass
                try:
                    composer=value[title.index("Artist")]
                except:
                    pass
                try:
                    name=value[title.index("Name")]
                except:
                    pass
                t.close()
            os.remove("infodir/"+file)
            os.rmdir("infodir")        
    for file in fz.namelist():
        if file.split(".")[-1]=="json":
            fz.extract(file,PEdata+"Resources/"+pezpath)
            chart=file
        elif file.split(".")[-1] in music:
            fz.extract(file,PEdata+"Resources/"+pezpath)
            music=file
        elif file.split(".")[-1] in picture:
            fz.extract(file,PEdata+"Resources/"+pezpath)
            picture=file
            
    fz.close()
    with open(PEdata+"Chartlist.txt","a",encoding="utf_8") as t:
        
        info=("\n#\nName: "+name+
              "\nPath: "+pezpath+
              "\nSong: "+music+
              "\nPicture: "+picture+
              "\nChart: "+chart+
              "\nLevel: "+level+
              "\nComposer: "+composer+
              "\nCharter: "+charter+
              "\n")
        t.write(info)
        t.close()
    messagebox.showinfo("Success","成功导入谱面")
    load_this_page(PEdata,T)

def exportchart(item,Path,T):
    
    def add_bom(file, bom: bytes):
        with open(file, 'r+b') as f:
            org_contents = f.read()
            f.seek(0)
            f.write(bom + org_contents)
    
    
    PEdata=Path.rstrip('\n')
    def infocsv(infolist):
        setinfo.destroy()
        item=infolist[8]
        savePath=filedialog.asksaveasfilename(initialfile=item[0]+'.pez',filetypes=[("RPE谱面", ".pez")])
# =============================================================================
#         with open("infodata","w",encoding="utf_8") as t:
#             t.write("Chart,Music,Image,Name,Artist,Level,Illustrator,Charter\n谱面,音乐,图片,名称,曲师,等级,曲绘,谱师\n")
#             t.write(infolist[0]+","+infolist[1]+","+infolist[2]+","+infolist[3]+","+infolist[4]+","+infolist[5]+","+infolist[6]+","+infolist[7])
#             t.close()
#         
#         add_bom("infodata", codecs.BOM_UTF8)
# =============================================================================
        
        with open("settingsdata","w",encoding="utf_8") as t:
            t.write("\n#\nName: "+infolist[3]+
                  "\nPath: "+infolist[6]+
                  "\nSong: "+infolist[1]+
                  "\nPicture: "+infolist[2]+
                  "\nChart: "+infolist[0]+
                  "\nLevel: "+infolist[5]+
                  "\nComposer: "+infolist[4]+
                  "\nCharter: "+infolist[7]+
                  "\n")
            t.close()
        z=zipfile.ZipFile(savePath,"w",zipfile.ZIP_DEFLATED)
        z.write(PEdata+"Resources/"+item[7]+"/"+item[3],item[3])
        z.write(PEdata+"Resources/"+item[7]+"/"+item[1],item[1])
        z.write(PEdata+"Resources/"+item[7]+"/"+item[2],item[2])
        #z.write("infodata","info.csv")
        z.write("settingsdata","info.txt")
        z.close()
        os.remove("settingsdata")
        messagebox.showinfo("Success","成功导出谱面")
        
    holdon=False
    #global table
    if item=="":
        messagebox.showinfo("Error","未选择谱面")
    else:
# =============================================================================
#         info=messagebox.askyesno("Export","是否使用默认信息")
# =============================================================================
        if True:
            setinfo=tkinter.Toplevel()
            setinfo.title("填写谱面信息")
            setinfo.geometry("300x300")
            subtitle=tkinter.Label(setinfo, text="填写谱面信息",font=('', 10),width=30,height=1)
            subtitle.place(relx=0.5,rely=0.1,anchor=tkinter.CENTER)
            
            name=tkinter.Label(setinfo, text='名称:',font=('',10),width=30,height=1)
            name.place(relx=0.15,rely=0.19,anchor=tkinter.CENTER)
            enname=tkinter.Entry(setinfo,show=None,width=25)
            enname.insert(0,item[0])
            enname.place(relx=0.52,rely=0.19,anchor=tkinter.CENTER)

            music=tkinter.Label(setinfo, text='音频:',font=('',10),width=30,height=1)
            music.place(relx=0.15,rely=0.28,anchor=tkinter.CENTER)
            enmusic=tkinter.Entry(setinfo,show=None,width=25)
            enmusic.insert(0,item[1])
            enmusic.place(relx=0.52,rely=0.28,anchor=tkinter.CENTER)

            photo=tkinter.Label(setinfo, text='背景:',font=('',10),width=30,height=1)
            photo.place(relx=0.15,rely=0.37,anchor=tkinter.CENTER)
            enphoto=tkinter.Entry(setinfo,show=None,width=25)
            enphoto.insert(0,item[2])
            enphoto.place(relx=0.52,rely=0.37,anchor=tkinter.CENTER)

            chart=tkinter.Label(setinfo, text='谱面:',font=('',10),width=30,height=1)
            chart.place(relx=0.15,rely=0.46,anchor=tkinter.CENTER)
            enchart=tkinter.Entry(setinfo,show=None,width=25)
            enchart.insert(0,item[3])
            enchart.place(relx=0.52,rely=0.46,anchor=tkinter.CENTER)

            level=tkinter.Label(setinfo, text='难度:',font=('',10),width=30,height=1)
            level.place(relx=0.15,rely=0.55,anchor=tkinter.CENTER)
            enlevel=tkinter.Entry(setinfo,show=None,width=25)
            enlevel.insert(0,item[4])
            enlevel.place(relx=0.52,rely=0.55,anchor=tkinter.CENTER)

            composer=tkinter.Label(setinfo, text='曲师:',font=('',10),width=30,height=1)
            composer.place(relx=0.15,rely=0.64,anchor=tkinter.CENTER)
            encomposer=tkinter.Entry(setinfo,show=None,width=25)
            encomposer.insert(0,item[5])
            encomposer.place(relx=0.52,rely=0.64,anchor=tkinter.CENTER)

            charter=tkinter.Label(setinfo, text='谱师:',font=('',10),width=30,height=1)
            charter.place(relx=0.15,rely=0.73,anchor=tkinter.CENTER)
            encharter=tkinter.Entry(setinfo,show=None,width=25)
            encharter.insert(0,item[6])
            encharter.place(relx=0.52,rely=0.73,anchor=tkinter.CENTER)

            illustrator=tkinter.Label(setinfo, text='路径:',font=('',10),width=30,height=1)
            illustrator.place(relx=0.15,rely=0.82,anchor=tkinter.CENTER)
            enillustrator=tkinter.Entry(setinfo,show=None,width=25)
            enillustrator.insert(0,item[7])
            enillustrator.place(relx=0.52,rely=0.82,anchor=tkinter.CENTER)

            done=tkinter.Button(setinfo,text='下一步',font=('',10),width=10,height=1,command=lambda:infocsv([enchart.get(),enmusic.get(),enphoto.get(),enname.get(),encomposer.get(),enlevel.get(),enillustrator.get(),encharter.get(),item]))
            done.place(relx=0.5,rely=0.92,anchor=tkinter.CENTER)
            setinfo.mainloop()
        else:
            holdon=True
        if holdon:
            savePath=filedialog.asksaveasfilename(initialfile=item[0]+'.pez',filetypes=[("RPE谱面", ".pez")])    
            z=zipfile.ZipFile(savePath,"w",zipfile.ZIP_DEFLATED)
            z.write(PEdata+"Resources/"+item[7]+"/"+item[3],item[3])
            z.write(PEdata+"Resources/"+item[7]+"/"+item[1],item[1])
            z.write(PEdata+"Resources/"+item[7]+"/"+item[2],item[2])
            z.close()
            messagebox.showinfo("Success","成功导出谱面")

def deletechart(item,Path,T):
    
    deletelist=list(item)
    
    #global table
    PEdata=Path.rstrip('\n')
    result=False
    if len(item)==0:
        messagebox.showinfo("Error","未选择谱面")
    elif len(item)==1:
        result=messagebox.askyesno("Delete","是否删除谱面 "+T.item((item[0],),"values")[0])
    else:
        result=messagebox.askyesno("Delete","是否删除 "+T.item((item[0],),"values")[0]+" 等 "+str(len(item))+" 个谱面")
    if result:
        for for_delete in deletelist:
            item=T.item((for_delete,),"values")
            info="\n#\nName: "+item[0]+"\nPath: "+item[7]+"\nSong: "+item[1]+"\nPicture: "+item[2]+"\nChart: "+item[3]+"\nLevel: "+item[4]+"\nComposer: "+item[5]+"\nCharter: "+item[6]
            with open(PEdata+"Chartlist.txt","r",encoding="utf_8") as t:
                basicset=t.read()
                t.close()
            with open(PEdata+"Chartlist.txt","w",encoding="utf_8") as t:
                t.write(basicset.replace(info,""))
                t.close()
            shutil.rmtree(PEdata+"Resources/"+item[7])
                
        messagebox.showinfo("Success","已删除谱面 ")
    load_this_page(PEdata,T)

def editinfo(item,Path,T):
    
    def newinfo(infolist,T):
        setinfo.destroy()
        PEdata=infolist[9]
        info=("#\nName: "+infolist[3]+
              "\nPath: "+infolist[6]+
              "\nSong: "+infolist[1]+
              "\nPicture: "+infolist[2]+
              "\nChart: "+infolist[0]+
              "\nLevel: "+infolist[5]+
              "\nComposer: "+infolist[4]+
              "\nCharter: "+infolist[7])
        
        with open(PEdata+"Chartlist.txt","r",encoding="utf_8") as t:
            settings=t.read()
            t.close()
        with open(PEdata+"Chartlist.txt","w",encoding="utf_8") as t:
            t.write(settings.replace(infolist[8],info))
            t.close()
        load_this_page(PEdata,T)
    
    PEdata=Path.rstrip('\n')
    
    if item=="":
        messagebox.showinfo("Error","未选择谱面")
    else:
        oldinfo=("#\nName: "+item[0]+
                 "\nPath: "+item[7]+
                "\nSong: "+item[1]+
                "\nPicture: "+item[2]+
                "\nChart: "+item[3]+
                "\nLevel: "+item[4]+
                "\nComposer: "+item[5]+
                "\nCharter: "+item[6])
        
        setinfo=tkinter.Toplevel()
        setinfo.title("编辑谱面信息")
        setinfo.geometry("300x300")
        setinfo.iconphoto(False,R)
        subtitle=tkinter.Label(setinfo, text="编辑谱面信息",font=('', 10),width=30,height=1)
        subtitle.place(relx=0.5,rely=0.1,anchor=tkinter.CENTER)
        
        name=tkinter.Label(setinfo, text='名称:',font=('',10),width=30,height=1)
        name.place(relx=0.15,rely=0.19,anchor=tkinter.CENTER)
        enname=tkinter.Entry(setinfo,show=None,width=25)
        enname.insert(0,item[0])
        enname.place(relx=0.52,rely=0.19,anchor=tkinter.CENTER)
    
        music=tkinter.Label(setinfo, text='音频:',font=('',10),width=30,height=1)
        music.place(relx=0.15,rely=0.28,anchor=tkinter.CENTER)
        enmusic=tkinter.Entry(setinfo,show=None,width=25)
        enmusic.insert(0,item[1])
        enmusic.place(relx=0.52,rely=0.28,anchor=tkinter.CENTER)
    
        photo=tkinter.Label(setinfo, text='背景:',font=('',10),width=30,height=1)
        photo.place(relx=0.15,rely=0.37,anchor=tkinter.CENTER)
        enphoto=tkinter.Entry(setinfo,show=None,width=25)
        enphoto.insert(0,item[2])
        enphoto.place(relx=0.52,rely=0.37,anchor=tkinter.CENTER)
    
        chart=tkinter.Label(setinfo, text='谱面:',font=('',10),width=30,height=1)
        chart.place(relx=0.15,rely=0.46,anchor=tkinter.CENTER)
        enchart=tkinter.Entry(setinfo,show=None,width=25)
        enchart.insert(0,item[3])
        enchart.place(relx=0.52,rely=0.46,anchor=tkinter.CENTER)
    
        level=tkinter.Label(setinfo, text='难度:',font=('',10),width=30,height=1)
        level.place(relx=0.15,rely=0.55,anchor=tkinter.CENTER)
        enlevel=tkinter.Entry(setinfo,show=None,width=25)
        enlevel.insert(0,item[4])
        enlevel.place(relx=0.52,rely=0.55,anchor=tkinter.CENTER)
    
        composer=tkinter.Label(setinfo, text='曲师:',font=('',10),width=30,height=1)
        composer.place(relx=0.15,rely=0.64,anchor=tkinter.CENTER)
        encomposer=tkinter.Entry(setinfo,show=None,width=25)
        encomposer.insert(0,item[5])
        encomposer.place(relx=0.52,rely=0.64,anchor=tkinter.CENTER)
    
        charter=tkinter.Label(setinfo, text='谱师:',font=('',10),width=30,height=1)
        charter.place(relx=0.15,rely=0.73,anchor=tkinter.CENTER)
        encharter=tkinter.Entry(setinfo,show=None,width=25)
        encharter.insert(0,item[6])
        encharter.place(relx=0.52,rely=0.73,anchor=tkinter.CENTER)
    
        illustrator=tkinter.Label(setinfo, text='路径:',font=('',10),width=30,height=1)
        illustrator.place(relx=0.15,rely=0.82,anchor=tkinter.CENTER)
        enillustrator=tkinter.Entry(setinfo,show=None,width=25)
        enillustrator.insert(0,item[7])
        enillustrator.place(relx=0.52,rely=0.82,anchor=tkinter.CENTER)
    
        done=tkinter.Button(setinfo,text='确认修改',font=('',10),width=10,height=1,command=lambda:newinfo([enchart.get(),enmusic.get(),enphoto.get(),enname.get(),encomposer.get(),enlevel.get(),enillustrator.get(),encharter.get(),oldinfo,PEdata],T))
        done.place(relx=0.5,rely=0.92,anchor=tkinter.CENTER)
        setinfo.mainloop()

def check(Path,T):
    
    def checked():
        show_lack.destroy()
    
    PEdata=Path.rstrip('\n')
    
    with open(PEdata+"Settings.txt","r",encoding="utf_8") as t:
        chartdata=t.readlines()
        t.close()
    
    charts=[]
    files=[]
    
    for i in range(0,len(chartdata)):
        if chartdata[i]=="#\n":
            charts.append([chartdata[i+1][6:-1],chartdata[i+4][7:-1]])
            files.append([chartdata[i+1][6:-1],chartdata[i+2][6:-1]])
            files.append([chartdata[i+1][6:-1],chartdata[i+3][9:-1]])
    
    chart_folder=os.listdir(PEdata)
    files_folder=os.listdir(PEdata+"Resources/")
    
    not_exist=[]
    
    for item in charts:
        if item[1] not in chart_folder:
            not_exist.append(item)
    
    for item in files:
        if item[1] not in files_folder:
            print(item)
            print(files_folder)
            not_exist.append(item)
    show_lack=tkinter.Toplevel()
    show_lack.title("资源检查完毕")
    show_lack.geometry("400x300")
    show_lack.iconphoto(False,R)
    
    if len(not_exist)==0:
        Ytitle=tkinter.Label(show_lack, text="没有缺失文件",font=('', 10),width=30,height=1)
    else:
        Ytitle=tkinter.Label(show_lack, text="缺失文件可能导致 PhiEditer 无法启动/闪退",font=('', 10),width=400,height=1)
    Ytitle.place(relx=0.5,rely=0.06,anchor=tkinter.CENTER)
    
    lack=ttk.Treeview(show_lack,columns=("关卡","文件"),show="headings")
    lack.column("关卡",width=185)
    lack.heading("关卡",text="所属关卡")
    lack.column("文件",width=185)
    lack.heading("文件",text="缺失文件")
    for i in range(len(not_exist)):
        lack.insert("",0,values=(not_exist[i][0],not_exist[i][1],))
    lack.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
    
    done=tkinter.Button(show_lack,text='已了解',font=('',10),width=10,height=1,command=checked)
    done.place(relx=0.5,rely=0.94,anchor=tkinter.CENTER)
    
    show_lack.update()
  
def add_page():
    
    def cancel():
        EnterName.destroy()
    
    def comfirm(Path):
        PageName=enname.get()
        if PageName=="":
            messagebox.showinfo("Error","不可以为空")
        else:
            with open("PEdata","a",encoding="utf_8") as t:
                t.write("\n"+PageName+"->"+Path)
                t.close()
            
            frame = Frame(notebook)
            Name=PageName
            table=ttk.Treeview(frame,columns=("名称","音频","背景","谱面","难度","曲师","谱师","路径"),show="headings")
            b1=tkinter.Button(frame,text='导入谱面',font=('',10),width=9,height=1,command=lambda P=Path,T=table:importchart(P,T))
            b1.place(relx=0.076,rely=0.055,anchor=tkinter.CENTER)
            b2=tkinter.Button(frame,text='导出谱面',font=('',10),width=9,height=1,command=lambda P=Path,T=table:exportchart(T.item(T.selection(),"values"),P,T))
            b2.place(relx=0.2,rely=0.055,anchor=tkinter.CENTER)
            b3=tkinter.Button(frame,text='删除谱面',font=('',10),width=9,height=1,command=lambda P=Path,T=table:deletechart(T.selection(),P,T))
            b3.place(relx=0.324,rely=0.055,anchor=tkinter.CENTER)
            b4=tkinter.Button(frame,text='编辑信息',font=('',10),width=9,height=1,command=lambda P=Path,T=table:editinfo(T.item(T.selection(),"values"),P,T))
            b4.place(relx=0.076,rely=0.144,anchor=tkinter.CENTER)
            b5=tkinter.Button(frame,text='检查资源',font=('',10),width=9,height=1,command=lambda P=Path,T=table:check(P,T))
            b5.place(relx=0.2,rely=0.144,anchor=tkinter.CENTER)
            b6=tkinter.Button(frame,text='刷新本页',font=('',10),width=9,height=1,command=lambda P=Path,T=table:load_this_page(P,T))
            #b6=tkinter.Button(root,text='检查资源',font=('',10),width=9,height=1,command=lambda:print(table.selection()))
            b6.place(relx=0.324,rely=0.144,anchor=tkinter.CENTER)
            b7=tkinter.Button(frame,text='新增页面',font=('',10),width=8,height=1,command=add_page)
            b7.place(relx=0.898,rely=0.055,anchor=tkinter.CENTER)
            b8=tkinter.Button(frame,text='删除本页',font=('',10),width=8,height=1,command=lambda P=Path:delete_page(P))
            b8.place(relx=0.898,rely=0.144,anchor=tkinter.CENTER)
    
            intro=tkinter.Label(frame, text="PhiEditerManager",font=('', 11),width=30,height=3)
            intro.place(relx=0.62,rely=0.1,anchor=tkinter.CENTER)
    
            
            table.column("名称",width=70)
            table.column("音频",width=70)
            table.column("背景",width=70)
            table.column("谱面",width=70)
            table.column("难度",width=70)
            table.column("曲师",width=70)
            table.column("谱师",width=70)
            table.column("路径",width=70)
            table.heading("名称",text="名称")
            table.heading("音频",text="音频")
            table.heading("背景",text="背景")
            table.heading("谱面",text="谱面")
            table.heading("难度",text="难度")
            table.heading("曲师",text="曲师")
            table.heading("谱师",text="谱师")
            table.heading("路径",text="路径")
            table.place(relx=0.485,rely=0.60,anchor=tkinter.CENTER)
            ybar=ttk.Scrollbar(frame,orient="vertical")
            #table["yscroll"]=ybar.set
            #ybar.place(relx=0.96,rely=0.3,anchor=tkinter.CENTER)
            ybar.pack(side="right",fill="y")
            ybar.config(command=table.yview)
            table.configure(yscrollcommand=ybar.set)
            notebook.add(frame, text=Name)
            load_this_page(Path,table)
            try:
                b0.destroy()
            except:
                pass
            EnterName.destroy()        
    messagebox.showinfo("绑定PE","选择您想要绑定的 Re:PhiEdit")
    Path=filedialog.askopenfilename(initialfile="Re:PhiEdit.exe",filetypes=[('Re:PhiEdit','.exe')])
    if Path=="":
        return messagebox.showinfo("Error","无效目录")
    EnterName=tkinter.Toplevel()
    EnterName.title("新增页面")
    EnterName.geometry("200x100")
    EnterName.iconphoto(False,R)
    
    name=tkinter.Label(EnterName, text='页面展示名:',font=('',10),width=30,height=1)
    name.place(relx=0.5,rely=0.23,anchor=tkinter.CENTER)
    
    enname=tkinter.Entry(EnterName,show=None,width=20)
    enname.insert(0,"Re:PhiEdit")
    enname.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
    Path=Path.replace("PhiEdit.exe","")
    done=tkinter.Button(EnterName,text='确定',font=('',10),width=8,height=1,command=lambda:comfirm(Path))
    done.place(relx=0.7,rely=0.8,anchor=tkinter.CENTER)
    cancel=tkinter.Button(EnterName,text='取消',font=('',10),width=8,height=1,command=cancel)
    cancel.place(relx=0.3,rely=0.8,anchor=tkinter.CENTER)
    EnterName.update()
    
def delete_page(Path,Name):
    
    Text=Name+"->"+Path
    
    result=messagebox.askyesno("Delete","是否删除本页,此操作不会删除源文件")
    
    if result:
        with open("PEdata","r",encoding="utf_8") as t:
            basicset=t.read()
            t.close()
        with open("PEdata","w",encoding="utf_8") as t:
            t.write(basicset.replace(Text,""))
            t.close()
        for tab_id in notebook.tabs():
            if notebook.tab(tab_id, 'text') == Name:
                notebook.forget(tab_id)
    
def on_closing():
    root.quit()
    root.destroy()
    
if __name__ == "__main__":    
    root=tkinter.Tk()
    root.title("RPE Manager")
    root.geometry("600x310")
    
    image_data = """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"""

    R = tkinter.PhotoImage(data=image_data)

# Attach the image to the root object to prevent it from being garbage collected.
    root.image = R
    
    root.iconphoto(False,R)
    
    notebook = Notebook(root)
    filename = 'PEdata'

    if os.path.exists(filename):
        with open('PEdata', 'r',encoding="utf_8") as f:
            lines = f.readlines()

        with open('PEdata', 'w',encoding="utf_8") as f:
            for line in lines:
                if line.strip():
                    f.write(line)
    else:
        with open(filename, 'w',encoding="utf_8") as f:
            f.close()
    with open('PEdata', 'r',encoding="utf_8") as file:
        lines = file.readlines()
        if len(lines)==0:
            b0=tkinter.Button(root,text='新增页面',font=('',10),width=10,height=2,command=add_page)
            b0.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
        for i, line in enumerate(lines):
            frame = Frame(notebook)
            Name=line.split("->")[0]
            Path=line.split("->")[1]
            table=ttk.Treeview(frame,columns=("名称","音频","背景","谱面","难度","曲师","谱师","路径"),show="headings")
            b1=tkinter.Button(frame,text='导入谱面',font=('',10),width=9,height=1,command=lambda P=Path,T=table:importchart(P,T))
            b1.place(relx=0.076,rely=0.055,anchor=tkinter.CENTER)
            b2=tkinter.Button(frame,text='导出谱面',font=('',10),width=9,height=1,command=lambda P=Path,T=table:exportchart(T.item(T.selection(),"values"),P,T))
            b2.place(relx=0.2,rely=0.055,anchor=tkinter.CENTER)
            b3=tkinter.Button(frame,text='删除谱面',font=('',10),width=9,height=1,command=lambda P=Path,T=table:deletechart(T.selection(),P,T))
            b3.place(relx=0.324,rely=0.055,anchor=tkinter.CENTER)
            b4=tkinter.Button(frame,text='编辑信息',font=('',10),width=9,height=1,command=lambda P=Path,T=table:editinfo(T.item(T.selection(),"values"),P,T))
            b4.place(relx=0.076,rely=0.144,anchor=tkinter.CENTER)
            b5=tkinter.Button(frame,text='检查资源',font=('',10),width=9,height=1,command=lambda P=Path,T=table:check(P,T))
            b5.place(relx=0.2,rely=0.144,anchor=tkinter.CENTER)
            b6=tkinter.Button(frame,text='刷新本页',font=('',10),width=9,height=1,command=lambda P=Path,T=table:load_this_page(P,T))
            #b6=tkinter.Button(root,text='检查资源',font=('',10),width=9,height=1,command=lambda:print(table.selection()))
            b6.place(relx=0.324,rely=0.144,anchor=tkinter.CENTER)
            b7=tkinter.Button(frame,text='新增页面',font=('',10),width=8,height=1,command=add_page)
            b7.place(relx=0.898,rely=0.055,anchor=tkinter.CENTER)
            b8=tkinter.Button(frame,text='删除本页',font=('',10),width=8,height=1,command=lambda P=Path,N=Name:delete_page(P,N))
            b8.place(relx=0.898,rely=0.144,anchor=tkinter.CENTER)
    
            intro=tkinter.Label(frame, text="Re:PhiEdit Manager",font=('', 11),width=30,height=3)
            intro.place(relx=0.62,rely=0.1,anchor=tkinter.CENTER)
            
            table.column("名称",width=70)
            table.column("音频",width=70)
            table.column("背景",width=70)
            table.column("谱面",width=70)
            table.column("难度",width=70)
            table.column("曲师",width=70)
            table.column("谱师",width=70)
            table.column("路径",width=70)
            table.heading("名称",text="名称")
            table.heading("音频",text="音频")
            table.heading("背景",text="背景")
            table.heading("谱面",text="谱面")
            table.heading("难度",text="难度")
            table.heading("曲师",text="曲师")
            table.heading("谱师",text="谱师")
            table.heading("路径",text="路径")
            table.place(relx=0.485,rely=0.60,anchor=tkinter.CENTER)
            ybar=ttk.Scrollbar(frame,orient="vertical")
            #table["yscroll"]=ybar.set
            #ybar.place(relx=0.96,rely=0.3,anchor=tkinter.CENTER)
            ybar.pack(side="right",fill="y")
            ybar.config(command=table.yview)
            table.configure(yscrollcommand=ybar.set)
            notebook.add(frame, text=Name)
            load_this_page(Path,table)
    notebook.pack(fill='both', expand=True)
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()