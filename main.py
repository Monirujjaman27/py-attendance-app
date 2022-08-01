from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image 
class St_Attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x750+0+0")        
        self.root.title("Student Menagement")
        # self.root.iconbitmap("logo.ico")


        headerImg = Image.open("img/education.jpg")
        headerImg=headerImg.resize((1500,150),Image.ANTIALIAS)
        self.headerImage = ImageTk.PhotoImage(headerImg)
        f_label = Label(self.root,image=self.headerImage)
        f_label.grid(row=0, column=0) 

        # button 
        b1 = Button      



if __name__ == "__main__":
    root=Tk()
    obj=St_Attendence(root)
    root.mainloop()
