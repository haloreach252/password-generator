import string
import random
import tkinter

#Size Vars
maxSize = 30
size = 18

#The Canvas
top = tkinter.Tk()
top.title("Password Generator")
top.resizable(width=False,height=False)
top.geometry('{}x{}'.format(550,200))

#Max Size Label
maxSizeLabel = tkinter.Label(top, text="Max Pwd Size: " + str(maxSize), bg="white")
maxSizeLabel.grid(row=3, column=3)

#Password size label
pwdSizeText = tkinter.Label(top, text="Pwd Size: " + str(size), bg="white")
pwdSizeText.grid(row=2, column=2)

#The password size entry box
entLabel = tkinter.Label(top, text="Enter Pwd Size: ", bg="white")
entLabel.grid(row=1, column=3)
entText = tkinter.IntVar()
e1 = tkinter.Entry(top, textvariable=entText)
e1.grid(row=2, column=3)

#The text of the password
passwordText = tkinter.Label(top, text="Please press button to begin", bg="white")
passwordText.grid(row=2, column=1)

#Special Circumstances Checkboxes Vars
'''
specCharCB = tkinter.IntVar()
upperCharCB = tkinter.IntVar()
lowerCharCB = tkinter.IntVar()
numberCharCB = tkinter.IntVar()

#Special Circumstances Checkboxes
needsSpecCharCheckb = tkinter.Checkbutton(top, text="Needs Special Characters", variable=specCharCB)
needsSpecCharCheckb.grid(row=3, column=1)
needsLowerCheckb = tkinter.Checkbutton(top, text="Needs Lowercase Characters", variable=lowerCharCB)
needsLowerCheckb.grid(row=3, column=2)
needsUpperCheckb = tkinter.Checkbutton(top, text="Needs Uppercase Characters", variable=upperCharCB)
needsUpperCheckb.grid(row=4, column=1)
needsNumbersCheckb = tkinter.Checkbutton(top, text="Needs Numerical Characters", variable=numberCharCB)
needsNumbersCheckb.grid(row=4, column=2)
'''

#Changes size based on what the entry box has
def changeSize():
	e1Size = e1.get()
	global size
	size = int(e1Size)
	pwdSizeText.config(text="Pwd Size: " + str(size))
	
#Generates the actual password
def id_generator():
	if(size <= maxSize):
		pwd = ''.join(random.choice(string.printable[:-30]) for _ in range(size))
		passwordText.config(text=pwd)
		return pwd
	else:
		pwd = ''.join(random.choice(string.printable[:-30]) for _ in range(30))
		passwordText.config(text=pwd)
		return pwd
		
def savePwd():
	pwdTxt = str(passwordText.cget('text'))
	file = open(".\SavedPasswords.txt","a+")
	file.write("\n" + pwdTxt)
	file.close()

#Generation Buttons
generateButton = tkinter.Button (top, text="Press to generate password", command=id_generator, width=22, bg="white")
generateButton.grid(row=1, column=1)

changeSizeButton = tkinter.Button(top, text="Press to change size", command=changeSize, width=22, bg="white")
changeSizeButton.grid(row=1, column=2)

savePwdButton = tkinter.Button(top, text="Save Password", command=savePwd, width=12, bg="white")
savePwdButton.grid(row=3, column=1)

top.mainloop()
