import telebot
from Data import values, TOKEN
from extensions import Converter, ConverterExeption

values1 = ""  # Для удобства вывода доступных валют
for i in values:
    values1 += i + "\n"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message: telebot.types.Message):
    """Обработка команд start и help которые выводят список доступных команд и шаблон ввода"""
    bot.send_message(message.chat.id, "Привет " + message.chat.username)
    bot.send_message(message.chat.id, "Я умею: \n\n /start - Начало работы \n\
 /help - Вывод доступных команд \n\
 /values - Список доступных валют\n\
 Отправьте сообщение в виде <имя валюты> <имя валюты> <количество первой валюты>.")


@bot.message_handler(commands=['values'])
def handle_start_help(message):
    """Обработка команды values которая выведет список доступных валют"""
    bot.send_message(message.chat.id, f'Доступны следующие валюты:\n{values1}')


@bot.message_handler(content_types=['text', ])
def handle_start_help(message: telebot.types.Message):
    """Обработка основного функционала бота"""
    try:
        qba = message.text.split(' ')
        amount, quote, result, base = Converter.get_price(qba)
    except ConverterExeption as e:
        bot.reply_to(message, f"Ошибка пользователя.\n{e}")
    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду.\n{e}")
    else:
        bot.send_message(message.chat.id, f'{amount} {quote} = {result} {base}')


@bot.message_handler(content_types=['photo', 'document', ])
def handle_start_help(message: telebot.types.Message):
    """Функция для фана"""
    bot.send_message(message.chat.id, "Nice cock")


bot.polling(none_stop=True)
