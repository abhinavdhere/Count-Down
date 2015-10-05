#Countdown from specified date and time.
#Known bugs have been specified in the file bugs.txt

import Tkinter
from datetime import date
from datetime import datetime

class Count_app(Tkinter.Tk):
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent=parent
		self.initialize()

	def initialize(self):
		menuBar= Tkinter.Menu(self, relief="flat")
		FileMenu=Tkinter.Menu(menuBar, tearoff=0)
		FileMenu.add_command(label="New Count",command=self.new)
		FileMenu.add_separator()
		FileMenu.add_command(label="Save data",command=self.save)
		FileMenu.add_command(label="Load Count",command=self.load)
		FileMenu.add_separator()
		FileMenu.add_command(label="Exit",command=self.quit)
		HelpMenu=Tkinter.Menu(menuBar,tearoff=0)
		HelpMenu.add_command(label="About",command=self.about)
		menuBar.add_cascade(label="File", menu=FileMenu)
		menuBar.add_cascade(label="Help", menu=HelpMenu)
		self.config(menu=menuBar)
		self.resizable(False,False)

	def new(self):
		self.f1=Tkinter.Frame(self)
		self.f1.pack(anchor="w")	
		nameLabel=Tkinter.Label(self.f1,anchor="w",text="Name of event:  ")
		nameLabel.pack(anchor="w",side="top",pady=10)
		self.name=Tkinter.StringVar()	
		nameEntry=Tkinter.Entry(self.f1,textvariable=self.name,width=30)
		nameEntry.pack(anchor="w")
		STLabel=Tkinter.Label(self.f1,text="Event Date(dd mm yyyy):  ")
		STLabel.pack(anchor="w",side="top",pady=10)
		self.STime=Tkinter.StringVar()	
		STEntry=Tkinter.Entry(self.f1,textvariable=self.STime,width=30)
		STEntry.pack(anchor="w")
		button=Tkinter.Button(self.f1,text=u"Launch Countdown",command=self.OnClick)
		button.pack(side="top",pady=10)
	
	def OnClick(self):
		try:
			errorVar=Tkinter.StringVar()
			errorVar.set("")
			errorLabel=Tkinter.Label(self,anchor="center",textvariable=errorVar)
			errorLabel.pack(side="top",pady=10)
			setTime=list(map(int,self.STime.get().split()))
			self.f1.destroy()
			self.f1=Tkinter.Frame(self)
			self.f1.pack(anchor="w")
			eventName=self.name.get()
			Title=Tkinter.Label(self.f1,anchor="center",text="\tTime left for "+eventName)
			Title.pack()
			count=Tkinter.StringVar()
			countLabel=Tkinter.Label(self.f1,anchor="center",textvariable=count)
			countLabel.pack(side="top",pady=30)
			def update_label():
				count.set(self.getCount(setTime))
				countLabel.after(1000,update_label)
			update_label()
		except ValueError:
			errorVar.set("Invalid Input")	#How to delete this label when correct val given is a problem
			self.f1.destroy()
			self.new()

	def getCount(self,setTime):
		'''
		Calculates the time left
		'''
		curTime=datetime.now()
		b=datetime.today().date()
		a=date(setTime[2],setTime[1],setTime[0])
		sec=60-curTime.second
		minute=59-curTime.minute
		hour=23-curTime.hour
		res="\t"+str((a-b).days-1)+" days, "+str(hour)+" hours, "+str(minute)+" minutes, "+str(sec)+" seconds."
		return str(res)

	def save(self):
		'''
		Save the data pertaining to the name of event and date set so that user
		can load this data and get the counter running easily.
		'''
		#To be implemented
		pass

	def load(self):
		'''
		Load a previously saved counter for a date and event.
		This should contain data for some popular awaited events such as new year etc.
		'''
		#To be implemented
		pass
		
	def about(self):
		AboutText="""
About

Countdown v1.0
Written by Abhinav Dhere. This software is open sourced 
	as per the MIT License provided in the file LICENSE.		
"""
		newWin=Tkinter.Toplevel()
		newWin.title("About")
		newWin.geometry("480x240",)
		aboutlab=Tkinter.Label(newWin,text=AboutText)
		aboutlab.pack()

if __name__=="__main__":
	app=Count_app(None)
	app.title("Countdown")
	app.geometry("350x270+1050+0")
	app.mainloop()
