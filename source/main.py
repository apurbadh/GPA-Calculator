from tkinter import *

root = Tk()
subList = ["English", "Nepali", "Maths", "Opt Maths", "Science", "EPH", "Social", "Computer"]
root.title("GPA Calculator")
row = 0
gpatxt = "    "
def subGPA(marks, type):
    gpaal = ['', 0.8, 1.2,1.6,2.0,2.4,2.8,3.2,3.6,4]
    if type == 'a':
        marks = (marks/75)*100
    elif type == 'b':
        marks = marks * 2
    marks = str(marks)
    if len(marks) == 1:
        return 0.8
    tenthpl = marks[0]
    return gpaal[int(tenthpl)]



for sub in subList:
    Label(root,text=sub + " : ").grid(row=row, column=0)
    row += 1

eng = Entry(root)
nep = Entry(root)
mat = Entry(root)
opt = Entry(root)
sci = Entry(root)
eph = Entry(root)
soc = Entry(root)
com = Entry(root)


allSubVar = [eng, nep, mat, opt, sci, eph, soc, com]

row = 0
for allVar in allSubVar:
    allVar.grid(row=row, column=1)
    row += 1

answer = Label(root, text=gpatxt)
answer.grid(row=8,column=0,columnspan=2)
def pressBut():
    allGPA = []
    i = 0
    engVal = int(eng.get())
    nepVal = int(nep.get())
    matVal = int(mat.get())
    optVal = int(opt.get())
    sciVal = int(sci.get())
    ephVal = int(eph.get())
    socVal = int(soc.get())
    comVal = int(com.get())
    allVal = [engVal, nepVal, matVal, optVal, sciVal, ephVal, socVal, comVal]
    for val in allVal:
        if i in [2,3]:
            type = 'c'
        elif i == 7:
            type = 'b'
        else:
            type = 'a'
        thegpa = subGPA(val, type)
        allGPA.append(thegpa)
        i += 1
    gpa = round(sum(allGPA)/8,2)
    answer.config(text=str(gpa)) 



submBut = Button(root, text="Submit",command=pressBut)
submBut.grid(row=9, column=0, columnspan=2)
root.mainloop()
