import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler

# Налаштування логування
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Функція для головного меню з кнопками
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Створюємо кнопки
    keyboard = [
        [InlineKeyboardButton("ℹ️ Інфо про гру", callback_data='info_pressed')],
        [InlineKeyboardButton("🎮 Канал розробника", url='https://t.me/your_channel')] # Заміни на свій лінк
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="Привіт! Дякую, що граєш у Nukecliker. Обирай дію нижче:",
        reply_markup=reply_markup
    )

# Функція, яка спрацьовує при натисканні на кнопку "Інфо"
async def button_tap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer() # Обов'язково підтверджуємо натискання

    if query.data == 'info_pressed':
        info_text = (
            "🚀 **Nukecliker**\n\n"
            "В клікері ви клікаєте і заробляєте гроші для прокачки. "
            "Якщо стати креатором, то отримаєте коди, але для цього треба тег #nukecliker"
        )
        await query.edit_message_text(text=info_text, parse_mode="Markdown")

if __name__ == '__main__':
    application = ApplicationBuilder().token('8670362414:AAHXzdc4_9cAv2sDWDPHc9HcAOtmku3HrII').build()
    
    # Обробник команди /start
    application.add_handler(CommandHandler('start', start))
    
    # Обробник натискань на кнопки
    application.add_handler(CallbackQueryHandler(button_tap))
    
    print("Бот запущений з кнопками!")
    application.run_polling()
