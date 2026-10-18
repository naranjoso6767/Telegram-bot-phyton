import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Enlace de tu Mini App alojada en GitHub Pages
    web_app_url = "https://naranjoso6767.github.io/Telegram-miniapp-/"
    
    keyboard = [
        [InlineKeyboardButton("💳 Abrir Pasarela de Pago", web_app=WebAppInfo(url=web_app_url))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "¡Hola! Presiona el botón de abajo para realizar tu pago de forma segura:",
        reply_markup=reply_markup
    )

if __name__ == '__main__':
    # Lee el token de forma segura desde las variables de entorno del servidor
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    
    if not TOKEN:
        print("Error: No se encontró la variable TELEGRAM_BOT_TOKEN.")
    else:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        
        print("Bot de Telegram iniciado correctamente...")
        app.run_polling()
      
