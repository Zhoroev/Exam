def func(message):
    vowels = 'aiouey'
    message = message.lower()
    num = 0
    for i in range(0, len(message)):
        if message[i] in vowels:
            num += 1
    return num


import telebot

TELEGRAM_TOKEN = '1700085538:AAHpB99bs-LmZvfGCiPwfTpLALBR2KVlbVk'

bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.send_message(message.chat.id, func(message.text))


bot.polling()
