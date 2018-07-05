# -*- coding: UTF-8 -*-
import os
import database as db
import selection as sl
from tkinter import *
import tkinter.messagebox as messagebox
#当前文件的路径
pwd = os.getcwd()
#全局变量
minnum = 0
notlist = []
notsamelist = []
mustlist = []
mustsamelist = []

class applicaton(Frame):
    def __init__(self,selectlist,database,master=None):
        self.database=database#必须写在前面
        self.selectlist=selectlist
        Frame.__init__(self,master)
        self.grid()
        self.create()


    def create(self):
        daylist=[None,'周一','周二','周三','周四','周五','周六','周日']
        for x in range(0,8):
            for y in range(0,13):
                if y==0:
                    currentlable = Label(self, text=daylist[x])
                    currentlable.grid(row=2 * y, column=4 * x, rowspan=2, columnspan=4)
                elif x==0:
                    currentlable = Label(self, text='第%s节'%y)
                    currentlable.grid(row=2 * y, column=4 * x, rowspan=2, columnspan=4)
                else:
                    Found=False
                    for item in self.selectlist:
                        currenttimes=self.database[item]
                        for time in currenttimes:#速度比较慢，可以优化
                            x1=daylist.index(time[0])
                            y1=time[1]
                            if x1==x and y1==y:
                                currentlable = Label(self, text=item)
                                currentlable.grid(row=2 * y, column=4 * x, rowspan=2, columnspan=4)
                                Found=True
                                break
                            if Found==True:
                                break
                        if Found==True:
                            break

                    if Found==False:
                        currentlable=Label(self,text='|----|')
                        currentlable.grid(row=2*y,column=4*x,rowspan=2,columnspan=4)
        pass

class application2(Frame):
    def __init__(self,database,master=None):
        self.database=database
        self.savelist=[]
        Frame.__init__(self,master)
        self.grid()
        self.createframe()
    def createframe(self):

        self.name=None
        savelist=[]
        self.high=Label(self,text='')
        self.data=Label(self,text='')
        title=Label(self,text="键入你的添加、删除课程，完毕后直接叉掉")

        #显示当前数据库部分，初始化
        label=Label(self,text='当前数据库：')
        label.grid(row=8)
        self.update()

        but=Button(self,text='清空数据库',command=lambda :self.clear())#别忘了lambda
        but.grid(row=10)
        #不知道什么命令是关闭当前窗口
        # but2=Button(self,text='课程规划',command=self.quit())
        # but2.grid(row=10,column=8)
        #按钮控制
        button0=Button(self,text='1、键入这个课程',command=lambda :self.getname(input))
        button0.grid(row=2,column=10)
        title.grid(row=0,column=0,sticky='s')

        classname=Label(self,text='课程名：（输入后请点击右侧键入）')
        classname.grid(row=2,column=0)
        input= Entry(self)
        input.grid(row=2,column=5)

        ########
        timetable=Label(self,text='周几？（如周一、周日）：')
        timetable.grid(row=4,column=0)
        input2= Entry(self)
        input2.grid(row=4,column=5)

        timetable2=Label(self,text='第几节？输数字：')
        timetable2.grid(row=6,column=0)
        input3= Entry(self)
        input3.grid(row=6,column=5)



        button1=Button(self,text='2、键入这个时间段，可以多次键入不同时间，以生成多个时间段',command=lambda :self.cheackappend(savelist,input2.get(),input3.get()))#第几节是int型
        print ('键入时间',self.database.get_courses())
        button1.grid(row=6,column=10)


        print (savelist)
        button=Button(self,text='3、生成该课程',command=lambda:self.result(self.name,savelist))
        #生成之后清空存储器
        button.grid(row=7,column=0)


        button2=Button(self,text='删除该课程（只需键入课程名，注意在删除前必须键入课程名！）',command=lambda:self.result2(input.get()))
        button2.grid(row=7,column=8)
        #######高级功能模块
        lab2=Label(self,text='==================筛选条件：').grid(row=12)
        #课程数多于某值
        numin=Entry(self)#一定要打self！！！！！
        numin.grid(row=13,column=5)
        but3=Button(self,text='课程不少于：(输入数字后点击以输入)',command=lambda:self.num(numin.get()))
        but3.grid(row=13,column=0)
        #不包含
        nothave=Entry(self)
        nothave.grid(row=14,column=5)
        but4=Button(self,text='加入不包含的：',command=lambda:self.nothave(nothave.get(),'plus'))
        but4.grid(row=14)
        but5=Button(self,text='删去',command=lambda:self.nothave(nothave.get(),'minus'))
        but5.grid(row=14,column=7)
        #不同时包含
        nothavesame=Entry(self)
        nothavesame.grid(row=15,column=5)
        but6=Button(self,text='不同时包含：(以“高数 数理”的形式)',command=lambda:self.nothavesame(nothavesame.get(),'plus'))
        but6.grid(row=15)
        but7=Button(self,text='删去',command=lambda:self.nothavesame(nothavesame.get(),'minus'))
        but7.grid(row=15,column=7)
        #必须包含
        musthave=Entry(self)
        musthave.grid(row=16,column=5)
        but8=Button(self,text='加入必须包含的：',command=lambda:self.musthave(musthave.get(),'plus'))
        but8.grid(row=16)
        but9=Button(self,text='删去',command=lambda:self.musthave(musthave.get(),'minus'))
        but9.grid(row=16,column=7)
        #必须同时包含
        musthavesame=Entry(self)
        musthavesame.grid(row=17,column=5)
        but10=Button(self,text='必须同时包含：(以“高数 数理”的形式)',command=lambda:self.musthavesame(musthavesame.get(),'plus'))
        but10.grid(row=17)
        but11=Button(self,text='删去',command=lambda:self.musthavesame(musthavesame.get(),'minus'))
        but11.grid(row=17,column=7)
    def musthavesame(self,name,mode):
        global mustsamelist
        waitlist = name.split()
        if mode=='plus':
            Found=False
            for item in mustsamelist:
                if item==waitlist:
                    Found=True
                    break
            if Found==False:
                mustsamelist.append(waitlist)
            self.update()
        elif mode=='minus':
            print (waitlist,mustsamelist)
            for item in mustsamelist:
                if item==waitlist:
                    print ('找到了')
                    mustsamelist.pop(mustsamelist.index(item))
            self.update()
    def musthave(self,name,mode):
        global mustlist
        if mode=='plus':
            Found=False
            for item in mustlist:
                if item==name:
                    Found=True
                    break
            if Found==False:
                mustlist.append(name)
            self.update()
        elif mode=='minus':
            for item in mustlist:
                if item==name:
                    mustlist.pop(mustlist.index(item))
            self.update()
    def nothavesame(self,name,mode):
        global notsamelist
        waitlist = name.split()
        if mode=='plus':
            Found=False
            for item in notsamelist:
                if item==waitlist:
                    Found=True
                    break
            if Found==False:
                notsamelist.append(waitlist)
            self.update()
        elif mode=='minus':
            print (waitlist,notsamelist)
            for item in notsamelist:
                if item==waitlist:
                    print ('找到了')
                    notsamelist.pop(notsamelist.index(item))
            self.update()
    def nothave(self,name,mode):
        global notlist
        if mode=='plus':
            Found=False
            for item in notlist:
                if item==name:
                    Found=True
                    break
            if Found==False:
                notlist.append(name)
            self.update()
        elif mode=='minus':
            for item in notlist:
                if item==name:
                    notlist.pop(notlist.index(item))
            self.update()


    def num(self,numin):
        global minnum
        num=int(numin)
        minnum=num
        self.update()

    def getname(self,input):
        self.name = input.get()
        print ('getname', self.database.get_courses())
        lab = Label(self,text='                                           ')
        lab.grid(row=4,column=10)
        return

    def clear(self):
        print ('调用清空')
        list=[]
        for item in self.database.get_courses():
            list.append(item)
        for item in list:
            self.database.rm_course(item)
        self.database.save()
        self.update()

    def cheackappend(self, savelist,data1,data2):
        lab = Label(self, text='请先键入课程名再输时间')
        if self.name!=None:
            savelist.append([data1, int(data2)])
            lab.destroy()
        else:
            lab.grid(row=4,column=10)

    def update(self):
        global minnum
        global notlist
        global notsamelist
        global mustlist
        global mustsamelist
        datalist=''
        for item in self.database.get_courses():
            datalist+=item
            datalist+=' '
        print ('shuju',datalist)
        self.data.destroy()
        self.data=Label(self,text='%s'%datalist)
        self.data.grid(row=9)

        self.high.destroy()
        self.high=Label(self,text='课程数不少于：%d\n不包含：%s\n不同时包含%s\n必须包含：%s\n必须同时包含：%s\n'%(minnum,notlist,notsamelist,mustlist,mustsamelist))
        self.high.grid(row=28)
        "还要再改！！，加入那几个模块高级功能"


    def result(self,name,savelist):
        print ('进入result',name,savelist)
        if name==None or savelist==[]:
            if name==None:
                savelist.clear()
            print ("加入了空课程，请重试")
            return 0
        print ("得到结果0",name,savelist,self.database.get_courses())
        "以索引取值！！！要改动必须复制！"
        self.database.add_course(name,savelist.copy())
        self.database.save()
        self.update()
        print (self.database.get_courses())
        savelist.clear()
        print ('清完之后的表',savelist)
        self.name=None
        print (self.database.get_courses())

    def result2(self,name):
        self.database.rm_course(name)
        self.database.save()
        self.update()


local_url = pwd + '\data'#当前目录下加入data文件


try:
    d = db.Database(local_url)
    print(d.get_courses())
except Exception:
    print ('出问题了')
    fobj = open(local_url, 'w')
    fobj.close()
    d = db.Database(local_url)
    print(d.get_courses())
#d.rm_all()
d.save()
app2=application2(d)
app2.mainloop()
# Do changes to database
'''
d.rm_all()
d.add_course('高数', [['周二', 3], ['周二', 4], ['周五', 1], ['周五', 2]])
print(d.get_courses())
d.save()
input('>')
'''
def nothave(sc):
    global notlist
    flag=True
    print ('找禁止的',sc,notlist)
    for item in sc:
        flag2=False
        for item2 in notlist:
            if item2==item:
                flag2=True
                break
        if flag2==True:
            flag=False
    return flag
def nothavesame(sc):
    global notsamelist
    print ('找不同时出现的')
    flag=True
    for item in notsamelist:
        flag2=False#是否满足这个要求
        for course in item:
            isin=False
            for items in sc:
                if items==course:
                    isin=True
                    break
            if isin==False:
                flag2=True
                break
        if flag2==False:
            flag=False
            break
    return flag
def musthave(sc):
    global mustlist
    flag=True
    print ('找必须的',sc,mustlist)
    for item in mustlist:
        flag2=False
        for item2 in sc:
            if item2==item:
                flag2=True
                break
        if flag2==False:
            flag=False
            break
    return flag
def musthavesame(sc):
    global mustsamelist
    print ('找必须同时出现的')
    flag=True
    for item in mustsamelist:
        flag2=True#是否满足这个要求
        for course in item:
            isin=False
            for items in sc:
                if items==course:
                    isin=True
                    break
            if isin==False:
                flag2=False
                break
        if flag2==False:
            flag=False
            break
    return flag
s = sl.Selection(d)
print([sc for sc in s.schemes()
       if len(sc)>=minnum and nothave(sc)==True and nothavesame(sc)==True and musthave(sc)==True and musthavesame(sc)==True ])
print (minnum)
for sc in s.schemes():
    if len(sc) >= minnum and nothave(sc) == True and nothavesame(sc) == True and musthave(sc) == True and musthavesame(sc) == True:
        app=applicaton(sc,d.get_courses())
        app.mainloop()

'''
print([sc for sc in s.schemes()
'''


