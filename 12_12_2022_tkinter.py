from tkinter import*
fb=Tk()
fb.title("Student form");
Label(fb,text="Student register id:").grid(row=0)
Label(fb,text="Student name:").grid(row=1)
Label(fb,text="Father name:").grid(row=2)
Label(fb,text="Group:").grid(row=3)
Label(fb,text="Phone number:").grid(row=4)
Label(fb,text="Email id:").grid(row=5)
Label(fb,text="Address:").grid(row=6)
Entry(fb).grid(row=0,column=1)
Entry(fb).grid(row=1,column=1)
Entry(fb).grid(row=2,column=1)
Entry(fb).grid(row=3,column=1)
Entry(fb).grid(row=4,column=1)
Entry(fb).grid(row=5,column=1)
Entry(fb).grid(row=6,column=1)
Button(fb,text="Submit").grid(row=7)
Button(fb,text="Cancel").grid(row=7,column=1)
mainloop()