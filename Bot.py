from telegram.ext import Updater, CommandHandler

TOKEN = "YOUR_BOT_API_TOKEN"

def start(update, context):

    update.message.reply_text("Xin chào, mình đang chạy trên server 🚀")

updater = Updater(TOKEN, use_context=True)

dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))

updater.start_polling()

updater.idle()
