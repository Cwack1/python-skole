import tkinter as tk

def show(a):
    R = int(r.get() * 2.55)
    G = int(g.get() * 2.55)
    B = int(b.get() * 2.55)
    can.configure(bg="#%02x%02x%02x" % ((R, G, B)))

main = tk.Tk()
main.title("Blande farger")
main.geometry("250x320")

r = tk.Scale(main, from_=0, to=100, command=show)
g = tk.Scale(main, from_=0, to=100, command=show)
b = tk.Scale(main, from_=0, to=100, command=show)
can = tk.Canvas(main, height=180, width=240, bg="black")
tk.Label(main, text="RØD").grid(row=1,column=0)
tk.Label(main, text="GRØNN").grid(row=1,column=1)
tk.Label(main, text="BLÅ").grid(row=1,column=2)

r.grid(row=0,column=0,padx=10,pady=10)
g.grid(row=0,column=1,padx=10,pady=10)
b.grid(row=0,column=2,padx=10,pady=10)
can.grid(row=2,column=0,columnspan=3)

main.mainloop()