#Task manager app

from tkinter import *
import sqlite3


#from PIL import ImageTk,Image

root=Tk()
root.geometry("400x550")
root.title("Task Manager")
root.configure(bg="#222831")
root.iconbitmap("TODO.ico")

frame=LabelFrame(root,padx=5,pady=5,bg="#e8e8e8",bd=5)
Label(frame,text="Task Manager",padx=30,bg="#e8e8e8",fg="#0a043c",font = "Verdana 12 bold").grid(row=0,column=0,columnspan=3)


################################dark and light mode and version details
def light():
    global tt
    root.configure(bg="#f6f6f6")
    tt.config(bg="#f6f6f6",fg="#222831")
    v.config(bg="#f6f6f6",fg="#222831")
def dark():
    tt.configure(bg="#222831",fg="White")
    v.configure(bg="#222831",fg="White")
    root.configure(bg="#222831")
    Label(root,text="Choose theme ",fg="white",bg="#222831") 



#########functions
def clearall(sc):
    
    global mon,tue,wed,thu,fri,sat,sun
    if sc>=0:
        if sc==0:
            mon=[]
            
            for q in range(len(check_boxlist[sc])):
                check_boxlist[sc][q].destroy()
                
        
            q=0
        elif sc==1:
            tue=[]
            
            for q in range(len(check_boxlist[sc])):
                check_boxlist[sc][q].destroy()
        
            q=0
        elif sc==2:
            wed=[]
            
            for q in range(len(check_boxlist[sc])):
                check_boxlist[sc][q].destroy()
        
            q=0
        elif sc==3:
            thu=[]
            
            for q in range(len(check_boxlist[sc])):
                check_boxlist[sc][q].destroy()
        
            q=0
        elif sc==4:
            fri=[]
            
            for q in range(len(check_boxlist[sc])):
                check_boxlist[sc][q].destroy()
        
            q=0
        elif sc==5:
            sat=[]
            
            for q in range(len(check_boxlist[sc])):
                check_boxlist[sc][q].destroy()
        
            q=0
        elif sc==6:
            sun=[]
            
            for q in range(len(check_boxlist[sc])):
                check_boxlist[sc][q].destroy()
        
            q=0
        
            
    
    
def entertask(task,day):
    if task!="" and task!="Enter your task":
        if day==days[0]:
            mon.append(task)
            
        elif day==days[1]:
            tue.append(task)
        elif day==days[2]:
            wed.append(task)
        elif day==days[3]:
            thu.append(task)
        elif day==days[4]:
            fri.append(task)
        elif day==days[5]:
            sat.append(task)
        elif day==days[6]:
            sun.append(task)
        e.delete(0,END)
        
show_count=0
task_count=0
check_Box=-1
#check_boxday=str()
check_boxlist=[0]*7
task_listbox=[]

def showtask(day):
    i=0
    global show_count,task_count,check_Box,check_boxlist,task_listbox
    if show_count==0:
        pass
        #Button(root,text="Clear all checks",padx=5,pady=5,width=10,bg="#f9813a",fg="black",command=lambda:allchecks(check_Box)).pack(pady=15)#clear checked    
       
    if show_count>0:
        for k in range(len(check_boxlist[check_Box])):
            check_boxlist[check_Box][k].destroy()
        
    
    if day==days[0] and days[0]!=[]:
        show_count+=1
        n=task_count=len(mon)
        check_Box=0
        var1=[j for j in range(0,n)]
        #for j in range(n):
            #j=IntVar()
        for i in range(n):
            c=Checkbutton(frame,text=mon[::-1][i],variable=var1[i],bg="#e8e8e8",font = "Verdana 10 bold")
            task_listbox.append(c)
            c.grid(row=i+5,column=0,columnspan=3)
        
    elif day==days[1] and days[1]!=[]:
        show_count+=1
        n=task_count=len(tue)
        check_Box=1
        var1=[j for j in range(100,n+100)]
        #for j in range(n):
            #j=IntVar()
        for i in range(n):
            c=Checkbutton(frame,text=tue[::-1][i],variable=var1[i],bg="#e8e8e8",font = "Verdana 10 bold")
            task_listbox.append(c)
            c.grid(row=i+5,column=0,columnspan=3)
    elif day==days[2] and days[2]!=[]:
        show_count+=1
        n=task_count=len(wed)
        check_Box=2
        var1=[j for j in range(200,n+200)]
        #for j in range(n):
            #j=IntVar()
        for i in range(n):
            c=Checkbutton(frame,text=wed[::-1][i],variable=var1[i],bg="#e8e8e8",font = "Verdana 10 bold")
            task_listbox.append(c)
            c.grid(row=i+5,column=0,columnspan=3)
    elif day==days[3] and days[3]!=[]:
        show_count+=1
        n=task_count=len(thu)
        check_Box=3
        var1=[j for j in range(300,n+300)]
        #for j in range(n):
        #    j=IntVar()
        for i in range(n):
            c=Checkbutton(frame,text=thu[::-1][i],variable=var1[i],bg="#e8e8e8",font = "Verdana 10 bold")
            task_listbox.append(c)
            c.grid(row=i+5,column=0,columnspan=3)
    elif day==days[4] and days[4]!=[]:
        show_count+=1
        n=task_count=len(fri)
        check_Box=4
        var1=[j for j in range(400,400+n)]
        #for j in range(n):
        #    j=IntVar()
        for i in range(n):
            c=Checkbutton(frame,text=fri[::-1][i],variable=var1[i],bg="#e8e8e8",font = "Verdana 10 bold")
            task_listbox.append(c)
            c.grid(row=i+5,column=0,columnspan=3)
    elif day==days[5] and days[5]!=[]:
        show_count+=1
        n=task_count=len(sat)
        check_Box=5
        var1=[j for j in range(500,500+n)]
        #for j in range(n):
        #    j=IntVar()
        for i in range(n):
            c=Checkbutton(frame,text=sat[::-1][i],variable=var1[i],bg="#e8e8e8",font = "Verdana 10 bold") 
            task_listbox.append(c)
            c.grid(row=i+5,column=0,columnspan=3)
    elif day==days[6] and days[6]!=[]:
        show_count+=1
        n=task_count=len(sun)
        check_Box=6
        var1=[j for j in range(600,600+n)]
        #for j in range(n):
        #    j=IntVar()
        for i in range(n):
            c=Checkbutton(frame,text=sun[::-1][i],variable=var1[i],bg="#e8e8e8",font = "Verdana 10 bold")
            task_listbox.append(c)
            c.grid(row=i+5,column=0,columnspan=3)
    check_boxlist.insert(check_Box,task_listbox)
    
    
    

#############################################dropdown
e=Entry(frame,bg="#eeeeee",borderwidth=3,width=30)
e.insert(0,"Enter your task")
e.grid(row=2,column=0 ,columnspan=3)
days=["Monday","Tuesday","wednesday","Thursday","Friday","Saturday","Sunday"]
mon=[]
tue=[]
wed=[]
thu=[]
fri=[]
thu=[]
fri=[]
sat=[]
sun=[]

var=StringVar()
var.set(days[0])

Label(frame,text="Select a day:   ",bg="#e8e8e8").grid(row=1,column=0,padx=50,columnspan=2)
menu=OptionMenu(frame,var,*days)
menu.grid(row=1,column=1,columnspan=3,pady=20)
###################################################
##################################


button=Button(frame,text="Enter Task",width=10,padx=5,pady=5,fg="#03506f",bg="#dbf6e9",command=lambda:entertask(e.get(),var.get()),bd=3)
button1=Button(frame,text="Show Tasks",width=10,padx=5,pady=5,fg="black",bg="#ffb0b0",command=lambda:showtask(var.get()),bd=3)
 
frame.pack(padx=30,pady=30)
button.grid(row=3,column=0,padx=20)
button1.grid(row=3,column=2,padx=20,pady=20)
Button(root,text="Clear all",padx=5,pady=5,width=10,bg="#f05454",fg="black",command=lambda:clearall(check_Box)).pack(pady=30)#clear all
tt=Label(root,text="Choose theme ",fg="white",bg="#222831")
tt.pack(pady=15)
Button(root,text="Light",bg="#f1f6f9",fg="#14274e",command=lambda:light()).pack(padx=5,pady=5)
Button(root,text="Dark",bg="#14274e",fg="#f1f6f9",command=lambda:dark(),padx=3).pack(padx=5,pady=5)

v=Label(root,text="Version 1.0",fg="white",bg="#222831")
v.pack(ipady=90)


###terminating app
root.mainloop()

#padding in frame instance variable is inner padding
#padding in method pack is outer padding.



