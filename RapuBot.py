import logging
import openai
from telegram.ext import Application, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# Set higher logging level for httpx to avoid excessive logging
logging.getLogger("httpx").setLevel(logging.WARNING)

# Initialize OpenAI with your API key (use environment variables for security)
openai.api_key = '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'

# Create the Application and pass it your bot's token
application = Application.builder().token("6650771018:AAFCQn3MfjPWVw9YPkU4OCbLz09kttewt6Y").build()

# Define a function to generate Rapunzel-like responses using GPT-3
async def generate_rapunzel_response(user_message):
    headers = {
        "Authorization: Bearer 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"
    }
    response = openai.Completion.create(
        engine="davinci",  # Choose the GPT-3 model/engine
        prompt=f"Rapunzel: {user_message}",  # Provide user's input as a prompt
        max_tokens=50,  # Adjust the length of the response
    )
    gpt3_response = response.choices[0].text
    return gpt3_response

# Define a message handler to respond to user messages
async def respond_to_message(update, context):
    user_message = update.message.text

    # Use GPT-3 to generate a Rapunzel-like response
    rapunzel_response = await generate_rapunzel_response(user_message)

    # Send the response back to the user
    update.message.reply_text(rapunzel_response)

# Add the message handler to the application
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respond_to_message))

# Run the bot
application.run_polling()
