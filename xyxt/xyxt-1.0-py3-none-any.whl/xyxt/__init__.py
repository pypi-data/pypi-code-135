import tkinter as tk
import Pmw
import datetime
import tkinter.constants as tkc
root = tk.Tk()
root.title("🌺小研系统🌺")
def bd():
    print("Aaaaaaaaaa")
button1 = tk.Button(root, text="课纲",command=bd)
button1.pack()
ppm3_tips = Pmw.Balloon(root)  # 新建Pmw.Balloon对象绑定窗口
ppm3_tips.bind(button1, "生成课纲"),  # 绑定按钮
w = tk.Label(root, text=datetime.datetime.now().strftime('%Y年%m月%d日'))
w.pack()
root.geometry("400x300")
root.mainloop()