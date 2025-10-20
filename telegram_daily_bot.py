import os
import json
import time
import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# === CONFIGURAÇÕES ===
TOKEN = os.environ.get('8121157944:AAH5lC2Pl-fCqznQqw0GaqccAD8CLdjwe7Q')  # Set this in PythonAnywhere env vars
CHAT_ID = "Apaxe"  # Your chat ID
HORA_ENVIO = "06:30"
DIAS_TOTAIS = 45

# Load lesson plan
try:
    with open("lessons/plan_45j.json", "r", encoding="utf-8") as f:
        plano = json.load(f)
except FileNotFoundError:
    print("❌ Erro: Arquivo plan_45j.json não encontrado!")
    plano = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bonjour 🇫🇷 ! Ton programme de 45 jours commence maintenant.")
    with open("progress.txt", "w") as f:
        f.write("1")

async def progresso(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        with open("progress.txt", "r") as f:
            dia = int(f.read().strip())
    except (FileNotFoundError, ValueError):
        dia = 1
    await update.message.reply_text(f"Tu es au jour {dia} sur {DIAS_TOTAIS}.")

async def enviar_licao_dia(application, dia, chat_id):
    if str(dia) not in plano:
        await application.bot.send_message(
            chat_id=chat_id, 
            text="🎉 Félicitations ! Tu as terminé les 45 jours !"
        )
        return
    
    licao = plano[str(dia)]
    msg = (
        f"📅 Jour {dia} / {DIAS_TOTAIS}\n"
        f"🎯 *Thème:* {licao['theme']}\n"
        f"🎧 Écoute: {licao['ecoute']}\n"
        f"🗣 Parle: {licao['parole']}\n"
        f"✍ Écris: {licao['ecriture']}\n"
    )
    await application.bot.send_message(
        chat_id=chat_id, 
        text=msg, 
        parse_mode="Markdown"
    )

def main():
    if not TOKEN:
        print("❌ Erro: TOKEN não configurado!")
        return
    
    application = Application.builder().token(TOKEN).build()
    
    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("progresso", progresso))
    
    print("🤖 Bot iniciado...")
    
    # For PythonAnywhere Always-On Task (polling)
    application.run_polling()

if __name__ == "__main__":
    main()