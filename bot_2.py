print('привет')
mport telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я телеграм бот.")

def echo(update, context):
    text = update.message.text.lower()
    if text == 'привет':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Привет!")
    elif text == 'как дела?':
        context.bot.send_message(chat_id=update.effective_chat.id, text="Хорошо, а у тебя?")
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Я не понимаю, что вы говорите. Попробуйте еще раз.")

bot = telegram.Bot(token='your_bot_token')
updater = Updater(bot=bot)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))
updater.start_polling()
