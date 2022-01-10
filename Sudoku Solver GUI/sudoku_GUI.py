import tkinter as tk
from tkinter import ttk
from sys import path
from tkinter.messagebox import showerror  #FOR EXCEPTION HANDLING
#path.append("e:\\python\\lib\\site-packages")
#path.append("C:\\Users\\alkiv\\AppData\Roaming\\Python\\Python39\\site-packages")
#enter custom path if needed
import sudoku_solver as sdk
from tkinter import scrolledtext

def report_callback_exception(self, exc, val, tb):
    showerror("Error", message=str(val))

def solve():
    sudoku_numbers=[]
    for row in range(9):
        sudoku_numbers.append([])
        for square in range((row//3)*3,(row//3 + 1)*3):
            if row==0 or row==3 or row==6:
                for col in range(3):
                    eval('sudoku_numbers['+str(row)+'].append(sqr_'+str(square)+'_'+str(col+1)+'.get())')
            elif row==1 or row==4 or row==7:
                for col in range(3,6):
                    eval('sudoku_numbers['+str(row)+'].append(sqr_'+str(square)+'_'+str(col+1)+'.get())')
            else:
                for col in range(6,9):
                    eval('sudoku_numbers['+str(row)+'].append(sqr_'+str(square)+'_'+str(col+1)+'.get())')

    # for i in range(len(sudoku_numbers)):
    #     print(sudoku_numbers[i])
    # print('')
    solution_print=sdk.sudoku_solver(sudoku_numbers)
    # print(solution_print)
    solution_txt.insert(tk.END, solution_print + '\n', ("centered",))
    solution_txt.tag_configure("centered", justify="center")




#FUNC FOR EXCEPTION HANDLING
tk.Tk.report_callback_exception = report_callback_exception

#MAIN WINDOW PROPERTIES
window=tk.Tk()
window.attributes('-alpha',1)
window.iconbitmap('sudoku.ico')
window.title("SUDOKU Solver")
window.geometry('700x350')
window.rowconfigure((0,1,2,3), weight=1)
window.columnconfigure((0,1,2,3), weight=1)


#FRAME 1 
frame_1=ttk.Frame(window)
frame_1.grid(row=0,column=0,sticky='nw',padx=5,pady=5)
frame_1.rowconfigure((0,1,2), weight=1)
frame_1.columnconfigure((0,1,2), weight=1)

sqr_0_1=tk.IntVar(frame_1,0)
sqr_0_1_entry=ttk.Entry(frame_1,textvariable=sqr_0_1,justify='center')
sqr_0_1_entry.grid(row=0,column=0,sticky='nw',padx=1,pady=1)

sqr_0_2=tk.IntVar(frame_1,0)
sqr_0_2_entry=ttk.Entry(frame_1,textvariable=sqr_0_2,justify='center')
sqr_0_2_entry.grid(row=0,column=1,sticky='n',padx=1,pady=1)

sqr_0_3=tk.IntVar(frame_1,0)
sqr_0_3_entry=ttk.Entry(frame_1,textvariable=sqr_0_3,justify='center')
sqr_0_3_entry.grid(row=0,column=2,sticky='ne',padx=1,pady=1)

sqr_0_4=tk.IntVar(frame_1,0)
sqr_0_4_entry=ttk.Entry(frame_1,textvariable=sqr_0_4,justify='center')
sqr_0_4_entry.grid(row=1,column=0,sticky='w',padx=1,pady=1)

sqr_0_5=tk.IntVar(frame_1,0)
sqr_0_5_entry=ttk.Entry(frame_1,textvariable=sqr_0_5,justify='center')
sqr_0_5_entry.grid(row=1,column=1,sticky='',padx=1,pady=1)

sqr_0_6=tk.IntVar(frame_1,0)
sqr_0_6_entry=ttk.Entry(frame_1,textvariable=sqr_0_6,justify='center')
sqr_0_6_entry.grid(row=1,column=2,sticky='e',padx=1,pady=1)

sqr_0_7=tk.IntVar(frame_1,0)
sqr_0_7_entry=ttk.Entry(frame_1,textvariable=sqr_0_7,justify='center')
sqr_0_7_entry.grid(row=2,column=0,sticky='sw',padx=1,pady=1)

sqr_0_8=tk.IntVar(frame_1,0)
sqr_0_8_entry=ttk.Entry(frame_1,textvariable=sqr_0_8,justify='center')
sqr_0_8_entry.grid(row=2,column=1,sticky='s',padx=1,pady=1)

sqr_0_9=tk.IntVar(frame_1,0)
sqr_0_9_entry=ttk.Entry(frame_1,textvariable=sqr_0_9,justify='center')
sqr_0_9_entry.grid(row=2,column=2,sticky='se',padx=1,pady=1)


#FRAME 2
frame_2=ttk.Frame(window)
frame_2.grid(row=0,column=1,sticky='n',padx=5,pady=5)
frame_2.rowconfigure((0,1,2), weight=1)
frame_2.columnconfigure((0,1,2), weight=1)

sqr_1_1=tk.IntVar(frame_2,0)
sqr_1_1_entry=ttk.Entry(frame_2,textvariable=sqr_1_1,justify='center')
sqr_1_1_entry.grid(row=0,column=0,sticky='nw',padx=1,pady=1)

sqr_1_2=tk.IntVar(frame_2,0)
sqr_1_2_entry=ttk.Entry(frame_2,textvariable=sqr_1_2,justify='center')
sqr_1_2_entry.grid(row=0,column=1,sticky='n',padx=1,pady=1)

sqr_1_3=tk.IntVar(frame_2,0)
sqr_1_3_entry=ttk.Entry(frame_2,textvariable=sqr_1_3,justify='center')
sqr_1_3_entry.grid(row=0,column=2,sticky='ne',padx=1,pady=1)

sqr_1_4=tk.IntVar(frame_2,0)
sqr_1_4_entry=ttk.Entry(frame_2,textvariable=sqr_1_4,justify='center')
sqr_1_4_entry.grid(row=1,column=0,sticky='w',padx=1,pady=1)

sqr_1_5=tk.IntVar(frame_2,0)
sqr_1_5_entry=ttk.Entry(frame_2,textvariable=sqr_1_5,justify='center')
sqr_1_5_entry.grid(row=1,column=1,sticky='',padx=1,pady=1)

sqr_1_6=tk.IntVar(frame_2,0)
sqr_1_6_entry=ttk.Entry(frame_2,textvariable=sqr_1_6,justify='center')
sqr_1_6_entry.grid(row=1,column=2,sticky='e',padx=1,pady=1)

sqr_1_7=tk.IntVar(frame_2,0)
sqr_1_7_entry=ttk.Entry(frame_2,textvariable=sqr_1_7,justify='center')
sqr_1_7_entry.grid(row=2,column=0,sticky='sw',padx=1,pady=1)

sqr_1_8=tk.IntVar(frame_2,0)
sqr_1_8_entry=ttk.Entry(frame_2,textvariable=sqr_1_8,justify='center')
sqr_1_8_entry.grid(row=2,column=1,sticky='s',padx=1,pady=1)

sqr_1_9=tk.IntVar(frame_2,0)
sqr_1_9_entry=ttk.Entry(frame_2,textvariable=sqr_1_9,justify='center')
sqr_1_9_entry.grid(row=2,column=2,sticky='se',padx=1,pady=1)


#FRAME 3
frame_3=ttk.Frame(window)
frame_3.grid(row=0,column=2,sticky='ne',padx=5,pady=5)
frame_3.rowconfigure((0,1,2), weight=1)
frame_3.columnconfigure((0,1,2), weight=1)

sqr_2_1=tk.IntVar(frame_3,0)
sqr_2_1_entry=ttk.Entry(frame_3,textvariable=sqr_2_1,justify='center')
sqr_2_1_entry.grid(row=0,column=0,sticky='nw',padx=1,pady=1)

sqr_2_2=tk.IntVar(frame_3,0)
sqr_2_2_entry=ttk.Entry(frame_3,textvariable=sqr_2_2,justify='center')
sqr_2_2_entry.grid(row=0,column=1,sticky='n',padx=1,pady=1)

sqr_2_3=tk.IntVar(frame_3,0)
sqr_2_3_entry=ttk.Entry(frame_3,textvariable=sqr_2_3,justify='center')
sqr_2_3_entry.grid(row=0,column=2,sticky='ne',padx=1,pady=1)

sqr_2_4=tk.IntVar(frame_3,0)
sqr_2_4_entry=ttk.Entry(frame_3,textvariable=sqr_2_4,justify='center')
sqr_2_4_entry.grid(row=1,column=0,sticky='w',padx=1,pady=1)

sqr_2_5=tk.IntVar(frame_3,0)
sqr_2_5_entry=ttk.Entry(frame_3,textvariable=sqr_2_5,justify='center')
sqr_2_5_entry.grid(row=1,column=1,sticky='',padx=1,pady=1)

sqr_2_6=tk.IntVar(frame_3,0)
sqr_2_6_entry=ttk.Entry(frame_3,textvariable=sqr_2_6,justify='center')
sqr_2_6_entry.grid(row=1,column=2,sticky='e',padx=1,pady=1)

sqr_2_7=tk.IntVar(frame_3,0)
sqr_2_7_entry=ttk.Entry(frame_3,textvariable=sqr_2_7,justify='center')
sqr_2_7_entry.grid(row=2,column=0,sticky='sw',padx=1,pady=1)

sqr_2_8=tk.IntVar(frame_3,0)
sqr_2_8_entry=ttk.Entry(frame_3,textvariable=sqr_2_8,justify='center')
sqr_2_8_entry.grid(row=2,column=1,sticky='s',padx=1,pady=1)

sqr_2_9=tk.IntVar(frame_3,0)
sqr_2_9_entry=ttk.Entry(frame_3,textvariable=sqr_2_9,justify='center')
sqr_2_9_entry.grid(row=2,column=2,sticky='se',padx=1,pady=1)

###########   SECOND ROW   ####################
###############################################
###############################################

#FRAME 4
frame_4=ttk.Frame(window)
frame_4.grid(row=1,column=0,sticky='w',padx=5,pady=5)
frame_4.rowconfigure((0,1,2), weight=1)
frame_4.columnconfigure((0,1,2), weight=1)

sqr_3_1=tk.IntVar(frame_4,0)
sqr_3_1_entry=ttk.Entry(frame_4,textvariable=sqr_3_1,justify='center')
sqr_3_1_entry.grid(row=0,column=0,sticky='nw',padx=1,pady=1)

sqr_3_2=tk.IntVar(frame_4,0)
sqr_3_2_entry=ttk.Entry(frame_4,textvariable=sqr_3_2,justify='center')
sqr_3_2_entry.grid(row=0,column=1,sticky='n',padx=1,pady=1)

sqr_3_3=tk.IntVar(frame_4,0)
sqr_3_3_entry=ttk.Entry(frame_4,textvariable=sqr_3_3,justify='center')
sqr_3_3_entry.grid(row=0,column=2,sticky='ne',padx=1,pady=1)

sqr_3_4=tk.IntVar(frame_4,0)
sqr_3_4_entry=ttk.Entry(frame_4,textvariable=sqr_3_4,justify='center')
sqr_3_4_entry.grid(row=1,column=0,sticky='w',padx=1,pady=1)

sqr_3_5=tk.IntVar(frame_4,0)
sqr_3_5_entry=ttk.Entry(frame_4,textvariable=sqr_3_5,justify='center')
sqr_3_5_entry.grid(row=1,column=1,sticky='',padx=1,pady=1)

sqr_3_6=tk.IntVar(frame_4,0)
sqr_3_6_entry=ttk.Entry(frame_4,textvariable=sqr_3_6,justify='center')
sqr_3_6_entry.grid(row=1,column=2,sticky='e',padx=1,pady=1)

sqr_3_7=tk.IntVar(frame_4,0)
sqr_3_7_entry=ttk.Entry(frame_4,textvariable=sqr_3_7,justify='center')
sqr_3_7_entry.grid(row=2,column=0,sticky='',padx=1,pady=1)

sqr_3_8=tk.IntVar(frame_4,0)
sqr_3_8_entry=ttk.Entry(frame_4,textvariable=sqr_3_8,justify='center')
sqr_3_8_entry.grid(row=2,column=1,sticky='sw',padx=1,pady=1)

sqr_3_9=tk.IntVar(frame_4,0)
sqr_3_9_entry=ttk.Entry(frame_4,textvariable=sqr_3_9,justify='center')
sqr_3_9_entry.grid(row=2,column=2,sticky='sw',padx=1,pady=1)


#FRAME 5
frame_5=ttk.Frame(window)
frame_5.grid(row=1,column=1,sticky='',padx=5,pady=5)
frame_5.rowconfigure((0,1,2), weight=1)
frame_5.columnconfigure((0,1,2), weight=1)

sqr_4_1=tk.IntVar(frame_5,0)
sqr_4_1_entry=ttk.Entry(frame_5,textvariable=sqr_4_1,justify='center')
sqr_4_1_entry.grid(row=0,column=0,sticky='nw',padx=1,pady=1)

sqr_4_2=tk.IntVar(frame_5,0)
sqr_4_2_entry=ttk.Entry(frame_5,textvariable=sqr_4_2,justify='center')
sqr_4_2_entry.grid(row=0,column=1,sticky='n',padx=1,pady=1)

sqr_4_3=tk.IntVar(frame_5,0)
sqr_4_3_entry=ttk.Entry(frame_5,textvariable=sqr_4_3,justify='center')
sqr_4_3_entry.grid(row=0,column=2,sticky='ne',padx=1,pady=1)

sqr_4_4=tk.IntVar(frame_5,0)
sqr_4_4_entry=ttk.Entry(frame_5,textvariable=sqr_4_4,justify='center')
sqr_4_4_entry.grid(row=1,column=0,sticky='w',padx=1,pady=1)

sqr_4_5=tk.IntVar(frame_5,0)
sqr_4_5_entry=ttk.Entry(frame_5,textvariable=sqr_4_5,justify='center')
sqr_4_5_entry.grid(row=1,column=1,sticky='',padx=1,pady=1)

sqr_4_6=tk.IntVar(frame_5,0)
sqr_4_6_entry=ttk.Entry(frame_5,textvariable=sqr_4_6,justify='center')
sqr_4_6_entry.grid(row=1,column=2,sticky='e',padx=1,pady=1)

sqr_4_7=tk.IntVar(frame_5,0)
sqr_4_7_entry=ttk.Entry(frame_5,textvariable=sqr_4_7,justify='center')
sqr_4_7_entry.grid(row=2,column=0,sticky='',padx=1,pady=1)

sqr_4_8=tk.IntVar(frame_5,0)
sqr_4_8_entry=ttk.Entry(frame_5,textvariable=sqr_4_8,justify='center')
sqr_4_8_entry.grid(row=2,column=1,sticky='sw',padx=1,pady=1)

sqr_4_9=tk.IntVar(frame_5,0)
sqr_4_9_entry=ttk.Entry(frame_5,textvariable=sqr_4_9,justify='center')
sqr_4_9_entry.grid(row=2,column=2,sticky='sw',padx=1,pady=1)


#FRAME 6
frame_6=ttk.Frame(window)
frame_6.grid(row=1,column=2,sticky='e',padx=5,pady=5)
frame_6.rowconfigure((0,1,2), weight=1)
frame_6.columnconfigure((0,1,2), weight=1)

sqr_5_1=tk.IntVar(frame_6,0)
sqr_5_1_entry=ttk.Entry(frame_6,textvariable=sqr_5_1,justify='center')
sqr_5_1_entry.grid(row=0,column=0,sticky='nw',padx=1,pady=1)

sqr_5_2=tk.IntVar(frame_6,0)
sqr_5_2_entry=ttk.Entry(frame_6,textvariable=sqr_5_2,justify='center')
sqr_5_2_entry.grid(row=0,column=1,sticky='n',padx=1,pady=1)

sqr_5_3=tk.IntVar(frame_6,0)
sqr_5_3_entry=ttk.Entry(frame_6,textvariable=sqr_5_3,justify='center')
sqr_5_3_entry.grid(row=0,column=2,sticky='ne',padx=1,pady=1)

sqr_5_4=tk.IntVar(frame_6,0)
sqr_5_4_entry=ttk.Entry(frame_6,textvariable=sqr_5_4,justify='center')
sqr_5_4_entry.grid(row=1,column=0,sticky='w',padx=1,pady=1)

sqr_5_5=tk.IntVar(frame_6,0)
sqr_5_5_entry=ttk.Entry(frame_6,textvariable=sqr_5_5,justify='center')
sqr_5_5_entry.grid(row=1,column=1,sticky='',padx=1,pady=1)

sqr_5_6=tk.IntVar(frame_6,0)
sqr_5_6_entry=ttk.Entry(frame_6,textvariable=sqr_5_6,justify='center')
sqr_5_6_entry.grid(row=1,column=2,sticky='e',padx=1,pady=1)

sqr_5_7=tk.IntVar(frame_6,0)
sqr_5_7_entry=ttk.Entry(frame_6,textvariable=sqr_5_7,justify='center')
sqr_5_7_entry.grid(row=2,column=0,sticky='',padx=1,pady=1)

sqr_5_8=tk.IntVar(frame_6,0)
sqr_5_8_entry=ttk.Entry(frame_6,textvariable=sqr_5_8,justify='center')
sqr_5_8_entry.grid(row=2,column=1,sticky='sw',padx=1,pady=1)

sqr_5_9=tk.IntVar(frame_6,0)
sqr_5_9_entry=ttk.Entry(frame_6,textvariable=sqr_5_9,justify='center')
sqr_5_9_entry.grid(row=2,column=2,sticky='sw',padx=1,pady=1)


###########   THIRD ROW   ####################
###############################################
###############################################

#FRAME 7
frame_7=ttk.Frame(window)
frame_7.grid(row=2,column=0,sticky='sw',padx=5,pady=5)
frame_7.rowconfigure((0,1,2), weight=1)
frame_7.columnconfigure((0,1,2), weight=1)

sqr_6_1=tk.IntVar(frame_7,0)
sqr_6_1_entry=ttk.Entry(frame_7,textvariable=sqr_6_1,justify='center')
sqr_6_1_entry.grid(row=0,column=0,sticky='nw',padx=1,pady=1)

sqr_6_2=tk.IntVar(frame_7,0)
sqr_6_2_entry=ttk.Entry(frame_7,textvariable=sqr_6_2,justify='center')
sqr_6_2_entry.grid(row=0,column=1,sticky='n',padx=1,pady=1)

sqr_6_3=tk.IntVar(frame_7,0)
sqr_6_3_entry=ttk.Entry(frame_7,textvariable=sqr_6_3,justify='center')
sqr_6_3_entry.grid(row=0,column=2,sticky='ne',padx=1,pady=1)

sqr_6_4=tk.IntVar(frame_7,0)
sqr_6_4_entry=ttk.Entry(frame_7,textvariable=sqr_6_4,justify='center')
sqr_6_4_entry.grid(row=1,column=0,sticky='w',padx=1,pady=1)

sqr_6_5=tk.IntVar(frame_7,0)
sqr_6_5_entry=ttk.Entry(frame_7,textvariable=sqr_6_5,justify='center')
sqr_6_5_entry.grid(row=1,column=1,sticky='',padx=1,pady=1)

sqr_6_6=tk.IntVar(frame_7,0)
sqr_6_6_entry=ttk.Entry(frame_7,textvariable=sqr_6_6,justify='center')
sqr_6_6_entry.grid(row=1,column=2,sticky='e',padx=1,pady=1)

sqr_6_7=tk.IntVar(frame_7,0)
sqr_6_7_entry=ttk.Entry(frame_7,textvariable=sqr_6_7,justify='center')
sqr_6_7_entry.grid(row=2,column=0,sticky='',padx=1,pady=1)

sqr_6_8=tk.IntVar(frame_7,0)
sqr_6_8_entry=ttk.Entry(frame_7,textvariable=sqr_6_8,justify='center')
sqr_6_8_entry.grid(row=2,column=1,sticky='sw',padx=1,pady=1)

sqr_6_9=tk.IntVar(frame_7,0)
sqr_6_9_entry=ttk.Entry(frame_7,textvariable=sqr_6_9,justify='center')
sqr_6_9_entry.grid(row=2,column=2,sticky='sw',padx=1,pady=1)


#FRAME 8
frame_8=ttk.Frame(window)
frame_8.grid(row=2,column=1,sticky='s',padx=5,pady=5)
frame_8.rowconfigure((0,1,2), weight=1)
frame_8.columnconfigure((0,1,2), weight=1)

sqr_7_1=tk.IntVar(frame_8,0)
sqr_7_1_entry=ttk.Entry(frame_8,textvariable=sqr_7_1,justify='center')
sqr_7_1_entry.grid(row=0,column=0,sticky='nw',padx=1,pady=1)

sqr_7_2=tk.IntVar(frame_8,0)
sqr_7_2_entry=ttk.Entry(frame_8,textvariable=sqr_7_2,justify='center')
sqr_7_2_entry.grid(row=0,column=1,sticky='n',padx=1,pady=1)

sqr_7_3=tk.IntVar(frame_8,0)
sqr_7_3_entry=ttk.Entry(frame_8,textvariable=sqr_7_3,justify='center')
sqr_7_3_entry.grid(row=0,column=2,sticky='ne',padx=1,pady=1)

sqr_7_4=tk.IntVar(frame_8,0)
sqr_7_4_entry=ttk.Entry(frame_8,textvariable=sqr_7_4,justify='center')
sqr_7_4_entry.grid(row=1,column=0,sticky='w',padx=1,pady=1)

sqr_7_5=tk.IntVar(frame_8,0)
sqr_7_5_entry=ttk.Entry(frame_8,textvariable=sqr_7_5,justify='center')
sqr_7_5_entry.grid(row=1,column=1,sticky='',padx=1,pady=1)

sqr_7_6=tk.IntVar(frame_8,0)
sqr_7_6_entry=ttk.Entry(frame_8,textvariable=sqr_7_6,justify='center')
sqr_7_6_entry.grid(row=1,column=2,sticky='e',padx=1,pady=1)

sqr_7_7=tk.IntVar(frame_8,0)
sqr_7_7_entry=ttk.Entry(frame_8,textvariable=sqr_7_7,justify='center')
sqr_7_7_entry.grid(row=2,column=0,sticky='',padx=1,pady=1)

sqr_7_8=tk.IntVar(frame_8,0)
sqr_7_8_entry=ttk.Entry(frame_8,textvariable=sqr_7_8,justify='center')
sqr_7_8_entry.grid(row=2,column=1,sticky='sw',padx=1,pady=1)

sqr_7_9=tk.IntVar(frame_8,0)
sqr_7_9_entry=ttk.Entry(frame_8,textvariable=sqr_7_9,justify='center')
sqr_7_9_entry.grid(row=2,column=2,sticky='sw',padx=1,pady=1)


#FRAME 9
frame_9=ttk.Frame(window)
frame_9.grid(row=2,column=2,sticky='se',padx=5,pady=5)
frame_9.rowconfigure((0,1,2), weight=1)
frame_9.columnconfigure((0,1,2), weight=1)

sqr_8_1=tk.IntVar(frame_9,0)
sqr_8_1_entry=ttk.Entry(frame_9,textvariable=sqr_8_1,justify='center')
sqr_8_1_entry.grid(row=0,column=0,sticky='nw',padx=1,pady=1)

sqr_8_2=tk.IntVar(frame_9,0)
sqr_8_2_entry=ttk.Entry(frame_9,textvariable=sqr_8_2,justify='center')
sqr_8_2_entry.grid(row=0,column=1,sticky='n',padx=1,pady=1)

sqr_8_3=tk.IntVar(frame_9,0)
sqr_8_3_entry=ttk.Entry(frame_9,textvariable=sqr_8_3,justify='center')
sqr_8_3_entry.grid(row=0,column=2,sticky='ne',padx=1,pady=1)

sqr_8_4=tk.IntVar(frame_9,0)
sqr_8_4_entry=ttk.Entry(frame_9,textvariable=sqr_8_4,justify='center')
sqr_8_4_entry.grid(row=1,column=0,sticky='w',padx=1,pady=1)

sqr_8_5=tk.IntVar(frame_9,0)
sqr_8_5_entry=ttk.Entry(frame_9,textvariable=sqr_8_5,justify='center')
sqr_8_5_entry.grid(row=1,column=1,sticky='',padx=1,pady=1)

sqr_8_6=tk.IntVar(frame_9,0)
sqr_8_6_entry=ttk.Entry(frame_9,textvariable=sqr_8_6,justify='center')
sqr_8_6_entry.grid(row=1,column=2,sticky='e',padx=1,pady=1)

sqr_8_7=tk.IntVar(frame_9,0)
sqr_8_7_entry=ttk.Entry(frame_9,textvariable=sqr_8_7,justify='center')
sqr_8_7_entry.grid(row=2,column=0,sticky='',padx=1,pady=1)

sqr_8_8=tk.IntVar(frame_9,0)
sqr_8_8_entry=ttk.Entry(frame_9,textvariable=sqr_8_8,justify='center')
sqr_8_8_entry.grid(row=2,column=1,sticky='sw',padx=1,pady=1)

sqr_8_9=tk.IntVar(frame_9,0)
sqr_8_9_entry=ttk.Entry(frame_9,textvariable=sqr_8_9,justify='center')
sqr_8_9_entry.grid(row=2,column=2,sticky='sw',padx=1,pady=1)


#SOLVER BUTTON
frame_10=ttk.Frame(window)
frame_10.grid(row=3,column=0,sticky='sw',padx=5,pady=5)
frame_10.rowconfigure(0, weight=1)
frame_10.columnconfigure(0, weight=1)

solve=ttk.Button(frame_10,text='Solve',command=solve)
solve.grid(row=0,column=0,sticky='w',pady=5,padx=5)

#FRAME 0 SOLUTION
frame_0=ttk.Frame(window)
frame_0.grid(row=0,column=3,sticky='nsew',padx=5,pady=5,rowspan=3,columnspan=1)
frame_0.rowconfigure(0, weight=1)
frame_0.columnconfigure(0, weight=1)
#CONSOLE OUTPUT
solution_txt=scrolledtext.ScrolledText(frame_0,height=5,font = ("Consolas",11))
solution_txt.grid(row=0,column=0,sticky='nsew',padx=5,pady=5)





window.mainloop()