#creating  a window
from tkinter import*
app=Tk()
# app.mainloop()
#giving title/name to app/window
app.title("GUIAPP")
#changing the size of the window/app
app.geometry("500x500")
#adding buttons to the window/app
# button1=Button(app,text="Click me",fg="cyan",bg="grey")  #use bg  to add color to the button background
# button1.pack(side=LEFT)
# button2=Button(app,text="Click me not",fg="green",activebackground="green") #use activebackground to change the color of the button when hovered on
# button2.pack(side=RIGHT)
#changing the color of whole window
app.configure(bg="black")
#organizing the buttons in tabular form using the grid method
button3=Button(app,text="BUTTON 1",fg="red",bg="blue")
button3.grid(row=0,column=0,padx=20,pady=20)  #padx and pady adds padding to the button/widget
button4=Button(app,text="BUTTON 2 ",fg="yellow",bg="purple")
button4.grid(row=0,column=1)
button5=Button(app,text="BUTTON 3",fg="blue",bg="red")
button5.grid(row=1,column=0)
button6=Button(app,text="BUTTON 4",fg="green",bg="cyan")
button6.grid(row=3,column=0)
#WE CAN ONLY USE GRID OR PACK METHOD NOT BOTH

#TRYING RUNNING MULTIPLE WINDOWS IN ONE PROGRAM
app2=Tk()
app2.title("SECOND GUIAPP")
app2.geometry("500x700")
app2.configure(bg="white")
button7=Button(app2,text="BUTTON 1",fg="blue",bg="green")
button7.pack(side=LEFT)

#USING THE LABEL ON APP2
label1=Label(app2,text="THIS IS A LABEL",fg="Green",bg="cyan")
label1.pack(side=TOP)

#Creating a new window/app and adding a image to the background
app3=Toplevel()   #always use top level for extra windows
app3.title("THIRD GUIAPP")
app3.geometry("1600x900")
app3.configure(bg="black")
#adding an image to the background
image=PhotoImage(file="/home/ubuntu/Downloads/Screenshot from 2025-08-05 10-32-39.png") #change this to the actual path of the image in your computer
label2=Label(app3,image=image)
label2.pack()
label2.image=image
app3.mainloop()
app.mainloop()
app2.mainloop()
