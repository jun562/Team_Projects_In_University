from tkinter import *
import csv

window = Tk()


def ReadRevise:
        lb1 = Listbox(window)
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
                temp.append(self.k)
                print("%s줄에서 발견되었습니다."%.k)
            k+=1
        b2 = Button(window, text= "수정", command = Revise)
        b2.pack(padx= 10,pady=10)
        infile.close()

def Revise():
    order = lb1.curselection()
    print(order)
        
    now = int(temp[order[0]]) #얘가 temp인덱스랑 같음. csv에서 몇째줄인지임
    print(now)
        
    f = open("검사표.csv","r+",newline='')
    wr = csv.writer(f)

    reading = [row for row in csv.reader(f)]
    print(reading)
    print(len(reading))
         
    if reading[now][3]=='양성':
        reading[now][3] = '음성'
    else:
        reading[now][3]='양성'

    f.seek(0)
        
    for row in reading:
        if row != '\n':
            wr.writerow(row)
           
    f.close()
    print("변경되었습니다")
        
question = Label(window, text = "검사 정보를 수정할 분의 성함을 말씀해주세요")
question.pack(padx=10,pady=10) 
box1 = Entry(window)
box1.pack(padx=10,pady=10)
b1 = Button(window,text="확인", command = ReadRevise).pack(padx=10,pady=10)


window.mainloop()

