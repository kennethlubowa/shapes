from tkinter import*

calc = ["PERIMETER/CIRCUMFERENCE","AREA","VOLUME"]

lat = Tk()

x = IntVar()

for index in range(len(calc)):
    radiobutton = Radiobutton(lat,
                            text=calc[index], #adds text to radiobuttons
                            variable=x, #groups radiobuttond together if they share the
                            value=index, #assignds each radiobutton a different value
                            padx=25,
                            font=("impact",30),
                            indicatoron=0, #eliminates circle indicators
                            width=100 #sets width of the push buttons
                            )
    radiobutton.pack(anchor=W) #could also be 'w'(not capital) meaning west


lat.mainloop()