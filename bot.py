from  telegram.ext import Updater,CommandHandler, MessageHandler, Filters

def greet_user(bot, update):
	print("Вызван /start")
	bot.sendMessage(update.message.chat_id, text="Привет, человек! Я бот, который помогает учиться на курсе Learn Python!")
	
def show_error(bot, update, error):
	print('Update "{}" caused error "{}"'.format(update, error))

def talk_to_me(bot, update):
	print("Пришло сообщение: {}".format(update.message.text))
	bot.sendMessage(update.message.chat_id, update.message.text)

def count_words(bot, update):
	print(update.message.text.split(' '))
	bot.sendMessage(update.message.chat_id, text = update.message.text.split)
	len(update.message.text)
	
di = {"привет": "И тебе привет!", "как дела": "Лучше всех", "пока": "Увидемся"}

def get_answer(k,d):
	return d[k]

value = get_answer("как дела", di)
print(value)

       

def run_bot():
	updater = Updater("319337485:AAGlmr5E0x_oyJ2-k6Bkxmc12zRUOyU9N0A")

	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", greet_user))
	dp.add_handler(CommandHandler("wordcount", count_words))
	dp.add_handler(MessageHandler([Filters.text], talk_to_me))
	dp.add_error_handler(show_error)

	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
    run_bot()

