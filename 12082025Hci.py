from tkinter import*
from tkinter import messagebox
app=Tk()
app.title("Myapp")
app.geometry("500x500")
#adding an image to the background
image=PhotoImage(file="/home/ubuntu/Downloads/2021-BMW-M4-Competition-001(1).png") #change this to the actual path of the image in your computer
label2=Label(app,image=image)
label2.pack()
label2.image=image
#creating message box syntax =messagebox.function_name(title,text) 
messagebox.showinfo("Important","This is a info message box")  #using info function
messagebox.showerror("ERROR","ERROR 404:NOT FOUND") #USING ERROR FUNCTION
messagebox.showwarning("WARNING!","This may cause harm to your system") #using warning function
messagebox.askquestion("Select an option","Do you see the image at the background?") #using askquestion function
messagebox.askokcancel("CHECK","You sure you want to continue?") #using askokcancel function
messagebox.askyesno("YES/NO","Do you see the image at the background?") #using askyesno function
#using widget message
app1=Toplevel(app) #made app1 child of app
app1.title("Myapp1")
app1.geometry("500x600")
var=StringVar()
msg=Message(app1,text="NOTHING TO SEE HERE",font=("Aerial",10),fg="blue",bg="green")
# msg.pack(side=LEFT) we can use pack with the message
msg.place(x=40,y=20)
# app1.mainloop() as we made app1 a child of app no need to do mainloop twice
#using canvas to make a reversed swastika
canvas=Canvas(app1,width=500,height=500)
canvas.pack()
#the syntax for create_line() function is   
canvas.create_line(50,50,450,450,fill="red",width=5)
canvas.create_line(450,50,50,450,fill="red",width=5)
canvas.create_line(50,450,450,50,fill="red",width=5)
canvas.create_line(450,450,50,50,fill="red",width=5)
#using checkbutton
var=IntVar()
checkbutton=Checkbutton(app1,text="Select me",variable=var,onvalue=1,offvalue=0)
checkbutton.place(x=40,y=100)


app.mainloop()

