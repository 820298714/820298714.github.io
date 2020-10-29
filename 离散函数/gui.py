import numpy as np
import matplotlib.pyplot as plt
from pylab import *

x=np.linspace(0,5,20)
x1=np.linspace(0,10,10)



def ls_sin():
    y1=np.sin(np.pi*x)
    plt.title('sin(n)')
    plt.grid(True)
    plt.stem(x,y1)
    plt.show()

def ls_exp():
    y2=e**x1
    plt.grid(True)
    plt.title('e^x(n)')
    plt.stem(x1,y2)
    plt.show()

def  ls_jieyue():
    def dwjy(t):
        r=np.where(t>=0.0,1.0,0.0)
        return r
    n=np.arange(-10,10)
    plt.ylim(0,3)
    plt.title('u(n)')
    plt.grid(True)
    plt.stem(n,dwjy(n))
    plt.show()

def ls_chongji():
    def dwxl(temp):
        r=np.where(temp==0.0,1.0,0.0)
        return r
    m=np.arange(-10,10)
    plt.ylim(0,3)
    plt.title('δ(n)')
    plt.grid(True)
    plt.stem(m,dwxl(m))
    plt.show()





import tkinter as tk
class App:
    def __init__(self, mygui):
        mygui.title("离散函数图像")
        frame = tk.Frame(mygui)
        frame.pack()
        self = tk.Button(frame, text="离散sin信号", fg="red", command=ls_sin)
        self.pack(side=tk.LEFT)
        self = tk.Button(frame, text="离散ex信号", fg="red", command=ls_exp)
        self.pack(side=tk.LEFT)
        self = tk.Button(frame, text="离散阶跃信号", fg="red", command=ls_jieyue)
        self.pack(side=tk.LEFT)
        self = tk.Button(frame, text="离散冲击信号", fg="red", command=ls_chongji)
        self.pack(side=tk.LEFT)

mygui = tk.Tk()
app = App(mygui)
mygui.mainloop()