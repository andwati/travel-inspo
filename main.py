import os
from dotenv import load_dotenv
from src.bot import run_bot


load_dotenv()

if __name__ == "__main__":
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")

    if not bot_token:
        raise ValueError("TELEGRAM_BOT_TOKEN is not set in the .env file")

    print("Starting bot...")
    run_bot(bot_token)
    print("Bot started successfully.")
