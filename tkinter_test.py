from tkinter import *
from tkinter import font

windows=Tk()
windows.title("ماشین حساب ")

#functions
text_input= StringVar()


def clear():
    text_input.set('')

def btn_click(number):
    global operator
    operator=operator+number
    text_input.set(operator)

def calculate():
    global operator
    result = eval(operator)
    text_input.set(result)
    
operator=''


#############################################################################################################################2
text_display = Entry(windows, font=('arial',20,'bold'), textvariable=text_input, bd=30, bg='powder blue',
                    insertwidth=4,justify='right').grid(columnspan=4)
#############################################################################################################################3
btn7=Button(windows,padx=16, pady=16 ,font=('arial',20,'bold'),bd=8,fg='black',text='7', command=lambda:btn_click('7'),bg='yellow').grid(row=1,column=0)
btn8=Button(windows,padx=16, pady=16 ,font=('arial',20,'bold'),bd=8,fg='black',text='8', command=lambda:btn_click('8'),bg='yellow').grid(row=1,column=1)
btn9=Button(windows,padx=16, pady=16 ,font=('arial',20,'bold'),bd=8,fg='black',text='9', command=lambda:btn_click('9'),bg='yellow').grid(row=1,column=2)
dev=Button(windows,padx=16, pady=16 ,font=('arial',20,'bold'),bd=8,fg='black',text='/', command=lambda:btn_click('/'),bg='yellow').grid(row=1,column=3)
#############################################################################################################################4
btn4=Button(windows,padx=16, pady=16 ,font=('arial',20,'bold'),bd=8,fg='black',text='4', command=lambda:btn_click('4'),bg='yellow').grid(row=2,column=0)
btn5=Button(windows,padx=16, pady=16 ,font=('arial',20,'bold'),bd=8,fg='black',text='5', command=lambda:btn_click('5'),bg='yellow').grid(row=2,column=1)
btn6=Button(windows,padx=16, pady=16 ,font=('arial',20,'bold'),bd=8,fg='black',text='6', command=lambda:btn_click('6'),bg='yellow').grid(row=2,column=2)
sum=Button(windows,padx=16, pady=16 ,font=('arial',20,'bold'),bd=8,fg='black',text='+', command=lambda:btn_click('+'),bg='yellow').grid(row=2,column=3)
#############################################################################################################################5
btn3=Button(windows,padx=16, pady=16 ,font=('arial',20,'bold'),bd=8,fg='black',text='3', command=lambda:btn_click('3'),bg='yellow').grid(row=3,column=0)
btn2=Button(windows,padx=16, pady=16 ,font=('arial',20,'bold'),bd=8,fg='black',text='2', command=lambda:btn_click('2'),bg='yellow').grid(row=3,column=1)
btn1=Button(windows,padx=16, pady=16 ,font=('arial',20,'bold'),bd=8,fg='black',text='1', command=lambda:btn_click('1'),bg='yellow').grid(row=3,column=2)
mul=Button(windows,padx=16, pady=16 ,font=('arial',20,'bold'),bd=8,fg='black',text='*', command=lambda:btn_click('*'),bg='yellow').grid(row=3,column=3)
#############################################################################################################################6
clear_btn=Button(windows,padx=16, pady=16 ,font=('arial',20,'bold'),bd=8,fg='black',text='C', command=lambda:clear(),bg='yellow').grid(row=4,column=0)
btn0=Button(windows,padx=16, pady=16 ,font=('arial',20,'bold'),bd=8,fg='black',text='0', command=lambda:btn_click('0'),bg='yellow').grid(row=4,column=1)
subtract=Button(windows,padx=16, pady=16 ,font=('arial',20,'bold'),bd=8,fg='black',text='-', command=lambda:btn_click('-'),bg='yellow').grid(row=4,column=3)
equal=Button(windows,padx=16, pady=16 ,font=('arial',20,'bold'),bd=8,fg='black',text='=',bg='yellow', command=lambda:calculate()).grid(row=4,column=2)




windows.mainloop()