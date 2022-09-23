from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='' :
        messagebox.showerror('Error','Fields cannot be empty')

    elif usernameEntry.get()=='Sandesh' and passwordEntry.get()=='1234':
        messagebox.showinfo('Login Successful','Welcome')
        window.destroy()
        import sms


    else:
        messagebox.showerror('Error','Incorrect Credentials')


window=Tk()

window.geometry('1280x700+120+0')
window.title('Login System')
window.resizable(False,False)

backgroundImage=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0)

loginFrame=Frame(window,bg='white')
loginFrame.place(x=400,y=150)

logoImage=PhotoImage(file='school.png')
logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)

usernameImage=PhotoImage(file='user.png' )
usernameLabel=Label(loginFrame,image=usernameImage,text='Student Name',compound=LEFT,
                    font=('times new roman',20,'bold'),bg='white',padx=10)

usernameLabel.grid(row=1,column=0,pady=10,padx=20)

usernameEntry=Entry(loginFrame,font=('arial',16),bd=5,fg='black')
usernameEntry.grid(row=1,column=1,pady=10,padx=20)


passwordImage=PhotoImage(file='password.png')
passwordLabel=Label(loginFrame,image=passwordImage,text='Password        ',compound=LEFT,
                    font=('times new roman',20,'bold'),bg='white',padx=10)

passwordLabel.grid(row=2,column=0,pady=10,padx=20)

passwordEntry=Entry(loginFrame,font=('arial',16),bd=5,fg='black')
passwordEntry.grid(row=2,column=1,pady=10,padx=20)

loginButton=Button(loginFrame,text='LOGIN',font=('arial',16,'bold'),width=15,fg='white',bg='palegreen',
                   activebackground='palegreen',activeforeground='white',cursor='hand2',command=login  )
loginButton.grid(row=3,column=1,pady=10)

window.mainloop()


