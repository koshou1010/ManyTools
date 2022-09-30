import json,time,os
from datetime import datetime,timezone,timedelta
import tkinter as tk


window = tk.Tk()
window.title('UnixTimeCalculator')
window.geometry('500x250')



def calculater(start, end):
    return (round((end-start)/60, 2))

def transfer(unit_time):
    return datetime.fromtimestamp(int(unit_time)).strftime('%Y/%m/%d %H:%M:%S')

def sign_result():
    if entry.get() == '' or entry2.get() == '':
        print('please enter unix time')
    label = tk.Label(window, text = '開始時間').grid(row=6, sticky=tk.W,padx=(90, 10))
    labe2 = tk.Label(window, text = transfer(entry.get())).grid(row=7, sticky=tk.W,padx=(55, 10))
    labe3 = tk.Label(window, text = '結束時間').grid(row=6, sticky=tk.W,padx=(340, 10))
    labe4 = tk.Label(window, text = transfer(entry2.get())).grid(row=7, sticky=tk.W,padx=(305, 10))
    res = calculater(int(entry.get()), int(entry2.get()))
    labe5 = tk.Label(window, text = '耗時 {} 分'.format(res)).grid(row=8, sticky=tk.W,padx=(190, 10))


def main():


    # 標示文字
    label = tk.Label(window, text = '開始時間').grid(row=0, sticky=tk.W,padx=(90, 10))
    label2 = tk.Label(window, text = '結束時間').grid(row=0, sticky=tk.W,padx=(340, 10))
    blank = tk.Label(window, text = '').grid(row=2, sticky=tk.W,padx=(0, 0))
    blank1 = tk.Label(window, text = '').grid(row=3, sticky=tk.W,padx=(0, 0))
    blank2 = tk.Label(window, text = '').grid(row=5, sticky=tk.W,padx=(0, 0))

    # 輸入欄位
    global entry, entry2
    entry = tk.Entry(window, width = 20)
    entry.grid(row=1, sticky=tk.W,padx=(50, 10))
    entry2 = tk.Entry(window, width = 20)
    entry2.grid(row=1, sticky=tk.W,padx=(290, 10))

    # 按鈕
    tk.Button(window, text='output', command = sign_result).grid(row=4, sticky=tk.W, pady=4,padx=(220, 10))
    # button = tk.Button(window, text = "OK", command = onOK)
    # button.pack()
    window.mainloop()


if __name__ == '__main__':
    main()