from chatterbot import ChatBot  # 引入ChatBot

from chatterbot.trainers import ChatterBotCorpusTrainer

from opencc import OpenCC


# 建立chatbot物件

bot = ChatBot(
    'Test Bot',
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter'],
    )

trainer = ChatterBotCorpusTrainer(bot)



# 中文的自動學習套件
trainer.train('chatterbot.corpus.chinese')


cc = OpenCC('tw2sp')

name = input("輸入你的名字: ")

print("Hi "+name+"， 請問需要什麼幫助呢？(如需結束，請輸入Bye)")

while True:
    text = cc.convert(input(name+':'))

    request = text

    if request == 'Bye' or request == 'bye':
        print("Test Bot:掰掰")
        break
    else:
        response = bot.get_response(request)
        print("Test Bot:",response)
