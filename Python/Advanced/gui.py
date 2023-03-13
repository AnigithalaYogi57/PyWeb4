import tkinter as tk
ws = tk.Tk()
ws.geometry('500x400')
ws.title('mytitle')
l1 = tk.Label(ws,text='Header')
l1.grid(row=1,column=1,padx=50,pady=20)
l3 = tk.Entry(ws,width=50)
l3.grid(row=2,column=1,padx=50,pady=20)
ws.mainloop()