
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename,asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os


 
root = Tk()
root.title("Image Enhancer")
root.geometry("650x640")
root.iconbitmap("logo.ico")
myfont = ("Times New Roman",12)

#functions
def selected():
    global img_path, img
    img_path = filedialog.askopenfilename(initialdir=os.getcwd()) 
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    #imgg = img.filter(ImageFilter.BoxBlur(0))
    img1 = ImageTk.PhotoImage(img)
    canvas2.create_image(300, 210, image=img1)
    canvas2.image=img1                                                                                                                                                                                                                

def blur(event):
    global img_path, img1, imgg
    for m in range(0, v1.get()+1):
            img = Image.open(img_path)
            img.thumbnail((350, 350))
            imgg = img.filter(ImageFilter.BoxBlur(m))
            img1 = ImageTk.PhotoImage(imgg) 
            canvas2.create_image(300, 210, image=img1)
            canvas2.image=img1

def brightness(event):
    global img_path, img2, img3
    for m in range(0, v2.get()+1):
            img = Image.open(img_path)
            img.thumbnail((350, 350))
            imgg = ImageEnhance.Brightness(img)
            img2 = imgg.enhance(m)
            img3 = ImageTk.PhotoImage(img2)
            canvas2.create_image(300, 210, image=img3)
            canvas2.image=img3

def Resize_image():
    
    global img_path, img4, img5
    img=Image.open(img_path)
    img.thumbnail((350, 350))
    size=(400,400)
    img4 =img.resize(size)
    img5 = ImageTk.PhotoImage(img4)
    canvas2.create_image(300, 210, image=img5)
    canvas2.image=img5

def crop():
    global img_path, img12, img13
    img=Image.open(img_path)
    img.thumbnail((350, 350))
    left = 55
    top = 145
    right = 280
    bottom = 250
    img12 = img.crop((left, top, right, bottom))
    img13 = ImageTk.PhotoImage(img12)
    canvas2.create_image(300, 210, image=img13)
    canvas2.image=img13
    
               

def rotate_image(event):
        global img_path, img6, img7
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        img6 = img.rotate(int(rotate_combo.get()))
        img7 = ImageTk.PhotoImage(img6)
        canvas2.create_image(300, 210, image=img7)
        canvas2.image=img7
        
def flip_image(event):
        global img_path, img8, img9
        img = Image.open(img_path)
        img.thumbnail((350, 350))
        if flip_combo.get() == "FLIP LEFT TO RIGHT":
            img8 = img.transpose(Image.FLIP_LEFT_RIGHT)
        elif flip_combo.get() == "FLIP TOP TO BOTTOM":
            img8 = img.transpose(Image.FLIP_TOP_BOTTOM)
        img9 = ImageTk.PhotoImage(img8)
        canvas2.create_image(300, 210, image=img9)
        canvas2.image=img9


def gray_scale():
    global img_path, img10, img11
    img = Image.open(img_path)
    img.thumbnail((350, 350))
    img10 = img.convert('L')
    img11 = ImageTk.PhotoImage(img10)
    canvas2.create_image(300, 210, image=img11)
    canvas2.image=img11

def clear():
    canvas2.delete("all")
    img= Image.open('bg1.jpg')


          
img1 = None
img3 = None
img5 = None
img7 = None
img9 = None
img11 = None
img12 = None
img13 = None

def save():
    global img_path, imgg, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12, img13
    #file=None
    ext = img_path.split(".")[-1]
    file=asksaveasfilename(defaultextension =f".{ext}",filetypes=[("All Files","*.*"),("PNG file","*.png"),("jpg file","*.jpg")])
    if file: 
            if canvas2.image==img1:
                imgg.save(file)
            elif canvas2.image==img3:
                img2.save(file)
            elif canvas2.image==img5:
                img4.save(file)
            elif canvas2.image==img7:
                img6.save(file)
            elif canvas2.image==img9:
                img8.save(file)
            elif canvas2.image==img11:
                img10.save(file)
            elif canvas2.image==img13:
                img12.save(file) 

# create labels, scales and comboboxes
blurr = Label(root, text="Blur:", font=myfont, width=9, anchor='e')
blurr.place(x=15, y=8)
v1 = IntVar()
scale1 = ttk.Scale(root, from_=0, to=10, variable=v1, orient=HORIZONTAL, command=blur) 
scale1.place(x=150, y=10)

bright = Label(root, text="Brightness:", font=myfont)
bright.place(x=8, y=50)
v2 = IntVar()   
scale2 = ttk.Scale(root, from_=0, to=10, variable=v2, orient=HORIZONTAL, command=brightness) 
scale2.place(x=150, y=55)

cropping = Button(root, text="Crop",font=myfont,command=crop)
cropping.place(x=150,y=92)

Resize = Button(root, text="Resize",font=myfont,command=Resize_image)
Resize.place(x=35, y=92)
   

rotate = Label(root, text="Rotate:", font=myfont)
rotate.place(x=370, y=8)

values = [0, 90, 180, 270, 360]
rotate_combo = ttk.Combobox(root, values=values, font=myfont)
rotate_combo.place(x=460, y=15)
rotate_combo.bind("<<ComboboxSelected>>", rotate_image)

flip = Label(root, text="Flip:", font=myfont)
flip.place(x=400, y=50)

values1 = ["FLIP LEFT TO RIGHT", "FLIP TOP TO BOTTOM"]
flip_combo = ttk.Combobox(root, values=values1, font=('ariel 10 bold'))
flip_combo.place(x=460, y=57)
flip_combo.bind("<<ComboboxSelected>>", flip_image)

Grayscale = Button(root, text="Gray Scale:", font=myfont,command=gray_scale)
Grayscale.place(x=480, y=92)

clear_canvas = Button(root, text="Refresh", font=myfont, command=clear)
clear_canvas.place(x=400,y=92 )





# create canvas to display image
canvas2 = Canvas(root, width="625", height="450", relief=RIDGE, bd=2)
canvas2.place(x=15, y=150)

# create buttons
btn1 = Button(root, text="Select Image", bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=selected)
btn1.place(x=100, y=595)

btn2 = Button(root, text="Save", width=12, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=save)
btn2.place(x=280, y=595)

btn3 = Button(root, text="Exit", width=12, bg='black', fg='gold', font=('ariel 15 bold'), relief=GROOVE, command=root.destroy)
btn3.place(x=460, y=595)

root.mainloop()
