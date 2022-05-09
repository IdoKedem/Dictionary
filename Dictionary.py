from tkinter import *
from tkinter import messagebox
import random

dic = {}

def add():

    org = orgEntry.get()

    tran = tranEntry.get()

    dic[org] = tran

    tranEntry.delete(0,END)
    orgEntry.delete(0,END)
def pMain():

    clear()

    title.grid(row = 0, column = 0)

    kList = list(dic)
    random.shuffle(kList)
 
    practiceEntry.grid(row = 2 , column = 0)

    labPractice = Label(app, text = "Enter translation for: " + kList[app.i],font = ("lucida", 16) )
    labPractice.grid(row = 1 , column = 0, padx = 170)

    practiceBtn = Button(app, text = "Check", width = 12, height = 2, command = lambda : check(kList,labPractice,practiceEntry.get()))
    practiceBtn.grid(row = 3 , column = 0, pady = 5)

def clear():

    labOrg.place_forget()
    labTran.place_forget()
    orgEntry.place_forget()
    tranEntry.place_forget()
    save.place_forget()
    train.place_forget()
    title.place_forget()
      
def check(kList, labPractice, entered):

    answer = dic[kList[app.i]]

    if ( entered== dic[kList[app.i]] ) and ( app.i!=len(kList)-1 ):    #right and not last item 

        labWrong.grid_remove()

        app.i+=1

        labPractice.config(text="Enter translation for: " + kList[app.i])

        practiceEntry.delete(0,END)

        labCorrect.grid(row = 5, column = 0)
    
    elif (entered== dic[kList[app.i]]) and (app.i==len(kList)-1):       #right and last item
        labWrong.grid_remove()
        labCorrect.grid(row = 5, column = 0)

        qAgain = messagebox.askquestion("Finished", "Go again?")  

        if qAgain == "yes":         # restart

            app.i = 0

            pMain()

            labCorrect.grid_remove()
        else:            # finish
            messagebox.showinfo("Done", "All done")   

            app.destroy()


    else:                               # wrong
        labCorrect.grid_remove()
        labWrong.grid(row = 5, column = 0)

        qAnswer = messagebox.askquestion("Answer","Show answer?", icon = "error")

        if qAnswer == "yes":
            messagebox.showinfo("Answer","The answer is: " + answer)

app = Tk()
app.geometry('600x450+1200+60')
app.title("Dictionary")
app.resizable(height = 0, width = 0)

app.i =0

title = Label(app, text = "Dictionary", font = ("lucida", 23))
title.place(x = 229.5)

labOrg = Label(app, text = "Enter Word:", font = ("lucida",13))
labOrg.place(x = 10, y= 50)

labTran = Label(app, text = "Enter Translation:", font = ("lucida",13))
labTran.place(x = 10, y = 80)

orgEntry = Entry(app, bg = "#DCEEFF")
orgEntry.place(x = 110, y = 53)

tranEntry = Entry(app, bg = "#DCEEFF")
tranEntry.place(x = 145, y = 83)

save = Button(app, text = "Save to dictionary", width = 20, height = 3, command = add)
save.place(x = 297, y = 50)

train = Button(app, text = "Start practicing", width = 61, height = 2, command = pMain)
train.place(x = 10, y = 120)

practiceEntry = Entry(app, bg = "#E6DCFF")
labCorrect = Label(app, text = "Correct!" , fg = "green")
labWrong = Label(app, text = "Wrong" , fg = "red")

app.mainloop()