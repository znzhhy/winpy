import pyttsx3

def fun_read():
    a = input('请输入文字（输入t为退出）：')
    if a == 't':
        exit()
    else:
        engine = pyttsx3.init()
        engine.say(a)
        engine.runAndWait()
    fun_read()

if __name__ == '__main__':
    fun_read()