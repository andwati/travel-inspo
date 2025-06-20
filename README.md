# Travel Inspo

Travel Inspo is a Telegram bot that provides curated travel inspiration, destination facts, and stunning images to help users discover their next adventure. The bot combines information from Wikipedia and Unsplash to deliver both knowledge and visual inspiration for a variety of travel interests.

## Features

- Interactive Telegram bot interface
- Curated destination suggestions based on user interests (beaches, mountains, cities, adventure, ancient ruins)
- Fetches destination summaries and facts from Wikipedia
- Retrieves high-quality images from Unsplash, with proper photographer attribution
- Sends multiple images per destination request

## Getting Started

### Prerequisites

- Python 3.10 or higher
- Telegram account and a Telegram Bot Token (from [BotFather](https://core.telegram.org/bots#botfather))
- Unsplash API Access Key (register at [Unsplash Developers](https://unsplash.com/developers))
- Wikipedia API (no key required)

### Installation

1. Clone the repository:

    ```shell
    git clone https://github.com/andwatiian/travel-inspo.git
    cd travel-inspo
    ```


1. Install dependencies:

    ```shell
    uv sync
    ```

1. Set up environment variables in a `.env` file in the project root:

    ```shell
    TELEGRAM_BOT_TOKEN=your-telegram-bot-token
    UNSPLASH_ACCESS_KEY=your-unsplash-access-key
    ```

### Running the Bot

Start the bot with:

```shell
python main.py
```

The bot will start and listen for messages on Telegram.

## Usage

- Start a chat with your bot on Telegram.
- Use the `/start` command to begin.
- Select a travel interest from the provided keyboard.
- The bot will respond with destination information and four related images.

## Attribution

This project uses the Unsplash API for images. All images are credited to their respective photographers as required by Unsplash's guidelines.

## License

This project is licensed under the [MIT License](./LICENSE).
