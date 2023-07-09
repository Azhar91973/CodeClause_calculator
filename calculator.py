# using tkinter inbuilt library 
import tkinter as Calculator
calculation = ""

#  Function for adding the symbols into the calculator
def add_calculation(symbol):
    global calculation 
    calculation += str(symbol)
    text_result .delete(1.0,"end")
    text_result.insert(1.0,calculation)

# Function for evaluating the expression
def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation)) 
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"Error")
#  Function for clear the text of the calculator
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0,"end")
    pass

root = Calculator.Tk()
# Declaring the Dimensions of the calculator
root.geometry("300x275")

root.title("Calculator") 

# Declaring the text area of the calculator
text_result = Calculator.Text(root,height = 2,width=15,font=("Arial",24),bg="Black",fg="White")
text_result.grid(columnspan=5)


# Declaring the Button's of the calculator 
btn_1 = Calculator.Button(root,text= "1",command=lambda: add_calculation(1),width=5,font=("Arial",14),fg="White",bg="Gray")
btn_1.grid(row=2,column=1)
btn_2 = Calculator.Button(root,text= "2",command=lambda: add_calculation(2),width=5,font=("Arial",14),fg="White",bg="Gray")
btn_2.grid(row=2,column=2)
btn_3 = Calculator.Button(root,text= "3",command=lambda: add_calculation(3),width=5,font=("Arial",14),fg="White",bg="Gray")
btn_3.grid(row=2,column=3)
btn_4 = Calculator.Button(root,text= "4",command=lambda: add_calculation(4),width=5,font=("Arial",14),fg="White",bg="Gray")
btn_4.grid(row=3,column=1)
btn_5 = Calculator.Button(root,text= "5",command=lambda: add_calculation(5),width=5,font=("Arial",14),fg="White",bg="Gray")
btn_5.grid(row=3,column=2)
btn_6 = Calculator.Button(root,text= "6",command=lambda: add_calculation(6),width=5,font=("Arial",14),fg="White",bg="Gray")
btn_6.grid(row=3,column=3)
btn_7 = Calculator.Button(root,text= "7",command=lambda: add_calculation(7),width=5,font=("Arial",14),fg="White",bg="Gray")
btn_7.grid(row=4,column=1)
btn_8 = Calculator.Button(root,text= "8",command=lambda: add_calculation(8),width=5,font=("Arial",14),fg="White",bg="Gray")
btn_8.grid(row=4,column=2)
btn_9 = Calculator.Button(root,text= "9",command=lambda: add_calculation(9),width=5,font=("Arial",14),fg="White",bg="Gray")
btn_9.grid(row=4,column=3)
btn_0 = Calculator.Button(root,text= "0",command=lambda: add_calculation(0),width=5,font=("Arial",14),fg="White",bg="Gray")
btn_0.grid(row=5,column=2)
btn_plus = Calculator.Button(root,text= "+",command=lambda: add_calculation("+"),width=5,font=("Arial",14),fg="black",bg="light Gray")
btn_plus.grid(row=2,column=4) 
btn_sub = Calculator.Button(root,text= "-",command=lambda: add_calculation("-"),width=5,font=("Arial",14),fg="black",bg="light Gray")
btn_sub.grid(row=3,column=4) 
btn_mul = Calculator.Button(root,text= "*",command=lambda: add_calculation("*"),width=5,font=("Arial",14),fg="black",bg="light Gray")
btn_mul.grid(row=4,column=4) 
btn_divide = Calculator.Button(root,text= "/",command=lambda: add_calculation("/"),width=5,font=("Arial",14),fg="black",bg="light Gray")
btn_divide.grid(row=5,column=4) 
btn_openbrace = Calculator.Button(root,text= "(",command=lambda: add_calculation("("),width=5,font=("Arial",14),fg="black",bg="light Gray")
btn_openbrace.grid(row=5,column=1) 
btn_closebrace = Calculator.Button(root,text= ")",command=lambda: add_calculation(")"),width=5,font=("Arial",14),fg="black",bg="light Gray")
btn_closebrace.grid(row=5,column=3)  
btn_clear = Calculator.Button(root,text= "Clear",command= clear_field,width=11,font=("Arial",14),fg="Black",bg="Light Gray")
btn_clear.grid(row=6,column=1,columnspan=2) 
btn_equal = Calculator.Button(root,text= "=",command = evaluate_calculation,width=11,font=("Arial",14),fg="White",bg="Orange")
btn_equal.grid(row=6,column=3,columnspan=2) 
root.mainloop()