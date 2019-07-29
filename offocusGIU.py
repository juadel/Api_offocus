#offocus GIU
from tkinter import *
from tkinter import filedialog
import api_cli
import networking
import image_processing


def offocusGiu():
    window = Tk()
    
    window.title("Off focus Finder V1.0 ")

    window.geometry('{}x{}'.format(400, 150))
    top_frame = Frame(window,width=250, height=30, pady=6)
    btm_frame = Frame(window,width=250, height=30, pady=6,bd=1, relief=SUNKEN) 

    window.grid_rowconfigure(1, weight=2)
    window.grid_columnconfigure(0,weight=2)
    top_frame.grid(row=0, columnspan =3 )
    btm_frame.grid(row=1, columnspan =3)

    #filename = str()
    


    lbl = Label(top_frame, text="  Starting IP:  ", font=("Arial", 10))
    lbl2 = Label(top_frame, text="  Ending IP:  ", font=("Arial", 10))
    lbl3 = Label(top_frame, text="  Password :  ", font=("Arial", 10))
    lbl4= Label(btm_frame, text="  Scan a Folder:  ", font=("Arial", 10))
    lbl.grid(column=0, row=0)
    lbl2.grid(column=0, row=1)
    lbl3.grid(column=0, row=3)
    lbl4.grid(column=0, row=7)


    ip_0 = Entry(top_frame,width=20)
    ip_0.focus()
    ip_1 = Entry(top_frame, width = 20)
    pas = Entry(top_frame, show="*", width = 20)
    ip_0.grid(column = 2, row = 0)
    ip_1.grid(column = 2, row = 1)
    pas.grid(column = 2, row =3)

    chk_state = BooleanVar() 
    chk_state.set(True) #set check state
    chk = Checkbutton(window, text='Show Images', var=chk_state)
    chk.grid(column=1, row=10)

    

    

    def clicked_1():
        ip0 = ip_0.get()
        ip1 = ip_1.get()
        password = pas.get()
        chk_st = chk_state.get()
        report = networking.main_Lan(ip0,ip1,password,chk_st)
        print_results(report)
    

    def clicked_2():
        global filename
        filename= filedialog.askdirectory()
        filename=filename + "/"
            

    def clicked_3():
        chk_st=chk_state.get()
        report = image_processing.main_folder(filename,chk_st)
        print_results(report)
        

    def print_results(report):
	    rw = Tk()
	    rw.title("Scan results")
	    result = Text(rw)
	    result.pack()

	    class PrintToT1(object): 
		    def write(self, s): 
			    result.insert(END, s) 
		
	    sys.stdout = PrintToT1()
	    print (report)

	    mainloop() 

    btn = Button(top_frame, text="Scan LAN", command=clicked_1)
    btn.grid(column = 3 , row = 3 ) 
    btn_2 = Button(btm_frame, text = "Browse", command=clicked_2)
    btn_2.grid(column = 2 , row = 7 ) 
    btn_3 = Button(btm_frame, text="Scan Folder", command=clicked_3)
    btn_3.grid(column = 3 , row = 7 ) 

    window.mainloop()


offocusGiu()