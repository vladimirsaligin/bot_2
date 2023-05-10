from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /start"""
    keyboard = [[InlineKeyboardButton("Показать меню", callback_data='menu')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Привет, я телеграм-бот! Я могу повторять за вами любые текстовые сообщения, которые вы мне отправите.', reply_markup=reply_markup)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик команды /hello"""
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}!')

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик кнопки меню"""
    text = "Это меню!"
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(text=text)

app = ApplicationBuilder().token("5987197501:AAFh8an4ZvHgwyFhjw7sQkU6gsAlS3qIjqo").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CallbackQueryHandler(menu, pattern='menu'))
app.run_polling()
