import os
from telebot import types, TeleBot
from dotenv import load_dotenv
from inverse_code import encode, decode


load_dotenv()

bot = TeleBot(os.getenv("API_TOKEN_ACCESS"))


# Create a message handler
@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    """Welcome"""

    markup = types.InlineKeyboardMarkup(row_width=3)

    button1 = types.InlineKeyboardButton("Encode", callback_data="btn1")
    button2 = types.InlineKeyboardButton("Decode", callback_data="btn2")
    button3 = types.InlineKeyboardButton("Convert", callback_data="btn3")
    button4 = types.InlineKeyboardButton("Helpers", callback_data="btn4")
    button5 = types.InlineKeyboardButton("About", callback_data="btn5")
    button6 = types.InlineKeyboardButton("Library", callback_data="btn6")

    markup.add(button1, button2, button3)
    markup.add(button4, button5, button6)

    bot.send_message(
        message.chat.id,
        """Welcome!
        I'm a bot powered by inverse-code library.
        Please select an option:""",
        reply_markup=markup,
    )


@bot.message_handler(commands=["encode"])
def encode_message(message):
    """Encode"""
    try:
        # Get the text to encode
        text = message.text.split("/encode ", 1)[1]
        encoded = encode.encode(text)
        bot.reply_to(message, f"Encoded: {encoded}")
    except IndexError:
        bot.reply_to(message, "Please provide text to encode. Example: /encode hello")
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")


@bot.message_handler(commands=["decode"])
def decode_message(message):
    """Decode"""
    try:
        # Get the text to decode
        text = message.text.split("/decode ", 1)[1]
        # Use your library to decode
        original_type = int(text)
        decoded = decode.decode(original_type)
        print(text)
        print(decoded)
        bot.reply_to(message, f"Decoded: {decoded}")
    except IndexError:
        bot.reply_to(message, "Please provide text to decode. Example: /decode xyz")
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")


# Handle button presses
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    """Callback"""
    if call.data == "btn1":
        bot.answer_callback_query(call.id)
        msg = bot.send_message(
            call.message.chat.id, "Send me the text you want to encode:"
        )
        bot.register_next_step_handler(msg, process_encode_step)
    elif call.data == "btn2":
        bot.answer_callback_query(call.id, "You selected Button 2!")
        bot.send_message(call.message.chat.id, "You selected Decode")
    elif call.data == "btn3":
        bot.send_message(call.message.chat.id, "You selected Convert")
    elif call.data == "btn4":
        bot.send_message(call.message.chat.id, "You selected Helpers")
    elif call.data == "btn5":
        bot.send_message(
            call.message.chat.id,
            """
            [Reverse Code](https://pypi.org/project/inverse-code/) is a library created for Python 
            to help developers encrypt and retrieve their data in a simple and dynamic way.\n
            This cryptography is at least vaguely similar to real-world things, such as Reed-Solomon 
            error correction codes or some interspersed data formats 
            that can be transmitted by IoT edge devices.\n
            ASCII, means American standard code for information exchange. 
            It is a 7 -bit character code where each individual bit represents a unique character.\n
            I used the 8-bit ASCII table with 256 characters and symbols, 
            which is based on the Windows-1252 characters set. \n
            """,
        )
    elif call.data == "btn6":
        bot.answer_callback_query(call.id, "Your pressed Library")


# Process the text received after pressing the Encode button
def process_encode_step(message):
    try:
        text = message.text
        encoded = encode.encode(text)
        bot.reply_to(message, f"Encoded: {encoded}")
    except IndexError:
        bot.reply_to(message, "Please provide text to encode. Example: /encode hello")
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")


# Start the bot
bot.polling()
