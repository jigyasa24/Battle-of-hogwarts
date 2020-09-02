from tkinter import *   
  
top = Tk()  
  
top.geometry("760x560")  

#creating a simple canvas  
c = Canvas(top,bg = "brown",height = "760",width = 1560)  

photo = PhotoImage(file= 'C:\\Users\\HP\\Desktop\\boh.PNG')

c.create_image(0,0, image= photo, anchor = NW)

def about():
    messagebox.showinfo("About the game?", "* This game works sort of like chess. You have to move all the pieces according to the rules and fight till one of the king's i.e.in our case either voldemort or harry falls. The rules for the movement of the pieces have been clearly instructed in the rules panel. Have a good game :)")

def Rules():
    messagebox.showinfo("Rules of the game:", "* Snake can move in any diagonal direction for any number of blocks. \n\n Voldemort and harry can move in any direction for 2 steps. \n\n Neville can also move in a diagonal direction. \n\n Bellatrix and stag can move in any direction for any number of steps.")    
    
def createNewWindow():
    cv = Canvas(top,bg = "brown",height = "400",width = 650)  
    cv.pack()

    photo = PhotoImage(file='C:\\Users\\HP\\Downloads\\Aboutbo.png')

    cv.create_image(0,0, image=photo, anchor=NW)

    root.mainloop()
    

bluebutton = Button(top, text = "Rules",command = Rules,fg = "black", height = "1",width = 30 ).place(x = 656,y = 400)
bluebutton = Button(top, text = "Single Player",command = createNewWindow,fg = "black", height = "1",width = 30 ).place(x = 656,y = 460)
bluebutton = Button(top, text = "Multi Player",fg = "black", height = "1",width = 30 ).place(x = 656,y = 520)

bluebutton = Button(top, text = "Share",fg = "black", height = "1",width = 5 ).place(x = 656,y = 640)

bluebutton = Button(top, text = "About",command = about,fg = "black", height = "1",width = 5 ).place(x = 738,y = 640)

bluebutton = Button(top, text = "Settings",fg = "black", height = "1",width = 5 ).place(x = 832,y = 640)

Label(top, text = 'Battle of hogwarts',fg = "white",bg = "black",font =( 
  'Algerian', 20)).place(x = 620,y = 200)

c.pack()  
  
top.mainloop()
