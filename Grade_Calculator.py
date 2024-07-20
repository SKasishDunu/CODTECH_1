# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 09:11:32 2024

@author: Kasish
"""

import tkinter
from tkinter import *

root=Tk()
root.title("Grade Calculator") 
root.geometry("500x500")

def Calculation():
    subject_1=int(subject1_entry.get())
    subject_2=int(subject2_entry.get())
    subject_3=int(subject3_entry.get())
    subject_4=int(subject4_entry.get())
    subject_5=int(subject5_entry.get())
    if subject_1<33 or  subject_2<33 or subject_3<33 or subject_4<33 or subject_5<33:
        Label(root, text="FAIL", font="arial 15 bold", fg="red").place(x=250, y=370)
    elif subject_1<101 or  subject_2<101 or subject_3<101 or subject_4<101 or subject_5<101:
        total=(subject_1+ subject_2+ subject_3+ subject_4+ subject_5)
        percent=total/5
        if percent<=100 and percent>=90:
            grade="O"
        elif percent<90 and percent>=80:
            grade="A+"
        elif percent<80 and percent>=70:
            grade="A"
        elif percent<70 and percent>=60:
            grade="B+"
        elif percent<60 and percent>=50:
            grade="B"
        elif percent<50 and percent>=40:
            grade="C"
        else:
            grade="D"
        Label(root, text=f"{percent}%", font="arial 15 bold").place(x=250, y=270)
        Label(root, text=f"{grade}", font="arial 15 bold").place(x=250, y=320)
        Label(root, text="PASS", font="arial 15 bold", fg="blue").place(x=250, y=370)
    else:
        Label(root, text="INVALID", font="arial 15 bold", fg="red").place(x=250, y=370)
    







sub1= Label(root, text="Subject 1 : ", font="Arial 10")
sub2= Label(root, text="Subject 2 : ", font="Arial 10")
sub3= Label(root, text="Subject 3 : ", font="Arial 10")
sub4= Label(root, text="Subject 4 : ", font="Arial 10")
sub5= Label(root, text="Subject 5 : ", font="Arial 10")
percentage= Label(root, text="Percentage : ", font="Arial 10")
grade= Label(root, text="Grade : ", font="Arial 10")
result= Label(root, text="Result : ", font="Arial 10")

sub1.place(x=50, y=20)
sub2.place(x=50, y=70)
sub3.place(x=50, y=120)
sub4.place(x=50, y=170)
sub5.place(x=50, y=220)
percentage.place(x=50, y=270)
grade.place(x=50, y=320)
result.place(x=50, y=370)

subject1_value=StringVar()
subject2_value=StringVar()
subject3_value=StringVar()
subject4_value=StringVar()
subject5_value=StringVar()

subject1_entry=Entry(root,textvariable=subject1_value,font="Arial 15", width=15)
subject2_entry=Entry(root,textvariable=subject2_value,font="Arial 15", width=15)
subject3_entry=Entry(root,textvariable=subject3_value,font="Arial 15", width=15)
subject4_entry=Entry(root,textvariable=subject4_value,font="Arial 15", width=15)
subject5_entry=Entry(root,textvariable=subject5_value,font="Arial 15", width=15)

subject1_entry.place(x=250, y=20)
subject2_entry.place(x=250, y=70)
subject3_entry.place(x=250, y=120)
subject4_entry.place(x=250, y=170)
subject5_entry.place(x=250, y=220)

Button(text="Calculate", font="Arial 15", bg="white", bd=10, command=Calculation).place(x=50, y=420)
Button(text="Exit", font="Arial 15", bg="white", bd=10, width=8, command=root.destroy).place(x=330, y=420)








root.mainloop()
































