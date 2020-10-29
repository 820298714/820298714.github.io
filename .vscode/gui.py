import numpy as np
import matplotlib.pyplot as plt
from pylab import *

x=np.linspace(0,5,20)
x1=np.linspace(0,10,10)
X=[2,1.5,1,0.5]

def lssin():
    y1=np.sin(np.pi*x+2)
    plt.title('sin(n)')
    plt.grid(True)
    plt.stem(x,y1)
    plt.show()

def lsex():
    y4=2*0.5**x1
    plt.grid(True)
    plt.title('e^x(n)')
    plt.stem(x1,y4)
    plt.show()

def  lsjy():
    def dwjy(t):
        r=np.where(t>=0.0,1.0,0.0)
        return r
    n=np.arange(-10,10)
    plt.ylim(0,3)
    plt.title('u(n)')
    plt.grid(True)
    plt.stem(n,dwjy(n))
    plt.show()

def lscj():
    def dwxl(temp):
        r=np.where(temp==0.0,1.0,0.0)
        return r
    m=np.arange(-10,10)
    plt.ylim(0,3)
    plt.title('δ(n)')
    plt.grid(True)
    plt.stem(m,dwxl(m))
    plt.show()


from tkinter import *
tk=Tk()
tk.title("离散信号图像")
Button(tk,text="离散sin",command=lssin).pack(side=LEFT)
Button(tk,text="离散e^x",command=lsex).pack(side=LEFT)
Button(tk,text="离散阶跃",command=lsjy).pack(side=LEFT)
Button(tk,text="离散冲击",command=lscj).pack(side=RIGHT)
tk.mainloop()