import tkinter

class BMI(tkinter.Tk):

  def __init__(self, parent):
    tkinter.Tk.__init__(self,parent)
    self.parent = parent
    self.initialize()

  def initialize(self):
    self.grid()

    self.Label1 =tkinter.Label(self, text='Enter Height(centimeters) : ')
    self.Label1.grid(column=0,row=0,padx=10,pady=10,sticky='EW') 
  
    self.entryVar1 = tkinter.StringVar()
    self.entry1 = tkinter.Entry(self, textvariable = self.entryVar1)
    self.entry1.grid(column = 1, row = 0,padx=10,pady=10, sticky = 'EW')
    self.entry1.bind("<Return>", self.forTab)
    
    self.label2 = tkinter.Label(self,text="Enter Weight(Kilograms) : ")
    self.label2.grid(column = 0, row = 1,pady=10, padx=10, sticky = 'EW') 

    self.entryVar2 = tkinter.StringVar()    
    self.entry2 = tkinter.Entry(self, textvariable = self.entryVar2)
    self.entry2.grid(column = 1, row = 1,padx=10,pady=10, sticky = 'EW')
    self.entry2.bind("<Return>", self.OnButtonClick)

    button = tkinter.Button(self, text = u"Calculate")
    button.grid(column = 0, row = 2,pady=10,padx=10)
    button.bind("<Button-1>",self.OnButtonClick)

    self.label3 = tkinter.Label(self, text="Answer : ") 
    self.label3.grid(column = 0, row = 3,pady=10,padx=10, sticky = 'EW')

    self.labelVar = tkinter.StringVar()
    label = tkinter.Label(self, textvariable = self.labelVar, bg = "black", fg = "white")
    label.grid(column = 1, row = 3,pady=10,padx=10)
    self.labelVar.set(u"-")

    self.label4 = tkinter.Label(self, text="Classification : ") 
    self.label4.grid(column = 0, row = 4,pady=10,padx=10, sticky = 'EW')

    self.labelVar2 = tkinter.StringVar()
    label2 = tkinter.Label(self, textvariable = self.labelVar2, bg = "black", fg = "white")
    label2.grid(column = 1, row = 4,pady=10,padx=10)
    self.labelVar2.set(u"-")

    self.resizable(False,False)
    self.entry1.focus_set() #This sets the cursor to first entry at initial program runtime

#This function is used when user is on second entry and press ENTER or user clicks calculate, this is the main function of the app.
  def OnButtonClick(self, event):
    ht = float(self.entryVar1.get())
    ht /= 100
    wt = float(self.entryVar2.get())
    bmi = float(wt/(ht*ht))
    self.labelVar.set(u"%.2f (kg/m\u00B2)"%bmi)
    if bmi<16.00:
      self.labelVar2.set("Severe thinness")
    elif bmi>=16.00 and bmi<17.00:
      self.labelVar2.set("Moderate thinness")    
    elif bmi>=17.00 and bmi<18.49:
      self.labelVar2.set("Mild thinness")
    elif bmi>=18.50 and bmi<25.00:
      self.labelVar2.set("Normal Range")
    elif bmi>=25.00 and bmi<30.00:
      self.labelVar2.set("Pre-obese")
    elif bmi>=30.00 and bmi<35.00:
      self.labelVar2.set("Pre-obese I")
    elif bmi>=35.00 and bmi<40.00:
      self.labelVar2.set("Pre-obese II")
    else:
      self.labelVar2.set("Pre-obese III")

#This funtion acts as a funtionality when person clicks enter on first entry it takes it as tab and move to next entry
  def forTab(self, event):
    self.entry2.focus_set()
    

if __name__ == "__main__":
  app = BMI(None)
  app.title("BMI Calculator")
  app.mainloop()
