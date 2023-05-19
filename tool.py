import tkinter
import tkinter.messagebox
import random

sign = True
running = False

def washList():
    wash_man = ['冒菜', '米线', '盖饭(木桶饭)', '猪脚饭', '抄手', '擂椒拌饭', '面']
    random.shuffle(wash_man)
    wash = []
    for i in range(0, 5):
        for j in wash_man:
            wash.append(j)
    random.shuffle(wash)
    return wash

def getOne():
    list = washList()
    wash_len = len(list) - 1
    key = random.randint(0, wash_len)
    return list[key]

# 修改标签上的文字
def change_label_text(label,top):
    global sign,running
    text = getOne()
    label.config(text=text)
    if sign:
        top.after(50,change_label_text,label,top)
        running = True
    else:
        sign = True
        running = False
        return

def start_text(label,top):
    global sign, running
    if running:
        return
    change_label_text(label,top)

def stop_text():
    global sign,running
    if running:
        if sign:
            sign = False
    else:
        sign = True

def confirm_to_quit(top):
    if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
        top.quit()

def main():

    defaultMan = '大太阳今日午饭'

    # 创建顶层窗口
    top = tkinter.Tk()

    # 设置窗口大小
    top.geometry('800x600')
    # 设置窗口标题
    top.title('小游戏')
    # 创建标签对象并添加到顶层窗口
    label = tkinter.Label(top, text=defaultMan, font='Arial -32', fg='red')
    label.pack(expand=1)
    # 创建一个装按钮的容器
    panel = tkinter.Frame(top)
    # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
    button1 = tkinter.Button(panel, text='开始', command=lambda: start_text(label,top), width=14, height=2, padx=50, activebackground='red')
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='停止', command=lambda: stop_text(), width=14, height=2, padx=50, activebackground='red')
    button2.pack(side='right')
    button3 = tkinter.Button(panel, text='结束', command=lambda: confirm_to_quit(top), width=14, height=2, padx=50, activebackground='red')
    button3.pack(side='right')
    panel.pack(side='bottom')
    # 开启主事件循环
    tkinter.mainloop()


if __name__ == '__main__':
    main()