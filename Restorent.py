import tkinter as tk 
from tkinter import Label, Button, image_names
import tkinter.messagebox
import time
from tkinter import font




localtime = time.asctime(time. localtime(time.time()))
class RestaurantApp:
    # Creating the window and its dimensions 
    def __init__(self, top):
        self.top = top
        top.title("Restaurant Management")
        top.geometry("1028x500")
        top.configure(background="#091833")

        font10 = "{Courier New} 10 normal"
        font11 = "{U.S 101} 30 bold"
        font12 = "Al-Aramco 11 bold"
        font13 = "{Courier New} 10 bold"
        font14 = "{Segoe UI} 15 bold"
        font15 = "Arial 13 bold"
        font16 = "{Segoe UI} 13 bold"

                #_______________________ variable______________________
        Order = tk.StringVar()
        Fried = tk.StringVar()
        Burger = tk.StringVar()
        Big = tk.StringVar()
        Royal = tk.StringVar()
        Veg = tk.StringVar()
        Drinks = tk.StringVar()
        Cost = tk.StringVar()
        Service = tk.StringVar()
        Tax = tk.StringVar()
        Subtotal = tk.StringVar()
        Total = tk.StringVar()
#_______________ Button's funt ______________________
        def Reset():
            Order.set("")
            Fried.set("")
            Burger.set("")
            Big.set("")
            Royal.set("")
            Veg.set("")
            Drinks.set("")
            Cost.set("")
            Service.set("")
            Tax.set("")
            Subtotal.set("")
            Total.set("")
        
        def Price():
            Fried.set("$12")
            Burger.set("$5")
            Big.set("$24")
            Royal.set("$56")
            Veg.set("$10")
            Drinks.set("$3")

        def Totale():

            TCost = ((int(Fried.get()) * 12) + (int(Burger.get()) * 5) + (int(Big.get()) * 24) + (int(Royal.get()) * 56) + (int(Veg.get()) * 10) + (int(Drinks.get()) * 3))
            TService = float(Service.get()) + float(Tax.get())
            TTotal = TCost + TService
            Cost.set(TCost)
            Subtotal.set(TService)
            Total.set(TTotal)
        
        def iExit():
            iExit = tk.messagebox.askyesno("Restaurant Management System","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
        
        #____info food___

        self.Label1 = tk.Label(master=top, text='Restaurant Management', background="#091833", font=font11, foreground="#f2a343")
        self.Label1.place(relx=0.268, rely=0.02, height=51, width=507)

        localtime1 = Label(master=top, text=localtime, background="#091833", font=font16, fg="steel blue")
        localtime1.place(relx=0.420, rely=0.12)

        #____ Label food____

        self.Label12 = tk.Label(master=top, text="Order Num :", foreground="#bac8bd", font=font12, background="#091833")
        self.Label12.place(relx=0.054, rely=0.25)
        self.Label12 = tk.Label(master=top, text="Fried Botato :", foreground="#bac8bd", font=font12, background="#091833")
        self.Label12.place(relx=0.044, rely=0.32)
        self.Label12 = tk.Label(master=top, text="Chk Burger :", foreground="#bac8bd", font=font12, background="#091833")
        self.Label12.place(relx=0.053, rely=0.4)
        self.Label12 = tk.Label(master=top, text="Big King :", foreground="#bac8bd", font=font12, background="#091833")
        self.Label12.place(relx=0.078, rely=0.48)
        self.Label12 = tk.Label(master=top, text="Chk Royal :", foreground="#bac8bd", font=font12, background="#091833")
        self.Label12.place(relx=0.060, rely=0.56)
        self.Label12 = tk.Label(master=top, text="Veg Saled :", foreground="#bac8bd", font=font12, background="#091833")
        self.Label12.place(relx=0.055, rely=0.64)
        self.Label12 = tk.Label(master=top, text="Drinks :", foreground="#1812c6", font=font12, background="#091833")
        self.Label12.place(relx=0.093, rely=0.71)

        #_______ Entry food _____

        self.OrderEntry1= tk.Entry(master=top,background="#d9d9d9", textvariable= Order, foreground="#c60000", selectbackground="#f2a343", font = font13)
        self.OrderEntry1.place(relx=0.18, rely=0.26)
        self.FriedEntry1= tk.Entry(master=top,background="#d9d9d9", textvariable= Fried, foreground="#c60000", selectbackground="#f2a343", font = font13)
        self.FriedEntry1.place(relx=0.18, rely=0.34)
        self.BurgerEntry1= tk.Entry(master=top,background="#d9d9d9", textvariable= Burger, foreground="#c60000", selectbackground="#f2a343", font = font13)
        self.BurgerEntry1.place(relx=0.18, rely=0.42)
        self.BigEntry1= tk.Entry(master=top,background="#d9d9d9", textvariable= Big, foreground="#c60000", selectbackground="#f2a343", font = font13)
        self.BigEntry1.place(relx=0.18, rely=0.5)
        self.RoyalEntry1= tk.Entry(master=top,background="#d9d9d9", textvariable= Royal, foreground="#c60000", selectbackground="#f2a343", font = font13)
        self.RoyalEntry1.place(relx=0.18, rely=0.58)
        self.VegEntry1= tk.Entry(master=top,background="#d9d9d9", textvariable= Veg, foreground="#c60000", selectbackground="#f2a343", font = font13)
        self.VegEntry1.place(relx=0.18, rely=0.66)
        self.DrinksEntry1= tk.Entry(master=top,background="#d9d9d9", textvariable= Drinks, foreground="#c60000", selectbackground="#f2a343", font = font13)
        self.DrinksEntry1.place(relx=0.18, rely=0.73)

        #________________________________________Clac____
        self.screm = tk.StringVar()

        def expression(bnt):
            toto = self.screm.get()+bnt
            self.screm.set(toto)
        
        def signe(btn):
            if self.screm.get() !="":
                operator =self.screm.get()
                lastnbr=len(operator)-1
                if operator[lastnbr] not in "+-*/." :
                    self.screm.set(operator+btn)
                else :
                    alafia=operator[:lastnbr] + btn + operator[lastnbr+1:]
                    self.screm.set(alafia)

#_________________________ split in table ______________
        def calcul(Writen):
            index=0
            self.elementos=[]
            for x in range(len(Writen)) :
                if Writen[x] in "+-*/" and x != 0:
                    posit=x
                    self.elementos.append(Writen[index:posit])
                    self.elementos.append(Writen[x])
                    index=posit+1
            self.elementos.append(Writen[index:])

#________________ define the expression calculation _______________
        def verif():
                if "-" in self.screm.get() and self.screm.get().rfind("-") != 0 or "+" in self.screm.get() or "/" in self.screm.get() or "*" in self.screm.get() :
                    return True
                else:
                    return False
        def egal():
            
            if verif() :
                calcul(self.screm.get())
# multiplication and division, precedence: whichever comes first from left to right
                while ("*" in self.elementos or "/" in self.elementos):
                    index = 0
                    for element in self.elementos:
                   
                        if (element == '*'):
                            index1 = self.elementos.index(element)
                            v1 = float(self.elementos[index1 - 1])
                            v2 = float(self.elementos[index1 + 1])
                            result = str(v1 * v2)
                            self.elementos[index] = result
                            self.elementos.pop(index1 + 1)
                            self.elementos.pop(index1 - 1)
                            index += 1
                            break
                        elif (element == '/'):
                            index1 = self.elementos.index(element)
                            v1 = float(self.elementos[index1 - 1])
                            v2 = float(self.elementos[index1 + 1])
                            result = str(v1 / v2)
                            self.elementos[index] = result
                            self.elementos.pop(index1 + 1)
                            self.elementos.pop(index1 - 1)
                            index += 1
                            break
                        else:
                            index += 1
# addition and subtraction
# Repeat until just about the result
                while (len(self.elementos) > 1):
                    index = 0
                    for element in self.elementos:
                    
                        if (element == '+'):
                            index1 = self.elementos.index(element)
                            v1 = float(self.elementos[index1 - 1])
                            v2 = float(self.elementos[index1 + 1])
                            result = str(v1 + v2)
                            self.elementos[index] = result
                            self.elementos.pop(index1 + 1)
                            self.elementos.pop(index1 - 1)
                            index += 1
                            break
                        if (element == '-'):
                            index1 = self.elementos.index(element)
                            v1 = float(self.elementos[index1 - 1])
                            v2 = float(self.elementos[index1 + 1])
                            result = str(v1 - v2)
                            self.elementos[index] = result
                            self.elementos.pop(index1 + 1)
                            self.elementos.pop(index1 - 1)
                            index += 1
                            break
                        else:
                            index += 1
                final_result = str( round( float(self.elementos[0]), 2 ) )
#include the result in the display
                self.screm.set(final_result)
            else :
                self.screm.set("")


        self.scremEntry = tk.Entry(master=top, background='#d9d9d9',textvariable=self.screm,foreground="#c60000",state="readonly",selectbackground="#f2a343",font= font13)
        self.scremEntry.place(relx = 0.705, rely=0.24, height=35,relwidth= 0.267)

        self.Button1 = tk.Button(master=top, text='''7''', background='#122c63', font = font14, foreground='#ffffff', borderwidth='0', command=lambda : expression("7"))
        self.Button1.place(relx=0.705, rely=0.34, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''8''', background='#122c63', font = font14, foreground='#ffffff', borderwidth='0', command=lambda : expression("8"))
        self.Button1.place(relx=0.780, rely=0.34, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''9''', background='#122c63', font = font14, foreground='#ffffff', borderwidth='0', command=lambda : expression("9"))
        self.Button1.place(relx=0.856, rely=0.34, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''/''', background='#122c63', font = font14, foreground='#ffffff', borderwidth='0', command=lambda : signe("/"))
        self.Button1.place(relx=0.934, rely=0.34, height=44, width=37)

        self.Button1 = tk.Button(master=top, text='''4''', background='#122c63', font = font14, foreground='#ffffff', borderwidth='0', command=lambda : expression("4"))
        self.Button1.place(relx=0.705, rely=0.44, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''5''', background='#122c63', font = font14, foreground='#ffffff', borderwidth='0', command=lambda : expression("5"))
        self.Button1.place(relx=0.780, rely=0.44, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''6''', background='#122c63', font = font14, foreground='#ffffff', borderwidth='0', command=lambda : expression("6"))
        self.Button1.place(relx=0.856, rely=0.44, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''*''', background='#122c63', font = font14, foreground='#ffffff', borderwidth='0', command=lambda : signe("*"))
        self.Button1.place(relx=0.934, rely=0.44, height=44, width=37)

        self.Button1 = tk.Button(master=top, text='''1''', background='#122c63', font = font14, foreground='#ffffff', borderwidth='0', command=lambda : expression("1"))
        self.Button1.place(relx=0.705, rely=0.54, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''2''', background='#122c63', font = font14, foreground='#ffffff', borderwidth='0', command=lambda : expression("2"))
        self.Button1.place(relx=0.780, rely=0.54, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''3''', background='#122c63', font = font14, foreground='#ffffff', borderwidth='0', command=lambda : expression("3"))
        self.Button1.place(relx=0.856, rely=0.54, height=44, width=67)
        self.Button1 = tk.Button(master=top, text='''-''', background='#122c63', font = font14, foreground='#ffffff', borderwidth='0', command=lambda : signe("-"))
        self.Button1.place(relx=0.934, rely=0.54, height=44, width=37)

        self.Button1 = tk.Button(master=top, text='''0''', background='#122c63', font = font14, foreground='#ffffff', borderwidth='0', command=lambda : expression("0"))
        self.Button1.place(relx=0.705, rely=0.64, height=35, width=146)
        self.Button1 = tk.Button(master=top, text='''.''', background='#122c63', font = font14, foreground='#ffffff', borderwidth='0', command=lambda : signe("."))
        self.Button1.place(relx=0.856, rely=0.64, height=35, width=67)
        self.Button1 = tk.Button(master=top, text='''+''', background='#122c63', font = font14, foreground='#ffffff', borderwidth='0', command=lambda : signe("+"))
        self.Button1.place(relx=0.934, rely=0.64, height=35, width=37)

        self.Button1 = tk.Button(master=top, text='''=''', background='#f2a343', font = font14, foreground='#ffffff', borderwidth='0', command=egal)
        self.Button1.place(relx=0.705, rely=0.72, height=34, width=272)

        #____ Cost ____
        self.Label12 = tk.Label(master=top, text="Cost :", foreground="#e16740", font=font12, background="#091833")
        self.Label12.place(relx=0.40, rely=0.32)

        self.Label12 = tk.Label(master=top, text="Service Charge :", foreground="#bac8bd", font=font12, background="#091833")
        self.Label12.place(relx=0.35, rely=0.4)
        self.Label12 = tk.Label(master=top, text="Tax :", foreground="#bac8bd", font=font12, background="#091833")
        self.Label12.place(relx=0.40, rely=0.48)
        self.Label12 = tk.Label(master=top, text="Subtotal :", foreground="#bac8bd", font=font12, background="#091833")
        self.Label12.place(relx=0.38, rely=0.56)
        self.Label12 = tk.Label(master=top, text="Total :", foreground="#bac8bd", font=font12, background="#091833")
        self.Label12.place(relx=0.40, rely=0.64 )

        #___ Entry Cost ___
        self.CostEntry13= tk.Entry(master=top,background="#d9d9d9", textvariable= Cost, foreground="#c60000", selectbackground="#f2a343", font = font13)
        self.CostEntry13.place(relx=0.467, rely=0.33)
        self.ServiceEntry13= tk.Entry(master=top,background="#d9d9d9", textvariable= Service, foreground="#c60000", selectbackground="#f2a343", font = font13)
        self.ServiceEntry13.place(relx=0.516, rely=0.41, relwidth=0.111)
        self.TaxEntry13= tk.Entry(master=top,background="#d9d9d9", textvariable= Tax, foreground="#c60000", selectbackground="#f2a343", font = font13)
        self.TaxEntry13.place(relx=0.467, rely=0.5)
        self.SubtotalEntry13= tk.Entry(master=top,background="#d9d9d9", textvariable= Subtotal, foreground="#c60000", selectbackground="#f2a343", font = font13)
        self.SubtotalEntry13.place(relx=0.479, rely=0.57, relwidth=0.146)
        self.TotalEntry13= tk.Entry(master=top,background="#d9d9d9", textvariable= Total, foreground="#c60000", selectbackground="#f2a343", font = font13)
        self.TotalEntry13.place(relx=0.466, rely=0.65)

        #____ Control Button ____
        self.Button2 = tk.Button(master=top, text="PRICE", background="#e16740", font=font16, command=Price)
        self.Button2.place(relx=0.039, rely=0.86, height=34, width=107)
        self.Button2 = tk.Button(master=top, text="TOTAL", background="#e16740", font=font16, command=Totale)
        self.Button2.place(relx=0.156, rely=0.86, height=34, width=107)
        self.Button2 = tk.Button(master=top, text="RESET", background="#e16740", font=font16, command=Reset)
        self.Button2.place(relx=0.272, rely=0.86, height=34, width=107)
        self.Button2 = tk.Button(master=top, text="EXIT", background="#e16740", font=font16, command=iExit)
        self.Button2.place(relx=0.389, rely=0.86, height=34, width=107)

        #++++++++++++++++++++++++++++++ Functions ++++++++++++++++++++++++



#Prevents the window from disappearing
root = tk.Tk()
my_gui= RestaurantApp(root)
root.mainloop()
