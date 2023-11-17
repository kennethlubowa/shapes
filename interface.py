from tkinter import *
from functions import Start

startwindow=Tk()     #will instantiate the window

startwindow.geometry("500x500")  #specifies the window size

startwindow.title("KALC U LATER") #specifies title

#ANYNAME = PhotoImage(file='ENTER PATH TO THE IMAGE') #adds image 

# window=iconphoto(True,ANYNAME)specifies logo for window

startwindow.config(background="brown")#specifies colour of the background


welcomelabel=Label(
            startwindow, text="welcome!", #text in the label
            
            font=('arial',40,'bold'),#type size,style
            
            fg='yellow', #foreground(colour of the words)
            
            bg='grey', #background(colour of label)
            
            bd='10', #body(size of the label)
            
            relief=RAISED,
            
            padx=10, #padding from x or y axes
            
            pady=10,
            
            #image=ANYNAME  adds image to the label
            
            #compound='bottom'  specifies where the image should be
            
            ) #creates a label in the window

welcomelabel.pack() #adds the label to the window


startbutton=Button(
            startwindow, text="START",command=Start, #text in the label
            
            font=('times new roman',60,'italic'),#type size,style
            
            fg='green', #foreground(colour of the words)
            
            bg='navyblue', #background(colour of label)
            
            activebackground='navyblue',
                                #to prevent flickering on click
            activeforeground='green',
            
            bd='20', #body(size of the label)
            
            relief=RAISED,
            
            padx=20, #padding from x or y axes
            
            pady=20,
            
            #image=ANYNAME  adds image to the label
            
            #compound='bottom'  specifies where the image should be
            
            ) #creates a label in the window

startbutton.pack() #adds the label to the window

startbutton.place(x=60,y=100) #specifies location of label in the window


startwindow.mainloop()#will show window on the screen & listen for events