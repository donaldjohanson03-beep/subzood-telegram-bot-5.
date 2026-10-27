import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "سلام! 👋\nبه ربات ساب‌زود خوش اومدی.\n\n"
        "لینک ویدیوت رو بفرست تا بررسیش کنیم."
    )

@bot.message_handler(func=lambda message: True)
def receive_message(message):
    bot.reply_to(
        message,
        "لینکت دریافت شد! ✅\n"
        "قابلیت پردازش ویدیو رو در مرحله بعد اضافه می‌کنیم."
    )

bot.infinity_polling()
