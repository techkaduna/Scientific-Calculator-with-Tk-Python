from tkinter import *
from tkinter import ttk
from Module import *
import logger

root = Tk()



class Calculator():
    def __init__(self,master):
        self.master = master
        #setting basic window
        self.master.title('Calculator')
        self.master.geometry('276x440')
        self.master.resizable(0,0)
        self.master.configure(bg='lightgrey')

        self.i = 0
        


        #creating frames
        self.frame1 = Frame(self.master,bg='lightgrey',)
        self.frame1.pack(fill='x')
        self.frame2 = Frame(self.master,bg='lightblue')
        self.frame2.pack(fill='x')
        self.frame3 = Frame(self.master,bg='lightgrey')
        self.frame3.pack(fill='x')
        self.frame4 = Frame(self.master,bg='lightblue')
        self.frame4.pack(fill='x')
        self.frame5 = Frame(self.master,bg='lightgrey')
        self.frame5.pack(fill='x')
        self.frame6 = Frame(self.master,bg='lightblue')
        self.frame6.pack(fill='x')
        self.frame7 = Frame(self.master,bg='lightgrey')
        self.frame7.pack(fill='x')
        self.frame8 = Frame(self.master,bg='lightblue')
        self.frame8.pack(fill='x')

        
        #Entry Widget
        #self.MainEntry = Entry(self.frame1,width=100)
        #self.MainEntry.config(font=('Banscrift',20))
        #self.MainEntry.pack()

        #Trying a text area
        self.MainEntry = Text(self.frame1)
        self.MainEntry.configure(font=('Banschrift',16),height=3,bg='lightgrey')
        self.MainEntry.pack()

        #imported calls
        math = Maths(self.MainEntry)
        op = operations(self.MainEntry)
        #Buttons
        
        self.B1 = Button(self.frame2,text='1',width=7,height=2,command=lambda:self.insert_num(1))
        self.B1.grid(row=0,column=0,padx=5,pady=5)
        self.B2 = Button(self.frame2,text='2',width=7,height=2,command=lambda:self.insert_num(2))
        self.B2.grid(row=0,column=1,padx=5,pady=5)
        self.B3 = Button(self.frame2,text='3',width=7,height=2,command=lambda:self.insert_num(3))
        self.B3.grid(row=0,column=2,padx=5,pady=5)
        # sine
        self.sine = Button(self.frame2,text='sin/sin-1',command=math.sine)
        self.sine.config(width=7,height=2,font=('arial',8))
        self.sine.bind("<Button-3>",math.sine_inv)
        self.sine.grid(row=0,column=3,padx=5,pady=5)

        self.B4 = Button(self.frame3,text='4',width=7,height=2,command=lambda:self.insert_num(4))
        self.B4.grid(row=0,column=0,padx=5,pady=5)
        self.B5 = Button(self.frame3,text='5',width=7,height=2,command=lambda:self.insert_num(5))
        self.B5.grid(row=0,column=1,padx=5,pady=5)
        self.B6 = Button(self.frame3,text='6',width=7,height=2,command=lambda:self.insert_num(6))
        self.B6.grid(row=0,column=2,padx=5,pady=5)

        #cosine
        self.cosine = Button(self.frame3,text='cos/cos-1',command=math.cosine)
        self.cosine.config(width=7,height=2,font=('arial',8))
        self.cosine.bind("<Button-3>",math.cos_inv)
        self.cosine.grid(row=0,column=3,padx=5,pady=5)

        self.B7 = Button(self.frame4,text='7',width=7,height=2,command=lambda:self.insert_num('7'))
        self.B7.grid(row=0,column=0,padx=5,pady=5)
        self.B8 = Button(self.frame4,text='8',width=7,height=2,command=lambda:self.insert_num('8'))
        self.B8.grid(row=0,column=1,padx=5,pady=5)
        self.B9 = Button(self.frame4,text='9',width=7,height=2,command=lambda:self.insert_num('9'))
        self.B9.grid(row=0,column=2,padx=5,pady=5)
        #tanget
        self.tangent = Button(self.frame4,text='tan/tan-1',command=math.tangent)
        self.tangent.config(width=7,height=2,font=('arial',8))
        self.tangent.bind("<Button-3>",math.tan_inv)
        self.tangent.grid(row=0,column=3,padx=5,pady=5)

        #zero and operationals
        self.addbtn = Button(self.frame5,text='+',width=7,height=2,command=op.addition)
        self.addbtn.grid(row=0,column=0,padx=5,pady=5)
        self.subbtn = Button(self.frame5,text='-',width=7,height=2,command=op.subtract)
        self.subbtn.grid(row=0,column=1,padx=5,pady=5)
        self.zero = Button(self.frame5,text='0',width=7,height=2,command=lambda:self.insert_num('0'))
        self.zero.grid(row=0,column=2,padx=5,pady=5)
        # logarithms_base10
        self.logs = Button(self.frame5,text='log/x10',command=math.log)
        self.logs.config(width=7,height=2,font=('arial',8))
        self.logs.bind("<Button-3>",math.antiLog)
        self.logs.grid(row=0,column=3,padx=5,pady=5)


        self.button_multiply = Button(self.frame6,text='x',width=7,height=2,command=op.multiply)
        self.button_multiply.grid(row=0,column=0,padx=5,pady=5)
        self.button_divide = Button(self.frame6,text='/',width=7,height=2,command=op.division)
        self.button_divide.grid(row=0,column=1,padx=5,pady=5)
        self.btn_fact = Button(self.frame6,text='!/perm',width=7,height=2,command=math.factorial)
        self.btn_fact.bind("<Button-3>",math.perm)
        self.btn_fact.grid(row=0,column=2,padx=5,pady=5)
        # exponential and naperian log
        self.exp_lin = Button(self.frame6,text='ex/lin',command=math.exponent)
        self.exp_lin.config(width=7,height=2,font=('arial',8))
        self.exp_lin.bind("<Button-3>",math.lin)
        self.exp_lin.grid(row=0,column=3,padx=5,pady=5)

        #other functions
        self.pi = Button(self.frame7,text='pi',width=6,height=2,font=('arial',8),command=math.pi)
        self.pi.grid(row=0,column=0,padx=4,pady=5)

        self.sqrt = Button(self.frame7,text='sqr/sqrt',width=6,height=2,font=('arial',8),command=math.sqr)
        self.sqrt.bind("<Button-3>",math.sqrt)
        self.sqrt.grid(row=0,column=1,padx=4,pady=5)
        
        self.cube = Button(self.frame7,text='cube/crt',width=6,height=2,font=('arial',8),command=math.cube)
        self.cube.bind("<Button-3>",math.cube_rt)
        self.cube.grid(row=0,column=2,padx=4,pady=5)

        self.rad_deg = Button(self.frame7,text='rad/deg',width=6,height=2,font=('arial',8),command=math.radians)
        self.rad_deg.bind("<Button-3>",math.degree)
        self.rad_deg.grid(row=0,column=3,padx=4,pady=5)

        self.dec_point = Button(self.frame7,text='.',width=6,height=2,command=lambda:self.insert_num('.'))
        self.dec_point.grid(row=0,column=4,padx=4,pady=5)


        #equal to and clear buttons
        self.btn_equals = Button(self.frame8,text='=',command=op.equals)
        self.btn_equals.config(width=14,height=2,font=('Arial',10))
        self.btn_equals.grid(row=0,column=0,padx=4,pady=5)

        self.btn_clear = Button(self.frame8,text='CLEAR',command=self.clear_btn)
        self.btn_clear.config(width=8,height=2,font=('Arial',10))
        self.btn_clear.grid(row=0,column=1,padx=4,pady=5)

        #tan inverse
        self.tan_inv = Button(self.frame8,text='DEL',width=7,height=2,font=('arial',8),command=self.delete)
        self.tan_inv.grid(row=0,column=3,padx=4,pady=5)
        


        self.master.mainloop()

    def insert_num(self,x):
        try:
            self.MainEntry.insert(INSERT, x)
            self.i += 1
        except Exception as e:
            logger.logger.error(e)

    def clear_btn(self):
        try:
            self.MainEntry.delete('1.0',END)
        except:
            logger.logger.error('Clear button error')

    def delete(self):
        try:
            logger.logger.info('Delete button under construction')
            #self.MainEntry.delete(1)
        except:
            logger.logger.error('An error occured while deleting from entry')

if __name__ == '__main__':
    calc = Calculator(root)