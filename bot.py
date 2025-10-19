import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# Configurazione - Render.com inserirà queste variabili
BOT_TOKEN = os.environ.get('BOT_TOKEN')
WEBAPP_URL = os.environ.get('WEBAPP_URL')

def start(update: Update, context: CallbackContext):
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton("📱 APRI RETEGRAMNEWS24", web_app={"url": WEBAPP_URL})
    ]])
    
    update.message.reply_text(
        "📺 **RetegramNews24**\n\n"
        "La tua app di streaming news!\n\n"
        "Clicca il pulsante qui sotto:",
        reply_markup=keyboard
    )

def main():
    updater = Updater(BOT_TOKEN)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.start_polling()
    print("✅ Bot RetegramNews24 online!")
    updater.idle()

if __name__ == '__main__':
    main()