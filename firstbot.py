# import logging
# from telegram import Update
# from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level=logging.INFO
# )

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(
#         chat_id=update.effective_chat.id,
#         text="Hello! I'm your bot. Available commands:\n/start\n/test\n/meme"
#     )

# async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(
#         chat_id=update.effective_chat.id,
#         text="✅ Bot is working perfectly!"
#     )


# async def send_meme(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     # Example meme URLs - replace with your actual image URLs
#     meme_urls = [
#         "https://preview.redd.it/what-game-is-it-v0-faxv6c9tfhue1.jpeg?width=640&crop=smart&auto=webp&s=c167f6a86e2254e34322a8c60b5f89b8c15fa5f0",
#     ]
    
#     # Send a random meme from the list
#     await context.bot.send_photo(
#         chat_id=update.effective_chat.id,
#         photo=meme_urls[0],  # Sends first meme, you can randomize this
#         caption="Here's your fresh meme! 🚀"
#     )
    
# if __name__ == '__main__':
#     application = ApplicationBuilder().token('7833685703:AAHZM2LrDcZ9XqXfHGh8aaXgvV5fonbLQfo').build()
#     start_handler = CommandHandler('start', start)
#     test_handler = CommandHandler('test', test)
#     meme_handler = CommandHandler('meme', send_meme)
#     application.add_handler(meme_handler)
#     application.add_handler(start_handler)
#     application.add_handler(test_handler)
#     application.run_polling()


import json
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import os


load_dotenv()

# Load your JSON file
with open('datav2.json', 'r') as f:
    memes = json.load(f)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = os.getenv("TELEGRAM_TOKEN")

async def meme_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a random meme when user types 'meme'."""
    message_text = update.message.text.lower()
    
    if 'meme' in message_text:
        # Select a random meme from the list
        random_meme = random.choice(memes)
        meme_url = random_meme['img']
        
        # Send the meme URL to the user
        await update.message.reply_photo(meme_url)
    else:
        await update.message.reply_text('W                          hat? just write "meme" or any word that include "meme" ')
        
def main() -> None:
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(TOKEN).build()

    # Register handlers
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, meme_handler))



    # Run the bot until you press Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()