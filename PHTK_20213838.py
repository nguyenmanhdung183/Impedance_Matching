import tkinter as tk
from tkinter import ttk
import L
import T
import Pi
def clear_screen(p):
    # Xóa nội dung của các Entry và Text Box
    if(p=="l"):
        text1.delete(1.0, tk.END)
        eline1l.delete(0,tk.END)
        eline2l.delete(0,tk.END)
        eline3l.delete(0,tk.END)
        
    if(p=="t"):
        text2.delete(1.0, tk.END)
        eline1t.delete(0,tk.END)
        eline2t.delete(0,tk.END)
        eline3t.delete(0,tk.END)
        eline4t.delete(0,tk.END)
    if(p=="p"):
        text3.delete(1.0, tk.END)
        eline1p.delete(0,tk.END)
        eline2p.delete(0,tk.END)
        eline3p.delete(0,tk.END)
        eline4p.delete(0,tk.END)

##########################################################
def solveL(loaimach):
    rll_value = float(rll.get())
    zinl_value = float(zinl.get())
    fl_value = float(fl.get())
    text1.delete(1.0, tk.END)

    if(loaimach==1 and zinl_value<rll_value):
        text1.insert(tk.END, "Error")
        return 0
    if(loaimach==2 and zinl_value<rll_value):
        text1.insert(tk.END, "Error")
        return 0
    if(loaimach==3 and zinl_value>rll_value):
        text1.insert(tk.END, "Error")
        return 0
    if(loaimach==4 and zinl_value>rll_value):
        text1.insert(tk.END, "Error")
        return 0
        
    

    L_value=L.solve_L(zinl_value,rll_value,fl_value,loaimach)
    C_value=L.solve_C(zinl_value,rll_value,fl_value,loaimach)
    Q_value=L.solve_Q(zinl_value,rll_value,fl_value,loaimach)


    print=f"L={L_value} (H)\nC={C_value} (F)\nQ={Q_value}"
    text1.insert(tk.END, print)
####################################################
def solveT(loaimach):
    #1 highpass, 2 lowpasss
    text2.delete(1.0, tk.END)
    rlt_value=float(rlt.get())
    zint_value=float(zint.get())
    ft_value=float(ft.get())
    rct_value=float(rct.get())
    if(rct_value<max(zint_value,rlt_value)):
        text2.insert(tk.END,"error")
        return 0
    thongso=T.T_solve(zint_value,rct_value,rlt_value,ft_value,loaimach)
    L1_value=thongso.solve_L1()
    L2_value=thongso.solve_L2()
    C1_value=thongso.solve_C1()
    C2_value=thongso.solve_C2()
    Q1_value=thongso.solve_Q1()
    Q2_value=thongso.solve_Q2()
    
    print=f"L1={L1_value} (H)\nL2={L2_value} (H)\nC1={C1_value} (F)\nC2={C2_value} (F)\nQ1={Q1_value}\nQ2={Q2_value}"
    text2.insert(tk.END, print)

    

####################################################
def solvePi(loaimach):
    #1 highpass, 2 lowpasss

    text3.delete(1.0, tk.END)
    rlp_value=float(rlp.get())
    zinp_value=float(zinp.get())
    fp_value=float(fp.get())
    rcp_value=float(rcp.get())
    if(rcp_value>min(zinp_value,rlp_value)):
        text3.insert(tk.END,"error")
        return 0
    thongso=Pi.Pi_solve(zinp_value,rcp_value,rlp_value,fp_value,loaimach)
    L1_value=thongso.solve_L1()
    L2_value=thongso.solve_L2()
    C1_value=thongso.solve_C1()
    C2_value=thongso.solve_C2()
    Q1_value=thongso.solve_Q1()
    Q2_value=thongso.solve_Q2()
    print=f"L1={L1_value} (H)\nL2={L2_value} (H)\nC1={C1_value} (F)\nC2={C2_value} (F)\nQ1={Q1_value}\nQ2={Q2_value}"
    text3.insert(tk.END, print)

         
# root window
root = tk.Tk()
root.geometry('340x300')
root.title('PHTK DTTT2 20213838')
root.resizable(0,0)
# create a notebook
notebook = ttk.Notebook(root)
notebook.grid(row=0)

# create frames
#1-----------------------------------------------------------------
frame1 = ttk.Frame(notebook, width=340, height=280)

frame1.columnconfigure(2, weight=1)


text1=tk.Text(frame1, height=8, width=40)
text1.grid(columnspan = 3,sticky="w", padx=5)

rll=tk.StringVar()
zinl=tk.StringVar()
ql=tk.StringVar()
fl=tk.StringVar()

line1l = ttk.Label(frame1, text="Zin:")
eline1l = ttk.Entry(frame1, textvariable=zinl)
line1l.grid(row=1, column=0, sticky='w')
eline1l.grid(row=1, column=1, sticky='w')

line2l = ttk.Label(frame1, text="RL:")
eline2l = ttk.Entry(frame1, textvariable=rll)
line2l.grid(row=2, column=0, sticky='w')
eline2l.grid(row=2, column=1, sticky='w')

line3l = ttk.Label(frame1, text="f:")
eline3l = ttk.Entry(frame1, textvariable=fl)
line3l.grid(row=3, column=0, sticky='w')
eline3l.grid(row=3, column=1, sticky='w')

#line4 = ttk.Label(frame1, text="Q:")
#eline4 = ttk.Entry(frame1, textvariable=ql)
#line4.grid(row=4, column=0, sticky='w')
#eline4.grid(row=4, column=1, sticky='w')

button=tk.Button(frame1,text="Pass DC-RS>RL", command=lambda:solveL(1), width=15)
button.grid(column=2,row=1,sticky="w")
button=tk.Button(frame1,text="Block DC-RS>RL",command=lambda:solveL(2),width=15)
button.grid(column=2,row=2,sticky="w")
button=tk.Button(frame1,text="Pass DC-RS<RL",command=lambda:solveL(3),width=15)
button.grid(column=2,row=3,sticky="w")
button=tk.Button(frame1,text="Block DC-RS<RL",command=lambda:solveL(4),width=15)
button.grid(column=2,row=4,sticky="w")
button=tk.Button(frame1,text="Clear", command=lambda:clear_screen("l"),width=10)
button.grid(column=1,row=4,sticky="w")
for i in frame1.winfo_children():
    i.grid(pady=4, padx=6)
    
    
    
    
#2-----------------------------------------------------------------
frame2 = ttk.Frame(notebook, width=340, height=280)
frame2.columnconfigure(2, weight=1)


text2=tk.Text(frame2, height=8, width=40)
text2.grid(columnspan = 3,sticky="w", padx=5)

rlt=tk.StringVar()
zint=tk.StringVar()
ft=tk.StringVar()
rct=tk.StringVar()

line1t = ttk.Label(frame2, text="Zin:")
eline1t = ttk.Entry(frame2, textvariable=zint)
line1t.grid(row=1, column=0, sticky='w')
eline1t.grid(row=1, column=1, sticky='w')

line2t = ttk.Label(frame2, text="RL:")
eline2t = ttk.Entry(frame2, textvariable=rlt)
line2t.grid(row=2, column=0, sticky='w')
eline2t.grid(row=2, column=1, sticky='w')

line3t = ttk.Label(frame2, text="f:")
eline3t = ttk.Entry(frame2, textvariable=ft)
line3t.grid(row=3, column=0, sticky='w')
eline3t.grid(row=3, column=1, sticky='w')

line4t = ttk.Label(frame2, text="Rcenter:")
eline4t = ttk.Entry(frame2, textvariable=rct)
line4t.grid(row=4, column=0, sticky='w')
eline4t.grid(row=4, column=1, sticky='w')

button=tk.Button(frame2,text="High Pass", command=lambda:solveT(1), width=15)
button.grid(column=2,row=1,sticky="w")
button=tk.Button(frame2,text="Low Pass",command=lambda:solveT(2),width=15)
button.grid(column=2,row=2,sticky="w")

button=tk.Button(frame2,text="Clear", command=lambda:clear_screen("t"),width=15)
button.grid(column=2,row=3,sticky="w" )
for i in frame2.winfo_children():
    i.grid(pady=4, padx=6)
    
    
    
    
    
    
#3-----------------------------------------------------------------
frame3 = ttk.Frame(notebook, width=340, height=280)
frame3.columnconfigure(2, weight=1)


text3=tk.Text(frame3, height=8, width=40)
text3.grid(columnspan = 3,sticky="w", padx=5)

rlp=tk.StringVar()
zinp=tk.StringVar()
rcp=tk.StringVar()
fp=tk.StringVar()

line1p = ttk.Label(frame3, text="Zin:")
eline1p = ttk.Entry(frame3, textvariable=zinp)
line1p.grid(row=1, column=0, sticky='w')
eline1p.grid(row=1, column=1, sticky='w')

line2p = ttk.Label(frame3, text="RL:")
eline2p = ttk.Entry(frame3, textvariable=rlp)
line2p.grid(row=2, column=0, sticky='w')
eline2p.grid(row=2, column=1, sticky='w')

line3p = ttk.Label(frame3, text="f:")
eline3p = ttk.Entry(frame3, textvariable=fp)
line3p.grid(row=3, column=0, sticky='w')
eline3p.grid(row=3, column=1, sticky='w')

line4p = ttk.Label(frame3, text="Rcenter:")
eline4p = ttk.Entry(frame3, textvariable=rcp)
line4p.grid(row=4, column=0, sticky='w')
eline4p.grid(row=4, column=1, sticky='w')

button=tk.Button(frame3,text="High Pass", command=lambda:solvePi(1), width=15)
button.grid(column=2,row=1,sticky="w")
button=tk.Button(frame3,text="Low Pass",command=lambda:solvePi(2),width=15)
button.grid(column=2,row=2,sticky="w")

button=tk.Button(frame3,text="Clear", command=lambda:clear_screen("p"),width=15)
button.grid(column=2,row=3,sticky="w" )
for i in frame3.winfo_children():
    i.grid(pady=4, padx=6)

frame1.grid()
frame2.grid()
frame3.grid()


# add frames to notebook

notebook.add(frame1, text='L Matching')
notebook.add(frame2, text='T Matching')
notebook.add(frame3, text='Pi Matching')



root.mainloop()