from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Enlace de tu Mini App alojada en GitHub Pages
    web_app_url = "https://naranjoso6767.github.io/Telegram-miniapp-/"
    
    keyboard = [
        [InlineKeyboardButton("📱 Rellenar Datos de Recarga", web_app=WebAppInfo(url=web_app_url))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "¡Hola! Presiona el botón de abajo para abrir el formulario y rellenar tus datos:",
        reply_markup=reply_markup
    )

# Función que captura los datos enviados desde tu página web
async def handle_web_app_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    datos_recibidos = update.message.web_app_data.data
    
    await update.message.reply_text(
        f"✅ ¡Datos recibidos correctamente!\n\n"
        f"Información del cliente:\n{datos_recibidos}\n\n"
        "Procesando solicitud..."
    )

def main():
    # Coloca el token de tu bot entre las comillas
    application = ApplicationBuilder().token("TU_BOT_TOKEN_AQUI").build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_web_app_data))
    
    print("Bot en ejecución...")
    application.run_polling()

if __name__ == "__main__":
    main()
