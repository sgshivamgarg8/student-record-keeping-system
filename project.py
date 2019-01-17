#Created By Shivam Garg

from Tkinter import *
from tkMessageBox import *

splash=Tk()
Label(splash,text="PYTHON PROJECT",relief='ridge',font='times 40',fg='chocolate',bg='maroon').grid(row=1,column=1,columnspan=5,pady=5)
Label(splash,text="Student Record Mangement System",relief='ridge',font='times 20',fg='royal blue').grid(row=2,column=1,columnspan=5,pady=5)
Label(splash,text="Created By - Shivam Garg",relief='ridge',fg='firebrick2').grid(row=3,column=1,columnspan=5,pady=5)
Label(splash,text="Enrollment number - 161B214",relief='ridge',fg='gold3').grid(row=4,column=1,columnspan=5,pady=5)

splash.after(5000,splash.destroy)
splash.mainloop()

tm=()

root=Tk()
import sqlite3
con=sqlite3.connect('project.db')
cur=con.cursor()
root.title("Student record management")

b=PhotoImage(file='background.gif')
Label(root,image=b).grid(row=0,column=0,columnspan=100,rowspan=100)

Label(root,text='Student Record Keeping System',font='times 30',bg='dark violet',relief='ridge').grid(row=1,column=1,padx=10,pady=10,  columnspan=10)
Label(root,text='Enter Enrollment Number',font='bold',bg='cyan2',relief='ridge').grid(row=2,column=1)
Label(root,text='Enter First Name',font='bold',bg='cyan2',relief='ridge').grid(row=3,column=1)
Label(root,text='Enter Last Name',font='bold',bg='cyan2',relief='ridge').grid(row=4,column=1)
Label(root,text='Enter  Enrollment Number to fetch record',relief='ridge',font='bold',bg='sandybrown').grid(row=2,column=4,padx=10)
Label(root,text='Enter DOB (DD-MMM-YYYY)',font='bold',relief='ridge',bg='cyan2').grid(row=5,column=1)
Label(root,text="Enter Father's Name",font='bold',bg='cyan2',relief='ridge').grid(row=6,column=1)
Label(root,text='Enter Registration Date',font='bold',bg='cyan2',relief='ridge').grid(row=7,column=1)
Label(root,text='Enter  Address',font='bold',bg='cyan2',relief='ridge').grid(row=8,column=1)
Label(root,text='Enter Student Mobile',font='bold',bg='cyan2',relief='ridge').grid(row=9,column=1)
Label(root,text='Enter Student Email',font='bold',bg='cyan2',relief='ridge').grid(row=10,column=1)
Label(root,text='Enter Hobbies',font='bold',bg='cyan2',relief='ridge').grid(row=12,column=1)
Label(root,text='Choose Class',font='bold',bg='cyan2',relief='ridge').grid(row=13,column=1)
v1=StringVar(value='0')
Radiobutton(root,text='11th',bg='SeaGreen1',relief='ridge',variable=v1,value='11th').grid(row=13,column=2)
Radiobutton(root,text='12th',bg='seagreen1',relief='ridge',variable=v1,value='12th').grid(row=13,column=3)

Label(root,text='Choose Subject',font='bold',bg='cyan2',relief='ridge').grid(row=14,column=1)
v2=StringVar(value='0')
Radiobutton(root,text='Science-Maths',bg='seagreen1',relief='ridge',variable=v2,value='Science-Maths').grid(row=14,column=2)
Radiobutton(root,text='Commerce',bg='seagreen1',relief='ridge',variable=v2,value='Commerce').grid(row=15,column=2)
Radiobutton(root,text='Biology',bg='seagreen1',relief='ridge',variable=v2,value='Biology').grid(row=16,column=2)    

e1=Entry(root,bd=5)
e1.grid(row=2,column=2)
e2=Entry(root)
e2.grid(row=3,column=2)
e3=Entry(root)
e3.grid(row=4,column=2)
e4=Entry(root,bd=5)
e4.grid(row=3,column=4)
e5=Entry(root)
e5.grid(row=5,column=2)
e6=Entry(root)
e6.grid(row=6,column=2)
e7=Entry(root)
e7.grid(row=7,column=2)
e8=Entry(root)
e8.grid(row=8,column=2)
e9=Entry(root)
e9.grid(row=9,column=2)
e10=Entry(root)
e10.grid(row=10,column=2)
e12=Entry(root)
e12.grid(row=12,column=2)

def insert():
    cur.execute("create table if not exists emp(id varchar(10) primary key,first_name char(15),last_name char(15),dob date,fname varchar(20),rdate date,address varchar(100),mobile number,email varchar(30),hobbies varchar(30),class varchar(10),subject varchar(15))")
    if e1.get()!='':
        try:
            cur.execute("insert into emp values(?,?,?,?,?,?,?,?,?,?,?,?)",(e1.get(),e2.get(),e3.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get(),e10.get(),e12.get(),v1.get(),v2.get()))
            showinfo('Success','Data Inserted Successfully')
        except:
            showerror('Error','Enrollment no. already exists')
    else:
        showerror('Error','Please Enter Data')
    con.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    e9.delete(0,END)
    e10.delete(0,END)
    e12.delete(0,END)
    
def delete():
    cur.execute("select id from emp where id=?",(e4.get(),))
    x=len(cur.fetchall())
    if x!=0:
        cur.execute("delete from emp where id=?",(e4.get(),))
        showinfo('Success','Deleted Successfully')
    else:
        showerror('Error','Please Enter Valid ID') 
    e4.delete(0,END)
    con.commit()
    
def show():
    show=Tk()
    show.title('show')
    show.configure(bg='black')
    Label(show,text='Student Details',bg='tomato',relief='ridge',font='times 20').grid(row=0,column=1,columnspan=3)
    Label(show,text='Enrollment number',bg='green',relief='ridge').grid(row=1,column=1,padx=5,pady=5)
    cur.execute("select id from emp where id=?",(e4.get(),))
    Label(show,text=cur.fetchall(),bg='blue',relief='ridge').grid(row=1,column=2)

    Label(show,text='First Name',bg='green',relief='ridge').grid(row=2,column=1,padx=5,pady=5)
    cur.execute("select first_name from emp where id=?",(e4.get(),))
    Label(show,text=cur.fetchall(),bg='blue',relief='ridge').grid(row=2,column=2)

    Label(show,text='Last Name',bg='green',relief='ridge').grid(row=3,column=1,padx=5,pady=5)
    cur.execute("select last_name from emp where id=?",(e4.get(),))
    Label(show,text=cur.fetchall(),bg='blue',relief='ridge').grid(row=3,column=2)

    Label(show,text='Date of Birth',bg='green',relief='ridge').grid(row=4,column=1,padx=5,pady=5)
    cur.execute("select dob from emp where id=?",(e4.get(),))
    Label(show,text=cur.fetchall(),bg='blue',relief='ridge').grid(row=4,column=2)

    Label(show,text="Father's Name",bg='green',relief='ridge').grid(row=5,column=1,padx=5,pady=5)
    cur.execute("select fname from emp where id=?",(e4.get(),))
    Label(show,text=cur.fetchall(),bg='blue',relief='ridge').grid(row=5,column=2)

    Label(show,text="Registration Date",bg='green',relief='ridge').grid(row=6,column=1,padx=5,pady=5)
    cur.execute("select rdate from emp where id=?",(e4.get(),))
    Label(show,text=cur.fetchall(),bg='blue',relief='ridge').grid(row=6,column=2)

    Label(show,text="Address",bg='green',relief='ridge').grid(row=7,column=1,padx=5,pady=5)
    cur.execute("select address from emp where id=?",(e4.get(),))
    Label(show,text=cur.fetchall(),bg='blue',relief='ridge').grid(row=7,column=2)

    Label(show,text="Mobile Number",bg='green',relief='ridge').grid(row=8,column=1,padx=5,pady=5)
    cur.execute("select mobile from emp where id=?",(e4.get(),))
    Label(show,text=cur.fetchall(),bg='blue',relief='ridge').grid(row=8,column=2)

    Label(show,text="E-Mail",bg='green',relief='ridge').grid(row=9,column=1,padx=5,pady=5)
    cur.execute("select email from emp where id=?",(e4.get(),))
    Label(show,text=cur.fetchall(),bg='blue',relief='ridge').grid(row=9,column=2)

    Label(show,text="Hobbies",bg='green',relief='ridge').grid(row=11,column=1,padx=5,pady=5)
    cur.execute("select hobbies from emp where id=?",(e4.get(),))
    Label(show,text=cur.fetchall(),bg='blue',relief='ridge').grid(row=11,column=2)

    Label(show,text="Class",bg='green',relief='ridge').grid(row=12,column=1,padx=5,pady=5)
    cur.execute("select class from emp where id=?",(e4.get(),))
    Label(show,text=cur.fetchall(),bg='blue',relief='ridge').grid(row=12,column=2)

    Label(show,text="Subject",bg='green',relief='ridge').grid(row=13,column=1,padx=5,pady=5)
    cur.execute("select subject from emp where id=?",(e4.get(),))
    Label(show,text=cur.fetchall(),bg='blue',relief='ridge').grid(row=13,column=2)
    e4.delete(0,END)
    show.mainloop()

def showall():
    showall=Tk()
    showall.title("showall")
    showall.configure(bg='black')
    Label(showall,text='Enrollment Number of Students are',bg='blue',relief='ridge').pack()
    cur.execute("select id from emp")
    a=cur.fetchall()
    for i in a:
        Label(showall,text=i,relief='ridge').pack()

    cur.execute("select count(id) from emp")
    Label(showall,text='Total number of Students',bg='blue',relief='ridge').pack()
    Label(showall,text=cur.fetchall()[0],bg='systemhighlight',relief='ridge').pack()
    
    showall.mainloop()

def at():
    
    at=Toplevel()
    at.title("at")

    c=PhotoImage(file='attendance.gif')
    Label(at,image=c).grid(row=0,column=0,columnspan=100,rowspan=100)
    
    Label(at,text='Choose Subject',bg='blue',relief='ridge',font='times 20 bold').grid(row=12,column=3)
    v=IntVar()
    Radiobutton(at,text='Science-Maths',bg='firebrick1',variable=v,value=1).grid(row=13,column=3)
    Radiobutton(at,text='Commerce',bg='firebrick1',variable=v,value=2).grid(row=14,column=3)
    Radiobutton(at,text='Biology',bg='firebrick1',variable=v,value=3).grid(row=15,column=3)

    Label(at,text='Enter Enrollment Number to Fetch Attendance',bg='midnight blue',fg='white',relief='ridge').grid(row=12,column=20,padx=10,pady=5)
    e=Entry(at,bd=5)
    e.grid(row=13,column=20)

    def insertat():
        iat=Tk()
        iat.title("iat")
        iat.configure(bg='black')
 
        if v.get()==1:  
            Label(iat,text='Enter Enrollment number',bg='cornflowerblue',relief='ridge').grid(row=0,column=0)
            e20=Entry(iat,bd=5)
            e20.grid(row=1,column=0)
            Label(iat,text='Enter Attendance of Maths',bg='cornflowerblue',relief='ridge').grid(row=2,column=0)
            e21=Entry(iat,bd=5)
            e21.grid(row=3,column=0)
            Label(iat,text='Enter Attendance of Physics',bg='cornflowerblue',relief='ridge').grid(row=4,column=0)
            e22=Entry(iat,bd=5)
            e22.grid(row=5,column=0)
            Label(iat,text='Enter Attendance of Chemistry',bg='cornflowerblue',relief='ridge').grid(row=6,column=0)
            e23=Entry(iat,bd=5)
            e23.grid(row=7,column=0)
            Label(iat,text='Enter Attendance of Hindi',bg='cornflowerblue',relief='ridge').grid(row=8,column=0)
            e24=Entry(iat,bd=5)
            e24.grid(row=9,column=0)
            Label(iat,text='Enter Attendance of English',bg='cornflowerblue',relief='ridge').grid(row=10,column=0)
            e25=Entry(iat,bd=5)
            e25.grid(row=11,column=0)

        if v.get()==2:
            Label(iat,text='Enter Enrollment number',bg='cornflowerblue',relief='ridge').grid(row=0,column=0)
            e20=Entry(iat,bd=5)
            e20.grid(row=1,column=0)
            Label(iat,text='Enter Attendance of Maths',bg='cornflowerblue',relief='ridge').grid(row=2,column=0)
            e21=Entry(iat,bd=5)
            e21.grid(row=3,column=0)
            Label(iat,text='Enter Attendance of Accounts',bg='cornflowerblue',relief='ridge').grid(row=4,column=0)
            e22=Entry(iat,bd=5)
            e22.grid(row=5,column=0)
            Label(iat,text='Enter Attendance of Economics',bg='cornflowerblue',relief='ridge').grid(row=6,column=0)
            e23=Entry(iat,bd=5)
            e23.grid(row=7,column=0)
            Label(iat,text='Enter Attendance of Physical',bg='cornflowerblue',relief='ridge').grid(row=8,column=0)
            e24=Entry(iat,bd=5)
            e24.grid(row=9,column=0)
            Label(iat,text='Enter Attendance of English',bg='cornflowerblue',relief='ridge').grid(row=10,column=0)
            e25=Entry(iat,bd=5)
            e25.grid(row=11,column=0)

        if v.get()==3:
            Label(iat,text='Enter Enrollment number',bg='cornflowerblue',relief='ridge').grid(row=0,column=0)
            e20=Entry(iat,bd=5)
            e20.grid(row=1,column=0)
            Label(iat,text='Enter Attendance of Biology',bg='cornflowerblue',relief='ridge').grid(row=2,column=0)
            e21=Entry(iat,bd=5)
            e21.grid(row=3,column=0)
            Label(iat,text='Enter Attendance of Physics',bg='cornflowerblue',relief='ridge').grid(row=4,column=0)
            e22=Entry(iat,bd=5)
            e22.grid(row=5,column=0)
            Label(iat,text='Enter Attendance of Chemistry',bg='cornflowerblue',relief='ridge').grid(row=6,column=0)
            e23=Entry(iat,bd=5)
            e23.grid(row=7,column=0)
            Label(iat,text='Enter Attendance of Hindi',bg='cornflowerblue',relief='ridge').grid(row=8,column=0)
            e24=Entry(iat,bd=5)
            e24.grid(row=9,column=0)
            Label(iat,text='Enter Attendance of English',bg='cornflowerblue',relief='ridge').grid(row=10,column=0)
            e25=Entry(iat,bd=5)
            e25.grid(row=11,column=0)
            
        def insert1():    
            cur.execute("create table if not exists at1(id varchar(10) primary key,s1 number,s2 number,s3 number,s4 number,s5 number)")
            if e20.get()!='':
                try:
                    cur.execute("insert into at1 values(?,?,?,?,?,?)",(e20.get(),e21.get(),e22.get(),e23.get(),e24.get(),e25.get()))
                    showinfo('Success','Data Inserted Successfully')
                except:
                    showerror('Error','Enter data')
            else:
                showerror('Error','Please Enter Data')
            con.commit()
            e20.delete(0,END)
            e21.delete(0,END)
            e22.delete(0,END)
            e23.delete(0,END)
            e24.delete(0,END)
            e25.delete(0,END)
                
        Button(iat,text='Insert',bg='darkturquoise',command=insert1).grid(row=20,column=0,padx=10,pady=10)

        def back():
            iat.destroy()
        Button(iat,text=' Back',bg='limegreen',command=back).grid(row=20,column=20,padx=10,pady=10)
        def exit():    
            iat.destroy()
            at.destroy()
            root.destroy()
        Button(iat,text=' Exit',bg='springgreen',command=exit).grid(row=21,column=20,padx=10,pady=2)

        iat.mainloop()

    def showat():
            showat=Toplevel()
            showat.title("showat")
            showat.configure(bg='black')
            Label(showat,text='Attendance',font='times 30',bg='navy',fg='white').grid(row=0,column=0,columnspan=4)            
       
            if v.get()==1:
                Label(showat,text='Enrollment no.',bg='green',relief='ridge').grid(row=2,column=1)
                cur.execute("select id from at1 where id=?",(e.get(),))
                Label(showat,text=cur.fetchall()[0],bg='blue',relief='ridge').grid(row=2,column=2)
                Label(showat,text='Maths',bg='green',relief='ridge').grid(row=3,column=1)
                cur.execute("select s1 from at1 where id=?",(e.get(),))
                Label(showat,text=cur.fetchall()[0],bg='blue',relief='ridge').grid(row=3,column=2)
                Label(showat,text='Physics',bg='green',relief='ridge').grid(row=4,column=1)
                cur.execute("select s2 from at1 where id=?",(e.get(),))
                Label(showat,text=cur.fetchall()[0],bg='blue',relief='ridge').grid(row=4,column=2)
                Label(showat,text='Chemistry',bg='green',relief='ridge').grid(row=5,column=1)
                cur.execute("select s3 from at1 where id=?",(e.get(),))
                Label(showat,text=cur.fetchall()[0],bg='blue',relief='ridge').grid(row=5,column=2)
                Label(showat,text='Hindi',bg='green',relief='ridge').grid(row=6,column=1)
                cur.execute("select s4 from at1 where id=?",(e.get(),))
                Label(showat,text=cur.fetchall()[0],bg='blue',relief='ridge').grid(row=6,column=2)
                Label(showat,text='English',bg='green',relief='ridge').grid(row=7,column=1)
                cur.execute("select s5 from at1 where id=?",(e.get(),))
                Label(showat,text=cur.fetchall()[0],bg='blue',relief='ridge').grid(row=7,column=2)

            if v.get()==2:
                Label(showat,text='Enrollment no.',bg='green',relief='ridge').grid(row=2,column=1)
                cur.execute("select id from at1 where id=?",(e.get(),))
                Label(showat,text=cur.fetchall()[0],bg='blue',relief='ridge').grid(row=2,column=2)
                Label(showat,text='Maths',bg='green',relief='ridge').grid(row=3,column=1)
                cur.execute("select s1 from at1 where id=?",(e.get(),))
                Label(showat,text=cur.fetchall()[0],bg='blue',relief='ridge').grid(row=3,column=2)
                Label(showat,text='Accounts',bg='green',relief='ridge').grid(row=4,column=1)
                cur.execute("select s2 from at1 where id=?",(e.get(),))
                Label(showat,text=cur.fetchall()[0],bg='blue',relief='ridge').grid(row=4,column=2)
                Label(showat,text='Economics',bg='green',relief='ridge').grid(row=5,column=1)
                cur.execute("select s3 from at1 where id=?",(e.get(),))
                Label(showat,text=cur.fetchall()[0],bg='blue',relief='ridge').grid(row=5,column=2)
                Label(showat,text='Physical',bg='green',relief='ridge').grid(row=6,column=1)
                cur.execute("select s4 from at1 where id=?",(e.get(),))
                Label(showat,text=cur.fetchall()[0],bg='blue',relief='ridge').grid(row=6,column=2)
                Label(showat,text='English',bg='green',relief='ridge').grid(row=7,column=1)
                cur.execute("select s5 from at1 where id=?",(e.get(),))
                Label(showat,text=cur.fetchall()[0],bg='blue',relief='ridge').grid(row=7,column=2)

            if v.get()==3:
                Label(showat,text='Enrollment no.',bg='green',relief='ridge').grid(row=2,column=1)
                cur.execute("select id from at1 where id=?",(e.get(),))
                Label(showat,text=cur.fetchall()[0],bg='blue',relief='ridge').grid(row=2,column=2)
                Label(showat,text='Biology',bg='green',relief='ridge').grid(row=3,column=1)
                cur.execute("select s1 from at1 where id=?",(e.get(),))
                Label(showat,text=cur.fetchall()[0],bg='blue',relief='ridge').grid(row=3,column=2)
                Label(showat,text='Physics',bg='green',relief='ridge').grid(row=4,column=1)
                cur.execute("select s2 from at1 where id=?",(e.get(),))
                Label(showat,text=cur.fetchall()[0],bg='blue',relief='ridge').grid(row=4,column=2)
                Label(showat,text='Chemistry',bg='green',relief='ridge').grid(row=5,column=1)
                cur.execute("select s3 from at1 where id=?",(e.get(),))
                Label(showat,text=cur.fetchall()[0],bg='blue',relief='ridge').grid(row=5,column=2)
                Label(showat,text='Hindi',bg='green',relief='ridge').grid(row=6,column=1)
                cur.execute("select s4 from at1 where id=?",(e.get(),))
                Label(showat,text=cur.fetchall()[0],bg='blue',relief='ridge').grid(row=6,column=2)
                Label(showat,text='English',bg='green',relief='ridge').grid(row=7,column=1)
                cur.execute("select s5 from at1 where id=?",(e.get(),))
                Label(showat,text=cur.fetchall()[0],bg='blue',relief='ridge').grid(row=7,column=2)

            showat.mainloop()
        
    Button(at,text='Show Attendance',bg='brown1',fg='white',command=showat).grid(row=14,column=20,pady=5)  
    Button(at,text=' Insert Attendance',bg='lightsalmon',command=insertat).grid(row=20,column=3,pady=5)

    def back():
        at.destroy()

    def exit():
        at.destroy()
        root.destroy()

    Button(at,text=' Exit',bg='tomato',command=exit).grid(row=21,column=20)     
    Button(at,text=' Back',bg='orangered',command=back).grid(row=20,column=20,pady=5)
    at.mainloop()

def m():
    
    m=Toplevel()
    m.title("m")

    b=PhotoImage(file='marks.gif')
    Label(m,image=b).grid(row=0,column=0,columnspan=100,rowspan=100)

    Label(m,text='Choose Subject',bg='blue',relief='ridge',font='times 20 bold').grid(row=12,column=3)
    v=IntVar()
    Radiobutton(m,text='Science-Maths',bg='limegreen',variable=v,value=1).grid(row=13,column=3)
    Radiobutton(m,text='Commerce',bg='lime green',variable=v,value=2).grid(row=14,column=3)
    Radiobutton(m,text='Biology',bg='lime green',variable=v,value=3).grid(row=15,column=3)

    Label(m,text='Enter Enrollment Number to Fetch Marks',bg='blue',relief='ridge',font='times 15').grid(row=12,column=20,padx=10,pady=5)
    e=Entry(m,bd=5)
    e.grid(row=13,column=20)

    def insertm():
        im=Tk()
        im.title("im")
        im.configure(bg='black')
 
        if v.get()==1: 
            Label(im,text='Enter Enrollment number',bg='blue',relief='ridge').grid(row=0,column=0)
            e20=Entry(im,bd=5)
            e20.grid(row=1,column=0)
            Label(im,text='Enter Marks of Maths',bg='blue',relief='ridge').grid(row=2,column=0)
            e21=Entry(im,bd=5)
            e21.grid(row=3,column=0)
            Label(im,text='Enter Marks of Physics',bg='blue',relief='ridge').grid(row=4,column=0)
            e22=Entry(im,bd=5)
            e22.grid(row=5,column=0)
            Label(im,text='Enter Marks of Chemistry',bg='blue',relief='ridge').grid(row=6,column=0)
            e23=Entry(im,bd=5)
            e23.grid(row=7,column=0)
            Label(im,text='Enter Marks of Hindi',bg='blue',relief='ridge').grid(row=8,column=0)
            e24=Entry(im,bd=5)
            e24.grid(row=9,column=0)
            Label(im,text='Enter Marks of English',bg='blue',relief='ridge').grid(row=10,column=0)
            e25=Entry(im,bd=5)
            e25.grid(row=11,column=0)

        if v.get()==2:
            Label(im,text='Enter Enrollment number',bg='blue',relief='ridge').grid(row=0,column=0)
            e20=Entry(im,bd=5)
            e20.grid(row=1,column=0)
            Label(im,text='Enter Marks of Maths',bg='blue',relief='ridge').grid(row=2,column=0)
            e21=Entry(im,bd=5)
            e21.grid(row=3,column=0)
            Label(im,text='Enter Marks of Accounts',bg='blue',relief='ridge').grid(row=4,column=0)
            e22=Entry(im,bd=5)
            e22.grid(row=5,column=0)
            Label(im,text='Enter Marks of Economics',bg='blue',relief='ridge').grid(row=6,column=0)
            e23=Entry(im,bd=5)
            e23.grid(row=7,column=0)
            Label(im,text='Enter Marks of Physical',bg='blue',relief='ridge').grid(row=8,column=0)
            e24=Entry(im,bd=5)
            e24.grid(row=9,column=0)
            Label(im,text='Enter Marks of English',bg='blue',relief='ridge').grid(row=10,column=0)
            e25=Entry(im,bd=5)
            e25.grid(row=11,column=0)

        if v.get()==3:
            Label(im,text='Enter Enrollment number',bg='blue',relief='ridge').grid(row=0,column=0)
            e20=Entry(im,bd=5)
            e20.grid(row=1,column=0)
            Label(im,text='Enter Marks of Biology',bg='blue',relief='ridge').grid(row=2,column=0)
            e21=Entry(im,bd=5)
            e21.grid(row=3,column=0)
            Label(im,text='Enter Marks of Physics',bg='blue',relief='ridge').grid(row=4,column=0)
            e22=Entry(im,bd=5)
            e22.grid(row=5,column=0)
            Label(im,text='Enter Marks of Chemistry',bg='blue',relief='ridge').grid(row=6,column=0)
            e23=Entry(im,bd=5)
            e23.grid(row=7,column=0)
            Label(im,text='Enter Marks of Hindi',bg='blue',relief='ridge').grid(row=8,column=0)
            e24=Entry(im,bd=5)
            e24.grid(row=9,column=0)
            Label(im,text='Enter Marks of English',bg='blue',relief='ridge').grid(row=10,column=0)
            e25=Entry(im,bd=5)
            e25.grid(row=11,column=0)
            
        def insert1():             
            cur.execute("create table if not exists m(id varchar(10) primary key,m1 number,m2 number,m3 number,m4 number,m5 number)")
            if e20.get()!='':
                try:
                    cur.execute("insert into m values(?,?,?,?,?,?)",(e20.get(),e21.get(),e22.get(),e23.get(),e24.get(),e25.get()))
                    showinfo('Success','Data Inserted Successfully')
                except:
                    showerror('Error','Enter data')
            else:
                showerror('Error','Please Enter Data')
            con.commit()
            e20.delete(0,END)
            e21.delete(0,END)
            e22.delete(0,END)
            e23.delete(0,END)
            e24.delete(0,END)
            e25.delete(0,END)
                
        Button(im,text='Insert',bg='chocolate',command=insert1).grid(row=20,column=0)

        def back():
            im.destroy()
        Button(im,text=' Back',bg='firebrick1',command=back).grid(row=20,column=20)

        def exit():    
            im.destroy()
            m.destroy()
            root.destroy()

        Button(im,text=' Exit',bg='orange',command=exit).grid(row=21,column=20)

        im.mainloop()

    def showm():
            showm=Toplevel()
            showm.title("showm")
            showm.configure(bg='black')
            
            Label(showm,text='Marks',font='times 30',bg='red2',relief='ridge').grid(row=0,column=0,columnspan=4,pady=10)            
       
            if v.get()==1:
             
                Label(showm,text='Enrollment no.',bg='green',relief='ridge').grid(row=2,column=1)
                cur.execute("select id from m where id=?",(e.get(),))
                
                Label(showm,text=cur.fetchall()[0],bg='blue',relief='ridge').grid(row=2,column=2)
                Label(showm,text='Maths',bg='green',relief='ridge').grid(row=3,column=1)
                cur.execute("select m1 from m where id=?",(e.get(),))
                m11=cur.fetchall()
                Label(showm,text=m11[0],bg='blue',relief='ridge').grid(row=3,column=2)
                Label(showm,text='Physics',bg='green',relief='ridge').grid(row=4,column=1)
                cur.execute("select m2 from m where id=?",(e.get(),))
                m12=cur.fetchall()
                Label(showm,text=m12[0],bg='blue',relief='ridge').grid(row=4,column=2)
                Label(showm,text='Chemistry',bg='green',relief='ridge').grid(row=5,column=1)
                cur.execute("select m3 from m where id=?",(e.get(),))
                m13=cur.fetchall()
                Label(showm,text=m13[0],bg='blue',relief='ridge').grid(row=5,column=2)
                Label(showm,text='Hindi',bg='green',relief='ridge').grid(row=6,column=1)
                cur.execute("select m4 from m where id=?",(e.get(),))
                m14=cur.fetchall()
                Label(showm,text=m14[0],bg='blue',relief='ridge').grid(row=6,column=2)
                Label(showm,text='English',bg='green',relief='ridge').grid(row=7,column=1)
                cur.execute("select m5 from m where id=?",(e.get(),))
                m15=cur.fetchall()
                Label(showm,text=m15[0],bg='blue',relief='ridge').grid(row=7,column=2)

            if v.get()==2:
                Label(showm,text='Enrollment no.',bg='green',relief='ridge').grid(row=2,column=1)
                cur.execute("select id from m where id=?",(e.get(),))
                Label(showm,text=cur.fetchall()[0],bg='blue',relief='ridge').grid(row=2,column=2)
                Label(showm,text='Maths',bg='green',relief='ridge').grid(row=3,column=1)
                cur.execute("select m1 from m where id=?",(e.get(),))
                m11=cur.fetchall()
                Label(showm,text=m11[0],bg='blue',relief='ridge').grid(row=3,column=2)
                Label(showm,text='Accounts',bg='green',relief='ridge').grid(row=4,column=1)
                cur.execute("select m2 from m where id=?",(e.get(),))
                m12=cur.fetchall()
                Label(showm,text=m12[0],bg='blue',relief='ridge').grid(row=4,column=2)
                Label(showm,text='Economics',bg='green',relief='ridge').grid(row=5,column=1)
                cur.execute("select m3 from m where id=?",(e.get(),))
                m13=cur.fetchall()
                Label(showm,text=m13[0],bg='blue',relief='ridge').grid(row=5,column=2)
                Label(showm,text='Physical',bg='green',relief='ridge').grid(row=6,column=1)
                cur.execute("select m4 from m where id=?",(e.get(),))
                m14=cur.fetchall()
                Label(showm,text=m14[0],bg='blue',relief='ridge').grid(row=6,column=2)
                Label(showm,text='English',bg='green',relief='ridge').grid(row=7,column=1)
                cur.execute("select m5 from m where id=?",(e.get(),))
                m15=cur.fetchall()
                Label(showm,text=m15[0],bg='blue',relief='ridge').grid(row=7,column=2)

            if v.get()==3:
                Label(showm,text='Enrollment no.',bg='green',relief='ridge').grid(row=2,column=1)
                cur.execute("select id from m where id=?",(e.get(),))
                Label(showm,text=cur.fetchall()[0],bg='blue',relief='ridge').grid(row=2,column=2)
                Label(showm,text='Biology',bg='green',relief='ridge').grid(row=3,column=1)
                cur.execute("select m1 from m where id=?",(e.get(),))
                m11=cur.fetchall()
                Label(showm,text=m11[0],bg='blue',relief='ridge').grid(row=3,column=2)
                Label(showm,text='Physics',bg='green',relief='ridge').grid(row=4,column=1)
                cur.execute("select m2 from m where id=?",(e.get(),))
                m12=cur.fetchall()
                Label(showm,text=m12[0],bg='blue',relief='ridge').grid(row=4,column=2)
                Label(showm,text='Chemistry',bg='green',relief='ridge').grid(row=5,column=1)
                cur.execute("select m3 from m where id=?",(e.get(),))
                m13=cur.fetchall()
                Label(showm,text=m13[0],bg='blue',relief='ridge').grid(row=5,column=2)
                Label(showm,text='Hindi',bg='green',relief='ridge').grid(row=6,column=1)
                cur.execute("select m4 from m where id=?",(e.get(),))
                m14=cur.fetchall()
                Label(showm,text=m14[0],bg='blue',relief='ridge').grid(row=6,column=2)
                Label(showm,text='English',bg='green',relief='ridge').grid(row=7,column=1)
                cur.execute("select m5 from m where id=?",(e.get(),))
                m15=cur.fetchall()
                Label(showm,text=m15[0],bg='blue',relief='ridge').grid(row=7,column=2)

            Label(showm,text='Obtained marks',bg='coral3',relief='ridge').grid(row=8,column=1,pady=10)
            Label(showm,text='Total Marks= 500',bg='coral3',relief='ridge').grid(row=9,column=1,columnspan=4,pady=10)
            global tm
            tm=()
            vv=()
            for v1  in m11:
                for vv  in m11:
                    tm+=vv
            for v2 in m12:
                for vv in m12:
                    tm+=vv
            for v3 in m13:
                for vv in m13:
                 tm+=vv
            for v4 in m14:
                for vv in m14:
                 tm+=vv
            for v5 in m15:
                for vv in m15:
                 tm+=vv
            s=0
            for i in tm:
                s+=i
            Label(showm,text=s,bg='coral3',relief='ridge').grid(row=8,column=2)
            Label(showm,text='CGPA',bg='coral3',relief='ridge').grid(row=10,column=1,pady=10)
            perc=s/5
            cgpa=perc/9.5
            Label(showm,text=cgpa,bg='coral3',relief='ridge').grid(row=10,column=2)
                  
            showm.mainloop()   
        
    Button(m,text='Show Marks',bg='firebrick1',command=showm).grid(row=14,column=20,pady=5)  
    Button(m,text='Insert Marks',bg='firebrick1',command=insertm).grid(row=20,column=3,pady=5)

    def back():
        m.destroy()

    def exit():
        m.destroy()
        root.destroy()

    Button(m,text='Exit',bg='cadet blue',command=exit).grid(row=21,column=20)     
    Button(m,text='Back',bg='lightsalmon',command=back).grid(row=20,column=20,pady=5)
    m.mainloop()

Button(root,text='Insert',bg='brown1',command=insert,bd=5).grid(row=19,column=1,columnspan=2)
Button(root,text='Show Details',bg='sandybrown',command=show).grid(row=4,column=4)
Button(root,text='Delete',bg='sandybrown',command=delete).grid(row=6,column=4)
Button(root,text='Show All',bg='mediumorchid',command=showall).grid(row=8,column=4)
Button(root,text='Attendance',bg='magenta',command=at).grid(row=10,column=4)
Button(root,text='Marks',bg='coral',command=m).grid(row=13,column=4)

def exit():
    root.destroy()
Button(root,text=' Exit',bg='orange',bd=5,command=exit).grid(row=19,column=4)

root.mainloop()
