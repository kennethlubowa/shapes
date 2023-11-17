from tkinter import *
#_________________________________________________________________________________
def Submit():
    selected = choice.get()
    print(selected)
#______________________________________________________________________________    
choicewindow=Tk()
choicewindow.geometry("500x500")
choicewindow.title("KALC U LATER")

choicedirective=Label(
            choicewindow, text="SELECT SHAPE",font=('arial',40,'bold'),fg='yellow',   bg='grey',bd='10',relief=RAISED,padx=10,pady=10,
            )
choicedirective.pack()

choices=Label(
            choicewindow, text="\n1.SQUARE\n\n2.RECTANGLE\n\n3.RHOMBUS\n\n4.PARALLELOGRAM\n\n5.TRAPEZIUM\n\n6.KITE\n\n7.CUBE\n\n8.CUBOID\n\n9.CIRCLE\n\n10.CYLINDER\n\n11.TRIANGLE\n",font=('times new roman',10,'italic',),fg='dark green',bg='sky blue',relief=SUNKEN,padx=150,pady=0,
            )
choices.place(x=0,y=0)
choices.pack() 

choice = Entry(         #where i will be selecting shape
    choicewindow,
    font=('times new roman',20,'bold'),fg='purple',bg='violet',bd='5',relief=SUNKEN,
    )

choice.pack(side=LEFT)

enter = Button(         #to submit the selected shape
    choicewindow,
    text="ENTER",font=('arial',20,'bold'),fg='indigo',bg='dark green',bd='10',relief=RAISED,
    command=Submit
    )
enter.pack(side=RIGHT)
choicewindow.mainloop()

