from Tkinter import *
from cmath import sin
from cmath import tan
from cmath import cos
import matplotlib.pyplot as plt
def a():
	#a=input()
	plt.plot([sin(x) for x in range(int(e.get()))])
	plt.show()
def b():
	#a=input()
	plt.plot([tan(x) for x in range(int(e.get()))])
	plt.show()
def c():
	#a=input()
	plt.plot([cos(x) for x in range(int(e.get()))])
	plt.show()
master=Tk()
master.title('Graph Generator')
e=Entry(master)
e.get()
#a=e.get()
e.pack()
#def evaluate(event):
    #res.configure(text = "Enter Range" + str(eval(entry.get())))
#entry = Entry(master)
#entry.bind("<Return>", evaluate)
#entry.pack()
Label(master, text="Enter the Range for which you want to plot a graph").pack()
res = Label(master)
res.pack()
widget=Button(None,text='Sin Graph',height=20,width=50, command=a)
widget.pack()
widget=Button(None,text='Tan Graph',height=20,width=50, command=b)
widget.pack()
widget=Button(None,text='Cos Graph',height=20,width=50, command=c)
widget.pack()
e.pack()
widget.mainloop()

