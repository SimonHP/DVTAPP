from tkinter import *
from tkinter import ttk 

import webbrowser

#from PIL import ImageTk, Image
root = Tk()
root.title ("L-Trip Score")
root.geometry("600x600")

#scroll

main_frame = Frame (root)
main_frame.pack(fill=BOTH, expand=1)

my_canvas = Canvas (main_frame)
my_canvas.pack(side = LEFT, fill=BOTH, expand = 1)

my_scrollbar = ttk.Scrollbar(main_frame, orient = VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side = RIGHT, fill = Y)
#name entry
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all") ))

second_frame = Frame(my_canvas)

my_canvas.create_window((0,0), window = second_frame, anchor = ("nw"))

#introduction

introLabel = Label(second_frame, text=" The L-TRIP (cast) score is useful to assess risk of thrombosis in patients with lower limb trauma requiring orthopaedic immobilisation")
introLabel.grid(column=0, row=1, padx=5, pady=5, columnspan=8, sticky=W,)

# warning label

warningLabel = Label(second_frame, text=" Patients with a history of DVT/PE or thrombophilia or achilles rupture should be considered high risk", fg="red", font=('Times New Roman', 20, 'bold'))

warningLabel.grid(column=0, row=2, padx=5, pady=5, columnspan=8, sticky=W )


#command

courseLabel = Label(second_frame, text="Enter the following data on an individual patient")
courseLabel.grid(column=0, row=3, padx=5, pady=20, columnspan=6, sticky=W)


#questions

agevar = IntVar()
age2var  = IntVar()
malevar = IntVar()
ocpvar = IntVar()
canvar = IntVar()
pregvar = IntVar()
BMIvar = IntVar()
BMI2var = IntVar()
pneumvar = IntVar()
famhisvar = IntVar()
covar = IntVar()
hovar = IntVar()
bedvar = IntVar()
surgvar = IntVar()
supvar = IntVar()
popcomvar = IntVar()
popcircvar = IntVar()
popfootvar = IntVar()
poplegvar = IntVar()
fhvar2 = IntVar()


scorepd = IntVar()
scorepd = ''

age = Label(second_frame, text=" Age>/=35 and </=55 years")
age.grid(column=0, row=4, padx=5, pady=5, sticky =W, columnspan=1)
R1 = Checkbutton(second_frame, variable=agevar, onvalue=2)
R1.grid(column=2, row=4, padx=5, pady=20, sticky=W, columnspan=1)

age2 = Label(second_frame, text=" Age >/=55 years")
age2.grid(column=0, row=5, padx=5, pady=5, sticky =W, columnspan=6)
R2 = Checkbutton(second_frame, variable=age2var, onvalue=3)
R2.grid(column=2, row=5, padx=5, pady=20, sticky=W, columnspan=6)

male = Label(second_frame, text=" Male sex")
male.grid(column=0, row=6, padx=5, pady=5, sticky =W, columnspan=6)
R3= Checkbutton(second_frame, variable=malevar, onvalue=1)
R3.grid(column=2, row=6, padx=5, pady=20, sticky=W, columnspan=6)

ocp = Label(second_frame, text="Current use of oral contraceptives")
ocp.grid(column=0, row=7, padx=5, pady=5,sticky=W, columnspan=6)
R4= Checkbutton(second_frame, variable=ocpvar, onvalue=4)
R4.grid(column=2, row=7, padx=5, pady=20,sticky=W, columnspan=6)

cancer = Label(second_frame, text="Cancer within the past 5 years")
cancer.grid(column=0, row=8, padx=5, pady=5, sticky =W, columnspan=6)
R5= Checkbutton(second_frame, variable=canvar, onvalue=3)
R5.grid(column=2, row=8, padx=5, pady=20, sticky=W, columnspan=6)

pregnancy = Label(second_frame, text="Pregnancy or puerperium")
pregnancy.grid(column=0, row=9, padx=5, pady=5, sticky =W, columnspan=6)
R6= Checkbutton(second_frame, variable=pregvar, onvalue=3)
R6.grid(column=2, row=9, padx=5, pady=20, sticky=W, columnspan=6)

BMI = Label(second_frame, text="BMI>/=25 and < 35 kg/m2")
BMI.grid(column=0, row=10, padx=5, pady=5, sticky =W, columnspan=6)
R7= Checkbutton(second_frame, variable=BMIvar, onvalue=1)
R7.grid(column=2, row=10, padx=5, pady=20, sticky=W, columnspan=6)

BMI2 = Label(second_frame, text="BMI>/= 35 kg/m2")
BMI2.grid(column=0, row=11, padx=5, pady=5, sticky =W, columnspan=6)
R8= Checkbutton(second_frame, variable=BMI2var, onvalue=2)
R8.grid(column=2, row=11, padx=5, pady=20, sticky=W, columnspan=6)

FH = Label(second_frame, text="Family History of VTE (first degree relative)")
FH.grid(column=0, row=12, padx=5, pady=5, sticky =W, columnspan=6)
R19= Checkbutton(second_frame, variable=fhvar2, onvalue=2)
R19.grid(column=2, row=12, padx=5, pady=20, sticky=W, columnspan=6)



co = Label(second_frame, text="Comorbidity (RA, CKD, COPD, MS)")
co.grid(column=0, row=13, padx=5, pady=5, sticky =W, columnspan=6)
R9= Checkbutton(second_frame, variable=covar, onvalue=1)
R9.grid(column=2, row=13, padx=5, pady=20, sticky=W, columnspan=6)

ho = Label(second_frame, text="Hospital admission within past 3 months")
ho.grid(column=0, row=14, padx=5, pady=5, sticky =W, columnspan=6)
R10= Checkbutton(second_frame, variable=hovar, onvalue=2)
R10.grid(column=2, row=14, padx=5, pady=20, sticky=W, columnspan=6)

bed = Label(second_frame, text="Bedridden within past 3 months")
bed.grid(column=0, row=15, padx=5, pady=5, sticky =W, columnspan=6)
R11= Checkbutton(second_frame, variable=bedvar, onvalue=2)
R11.grid(column=2, row=15, padx=5, pady=20, sticky=W, columnspan=6)

surg = Label(second_frame, text="Surgery within past 3 months")
surg.grid(column=0, row=16, padx=5, pady=5, sticky =W, columnspan=6)
R12= Checkbutton(second_frame, variable=surgvar, onvalue=2)
R12.grid(column=2, row=16, padx=5, pady=20, sticky=W, columnspan=6)

sup = Label(second_frame, text="History of superficial vein thrombosis")
sup.grid(column=0, row=17, padx=5, pady=5, sticky =W, columnspan=6)
R13= Checkbutton(second_frame, variable=supvar, onvalue=3)
R13.grid(column=2, row=17, padx=5, pady=20, sticky=W, columnspan=6)

popcom = Label(second_frame, text="Plaster cast: complete leg")
popcom.grid(column=0, row=18, padx=5, pady=5, sticky =W, columnspan=6)
R14= Checkbutton(second_frame, variable=popcomvar, onvalue=5)
R14.grid(column=2, row=18, padx=5, pady=20, sticky=W, columnspan=6)

popcirc = Label(second_frame, text="Plaster cast: cylinder knee cast (ankle free)")
popcirc.grid(column=0, row=19, padx=5, pady=5, sticky =W, columnspan=6)
R15= Checkbutton(second_frame, variable=popcircvar, onvalue=2)
R15.grid(column=2, row=19, padx=5, pady=20, sticky=W, columnspan=6)

popfoot = Label(second_frame, text="Plaster cast: foot only ")
popfoot.grid(column=0, row=20, padx=5, pady=5, sticky =W, columnspan=6)
R16= Checkbutton(second_frame, variable=popfootvar, onvalue=2)
R16.grid(column=2, row=20, padx=5, pady=20, sticky=W, columnspan=6)

popleg = Label(second_frame, text="Plaster cast: below knee")
popleg.grid(column=0, row=21, padx=5, pady=5, sticky =W, columnspan=6)
R17= Checkbutton(second_frame, variable=poplegvar, onvalue=4)
R17.grid(column=2, row=21, padx=5, pady=20, sticky=W, columnspan=6)

#score and reset button


def scorepd():
    
    global scorepd
    scorepd = agevar.get() + age2var.get() + malevar.get() + ocpvar.get() + canvar.get() + pregvar.get() + BMIvar.get() + BMI2var.get() + pneumvar.get() + fhvar2.get() + covar.get() + hovar.get() + supvar.get() + popcomvar.get()+ popcircvar.get() + popfootvar.get() + poplegvar.get()
    scorepd = str(scorepd)
    result = "The L-Trip score score is " + scorepd
    label.config(text = result)
    label2.config(text = "If score is > 8 , patient is considered high risk for thrombosis, consider thromboprophylaxis")

def reset():
    
    R1.deselect()
    R2.deselect()
    R3.deselect()
    R4.deselect()
    R5.deselect()
    R6.deselect()
    R7.deselect()
    R8.deselect()
    R9.deselect()
    R10.deselect()
    R11.deselect()
    R12.deselect()
    R13.deselect()
    R14.deselect()
    R15.deselect()
    R16.deselect()
    R17.deselect()
    R19.deselect()
    
    
def func1(*funcs):
    
    def inner_combined_func(*args, **kwargs): 
        for f in funcs: 
  
            # Calling functions with arguments, if any 
            f(*args, **kwargs) 
  
    # returning the reference of inner_combined_func 
    # this reference will have the called result of all 
    # the functions that are passed to the combined_funcs 
    return inner_combined_func 


calButton = Button(second_frame, text = "show L-Trip score", fg="red",highlightbackground = "yellow", command=scorepd, padx=50, pady=20, )
calButton.grid(column=0, row=22, padx=10, pady=20, sticky = W,columnspan=1)

label = Label(second_frame, fg="red",font=('Times New Roman', 25, 'bold'))
label.grid(column=0, row=23, padx=10, pady=0, sticky=  W, columnspan=1)

label2 = Label(second_frame, font=('Times New Roman', 10, 'bold'))
label2.grid(column=0, row=24, padx=10, pady=0, sticky=  W, columnspan=1)


resetButton = Button(second_frame, text = "reset", fg="red",command=func1(reset, scorepd), padx=50, pady=20, )
resetButton.grid(column=0, row=25, padx=10, pady=20,sticky= W, columnspan=1)

new = 1
url = "https://forms.gle/8UaE1oqxNMfCVMok6"

def openweb():
    webbrowser.open(url,new=new)

feedbackButton = Button(second_frame, text = "feedback please", fg="red",command=openweb, padx=50, pady=20, )
feedbackButton.grid(column=0, row=26, padx=10, pady=20,sticky= W, columnspan=1)


url2 = "https://dial.uclouvain.be/pr/boreal/object/boreal%3A252006/datastream/PDF_01/view"

def openweb2():
    webbrowser.open(url2,new=new)

accesspaperButton = Button(second_frame, text = "Click HERE for access to L-Trip paper", fg="red",command=openweb2, padx=10, pady=10, font=('Times New Roman', 10, 'bold'))
accesspaperButton.grid(column=0, row=27, padx=5, pady=20,sticky= W, columnspan=1)

copywrightLabel = Label(second_frame, text="Created by Simon H Palmer FRCS", font=('Times New Roman', 10))
copywrightLabel.grid(column=0, row=28, padx=30, pady=20, columnspan=6, sticky=W)


root.mainloop()