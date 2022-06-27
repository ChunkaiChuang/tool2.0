import tkinter
from tkinter.constants import N, NE
from PIL import Image, ImageTk
import os
import method
# from PIL import ImageTk

window = tkinter.Tk()


window.title('耖拎呆2.0')
window.geometry('800x230')

def resize( w_box, h_box, pil_image): #参数是：要适应的窗口宽、高、Image.open后的图片
  w, h = pil_image.size #获取图像的原始大小   
  f1 = 1.0*w_box/w 
  f2 = 1.0*h_box/h    
  factor = min([f1, f2])   
  width = int(w*factor)    
  height = int(h*factor)    
  return pil_image.resize((width, height), Image.ANTIALIAS)    


  
label=tkinter.LabelFrame(window,text="Back up")   #label 1
Name=tkinter.Button(label,text='Name',command=method.name)
Bace=tkinter.Button(label,text='Bace information', command=method.base)
account=tkinter.Button(label, text='account',command=method.account)
password=tkinter.Button(label,text='password',command=method.password)

label2=tkinter.LabelFrame(window,text='betterbug') #label 2
LDAP=tkinter.Button(label2,text='LDAP', command= method.LDAP)
Lpaasword=tkinter.Button(label2,text='L_password',command=method.L_password)
qa=tkinter.Button(label2, text='QA',command=method.QA)
test=tkinter.Button(label2, text='Test',command=method.Test)

label3=tkinter.LabelFrame(window, text='OTA')     #label 3
OTA=tkinter.Button(label3, text='OTA',command=method.OTA)
reboot=tkinter.Button(label3, text='reboot',command=method.reboot)
before=tkinter.Button(label3, text='before reboot',command=method.before)
lock=tkinter.Button(label3, text='lock',command=method.lock)
var = tkinter.StringVar()

label4=tkinter.LabelFrame(window,text='Input what you want')
some=tkinter.Entry(label4,textvariable=var)

some.grid(row=3,column=0,sticky='nw')


def bbb():
    aaa=some.get()
    os.system(f'''adb shell input text "{aaa}"''')

w_box=800
h_box=200    

img= Image.open('1655965400357.jpg')

img_resize=resize(w_box,h_box,img)
tk_img=ImageTk.PhotoImage(img_resize)
imglabel=tkinter.Label(window,image=tk_img)



OK=tkinter.Button(label4,text='OK',command=bbb)

Name.grid(row=0,column=0)
Bace.grid(row=0,column=1)
account.grid(row=0,column=2)
password.grid(row=0,column=3)
label.grid(row=0,column=0,ipadx=5,ipady=1,sticky='nw')
label2.grid(row=1,column=0,ipadx=20,ipady=1,sticky='nw')
label3.grid(row=2,column=0,ipadx=6,ipady=1,sticky='nw')
label4.grid(row=3,column=0,ipadx=6,ipady=1,sticky='nw')
LDAP.grid(row=0,column=0)
Lpaasword.grid(row=0,column=1)
qa.grid(row=0,column=2)
test.grid(row=0,column=3)
OTA.grid(row=0,column=0)
reboot.grid(row=0,column=1)
before.grid(row=0,column=2)
lock.grid(row=0,column=3)
# some.grid(row=3,column=0,sticky='nw')
OK.grid(row=2,column=3, rowspan=2, padx=5, pady=5,sticky='nw')
imglabel.grid(row=0, column=40, rowspan=4, padx=7, pady=5)


window.mainloop()