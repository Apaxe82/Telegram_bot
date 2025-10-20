import os
import json
import time
import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# === CONFIGURAÇÕES ===
TOKEN = os.environ.get('8121157944:AAH5lC2Pl-fCqznQqw0GaqccAD8CLdjwe7Q')  # Fixed syntax error
CHAT_ID = "Apaxe"  # obtém enviando /start ao bot e lendo o log
HORA_ENVIO = "06:30"  # hora diária para envio (HH:MM)
DIAS_TOTAIS = 45

# === Carrega o plano diário ===
try:
    with open("lessons/plan_45j.json", "r", encoding="utf-8") as f:
        plano = json.load(f)
except FileNotFoundError:
    print("❌ Erro: Arquivo plan_45j.json não encontrado!")
    plano = {}
except json.JSONDecodeError:
    print("❌ Erro: Arquivo JSON inválido!")
    plano = {}

# === Funções ===
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

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para comando /start"""
    await update.message.reply_text("Bonjour 🇫🇷 ! Ton programme de 45 jours commence maintenant.")
    
    # Salva o progresso
    with open("progress.txt", "w") as f:
        f.write("1")

async def progresso(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handler para comando /progresso"""
    try:
        with open("progress.txt", "r") as f:
            dia = int(f.read().strip())
    except (FileNotFoundError, ValueError):
        dia = 1
    
    await update.message.reply_text(f"Tu es au jour {dia} sur {DIAS_TOTAIS}.")

def ler_progresso():
    """Lê o progresso atual do arquivo"""
    try:
        with open("progress.txt", "r") as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 1

def salvar_progresso(dia):
    """Salva o progresso no arquivo"""
    with open("progress.txt", "w") as f:
        f.write(str(dia))

async def enviar_licao_diaria(application):
    """Envia a lição do dia no horário programado"""
    dia = ler_progresso()
    if dia <= DIAS_TOTAIS:
        await enviar_licao_dia(application, dia, CHAT_ID)
        salvar_progresso(dia + 1)
        print(f"✅ Lição do dia {dia} enviada com sucesso!")
    else:
        print("🎉 Todas as lições foram concluídas!")

def setup_application():
    """Configura a aplicação do Telegram"""
    application = Application.builder().token(TOKEN).build()
    
    # Adiciona handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("progresso", progresso))
    
    return application

def main():
    """Função principal"""
    # Verifica se o token está disponível
    if not TOKEN:
        print("❌ Erro: TOKEN não encontrado nas variáveis de ambiente!")
        return
    
    application = setup_application()
    
    print("🤖 Bot Telegram diário iniciado...")
    print(f"⏰ Enviando lições às {HORA_ENVIO} todos os dias")
    
    # Loop principal para envio diário
    while True:
        agora = datetime.datetime.now().strftime("%H:%M")
        if agora == HORA_ENVIO:
            try:
                # Usa run_async para operações assíncronas
                application.create_task(enviar_licao_diaria(application))
                time.sleep(60)  # Evita múltiplos envios no mesmo minuto
            except Exception as e:
                print(f"❌ Erro ao enviar lição: {e}")
        
        time.sleep(30)  # Verifica a cada 30 segundos

if __name__ == "__main__":
    main()
