from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime


class Hotel:
    def __init__(self,root) :
        self.root=root
        self.root.title("Hotel Management Systems")
        self.root.geometry("1350x750+0+0")
        self.root.config(background= "powder blue")

        MainFrame = Frame(self.root)
        MainFrame.grid()

        TopFrame = Frame(MainFrame, bd=14, width=1350, height=550, padx=20, relief=RIDGE, bg="cadet blue")
        TopFrame.pack(side=TOP)

        LeftFrame = Frame(TopFrame, bd=10, width=450, height=550, padx=2, relief=RIDGE, bg="powder blue")
        LeftFrame.pack(side=LEFT)

        RightFrame = Frame(TopFrame, bd=10, width=820, height=550, padx=2, relief=RIDGE, bg="cadet blue")
        RightFrame.pack(side=RIGHT)

        BottomFrame = Frame(MainFrame, bd=10, width=1350, height=150, padx=20, relief=RIDGE, bg="powder blue")
        BottomFrame.pack(side=BOTTOM)

        #================================= Function =========================
        global txtError
        txtError=" "
        def iExit():
            iExit = tkinter.messagebox.askyesno("Hotel Management System","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
        
        def Receipt():
            self.txtReceipt.insert(END, CustomerRef.get()+"\t"+Firstname.get()+"\t"+Surname.get()+"\t"+Address.get()+"\t"+PostCode.get()+"\t"+Mobile.get()+"\t"+Nationality.get()+"\t"+CheckInDate.get()+"\t"+CheckOutDate.get()+"\t"+PaidTax.get()+"\t"+SubTotal.get()+"\t"+TotalCost.get()+"\n")

        def Reset():
            CustomerRef.set("")
            Firstname.set("")
            Surname.set("")
            Address.set("")
            PostCode.set("")
            Mobile.set("")
            Email.set("")
            Nationality.set("")
            DOB.set("")
            IDType.set("")
            Gender.set("")
            CheckInDate.set("")
            CheckOutDate.set("")
            Meal.set("")
            RoomType.set("")
            RoomNo.set("")
            RoomExtNo.set("")
            TotalCost.set("")
            SubTotal.set("")
            PaidTax.set("")
            TotalDays.set("")
            self.txtReceipt.delete("1.0",END)

        def TotalCostandDate():
            if CheckInDate.get() != "" and CheckOutDate.get() != "" :

                if "/" in CheckInDate.get() and "/" in CheckOutDate.get() :

                    InDate = CheckInDate.get()
                    OutDate = CheckOutDate.get()
                    date_format = "%d/%m/%Y"
                    InDate = datetime.strptime(InDate, date_format )
                    OutDate = datetime.strptime(OutDate, date_format)
                    TotalDays.set(abs((OutDate - InDate).days))
                else :
                    txtError = "Error: Enter a valide date\n"

            else :
                txtError = "Error: Champ 'Check In date' or 'Check Out date' empty\n"

            if Meal.get() == "Breakfast" and RoomType.get() == "Single" :
                q1 = float(17)
                q2 = float(34)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 * q4)
                Tax = "$" + str('%.2f'%((q5)*0.09))
                ST = "$" + str('%.2f'%((q5)))
                TT = "$" + str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)

            elif Meal.get() == "Breakfast" and RoomType.get() == "Double" :
                q1 = float(35)
                q2 = float(43)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 * q4)
                Tax = "$" + str('%.2f'%((q5)*0.09))
                ST = "$" + str('%.2f'%((q5)))
                TT = "$" + str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)

            elif Meal.get() == "Breakfast" and RoomType.get() == "Family" :
                q1 = float(45)
                q2 = float(63)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 * q4)
                Tax = "$" + str('%.2f'%((q5)*0.09))
                ST = "$" + str('%.2f'%((q5)))
                TT = "$" + str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)
                
            elif Meal.get() == "Lunch" and RoomType.get() == "Single" :
                q1 = float(29)
                q2 = float(37)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 * q4)
                Tax = "$" + str('%.2f'%((q5)*0.09))
                ST = "$" + str('%.2f'%((q5)))
                TT = "$" + str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)
            
            elif Meal.get() == "Lunch" and RoomType.get() == "Double" :
                q1 = float(37)
                q2 = float(43)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 * q4)
                Tax = "$" + str('%.2f'%((q5)*0.09))
                ST = "$" + str('%.2f'%((q5)))
                TT = "$" + str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)

            elif Meal.get() == "Lunch" and RoomType.get() == "Family" :
                q1 = float(46)
                q2 = float(63)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 * q4)
                Tax = "$" + str('%.2f'%((q5)*0.09))
                ST = "$" + str('%.2f'%((q5)))
                TT = "$" + str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)

            elif Meal.get() == "Dinner" and RoomType.get() == "Single" :
                q1 = float(28)
                q2 = float(37)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 * q4)
                Tax = "$" + str('%.2f'%((q5)*0.09))
                ST = "$" + str('%.2f'%((q5)))
                TT = "$" + str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)
                
            elif Meal.get() == "Dinner" and RoomType.get() == "Double" :
                q1 = float(30)
                q2 = float(43)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 * q4)
                Tax = "$" + str('%.2f'%((q5)*0.09))
                ST = "$" + str('%.2f'%((q5)))
                TT = "$" + str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)

            elif Meal.get() == "Dinner" and RoomType.get() == "Family" :
                q1 = float(43)
                q2 = float(63)
                q3 = float(TotalDays.get())
                q4 = float(q1 + q2)
                q5 = float(q3 * q4)
                Tax = "$" + str('%.2f'%((q5)*0.09))
                ST = "$" + str('%.2f'%((q5)))
                TT = "$" + str('%.2f'%(q5 + ((q5)*0.09)))
                PaidTax.set(Tax)
                SubTotal.set(ST)
                TotalCost.set(TT)

            else :
                txtError="Error: Check the 'Meal' or the 'Room Type'\n"


        CustomerRef = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        PostCode = StringVar()
        Mobile = StringVar()
        Email = StringVar()
        Nationality = StringVar()
        DOB = StringVar()
        IDType = StringVar()
        Gender = StringVar()
        CheckInDate = StringVar()
        CheckOutDate = StringVar()
        Meal = StringVar()
        RoomType = StringVar()
        RoomNo = StringVar()
        RoomExtNo = StringVar()
        TotalCost = StringVar()
        SubTotal = StringVar()
        PaidTax = StringVar()
        TotalDays = StringVar()

        #=============== Widget ================

        self.lblError = Label(BottomFrame, font=('arial',18, 'bold'), text=txtError, padx=2,bg="powder blue",fg="red")
        self.lblError.grid(row=1,column=4)

        self.lblCustomer_Ref = Label(LeftFrame, font=('arial',12, 'bold'), text="Customer Ref:", padx=2,bg="powder blue")
        self.lblCustomer_Ref.grid(row=0, column=0, sticky=W)
        self.txtCustomer_Ref = Entry(LeftFrame, font=('arial',12, 'bold'), textvariable=CustomerRef, width=20)
        self.txtCustomer_Ref.grid(row=0, column=1, padx=20, pady=3)

        self.lblFirstname = Label(LeftFrame, font=('arial',12, 'bold'), text="Firstname:", padx=2,bg="powder blue")
        self.lblFirstname.grid(row=1, column=0, sticky=W)
        self.txtFirstname = Entry(LeftFrame, font=('arial',12, 'bold'), textvariable=Firstname, width=20)
        self.txtFirstname.grid(row=1, column=1, padx=20, pady=3)

        self.lblSurname = Label(LeftFrame, font=('arial',12, 'bold'), text="Surname:", padx=2,bg="powder blue")
        self.lblSurname.grid(row=2, column=0, sticky=W)
        self.txtSurname = Entry(LeftFrame, font=('arial',12, 'bold'), textvariable=Surname, width=20)
        self.txtSurname.grid(row=2, column=1, padx=20, pady=3)

        self.lblAddress = Label(LeftFrame, font=('arial',12, 'bold'), text="Address:", padx=2,bg="powder blue")
        self.lblAddress.grid(row=3, column=0, sticky=W)
        self.txtAddress = Entry(LeftFrame, font=('arial',12, 'bold'), textvariable=Address, width=20)
        self.txtAddress.grid(row=3, column=1, padx=20, pady=3)

        self.lblPostCode = Label(LeftFrame, font=('arial',12, 'bold'), text="PostCode:", padx=2,bg="powder blue")
        self.lblPostCode.grid(row=4, column=0, sticky=W)
        self.txtPostCode = Entry(LeftFrame, font=('arial',12, 'bold'), textvariable=PostCode, width=20)
        self.txtPostCode.grid(row=4, column=1, padx=20, pady=3)

        self.lblMobile = Label(LeftFrame, font=('arial',12, 'bold'), text="Mobile:", padx=2,bg="powder blue")
        self.lblMobile.grid(row=5, column=0, sticky=W)
        self.txtMobile = Entry(LeftFrame, font=('arial',12, 'bold'), textvariable=Mobile, width=20)
        self.txtMobile.grid(row=5, column=1, padx=20, pady=3)

        self.lblEmail = Label(LeftFrame, font=('arial',12, 'bold'), text="Email:", padx=2,bg="powder blue")
        self.lblEmail.grid(row=6, column=0, sticky=W)
        self.txtEmail = Entry(LeftFrame, font=('arial',12, 'bold'), textvariable=Email, width=20)
        self.txtEmail.grid(row=6, column=1, padx=20, pady=3)
        #============ Combobox =======
        self.lblNationality = Label(LeftFrame, font=('arial',12, 'bold'), text="Nationality:", padx=2,bg="powder blue")
        self.lblNationality.grid(row=7, column=0, sticky=W)
        self.cboNationality = ttk.Combobox(LeftFrame, font=('arial',12, 'bold'), textvariable=Nationality, state='readonly', width=18)
        self.cboNationality['value'] = ('','British','Nigeria','Kenya','India','France','Iran','Morocco','Canada','Norway')
        self.cboNationality.current(0)
        self.cboNationality.grid(row=7, column=1, padx=20, pady=3)

        self.lblDOB = Label(LeftFrame, font=('arial',12, 'bold'), text="Date of birth:", padx=2,bg="powder blue")
        self.lblDOB.grid(row=8, column=0, sticky=W)
        self.txtDOB = Entry(LeftFrame, font=('arial',12, 'bold'), textvariable=DOB, width=20)
        self.txtDOB.grid(row=8, column=1, padx=20, pady=3)

        self.lblIDType = Label(LeftFrame, font=('arial',12, 'bold'), text="Type of ID:", padx=2,bg="powder blue")
        self.lblIDType.grid(row=9, column=0, sticky=W)
        self.cboIDType = ttk.Combobox(LeftFrame, font=('arial',12, 'bold'), textvariable=IDType, state='readonly', width=18)
        self.cboIDType['value'] = ('','Pilot licence','Driving licence','Student ID','Passport')
        self.cboIDType.current(0)
        self.cboIDType.grid(row=9, column=1, padx=20, pady=3)

        self.lblGender = Label(LeftFrame, font=('arial',12, 'bold'), text="Gender:", padx=2,bg="powder blue")
        self.lblGender.grid(row=10, column=0, sticky=W)
        self.cboGender = ttk.Combobox(LeftFrame, font=('arial',12, 'bold'), textvariable=Gender, state='readonly', width=18)
        self.cboGender['value'] = ('','Male','Femele')
        self.cboGender.current(0)
        self.cboGender.grid(row=10, column=1, padx=20, pady=3)

        self.lblCheckInDate = Label(LeftFrame, font=('arial',12, 'bold'), text="Check in Date:", padx=2,bg="powder blue")
        self.lblCheckInDate.grid(row=11, column=0, sticky=W)
        self.txtCheckInDate = Entry(LeftFrame, font=('arial',12, 'bold'), textvariable=CheckInDate, width=20)
        self.txtCheckInDate.grid(row=11, column=1, padx=20, pady=3)

        self.lblCheckOutDate = Label(LeftFrame, font=('arial',12, 'bold'), text="Check Out Date:", padx=2,bg="powder blue")
        self.lblCheckOutDate.grid(row=12, column=0, sticky=W)
        self.txtCheckOutDate = Entry(LeftFrame, font=('arial',12, 'bold'), textvariable=CheckOutDate, width=20)
        self.txtCheckOutDate.grid(row=12, column=1, padx=20, pady=3)

        self.lblMeal = Label(LeftFrame, font=('arial',12, 'bold'), text="Meal:", padx=2,bg="powder blue")
        self.lblMeal.grid(row=13, column=0, sticky=W)
        self.cboMeal = ttk.Combobox(LeftFrame, font=('arial',12, 'bold'), textvariable=Meal, state='readonly', width=18)
        self.cboMeal['value'] = ('','Breakfast','Lunch','Dinner')
        self.cboMeal.current(0)
        self.cboMeal.grid(row=13, column=1, padx=20, pady=3)

        self.lblRoomType = Label(LeftFrame, font=('arial',12, 'bold'), text="Room Type:", padx=2,bg="powder blue")
        self.lblRoomType.grid(row=14, column=0, sticky=W)
        self.cboRoomType = ttk.Combobox(LeftFrame, font=('arial',12, 'bold'), textvariable=RoomType, state='readonly', width=18)
        self.cboRoomType['value'] = ('','Single','Double','Family')
        self.cboRoomType.current(0)
        self.cboRoomType.grid(row=14, column=1, padx=20, pady=3)

        self.lblRoomNo = Label(LeftFrame, font=('arial',12, 'bold'), text="Room No:", padx=2,bg="powder blue")
        self.lblRoomNo.grid(row=15, column=0, sticky=W)
        self.cboRoomNo = ttk.Combobox(LeftFrame, font=('arial',12, 'bold'), textvariable=RoomNo, state='readonly', width=18)
        self.cboRoomNo['value'] = ('','001','002','003')
        self.cboRoomNo.current(0)
        self.cboRoomNo.grid(row=15, column=1, padx=20, pady=3)

        self.lblRoomExtNo = Label(LeftFrame, font=('arial',12, 'bold'), text="Room Ext No:", padx=2,bg="powder blue")
        self.lblRoomExtNo.grid(row=16, column=0, sticky=W)
        self.cboRoomExtNo = ttk.Combobox(LeftFrame, font=('arial',12, 'bold'), textvariable=RoomExtNo, state='readonly', width=18)
        self.cboRoomExtNo['value'] = ('','1001','1002','1003')
        self.cboRoomExtNo.current(0)
        self.cboRoomExtNo.grid(row=16, column=1, padx=20, pady=3)

        #====================== Receipt ==============

        self.lblLabel = Label(RightFrame,font=('arial', 10, 'bold'),pady=10,bg="cadet Blue",text="Customer Ref\tFirstname\tSurname\tAddress\tPostCode\tMobile\tNationality\tCheckOutDate")
        self.lblLabel.grid(row=0, column=0,columnspan=17)

        self.txtReceipt = Text(RightFrame,height=15,width=108,bd=10,font=('arial', 11, 'bold'))
        self.txtReceipt.grid(row=1,column=0, columnspan=2, padx=2, pady=5)

        self.lblDays = Label(RightFrame, font=('arial',14, 'bold'), text="No of Days:", padx=2,bg="cadet blue",bd=7, fg="black")
        self.lblDays.grid(row=2, column=0, sticky=W)
        self.txtDays = Entry(RightFrame, font=('arial',14, 'bold'), textvariable=TotalDays, width=67, bd=7, bg="white", justify=LEFT)
        self.txtDays.grid(row=2, column=1)

        self.lblPaidTax = Label(RightFrame, font=('arial',14, 'bold'), text="Paid Tax:", padx=2,bg="cadet blue",bd=7, fg="black")
        self.lblPaidTax.grid(row=3, column=0, sticky=W)
        self.txtPaidTax = Entry(RightFrame, font=('arial',14, 'bold'), textvariable=PaidTax, width=67, bd=7, bg="white", justify=LEFT)
        self.txtPaidTax.grid(row=3, column=1)

        self.lblSubTotal = Label(RightFrame, font=('arial',14, 'bold'), text="SubTotal:", padx=2,bg="cadet blue",bd=7, fg="black")
        self.lblSubTotal.grid(row=4, column=0, sticky=W)
        self.txtSubTotal = Entry(RightFrame, font=('arial',14, 'bold'), textvariable=SubTotal, width=67, bd=7, bg="white", justify=LEFT)
        self.txtSubTotal.grid(row=4, column=1)

        self.lblTotalCost = Label(RightFrame, font=('arial',14, 'bold'), text="TotalCost:", padx=2,bg="cadet blue",bd=7, fg="black")
        self.lblTotalCost.grid(row=5, column=0, sticky=W)
        self.txtTotalCost = Entry(RightFrame, font=('arial',14, 'bold'), textvariable=TotalCost, width=67, bd=7, bg="white", justify=LEFT)
        self.txtTotalCost.grid(row=5, column=1)

        #=========================Button================
        self.btnTotal=Button(BottomFrame,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=21,height=2,bg='powder blue',text="Total",command=TotalCostandDate).grid(row=0,column=4,padx=4)

        self.btnReceipt=Button(BottomFrame,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=21,height=2,bg='powder blue',text="Receipt",command=Receipt).grid(row=0,column=5,padx=5)

        self.btnReset=Button(BottomFrame,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=21,height=2,bg='powder blue',text="Reset",command=Reset).grid(row=0,column=6,padx=5)

        self.btnExit=Button(BottomFrame,padx=16,pady=1,bd=4,fg="black",font=('arial',16,'bold'),width=21,height=2,bg='powder blue',text="Exit",command=iExit ).grid(row=0,column=7,padx=5)
        




if __name__=='__main__':
    root = Tk()
    application = Hotel(root)
    root.mainloop()
