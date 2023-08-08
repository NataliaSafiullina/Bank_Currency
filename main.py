import telebot
from config import currencies, TOKEN
from extensions import ConvertionException, ConverterClass

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def job_comands_start(message):
    message_text = f'Привет, {message.chat.username}! ' \
                   '\n Я - бот-конвертер валют.' \
                   '\n Напиши: <валюта_исходная> <валюта_целевая> <сумма>.' \
                   '\n Доступные команды:' \
                   '\n /help - помощь ' \
                   '\n /values - список валют'
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

@bot.message_handler(content_types=['text', ])
def job_text(message):
    try:
        values = message.text.split()
        if len(values) != 3:
            raise ConvertionException('Не корректное количество параметров')
        quote, base, amount = values
        sum_base = ConverterClass.get_price(quote.lower(), base.lower(), amount)
        message_text = f'{amount} {quote} = {sum_base} {base}'
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка ввода.\n{e}')
    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду.\n{e}")
    else:
        bot.reply_to(message, message_text)

bot.polling(none_stop=True)


