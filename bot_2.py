import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    """Обработчик команды /start"""
    context.bot.send_message(chat_id=update.effective_chat.id, text='Привет, я телеграм-бот! Я могу повторять за вами любые текстовые сообщения, которые вы мне отправите.')

def help(update, context):
    """Обработчик команды /help"""
    context.bot.send_message(chat_id=update.effective_chat.id, text='Это помощь!')

def echo(update, context):
    """Обработчик текстовых сообщений"""
    text = update.message.text
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def main():
    """Основная функция бота"""

    # Создаем экземпляр бота и получаем его токен
    bot = telegram.Bot(token='YOUR_BOT_TOKEN')

    # Создаем экземпляр Updater и передаем ему бота
    updater = Updater(bot=bot, use_context=True)

    # Добавляем обработчики команд и текстовых сообщений
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, echo))

    # Запускаем бота
    updater.start_polling()

    # Запускаем цикл обработки сообщений
    updater.idle()

if __name__ == '__main__':
    main()