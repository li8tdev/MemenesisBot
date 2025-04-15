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
