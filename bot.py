from  telegram.ext import Updater,CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup


def greet_user(bot, update):
    print("Вызван /start")
    bot.sendMessage(update.message.chat_id, "Привет, человек! Я бот, который помогает учиться на курсе Learn Python!")


def get_answer(question):
    answers = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидимся"}
    answer = answers.get(question, 'Я не понял.')
    return answer


def talk_to_me(bot, update):
    print("Пришло сообщение: {}".format(update.message.text))
    bot.sendMessage(update.message.chat_id, get_answer(update.message.text))


def count_words(bot, update):
    words = update.message.text.split()
    if len(words) < 2:
        bot.sendMessage(update.message.chat_id, "Нечего подсчитывать.")
        return
    words = words[1:]
    if words[0][0] != '"' or words[-1][-1] != '"':
        bot.sendMessage(update.message.chat_id, "Нет двойных кавычек.")
        return
    wordcount = len(words)
    text = "Кол-во слов: {} шт.".format(wordcount)
    bot.sendMessage(update.message.chat_id, text)


def bot_calculator(bot, update):
    numbers = update.message.text.split()

    if len(numbers) != 5:
        bot.sendMessage(update.message.chat_id, "Вот как надо писать:  2 + 3 =")
        return

    numbers = numbers[1:]

    if numbers[0].isdigit() == False or numbers[2].isdigit() == False:
        bot.sendMessage(update.message.chat_id, "Пишите числа.")
        return

    if numbers[1] == '+':
        resalt = int(numbers[0]) + int(numbers[2])
        bot.sendMessage(update.message.chat_id, resalt)

    elif numbers[1] == '-':
        resalt = int(numbers[0]) - int(numbers[2])
        bot.sendMessage(update.message.chat_id, resalt)

    elif numbers[1] == '*':
        resalt = int(numbers[0]) * int(numbers[2])
        bot.sendMessage(update.message.chat_id, resalt)

    elif numbers[1] == '/': 
        if numbers[2] == '0':
            bot.sendMessage(update.message.chat_id, "На ноль мы не делим.")
        resalt = int(numbers[0]) / int(numbers[2])
        bot.sendMessage(update.message.chat_id, resalt)

    else:
        bot.sendMessage(update.message.chat_id, "Надо писать:  2 + 3 =")
        

def calculator_inbot(bot, update):
    try:
        custom_keyboard = [['1', '2', '3', '4', '5', '+', '-'], 
                           ['6', '7', '8', '9', '0', '*', '/']]
        reply_markup = ReplyKeyboardMarkup(custom_keyboard)
        bot.sendMessage(update.message.chat_id, 
                        text="Custom Keyboard Test", 
                        reply_markup=reply_markup)
    except Exception as e:
        print(e)


bot_cities = ['Астрахань', 'Омск', 'Киев']
bot_city_end = {}


def city_game(bot, update):
    global bot_cities
    if not bot_cities:
        bot_cities = ['Астрахань', 'Омск', 'Киев']
    user_city = update.message.text.split()
    if len(user_city) < 2:
        bot.sendMessage(update.message.chat_id, "Напиши какой-нибудь город.")
        return
    user_city = user_city[1]
    last_city = bot_city_end.get(update.message.chat_id)
    if last_city and (user_city[0].lower() != last_city[-1].lower()):
        bot.sendMessage(update.message.chat_id, "Город пишем с последней буквы")
        return
    for bot_city in bot_cities:
        if bot_city[0].lower() == user_city[-1].lower():
            bot.sendMessage(update.message.chat_id, bot_city)
            bot_cities.remove(bot_city)
            bot_city_end[update.message.chat_id] = bot_city
            return
    bot.sendMessage(update.message.chat_id, "Ты победил.")
    

def run_bot():
    updater = Updater("319337485:AAGlmr5E0x_oyJ2-k6Bkxmc12zRUOyU9N0A")

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", greet_user))

    dp.add_handler(MessageHandler([Filters.text], talk_to_me))

    dp.add_handler(CommandHandler("wordcount", count_words))

    dp.add_handler(CommandHandler("calculator", bot_calculator))

    dp.add_handler(CommandHandler("calc", calculator_inbot))

    dp.add_handler(CommandHandler("city", city_game))
    
    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    run_bot()

