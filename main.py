from tkinter import *

def MouseMove(event,cv:Canvas):
    print(event.x,event.y)
    cv.create_oval(event.x,event.y,event.x+1,event.y+1,fill='black',width=10)

def clean(cv:Canvas):
    print('deleted')
    cv.delete('all')

class App:
    def __init__(self,w,h):
        self.w,self.h = w,h
        self.size = f'{w}x{h}'
        self.root = Tk()
        self.root.title("Title")
        self.root.geometry("1200x900")
        self.root.config(bg="dark gray")


        self.cv = Canvas(self.root,width=self.w,height=self.h,bg='beige',cursor='dot')
        self.cv.bind("<B1-Motion>",lambda e:MouseMove(e,self.cv))
        self.cv.bind("<Button-3>",lambda e:clean(self.cv))
        self.cv.pack()
    
    def run(self):
        self.root.mainloop()
        return self

if __name__ == "__main__":
    app = App(1200,900).run()