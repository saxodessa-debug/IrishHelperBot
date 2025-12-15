import os
import telebot

TOKEN = os.environ.get('BOT_TOKEN')

if not TOKEN:
    print("Error: BOT_TOKEN not set in environment variables")
    exit(1)

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm your Telegram bot. I'm always online!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

print("Bot is starting...")
bot.infinity_polling()
