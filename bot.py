import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Замените на токен вашего бота от BotFather
TELEGRAM_BOT_TOKEN = "7654011248:AAHr_1UPzZ0ySPhiqriBAEW21UJvKYYfdi4"

# Ссылка на ваш Telegram Mini App
MINI_APP_URL = "MINI_APP_URL"

# Инициализация бота
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    """Обработка команды /start"""
    bot.send_message(
        message.chat.id,
        "Привет! Я бот для просмотра замен. Используй команды:\n"
        "/open - Открыть Mini App"
    )

@bot.message_handler(commands=['open'])
def open_command(message):
    """Обработка команды /open для открытия Mini App"""
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton("Открыть Mini App", url=MINI_APP_URL)
    markup.add(button)
    bot.send_message(
        message.chat.id,
        "Нажми кнопку ниже, чтобы открыть Mini App:",
        reply_markup=markup
    )

if __name__ == "__main__":
    print("Бот запущен!")
    bot.infinity_polling()
