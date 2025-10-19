import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Configurazione
BOT_TOKEN = os.environ.get('BOT_TOKEN')
WEBAPP_URL = os.environ.get('WEBAPP_URL', 'https://tuousername.github.io/retegramnews24/')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton("📱 APRI RETEGRAMNEWS24", web_app={"url": WEBAPP_URL})
    ]])
    
    await update.message.reply_text(
        "📺 **RetegramNews24**\n\n"
        "La tua app di streaming news!\n\n"
        "Clicca il pulsante qui sotto:",
        reply_markup=keyboard
    )

def main():
    # Crea l'applicazione con la nuova sintassi
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Aggiungi handler
    application.add_handler(CommandHandler("start", start))
    
    # Avvia il bot
    application.run_polling()
    print("✅ Bot RetegramNews24 online!")

if __name__ == '__main__':
    main()
