#!C:/python/python.exe
# -*- coding: utf-8-*-
import pyttsx3
import time
from retrying import retry

a = input('请输入指令（r->读\te->退出）:')

def fun_read(*args,**kwargs):

    global a

    if a == 'r':

        engine = pyttsx3.init()


        @retry()
        def fun_readlines():

            b = input('请输入要读的文件名：')

            with open(b, "r") as f:

                txt = f.readlines()
                engine.say("我开始读了欧。")

            for s in txt:

                time.sleep(1)
                engine.say(s)
                engine.runAndWait()

            print('内容已读完，谢谢使用')

        fun_readlines()

        fun_confirm()

    elif a == 'e':

        exit()

    else:

        print('输入错误请重新输入')
        a = input('请输入指令（r->读\te->退出）:')
        fun_read(a)

def fun_confirm():
    c = input('是否继续阅读其他文件？(y->是\tn->否)')

    if c == 'y':
        fun_read()
    elif c == 'n':
        exit()
    else:
        print('输入错误，请重新输入：')
        fun_confirm()

if __name__ == '__main__':
    fun_read(a)

