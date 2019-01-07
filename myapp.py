import tkinter as tk
from example import *


class MyApp:
    stroka = ''
    n = 0
    a = ['']
    index = 0

    def __init__(self, master):
        self.master = master
        self.screen = tk.Label(bg='#ccc')
        self.screen['text'] = 'qeqweqw'


        self.button = tk.Button(text='1', command=lambda: self.take_button(1))
        self.button1 = tk.Button(text='2', command=lambda: self.take_button(2))
        self.button2 = tk.Button(text='3', command=lambda: self.take_button(3))
        self.button3 = tk.Button(text='4', command=lambda: self.take_button(4))
        self.button4 = tk.Button(text='5', command=lambda: self.take_button(5))
        self.button5 = tk.Button(text='6', command=lambda: self.take_button(6))
        self.button6 = tk.Button(text='7', command=lambda: self.take_button(7))
        self.button7 = tk.Button(text='8', command=lambda: self.take_button(8))
        self.button8 = tk.Button(text='9', command=lambda: self.take_button(9))
        self.button9 = tk.Button(text='/', command=lambda: self.take_button('/'))
        self.button10 = tk.Button(text='*', command=lambda: self.take_button('*'))
        self.button11 = tk.Button(text='-', command=lambda: self.take_button('-'))
        self.button12 = tk.Button(text='+', command=lambda: self.take_button('+'))
        self.button13 = tk.Button(text='.', command=lambda: self.take_button('.'))
        self.button14 = tk.Button(text='=', command=lambda: self.take_button('='))
        self.button15 = tk.Button(text='0', command=lambda: self.take_button(0))
        self.button16 = tk.Button(text='%', command=lambda: self.take_button('%'))
        self.button17 = tk.Button(text='C', command=lambda: self.take_button('C'))

        self.screen.place(x=0, y=0, height=81.6, width=285, command=self.screen_out())


        self.button9.place(x=0, y=81.6, height=40.8, width=54)
        self.button10.place(x=54, y=81.6, height=40.8, width=54)
        self.button11.place(x=108, y=81.6, height=40.8, width=54)
        self.button12.place(x=162, y=81.6, height=81.3, width=54)

        self.button6.place(x=0, y=122.4, height=40.8, width=54)
        self.button7.place(x=54, y=122.4, height=40.8, width=54)
        self.button8.place(x=108, y=122.4, height=40.8, width=54)

        self.button3.place(x=0, y=163.2, height=40.8, width=54)
        self.button4.place(x=54, y=163.2, height=40.8, width=54)
        self.button5.place(x=108, y=163.2, height=40.8, width=54)
        self.button14.place(x=162, y=163.2, height=81.6, width=54)

        self.button.place(x=0, y=204, height=40.8, width=54)
        self.button1.place(x=54, y=204, height=40.8, width=54)
        self.button2.place(x=108, y=204, height=40.8, width=54)

        self.button15.place(x=0, y=244.8, height=40.8, width=54)
        self.button16.place(x=54, y=244.8, height=40.8, width=54)
        self.button13.place(x=108, y=244.8, height=40.8, width=54)
        self.button17.place(x=162, y=244.8, height=40.8, width=54)


    def take_button(self, line):
        operator = '-+*/%'
        equally = '='
        if str(line) in operator:
            self.a.append('')
            self.n = self.n + 1
            self.a[self.n] = self.a[self.n] + str(line)
            self.a.append('')
            self.n = self.n + 1
            self.index = self.index + 1
            if self.index > 1:
                self.a[0] = str(math_operation(self.a))
                del self.a[2:]
                self.a[1] = str(line)
                self.n = 2
                self.a.append('')
                print(self.a)
                return self.screen_out(self.a[0])
        elif str(line) in equally:
            y = str(math_operation(self.a))
            del self.a[0:]
            self.n = 0
            self.a = ['']
            self.index = 0
            return self.screen_out(y)
        elif str(line) == 'C':
            del self.a[0:]
            self.n = 0
            self.a = ['']
            self.index = 0
            return self.screen_out("0")
        else:
            self.a[self.n] = self.a[self.n] + str(line)
        print(self.a)
        return self.screen_out(self.a)


    def screen_out(self, x=0):
        self.screen['text'] = x




def main():
    root = tk.Tk()
    root.geometry('216x286+700+200')
    app = MyApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()