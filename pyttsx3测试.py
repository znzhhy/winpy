import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for voice in voices:
    engine.setProperty('voice', voice.id)
    engine.say('我是来做测试的')
#
# rate = engine.getProperty('rate')
# engine.setProperty('rate', rate + 0)
#
# engine.say('我是来做测试的')
engine.runAndWait()