from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox
import pymysql

#functionality Part
def show_student():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)


def delete_student():
    indexing=studentTable.focus()
    print(indexing)
    content=studentTable.item(indexing)
    content_id=content['values'][0]
    query='delete from student where id=%s'
    mycursor.execute(query,content_id)
    com.commit()
    messagebox.showinfo('Deleted',f' ID {content_id} is deleted successfully ')
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)


def search_student():
    def search_data():
        query='select * from student where id =%s or name=%s or email=%s or mobile=%s or address=%s or gender=%s or dob=%s'
        mycursor.execute(query,(idEntry.get(),nameEntry.get(),emailEntry.get(),phoneEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get()))
        studentTable.delete(*studentTable.get_children())
        fetched_data=mycursor.fetchall()

        for data in fetched_data:
            studentTable.insert('',END,values=data)




    search_window = Toplevel()
    search_window.title('Search Student')
    search_window.grab_set()
    search_window.resizable(False, False)
    idLabel = Label(search_window, text='ID', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(search_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    phoneLabel = Label(search_window, text='Phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    phoneEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(search_window, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    emailEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel = Label(search_window, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    genderLabel = Label(search_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, pady=15, padx=10)

    dobLabel = Label(search_window, text='DOB', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, pady=15, padx=10)

    search_student_button = ttk.Button(search_window, text='SEARCH STUDENT', command=search_data)
    search_student_button.grid(row=7, columnspan=2)



def add_student():
    def add_data():
        if idEntry.get() == '' or nameEntry.get() == '' or phoneEntry.get()=='' or emailEntry.get()=='' or addressEntry.get()=='' or genderEntry.get()=='' or dobEntry.get()=='' :
            messagebox.showerror('Error','Provide all details',parent=add_window)

        else:
            currentdate = time.strftime('%B %d,%Y')
            currenttime = time.strftime('%H:%M:%S %p')

            try:
                query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get(),currentdate,currenttime))
                com.commit()
                result=messagebox.askyesno('Confirm','Data added successfully.Do you want to clean the form?',parent=add_window)
                if result:
                    idEntry.delete(0,END)
                    phoneEntry.delete(0,END)
                    nameEntry.delete(0,END)
                    emailEntry.delete(0,END)
                    addressEntry.delete(0,END)
                    genderEntry.delete(0,END)
                    dobEntry.delete(0,END)
                else:
                    pass
            except:
                messagebox.showerror('Error','ID cannot be repeated',parent=add_window)
                return

            query='select * from student'
            mycursor.execute(query)
            fetched_data=mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for data in fetched_data:
                studentTable.insert('',END,values=data)



    add_window=Toplevel()
    add_window.grab_set()
    add_window.title('Add Student')
    add_window.resizable(False,False)
    idLabel=Label(add_window,text='ID',font=('times new roman',20,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,pady=15,padx=10)

    nameLabel = Label(add_window, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15,sticky=W)
    nameEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    phoneLabel = Label(add_window, text='Phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15,sticky=W)
    phoneEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(add_window, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15,sticky=W)
    emailEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel = Label(add_window, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15,sticky=W)
    addressEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    genderLabel = Label(add_window, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=30, pady=15,sticky=W)
    genderEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, pady=15, padx=10)

    dobLabel = Label(add_window, text='DOB', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=30, pady=15,sticky=W)
    dobEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, pady=15, padx=10)

    add_student_button=ttk.Button(add_window,text='ADD STUDENT',command=add_data)
    add_student_button.grid(row=7,columnspan=2)


def connect_database():

    def connect():
        global mycursor,com
        try:
            com=pymysql.connect(host='localhost',user='root',password='147896325')
            mycursor=com.cursor()
            #messagebox.showinfo('Success','Database Connection is successful',parent=connectWIndow)
        except:
            messagebox.showerror('Error!',' Invalid Details',parent=connectWIndow)
            return
        try:
            query = 'create database studentmanagementsystem'
            mycursor.execute(query)
            query = 'use studentmanagementsystem'
            mycursor.execute(query)
            query = 'create table student(ID int not null primary key,name varchar(30),mobile varchar(10),email varchar(30),address varchar(100),gender varchar(20),dob varchar(20),date varchar(50),time varchar(50))'
            mycursor.execute(query)
        except:
            query='use studentmanagementsystem'
            mycursor.execute(query)
        messagebox.showinfo('Success','Database Connection is Successful',parent= connectWIndow)
        connectWIndow.destroy()
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportstudentButton.config(state=NORMAL)










    connectWIndow=Toplevel()
    connectWIndow.grab_set()
    connectWIndow.geometry('470x250+730+230')
    connectWIndow.title('DataBase Connection')
    connectWIndow.resizable(0,0)

    hostnameLabel=Label(connectWIndow,text='Host Name',font=('arial,20,bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)
    hostEntry=Entry(connectWIndow,font=('roman',14,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel = Label(connectWIndow, text='User Name', font=('arial,20,bold'))
    usernameLabel.grid(row=1, column=0, padx=20)
    usernameEntry = Entry(connectWIndow, font=('roman', 14, 'bold'), bd=2)
    usernameEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordLabel = Label(connectWIndow, text='Password', font=('arial,20,bold'))
    passwordLabel.grid(row=2, column=0, padx=20)
    passwordEntry = Entry(connectWIndow, font=('roman', 14, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)
    
    connectButton=ttk.Button(connectWIndow,text='CONNECT',command=connect)
    connectButton.grid(row=3,columnspan=2 )

    




count=0
text=''
def slider():
    global text, count
    if count == len(s):
        count = 0
        text = ''
    text = text+s[count]
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(200,slider)
def clock():

    date =time.strftime('%B %d,%Y' )
    currenttime = time.strftime('%H:%M:%S %p')
    datetimeLabel.config(text=f'{date}\n{currenttime}')


    datetimeLabel.after(1000,clock)


#GUI Part
root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')

root.geometry('1280x700+120+0')
root.title('Student Management System')
root.resizable(False,False)

datetimeLabel=ttk.Label(root,text='Hello',font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()

s='Student Management System'
sliderLabel=ttk.Label(root,text=s,font=('arial',28,'italic bold'))
sliderLabel.place(x=400,y=0)
slider()


connectButton=ttk.Button(root,text='Connect To Database',command=connect_database)
connectButton.place(x=1100,y=20)

leftFrame=Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)

logo_image=PhotoImage(file='student (1).png')
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)

addstudentButton=ttk.Button(leftFrame,text='Add Student',width=25,state=DISABLED,command=add_student)
addstudentButton.grid(row=1,column=0,pady=20)

searchstudentButton=ttk.Button(leftFrame,text='Search Student',width=25,state=DISABLED,command=search_student)
searchstudentButton.grid(row=2,column=0,pady=20)

deletestudentButton=ttk.Button(leftFrame,text='Delete Student',width=25,state=DISABLED,command=delete_student)
deletestudentButton.grid(row=3,column=0,pady=20)

updatestudentButton=ttk.Button(leftFrame,text='Update Student',width=25,state=DISABLED)
updatestudentButton.grid(row=4,column=0,pady=20)

showstudentButton=ttk.Button(leftFrame,text='Show Student',width=25,state=DISABLED,command=show_student)
showstudentButton.grid(row=5,column=0,pady=20)

exportstudentButton=ttk.Button(leftFrame,text='Export Data',width=25,state=DISABLED)
exportstudentButton.grid(row=6,column=0,pady=20)

exitstudentButton=ttk.Button(leftFrame,text='Exit',width=25)
exitstudentButton.grid(row=7,column=0,pady=20)



rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)


scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)


studentTable=ttk.Treeview(rightFrame,columns=('ID','Name','Mobile','Email','Address','Gender',
                                 'D.O.B','Added Date','Added Time'),
                          xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)


scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)


studentTable.pack(fill=BOTH,expand=1)


studentTable.heading('ID',text='ID')
studentTable.heading('Name',text='Full-Name')
studentTable.heading('Mobile',text='Mobile Number')
studentTable.heading('Email',text='Email-ID')
studentTable.heading('Address',text='Address')
studentTable.heading('Gender',text='Gender')
studentTable.heading('D.O.B',text='Date of Birth')
studentTable.heading('Added Date',text='Added Date')
studentTable.heading('Added Time',text='Added Time')

studentTable.column('ID',width=50,anchor=CENTER)
studentTable.column('Name',width=200,anchor=CENTER)
studentTable.column('Mobile',width=150,anchor=CENTER)
studentTable.column('Email',width=300,anchor=CENTER)
studentTable.column('Address',width=350,anchor=CENTER)
studentTable.column('Gender',width=100,anchor=CENTER)
studentTable.column('D.O.B',width=150,anchor=CENTER)
studentTable.column('Added Date',width=300,anchor=CENTER)
studentTable.column('Added Time',width=300,anchor=CENTER)

style=ttk.Style()

style.configure('Treeview',rowheight=40,font=('arial',12,'bold'),background='white',fieldbackground='white')
style.configure('Treeview.Heading',font=('arial',14,'bold'))

studentTable.config(show='headings')
root.mainloop()
