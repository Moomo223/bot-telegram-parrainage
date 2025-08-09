from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

LIEN_1XBET = "https://refpa.top/L?tag=d_1208203m_97c_&site=1208203&ad=97"
LIEN_BET223 = "https://www.bet2africa.ml/affiliates/?btag=2107527"
LIEN_BETWINNER = "https://bwredir.com/1HGY?p=%2Fregistration%2F"

async def lien(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "📌 Voici mes liens de parrainage :\n\n"
        f"🎯 1XBET : {LIEN_1XBET}\n"
        f"🎯 Bet223 : {LIEN_BET223}\n"
        f"🎯 Betwinner : {LIEN_BETWINNER}\n"
    )
    await update.message.reply_text(message)

async def mots_cles(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texte = update.message.text.lower()
    if "pari" in texte or "1xbet" in texte or "bet" in texte:
        await lien(update, context)

def main():
    app = Application.builder().token("8445087702:AAEDwvAeYhX2-_zy06GsbLaNg9V_guRbGmU").build()

    app.add_handler(CommandHandler("lien", lien))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, mots_cles))

    print("🤖 Bot lancé...")
    app.run_polling()

if __name__ == "__main__":
    main()
