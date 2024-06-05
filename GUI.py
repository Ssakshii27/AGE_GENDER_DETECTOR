import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
from tensorflow.keras.models import load_model

# Loading the model
model = load_model('Age_Sex_Detection.keras')

# Initializing the GUI
top = tk.Tk()
top.geometry('800x600')
top.title('AGE AND GENDER DETECTOR')
top.configure(background='#FCE6C9')

# Initializing the Labels (1 for age and 1 for gender)
label1 = Label(top, background="#FCE6C9", font=('times new roman', 18, "bold"))
label2 = Label(top, background="#FCE6C9", font=('times new roman', 18, "bold"))
sign_image = Label(top)

# Defining detect function which detects the age and gender of the person in image using the model
def Detect(file_path):
    global label_packed
    image=Image.open(file_path)
    image=image.resize((48,48))
    image=np.expand_dims(image,axis=0)
    iamge=np.array(image)
    image=np.delete(image,0,1)
    image=np.resize(image,(48,48,3))
    print(image.shape)
    sex_f=["Male","Female"]
    image=np.array([image])/255
    pred=model.predict(image)
    age=int(np.round(pred[1][0]))
    sex=int(np.round(pred[0][0]))
    print("Predicted Age is: "+str(age))
    print("Predicted Gender is "+sex_f[sex])
    label1.configure(foreground="#B22222",text=age)
    label2.configure(foreground="#B22222",text=sex_f[sex])

# Defining show_detect button function
def show_detect_button(file_path):
    Detect_b=Button(top,text="Detect Image",command=lambda: Detect(file_path),padx=10,pady=5)
    Detect_b.configure(background="#FF7D40",foreground='#FCE6C9',font=('times new roman',15,"bold"))
    Detect_b.place(relx=0.79,rely=0.46) 

# Defining upload Image Function
def upload_image():
    try:
        file_path=filedialog.askopenfilename()
        uploaded=Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width()/2.25),(top.winfo_height()/2.25)))
        im=ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image=im
        label1.configure(text='')
        label2.configure(text='')
        show_detect_button(file_path)
    except:
        pass

upload=Button(top,text="Upload an Image",command=upload_image,padx=10,pady=5)
upload.configure(background="#FF7D40",foreground='#FCE6C9',font=('times new roman',15,"bold"))              
upload.pack(side='bottom',pady=50)
sign_image.pack(side='bottom',expand=True)

label1.pack(side='bottom', expand=True)
label2.pack(side='bottom', expand=True)
heading = Label(top, text="AGE AND GENDER DETECTOR", pady=20, font=('times new roman', 20, "bold"))
heading.configure(background="#FCE6C9", foreground="#FF3030")
heading.pack()

top.mainloop()
