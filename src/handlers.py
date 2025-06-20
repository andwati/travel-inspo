from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from .api_clients import get_unsplash_image, get_destination_info

DESTINATIONS = {
    "beaches": ["Maldives", "Bora Bora", "Phuket"],
    "mountains": ["Swiss Alps", "Mount Everest", "Andes"],
    "cities": ["Tokyo", "Paris", "New York City"],
    "adventure": ["Costa Rica", "New Zealand", "Patagonia"],
    "ancient ruins": ["Machu Picchu", "Rome", "Angkor Wat"],
}


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a welcome message  when the /start command is issued.

    Args:
        update (Update): _description_
        context (ContextTypes.DEFAULT_TYPE): _description_
    """
    keyboard = [
        [InlineKeyboardButton("Beaches 🏖️", callback_data="beaches")],
        [InlineKeyboardButton("Mountains 🏔️", callback_data="mountains")],
        [InlineKeyboardButton("Cities 🏙️", callback_data="cities")],
        [InlineKeyboardButton("Adventure 🧗", callback_data="adventure")],
        [InlineKeyboardButton("Ancient Ruins 🏛️", callback_data="ancient ruins")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    if update.message:
        await update.message.reply_text(
            "Welcome, wanderer! ✨\n\nI'm your personal TravelInspo Bot. "
            "What kind of adventure are you dreaming of today?",
            reply_markup=reply_markup,
        )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles button presses and sends destination information.

    Args:
        update (Update): The update containing the button press.
        context (ContextTypes.DEFAULT_TYPE): The context of the update.
    """
    query = update.callback_query
    if query is None:
        return

    await query.answer()

    interest = query.data
    if interest in DESTINATIONS:
        destination_name = DESTINATIONS[interest][0]

        await query.edit_message_text(
            text=f"Great choice! Searching for inspiration in {destination_name}..."
        )

        # Fetch destination info and image

        info = get_destination_info(destination_name)
        image_data = get_unsplash_image(destination_name)

        if image_data and info:
            image = image_data[0]  # Get the first image
            caption = (
                f"📍 *{destination_name}*\n\n"
                f"{info['summary']}\n\n"
                f"[Read more on Wikipedia]({info['url']})\n\n"
                f"📸 Photo by [{image['photographer_name']}]({image['photographer_profile']}) on Unsplash"
            )
            await context.bot.send_photo(
                chat_id=query.message.chat.id,  # type: ignore
                photo=image["url"],
                caption=caption,
                parse_mode="Markdown",
            )
        else:
            await context.bot.send_message(
                chat_id=query.message.chat.id,  # type: ignore
                text="Sorry, I couldn't find information for that destination.",
            )
