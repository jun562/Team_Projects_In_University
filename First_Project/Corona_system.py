from tkinter import *
import csv 

window = Tk()

class App:
    def __init__(self):
        window.title(" 대기소 기말 프로젝트~ ")
        window.geometry("640x500+100+100")
        window.configure(bg='white')
        photo = PhotoImage(file='COVID-19.png')
        label = Label(window,text=" COVID19 확진자 관리 시스템",font="Helcetica 16")
        label.pack(padx=10,pady=10)
        image = Label(window,image=photo)
        image.photo = photo
        image.pack()

        btn1 = Button(window,text='확진자 목록 ',command= self.insp_list)
        btn2 = Button(window,text='목록 추가하기 ',command=self.append_list)
        btn3 = Button(window,text='목록 수정하기',command=self.edit_list)
        btn4 = Button(window,text='나가기',command=quit)

        btn1.pack(padx=10,pady=10)
        btn2.pack(padx=10,pady=10)
        btn3.pack(padx=10,pady=10)
        btn4.pack(padx=10,pady=10)

        window.mainloop()
        
    def insp_list(self):
        win = Toplevel(window)
        win.geometry("320x400")
        win.title("코로나 명단")
        print("\n-------------명단-------------")
        
        f = open("검사표.csv","r")
        line = f.readline()
        temp = line.rstrip()
        temp = temp.split(',')
        n = 1
        
        while line != "":
            for i in range(4):
                Label(win,
                      justify=LEFT,
                      text='%s'%temp[i]).grid(row=n,column=i, padx=(10, 10),pady=(10, 5))
            
            line = f.readline()
            temp = line.rstrip()
            temp = temp.split(',')
            n += 1
            
        f.close()
        
    def append_list(self):
        def app_ok():
            
            f = open("검사표.csv","a",newline='')

            wr = csv.writer(f)
        
            temp = [e1.get(),e1.get(),e1.get(),e1.get()]
            temp[0] = e1.get()
            temp[1] = e2.get()
            temp[2] = e3.get()
            temp[3] = e4.get()
        
            wr.writerow(temp)
            f.close()
            print("추가되었습니다.")
            win.destroy()
                
        print("\n-------------추가하기-------------")
        win = Toplevel(window)
        win.geometry("320x200")
        win.title("추가하기")

        Label(win,text='이름').grid(row=0,padx=(10, 10),pady=(10, 5))
        Label(win,text='나이').grid(row=1,padx=(10, 10),pady=(10, 5))
        Label(win,text='구역').grid(row=2,padx=(10, 10),pady=(10, 5))
        Label(win,text='결과').grid(row=3,padx=(10, 10),pady=(10, 5))
        
        e1 = Entry(win)
        e2 = Entry(win)
        e3 = Entry(win)
        e4 = Entry(win)

        e1.grid(row=0,column=1,pady=(10, 5))
        e2.grid(row=1,column=1,pady=(10, 5))
        e3.grid(row=2,column=1,pady=(10, 5))
        e4.grid(row=3,column=1,pady=(10, 5))
        
        b1 = Button(win,text='확인',command= app_ok)
        b1.grid(row=5,column=3,padx=(10, 10),pady=(10, 5))
        
        win.mainloop()

    def edit_list(self):
        def Revise():
            order = lb1.curselection()
            now = int(temp[order[0]])
        
            f = open("검사표.csv","r+",newline='')
            wr = csv.writer(f)

            reading = [row for row in csv.reader(f)]
            
            if reading[now][3]=='양성':
                reading[now][3] = '음성'
            else:
                reading[now][3]='양성'

            f.seek(0)
        
            for row in reading:
                if row != '\n':
                    wr.writerow(row)
           
            f.close()
            print("변경되었습니다.")
            win.destroy()

        def Read():
            global lb1
            global temp
            lb1 = Listbox(win)
            n = 0
            lb1.pack(padx= 10,pady=10)
            infile = open("검사표.csv","r")
            name = box1.get()
            k = 0
            temp = []
            for file in infile.readlines():
                if name in file.split(","):
                    lb1.insert(n,file)
                    n+=1
                    temp.append(k)
                k+=1
            b2 = Button(win, text= "수정", command = Revise)
            b2.pack(padx= 10,pady=10)
            infile.close()

        print("\n-------------수정하기-------------")
        win = Toplevel(window)
        win.geometry("320x400")
        win.title("코로나 명단")
        question = Label(win, text = "검사 정보를 수정할 분의 성함을 말씀해주세요")
        question.pack(padx=10,pady=10) 
        box1 = Entry(win)
        box1.pack(padx=10,pady=10)
        b1 = Button(win,text="확인", command = Read).pack(padx=10,pady=10)
        win.mainloop()
        
    
App()
