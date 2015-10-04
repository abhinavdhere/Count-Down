#Countdown from specified date and time.

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
		FileMenu.add_command(label="Load data",command=self.load)
		FileMenu.add_separator()
		FileMenu.add_command(label="Exit",command=self.quit)
		HelpMenu=Tkinter.Menu(menuBar,tearoff=0)
		HelpMenu.add_command(label="About",command=self.about)
		menuBar.add_cascade(label="File", menu=FileMenu)
		menuBar.add_cascade(label="Help", menu=HelpMenu)
		self.config(menu=menuBar)
		self.resizable(False,False)

	def new(self):
		pass
	
	def save(self):
		pass

	def load(self):
		pass

	def about(self):
		AboutText="""
About

Countdown v1.0
Written by Abhinav Dhere.This software is open sourced 
as per the MIT License provided in the file LICENSE.txt.
		
Disclaimer

This software is provided "as is" and without any warranty whatsoever.
All computations are based on data available in public domain.
The developer does not take any guarantee for accuracy of results.
"""
		
		newWin=Tkinter.Toplevel()
		newWin.title("About")
		newWin.geometry("480x240",)
		aboutlab=Tkinter.Label(newWin,text=AboutText)
		aboutlab.pack()

# setTime=list(map(int,input().split()))
# curTime=datetime.now()
# b=datetime.today().date()
# a=date(setTime[2],setTime[1],(setTime[0]))
# sec=60-curTime.second
# minute=59-curTime.minute
# hour=23-curTime.hour
# print ("You have "+str((a-b).days-1)+" days, "+str(hour)+" hours "+str(minute)+" minutes and "+str(sec)+" seconds left.")

if __name__=="__main__":
	app=Count_app(None)
	app.title("Countdown")
	app.mainloop()
