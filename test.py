from datetime import datetime
from tkinter import *
from tkinter import messagebox
import os

#dat="22/04/2012"
#dat=datetime.strptime(dat,"%d/%m/%Y")
#print(isinstance(dat, datetime))

creds = "tempfile.temp"
def Signup():
    global pwordE
    global nameE
    global roots

    roots = Tk()
    roots.title("SignUp")
    introduction = Label(roots, text="Please Enter new Credentials\n")
    introduction.grid(row=0, column=0,sticky=E)

    nameL = Label(roots, text="New Username: ")
    nameL.grid(row=1,column=0, sticky=W)

    pwordL = Label(roots, text="New Password: ")
    pwordL.grid(row=2,column=0, sticky=W)

    nameE = Entry(roots,font=('arial',14,'bold'))
    nameE.grid(row=1, column=1)

    pwordE = Entry(roots, show=".", font=('arial',14,'bold'))
    pwordE.grid(row=2, column=1)

    signupButton = Button(roots, text='SignUp', command=FSSignup)
    signupButton.grid(row=3, column=0, columnspan=2)

    roots.mainloop()


def FSSignup():
    with open(creds, 'w') as f:
        f.write(nameE.get())
        f.write('\n')
        f.write(pwordE.get())
        f.close()
    roots.destroy()
    Login()
#========================Login=========================

def Login():
    global pwordEL
    global nameEL
    global rootA

    rootA = Tk()
    rootA.title('Login')

    introduction = Label(rootA, text="Please LogIn\n")
    introduction.grid(sticky=E)

    nameL = Label(rootA, text="Username: ")
    nameL.grid(row=1,column=0, sticky=W)

    pwordL = Label(rootA, text="Password: ")
    pwordL.grid(row=2,column=0, sticky=W)

    nameEL = Entry(rootA,font=('arial',14,'bold'))
    nameEL.grid(row=1, column=1)

    pwordEL = Entry(rootA, show="*", font=('arial',14,'bold'))
    pwordEL.grid(row=2, column=1)

    loginB = Button(rootA, text='LogIn', command=CheckLogin)
    loginB.grid(row=3, column=0, columnspan=2,sticky=W)

    rmuser = Button(rootA, text='DeletUser', command=DelUser)
    rmuser.grid(row=3, column=3, columnspan=2,sticky=W)

    rootA.mainloop()

#=====================CheckLogin================
def CheckLogin():
    with open(creds) as f:
        data=f.readlines()
        uname=data[0].rstrip()
        pword=data[1].rstrip()

    if nameEL.get() == uname and pwordEL.get() == pword :
        rlbl=messagebox.showinfo("Login","Logged In")
    else :
        rlbl=messagebox.showwarning("Error","Invalid login")
    
#=========================DelUser======================

def DelUser():
    os.remove(creds)
    rootA.destroy()
    Signup()

if os.path.isfile(creds):
    Login()
else:
    Signup()
    
