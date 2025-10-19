import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# Configura logging
logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.environ.get('BOT_TOKEN')
WEBAPP_URL = os.environ.get('WEBAPP_URL', 'https://glauscat.github.io/retegramnews24/')

def start(update: Update, context: CallbackContext):
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton("📱 APRI RETEGRAMNEWS24", web_app={"url": WEBAPP_URL})
    ]])
    
    update.message.reply_text(
        "📺 **RetegramNews24**\n\nClicca il pulsante per aprire l'app:",
        reply_markup=keyboard
    )

def main():
    print("🚀 Avvio bot RetegramNews24...")
    updater = Updater(BOT_TOKEN, use_context=True)
    
    # Aggiungi handler
    updater.dispatcher.add_handler(CommandHandler("start", start))
    
    # Avvia il bot
    updater.start_polling()
    print("✅ Bot RetegramNews24 online e in ascolto!")
    updater.idle()

if __name__ == '__main__':
    main()
