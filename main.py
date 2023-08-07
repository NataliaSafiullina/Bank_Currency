import telebot

TOKEN = "6409800714:AAHkmZmobG1sCuDZIusrYSK0rqPy9i5-_RQ"
bot = telebot.TeleBot(TOKEN)

currencies = {
    'бат': 'THB',
    'дирхам': 'AED',
    'доллар': 'USD',
    'евро': 'EUR',
    'рубль': 'RUB',
    'тенге': 'KZT',
    'юань': 'CNY'
}

@bot.message_handler(commands=['start'])
def job_comands_start(message):
    message_text = f'Привет, {message.chat.username}! ' \
                   f'\n Я - бот-конвертер валют.' \
                   f'\n Напиши: <валюта_исходная> <валюта_целевая> <сумма>.' \
                   f'\n Доступные команды:' \
                   f'\n /help - помощь ' \
                   f'\n /values - список валют'
    bot.reply_to(message, message_text)

@bot.message_handler(commands=['help'])
def job_comands_help(message):
    message_text = '\n Я - бот-конвертер валют.' \
                   '\n Напиши: <валюта_исходная> <валюта_целевая> <сумма>.' \
                   '\n Доступные команды:' \
                   '\n /help - помощь ' \
                   '\n /values - список валют'
    bot.reply_to(message, message_text)

@bot.message_handler(commands=['values'])
def job_comands_values(message):
    message_text = 'Доступные валюты: '
    for curr in currencies.keys():
        message_text = '\n'.join((message_text, curr))
    bot.reply_to(message, message_text)

@bot.message_handler(content_types=['photo'])
def job_text(message):
    bot.reply_to(message, f"Nice photo, {message.chat.username}")

@bot.message_handler(content_types=['text'])
def job_text(message):
    message_text = 'тут будут конвертирование валют'
    bot.reply_to(message, message_text)


bot.polling(none_stop=True)
