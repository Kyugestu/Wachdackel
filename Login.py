from Tkinter import *
import os
import time
import datetime
import MySQLdb
 
creds = 'tempfile.temp' # This just sets the variable creds to 'tempfile.temp'

def Login():
    global nameEL
    global pwordEL # More globals :D
    global rootA
 
    rootA = Tk() # This now makes a new window.
    rootA.title('Login') # This makes the window title 'login'
 
    intruction = Label(rootA, text='Please Login\n') # More labels to tell us what they do
    intruction.grid(sticky=E) # Blahdy Blah
 
    nameL = Label(rootA, text='Username: ') # More labels
    pwordL = Label(rootA, text='Password: ') # ^
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)
 
    nameEL = Entry(rootA) # The entry input
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)
 
    loginB = Button(rootA, text='Login', command=CheckLogin) # This makes the login button, which will go to the CheckLogin def.
    loginB.grid(columnspan=2, sticky=W)
    
    rootA.mainloop()
 
def CheckLogin():
    with open(creds) as f:
        data = f.readlines() # This takes the entire document we put the info into and puts it into the data variable
        uname = data[0].rstrip() # Data[0], 0 is the first line, 1 is the second and so on.
        pword = data[1].rstrip() # Using .rstrip() will remove the \n (new line) word from before when we input it
 
    if nameEL.get() == uname and pwordEL.get() == pword: # Checks to see if you entered the correct data.
        r = Tk() # Opens new window
        r.title(':D')
        r.geometry('150x50') # Makes the window a certain size
        rlbl = Label(r, text='\n[+] Logged In') # "logged in" label
        rlbl.pack() # Pack is like .grid(), just different
        
        ts = time.time()#Zeitstempel
        UhrInMin = int(datetime.datetime.fromtimestamp(ts).strftime('%H'))*60 + int(datetime.datetime.fromtimestamp(ts).strftime('%M'))
        Datum = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        filename = nameEL.get()

        datei = "/home/pi/Downloads/Python"+filename+".temp"
        verzeichnis = os.path.dirname(datei)
        if os.path.isfile(filename+".temp"):
            print "vorhanden"
            with open(str(filename)+'.temp') as k:
                datak = k.readlines()
                Zeit1 = int(datak[0].rstrip())
                Zeit2 = int(datetime.datetime.fromtimestamp(ts).strftime('%H'))*60 + int(datetime.datetime.fromtimestamp(ts).strftime('%M'))
                diff = Zeit2 - Zeit1
                print diff
                k.close()
                os.remove(filename+'.temp')
            #TODO = Zeit "diff" an DB übergeben
        else:
            print "nicht vorhanden"        
            with open(str(filename)+'.temp', 'a') as k: # Creates a document using the variable we made at the top.
                k.write(str(UhrInMin)) # nameE is the variable we were storing the input to. Tkinter makes us use .get() to get the actual string.
                k.write('\n') # Splits the line so both variables are on different lines.
                k.write(Datum)
                k.close() # Closes the file
        r.mainloop()
    else:
        r = Tk()
        r.title('D:')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[!] Invalid Login')
        rlbl.pack()
        r.mainloop()
 
if os.path.isfile(creds):
    Login()
