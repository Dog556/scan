import tkinter as tk
import tkinter.filedialog
import requests
from tkinter import ttk
from tkinter.messagebox import *
import time
import os
import sys
# askopenfilename() 用于打开文件
# asksaveasfilename() 用于保存文件

def stop():
  list_widget.delete(0, tk.END)
  txt.delete(0, tk.END)


class MyApp:
    def __init__(self, master):
        self.master = master
        self.button = tk.Button(self.master, text="退出程序", command=self.quit)
        self.button.pack()

    def quit(self):
        # 关闭主窗口后自动结束程序
        self.master.destroy()
        sys.exit()


def file():
  txt.delete(0, tk.END)
  file_name = tk.filedialog.askopenfilename()
  txt.insert(tk.END, file_name)

def callback():
  txt = url.get()
  find = txt.find('http' or 'HTTP')
  if txt == "":
    result2 = showinfo('温馨提示', f'URL 不能为空')
  else:
    if find == -1:
      result2 = showinfo('温馨提示', f'请输入正确链接！\n格式：https://www.xxx.com')
    else:
      callbackto()




def callbackto():
    sub = 0
    num =0
    time_start = time.time()
    leb2.config(text="正在计算中...",foreground='red')
    bnt.config(text="开始扫描中请勿关闭")
    list_widget.insert(tk.END,'正在运行当中请耐心等待....\n')
    texturl = url.get()
    new_url = txt.get()
    f = open(new_url, 'r',encoding="GB2312")
    mup = f.read().splitlines()
    f.close()
    succes = ['成功的有:']
    for i in mup:
      num += 1
      root.after(100)
      geturl = f'{texturl}{i}'
      reqs = requests.get(geturl)
      code = reqs.status_code
      leb2.config(text=f'一共扫描了: {num} 成功: {sub}',foreground='red')
      root.update()
      if code == 200:
        list_widget.insert(tk.END,f"{code}:成功:{geturl}" + '\n')
        root.update()
        sub += 1
        # 加入数组将URL
        succes.insert(sub,f'{code}:{geturl}')
      else:
        list_widget.insert(tk.END,f"{code}:失败:{geturl}"  + '\n')
        root.update()
    time_end = time.time()
    time_t = int(time_end - time_start)
    leb2.config(text=f'一共扫描了: {num} 成功: {sub} 一共花费 {time_t} S',foreground='red')
    bnt.config(text="打开字典")
    result = showinfo('温馨提示', f'扫描完成有 {sub} 个成功！')
    for n in range(len(succes)):
     list_widget.insert(tk.END,succes[n] + '\n')


#  创建提示框窗口
window = tkinter.Tk()
window.withdraw()
# 创建GUI窗口
root = tk.Tk()
root.title('Hack原创目录扫描v2.0(请勿用于非法用途)')
root.geometry('1200x700')
# ico =  os.path.abspath('chengzi.ico')
# root.iconbitmap(ico)
# 创建 Scrollbar 和 Listbox
sc = tkinter.Scrollbar(root)
sc.pack(side=tkinter.RIGHT, fill=tkinter.Y)
# filename
leb = tk.Label(root,text="输入目标URL")
leb.place(x=10,y=10)
leb3 = tk.Label(root,text="免责声明\n请勿用于非法用途\ns违法必究\n如有违法行为，与本人无关\n欢迎交流：作者QQ：582949896",foreground='red')
leb3.place(x=1000,y=10)
url = tk.Entry(root)
url.place(x=90, y=10)
url.insert(tk.END,'https://www.gxaqzy.cn')
bnt = tk.Button(root, text="打开字典",command=file)
txt = tk.Entry(root,width=22)
bnt.place(x=180,y=35)
txt.place(x=10,y=40)
buutont = tk.Button(root, text='开始扫描',command=callback)
buutont.place(x=60,y=60)
leb2 = tk.Label(root,text="未开始")
leb2.pack()
# 创建Listbox组件
list_widget = tk.Listbox(root,width=160,height=30,yscrollcommand=sc.set)
# 创建下拉框
list_widget.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
sc.config(command=list_widget.yview)
list_widget.place(x=10,y=100)
app = MyApp(root)
stop = tk.Button(root,text="Clear",command=stop)
stop.place(x=130,y=60)
leb4 = tk.Label(root,text="地址格式为:https//xxxx.com",foreground='red')
leb4.place(x=245,y=10)
root.mainloop()
