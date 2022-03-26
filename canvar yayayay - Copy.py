from tkinter import *
from tkinter import ttk

root = Tk()
root.title("                                                                                                                                                                                         -:Canvas:-")
root.maxsize(1300,650)
root.minsize(1300,650)



coordinates_values = ["0","25","50","75","100","125","150","175","200","225","250","275","300","325","350","375","400","425","450","475","500","525","550","575","600","625","650","675","700","725","750","775","800","825","850","875","900","925","950","975","1000","1025","1050","1075","1100","1125","1150","1175","1200","1225","1250","1275","1300"]

canvas = Canvas(root,width = 1300,height = 400)
canvas.pack()





fillcolour = ["red","yellow","white","black","grey","brown","pink","blue","orange"]

label = Label(root,text = "choose colour")
label.place(relx = 0.4,rely = 0.7,anchor = CENTER)

dash_label = Label(root,text = " - ")
dash_label.place(relx = 4.5,rely = 0.7,anchor = CENTER)

dropdown_color = ttk.Combobox(root,state = "readonly",values = fillcolour,width = "10")
dropdown_color.place(relx = 0.5,rely = 0.7,anchor = CENTER)





startx = Label(root,text = "start x - ",)
startx.place(relx = 0.1,rely = 0.8,anchor = CENTER)

dropdown_startx = ttk.Combobox(root,state = "readonly",values = coordinates_values,width = "10")
dropdown_startx.place(relx = 0.2,rely = 0.8,anchor = CENTER)



starty = Label(root,text = "start y - ",)
starty.place(relx = 0.3,rely = 0.8,anchor = CENTER)

dropdown_starty = ttk.Combobox(root,state = "readonly",values = coordinates_values,width = "10")
dropdown_starty.place(relx = 0.4,rely = 0.8,anchor = CENTER)



endx = Label(root,text = "end x - ")
endx.place(relx = 0.5,rely = 0.8,anchor = CENTER)

dropdown_endx = ttk.Combobox(root,state = "readonly",values = coordinates_values,width = "10")
dropdown_endx.place(relx = 0.6,rely = 0.8,anchor = CENTER)



endy = Label(root,text = "end y - ")
endy.place(relx = 0.7,rely = 0.8,anchor = CENTER)

dropdown_endy = ttk.Combobox(root,state = "readonly",values = coordinates_values,width = "10")
dropdown_endy.place(relx = 0.8,rely = 0.8,anchor = CENTER)

oldx = 0
oldy = 0
newx = 0
newy = 0
keypress = ""

def circle(event):
    global oldx
    global oldy
    global newx
    global newy
    global keypress
    oldx = dropdown_startx.get()
    oldy = dropdown_starty.get()
    newx = dropdown_endx.get()
    newy = dropdown_endy.get()
    keypress = "c"
    draw(keypress,oldx,oldy,newx,newy)

def rectangle(event):
    global oldx
    global oldy
    global newx
    global newy
    global keypress
    oldx = dropdown_startx.get()
    oldy = dropdown_starty.get()
    newx = dropdown_endx.get()
    newy = dropdown_endy.get()
    keypress = "r"
    draw(keypress,oldx,oldy,newx,newy)

def line(event):
    global oldx
    global oldy
    global newx
    global newy
    global keypress
    oldx = dropdown_startx.get()
    oldy = dropdown_starty.get()
    newx = dropdown_endx.get()
    newy = dropdown_endy.get()
    keypress = "i"
    draw(keypress,oldx,oldy,newx,newy)
    
def draw(keypress,oldx,oldy,newx,newy):
    colour = dropdown_color.get()
    
    if (keypress=="c"):
        
        canvas.create_oval(oldx,oldy,newx,newy,width = 3,fill = colour)
        
    if (keypress=="r"):
                canvas.create_rectangle(oldx,oldy,newx,newy,width = 3,fill = colour)
        
    if(keypress=="i"):
                canvas.create_line(oldx,oldy,newx,newy,width = 3,fill= colour)
    
        
root.bind("<c>",circle)
root.bind("<r>",rectangle)
root.bind("<i>",line)

root.mainloop()