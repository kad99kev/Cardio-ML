import tkinter as tt
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as tk
import cardio_ml as ml


def main():

    bg='whitesmoke'
    fg='navy'

    root = Tk()
    root.title("Cardiovascular Disease Examination")
    root.configure(background=bg)
    root.geometry('500x700')

    def popupmsg(msg):
        popup = Tk()
        popup.title("Cardiovascular Disease Probability")
        popup.configure(background=bg)
        popup.geometry('400x100')

        label = Label(popup, text=msg, bg=bg, fg=fg)
        label.pack(side="top", fill="x", pady=10)

        B1 = Button(popup, text="Okay", command = popup.destroy)
        B1.pack()

        popup.mainloop()

    def clicked():
        data = []
        data.append(sel_gen.get())
        data.append(int(txt_hei.get()))
        data.append(int(txt_wei.get()))
        data.append(int(txt_sys.get()))
        data.append(int(txt_dia.get()))
        data.append(com_cho.current()+1)
        data.append(com_glu.current()+1)
        data.append(sel_smo.get())
        data.append(sel_alc.get())
        data.append(sel_act.get())
        data.append(int(txt_age.get()))
        print(data)
        prob = ml.predict([data])
        popupmsg(f'Probability of CVD is {prob}%')



    lbl_age = Label(root, text="Enter Age (in Years)", bg=bg, fg=fg)
    lbl_age.grid(row=0,sticky=NW)
    txt_age = Entry(root, width=10, bg=bg, fg=fg)
    txt_age.grid(row=1,sticky=NW, padx=10, pady=5)

    sel_gen = IntVar()
    lbl_gen = Label(root, text="Select Gender", bg=bg, fg=fg)
    lbl_gen.grid(row=2, sticky=SW, padx=10)
    rad_m = Radiobutton(root,text='Male', value=2, variable=sel_gen, bg=bg, fg=fg)
    rad_f = Radiobutton(root,text='Female', value=1, variable=sel_gen, bg=bg, fg=fg)
    rad_m.grid(row=3, column=0, sticky=NW, padx=10)
    rad_f.grid(row=3, column=1, sticky=NW, padx=10)

    lbl_hei = Label(root, text="Enter Height (in cms)", bg=bg, fg=fg)
    lbl_hei.grid(row=4,sticky=NW)
    txt_hei = Entry(root, width=10, bg=bg, fg=fg)
    txt_hei.grid(row=5,sticky=NW, padx=10, pady=5)


    lbl_wei = Label(root, text="Enter Weight (in kgs)", bg=bg, fg=fg)
    lbl_wei.grid(row=6,sticky=NW)
    txt_wei = Entry(root, width=10, bg=bg, fg=fg)
    txt_wei.grid(row=7,sticky=NW, padx=10, pady=5)

    lbl_sys = Label(root, text="Enter Systolic Pressure (in mmHg)", bg=bg, fg=fg)
    lbl_sys.grid(row=8,sticky=NW)
    txt_sys = Entry(root, width=10, bg=bg, fg=fg)
    txt_sys.grid(row=9,sticky=NW, padx=10, pady=5)

    lbl_dia = Label(root, text="Enter Diastolic Pressure (in mmHg)", bg=bg, fg=fg)
    lbl_dia.grid(row=10,sticky=NW)
    txt_dia = Entry(root, width=10, bg=bg, fg=fg)
    txt_dia.grid(row=11,sticky=NW, padx=10, pady=5)

    lbl_cho = Label(root, text="Choose Cholesterol Level", bg=bg, fg=fg)
    lbl_cho.grid(row=12,sticky=NW)
    com_cho = tk.Combobox(root, state='readonly')
    com_cho.config(background=bg)
    com_cho['values']= ("Normal", "Above Normal", "Well Above Normal")
    com_cho.current(0) #set the selected item
    com_cho.grid(row=13)

    lbl_glu = Label(root, text="Choose Glucose Level", bg=bg, fg=fg)
    lbl_glu.grid(row=14,sticky=NW)
    com_glu = tk.Combobox(root, state='readonly')
    com_glu.config(background=bg)
    com_glu['values']= ("Normal", "Above Normal", "Well Above Normal")
    com_glu.current(0) #set the selected item
    com_glu.grid(row=15)

    sel_smo = IntVar()
    lbl_smo = Label(root, text="Smoking", bg=bg, fg=fg)
    lbl_smo.grid(row=16,sticky=NW)
    rad_smoy = Radiobutton(root,text='Yes', value=1, variable=sel_smo, bg=bg, fg=fg)
    rad_smon = Radiobutton(root,text='No', value=0, variable=sel_smo, bg=bg, fg=fg)
    rad_smoy.grid(row=17, column=0, sticky=NW, padx=10)
    rad_smon.grid(row=18, column=1, sticky=NW, padx=10)

    sel_alc = IntVar()
    lbl_alc = Label(root, text="Alochol Intake", bg=bg, fg=fg)
    lbl_alc.grid(row=19,sticky=NW)
    rad_alcy = Radiobutton(root,text='Yes', value=1, variable=sel_alc, bg=bg, fg=fg)
    rad_alcn = Radiobutton(root,text='No', value=0, variable=sel_alc, bg=bg, fg=fg)
    rad_alcy.grid(row=20, column=0, sticky=NW, padx=10)
    rad_alcn.grid(row=21, column=1, sticky=NW, padx=10)

    sel_act = IntVar()
    lbl_act = Label(root, text="Active", bg=bg, fg=fg)
    lbl_act.grid(row=22,sticky=NW)
    rad_acty = Radiobutton(root,text='Yes', value=1, variable=sel_act, bg=bg, fg=fg)
    rad_actn = Radiobutton(root,text='No', value=0, variable=sel_act, bg=bg, fg=fg)
    rad_acty.grid(row=23, column=0, sticky=NW, padx=10)
    rad_actn.grid(row=24, column=1, sticky=NW, padx=10)

    btn = Button(root, text="Enter", command=clicked, bg=bg)
    btn.grid(row=25, column=0, padx=10, pady=10)

    root.mainloop()

main()
