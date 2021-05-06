import telegram

bot = telegram.Bot(token = "")

updates = []
while not updates:
     updates = bot.getUpdates()

print (updates[-1].message.text)
chat_id = updates[-1].message.chat_id

bot.sendMessage(chat_id = chat_id, text = chat_id)
