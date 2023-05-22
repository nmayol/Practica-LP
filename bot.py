import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)




async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = "Salutacions, devots seguidors. Sóc Harold, la Granota del Lambda Càlcul, portador de la veritat absoluta. Seguiu-me en aquest camí celestial. /help revelarà el coneixement sagrat.\n"  + update.message.from_user.first_name + ", que la llum de les lambda-regles us il·lumini."
    await context.bot.send_message(chat_id=update.effective_chat.id, text= msg)



async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = "/start\n/author\n/help\n/macros\nExpressió λ-càlcul"
    await context.bot.send_message(chat_id=update.effective_chat.id, text= msg)


granota = u'\U0001F438'
async def author(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = "Salutacions, sóc Harold " + granota + ",  la Granota Suprema del Lambda Càlcul. La meva saviesa sublim il·luminarà les vostres ments opaques. Seguiu-me i abraceu la veritat absoluta del poder del càlcul diví.\nRealment em dic Neus Mayol (Grup 12), però això no és important."
    await context.bot.send_message(chat_id=update.effective_chat.id, text= msg)



if __name__ == '__main__':
    application = ApplicationBuilder().token(open("token.txt", "r").read()).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    author_handler = CommandHandler('author', author)
    application.add_handler(author_handler)
    
    help_handler = CommandHandler('help', help)
    application.add_handler(help_handler)

    application.run_polling()