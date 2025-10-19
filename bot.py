import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# Configura logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BOT_TOKEN = os.environ.get('BOT_TOKEN')
WEBAPP_URL = os.environ.get('WEBAPP_URL', 'https://glauscat.github.io/retegramnews24/')

def start(update: Update, context: CallbackContext):
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton("📱 APRI RETEGRAMNEWS24", web_app={"url": WEBAPP_URL})
    ]])
    
    update.message.reply_text(
        "📺 **RetegramNews24**\n\n"
        "Clicca il pulsante per aprire l'app di streaming news:",
        reply_markup=keyboard
    )

def main():
    print("🚀 Avvio bot RetegramNews24...")
    
    # Crea updater con use_context=True per compatibilità
    updater = Updater(BOT_TOKEN, use_context=True)
    
    # Aggiungi handler
    updater.dispatcher.add_handler(CommandHandler("start", start))
    
    # Avvia il bot
    updater.start_polling()
    print("✅ Bot RetegramNews24 online e in ascolto!")
    
    # Mantieni il bot in esecuzione
    updater.idle()

if __name__ == '__main__':
    main()
