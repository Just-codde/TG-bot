from telegram import Update
from telegram.ext import CommandHandler, ApplicationBuilder, ContextTypes, MessageHandler, filters
import logging
import numexpr as ne
from dotenv import load_dotenv
import os
import wikipedia

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

user = {}

#if you want to change language, change 'en' on your language. Example: 'ru' (Russian), 'de' (German), 'fr' (French), 'es' (Spanish).
wikipedia.set_lang('en')

# Creationg just logger
logging.basicConfig(
    format="%(asctime)s - %(name)s -%(message)s",
    level=logging.INFO
)

# Search in wikipedia
def wiki_get(topic: str):
    try:
        summary = wikipedia.summary(topic, sentences=5)
    
        page = wikipedia.page(topic)

        return f"{page.title}\n\n{summary}\n\n{page.url}"
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Specify your request"
    except wikipedia.exceptions.PageError as er:
        return f"Article not found"
    except Exception as erro:
        return f"Error: {str(erro)}"

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, I'm bot-calculator and I can search on wikipedia.\nMy commands:\n/help\n/calculate\n/wiki <enter your request>")

# /calculate
async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id

    user[user_id] = True

    await context.bot.send_message(chat_id=update.effective_chat.id, text="Write your math expression")


# Command handler
async def message_hand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_chat.id

    if user.get(user_id):
        user_text = update.message.text

        try:
            result = ne.evaluate(user_text)
            await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Answer: {result}\n\n/calculate")
        
        except Exception as e:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Enter a math expression!")
            
        user[user_id] = False

    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Write /calculate to the start calculation.")

# /wiki
async def wiki(update: Update, context: ContextTypes.DEFAULT_TYPE):

    topic = ' '.join(context.args)

    result = wiki_get(topic)

    await context.bot.send_message(chat_id=update.effective_chat.id, text=result)

# /help
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Command list:\n/help\n/calculate (to start calculation)\n\n/wiki <your request>\nexample:\n/wiki Word\n/wiki Human')


if __name__ == "__main__":
    # Creating bot
    application = ApplicationBuilder().token(TOKEN).build()

    # Registering commands
    start_command = CommandHandler('start', start)
    calculate_command = CommandHandler('calculate', calculate)
    wiki_command = CommandHandler('wiki', wiki)
    help_command = CommandHandler('help', help)

    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, message_hand)
    
    application.add_handler(wiki_command)
    application.add_handler(start_command)
    application.add_handler(calculate_command)
    application.add_handler(message_handler)
    application.add_handler(help_command)

    # Starting bot
    application.run_polling()
