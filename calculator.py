
import tkinter as tk
def print_Hello():
    num1= eval(user_input1.get())
    num2= eval(user_input2.get())
    result = num1 + num2
    output.config(text=f'The sum of {num1} and {num2} is {result}')

# output.config(text='Hello Garima')


root = tk.Tk()
root.title='Calculator'
root.geometry('550x600')
root.config(bg='white')



heading = tk.Label(text='Calculator',font=('Harlow Soild Italic',60),
                   bg='white',fg='#ef233c')
heading.pack(pady=15)

tk.Label(text='Enter Number 1:',font=('Harlow Soild Italic',30),
                   bg='white',fg='#8d99ae').pack()



user_input1= tk.Entry(font=('Harlow Soild Italic',20),bg='#98c1d9',width=30)
user_input1.pack(pady=10)

tk.Label(text='Enter Number 2:',font=('Harlow Soild Italic',30),
                   bg='white',fg='#8d99ae').pack()

user_input2= tk.Entry(font=('Harlow Soild Italic',20),bg='#98c1d9',width=30)
user_input2.pack(pady=10)

btn=tk.Button(text='Calculator',font=('Harlow Soild Italic',60),
                   bg='white',fg='#ef233c',width=18,relief='solid',command=print_Hello)

btn.pack()


output = tk.Label(text='The Sum of 10 and 20 is 30',font=('Harlow Soild Italic',20),
                bg='white',fg='#ef233c')
output.pack(pady=20)
root.mainloop()


