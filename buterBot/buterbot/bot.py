from message_texts import GREETINGS
from config import TG_TOKEN
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO
)

logger = logging.getLogger(__name__)

TELEGRAM_BOT_TOKEN_TOKEN = TG_TOKEN 
if not TELEGRAM_BOT_TOKEN_TOKEN:
    exit('Specify TELEGRAM_BOT_TOKEN_TOKEN env variable')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    effective_chat=update.effective_chat
    if not effective_chat:
        logger.warning('effective_chat is None')
        return
    await context.bot.send_message(chat_id=effective_chat.id, text=GREETINGS)

if __name__=='__main__':
    application= ApplicationBuilder().token(TELEGRAM_BOT_TOKEN_TOKEN).build()

    start_handler= CommandHandler('start', start)
    application.add_handler(start_handler)

    application.run_polling()



