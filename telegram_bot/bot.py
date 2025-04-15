from inverse_code import encode, decode
from helpers import (
    decimal as hp_decimal,
    menu as hp_menu,
    octal as hp_octal,
    hexadecimal as hp_hexadecimal,
    binary as hp_binary,
    symbol as hp_symbol,
)
from convert import menu as cv_menu, cdecimal, coctal, chexadecimal, cbinary, csymbol
from inverse_code.convert import cdec
import about
from token_bot import bot, types, time


# Create a message handler
@bot.message_handler(commands=["start", "menu"])
def show_main_menu(message):
    """Welcome"""

    markup = types.InlineKeyboardMarkup(row_width=2)

    item1 = types.InlineKeyboardButton("Encode", callback_data="static_encode")
    item2 = types.InlineKeyboardButton("Decode", callback_data="static_decode")
    item3 = types.InlineKeyboardButton("Convert", callback_data="menu_convert")
    item4 = types.InlineKeyboardButton("Helpers", callback_data="menu_helpers")
    item5 = types.InlineKeyboardButton("Division", callback_data="static_division")
    item6 = types.InlineKeyboardButton("About", callback_data="static_about")

    markup.add(item1, item2, item3, item4, item5, item6)

    bot.send_message(
        message.chat.id,
        """
        Welcome! I'm a bot powered by inverse-code library.\n\n🤗 Please select an option:
        """,
        reply_markup=markup,
    )


# +---------------------------------------------------------------------------------+
# Button
# +---------------------------------------------------------------------------------+


# Handle button presses
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    """Callback"""
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    if call.data == "main_menu":
        markup = types.InlineKeyboardMarkup(row_width=2)

        item1 = types.InlineKeyboardButton("Encode", callback_data="static_encode")
        item2 = types.InlineKeyboardButton("Decode", callback_data="static_decode")
        item3 = types.InlineKeyboardButton("Convert", callback_data="menu_convert")
        item4 = types.InlineKeyboardButton("Helpers", callback_data="menu_helpers")
        item5 = types.InlineKeyboardButton("Division", callback_data="static_division")
        item6 = types.InlineKeyboardButton("About", callback_data="static_about")

        markup.add(item1, item2, item3, item4, item5, item6)
        bot.edit_message_text("📋 Main Menu:", chat_id, message_id, reply_markup=markup)
    elif call.data == "static_encode":
        bot.answer_callback_query(call.id)
        msg = bot.send_message(
            call.message.chat.id, "Send me the text you want to encode:"
        )
        bot.register_next_step_handler(msg, process_encode_step)
    elif call.data == "static_decode":
        bot.answer_callback_query(call.id)
        msg = bot.send_message(
            call.message.chat.id, "Send me the text you want to decode:"
        )
        bot.register_next_step_handler(msg, process_decode_step)
    elif call.data == "static_division":
        msg = bot.send_message(
            call.message.chat.id, "Send me the number you want to divide:"
        )
        bot.register_next_step_handler(msg, process_division_step)
    elif call.data == "static_about":
        about.static_about(bot, call)
        show_main_menu(call.message)

    ##########################################################################
    elif call.data == "menu_convert":
        cv_menu.menu_convert(bot, call, types)
    # ----------------------------------------------------------------------
    # Sub menu convert
    # ----------------------------------------------------------------------
    elif call.data == "show_convert_decimal":
        cdecimal.show_convert_decimal(chat_id, message_id)
    elif call.data == "convert_decimal_octal":
        msg = bot.send_message(
            call.message.chat.id,
            "Send me a decimal number that you want to convert to octal:",
        )
        bot.register_next_step_handler(msg, cdecimal.convert_decimal_octal)
    elif call.data == "convert_decimal_hexadecimal":
        msg = bot.send_message(
            call.message.chat.id,
            "Send me a decimal number that you want to convert to hexadecimal:",
        )
        bot.register_next_step_handler(msg, cdecimal.convert_decimal_hexadecimal)
    elif call.data == "convert_decimal_binary":
        msg = bot.send_message(
            call.message.chat.id,
            "Send me a decimal number that you want to convert to binary:",
        )
        bot.register_next_step_handler(msg, cdecimal.convert_decimal_binary)
    elif call.data == "convert_decimal_symbol":
        msg = bot.send_message(
            call.message.chat.id,
            "Send me a decimal number that you want to convert to Symbol:",
        )
        bot.register_next_step_handler(msg, cdecimal.convert_decimal_symbol)

    # Octal
    elif call.data == "show_convert_octal":
        coctal.show_convert_octal(chat_id, message_id)
    elif call.data == "convert_octal_decimal":
        msg = bot.send_message(
            call.message.chat.id,
            "Send me a octal number that you want to convert to decimal:",
        )
        bot.register_next_step_handler(msg, coctal.convert_octal_decimal)
    elif call.data == "convert_octal_hexadecimal":
        msg = bot.send_message(
            call.message.chat.id,
            "Send me a octal number that you want to convert to hexadecimal:",
        )
        bot.register_next_step_handler(msg, coctal.convert_octal_hexadecimal)
    elif call.data == "convert_octal_binary":
        msg = bot.send_message(
            call.message.chat.id,
            "Send me a octal number that you want to convert to binary:",
        )
        bot.register_next_step_handler(msg, coctal.convert_octal_binary)
    elif call.data == "convert_octal_symbol":
        msg = bot.send_message(
            call.message.chat.id,
            "Send me a octal number that you want to convert to Symbol:",
        )
        bot.register_next_step_handler(msg, coctal.convert_octal_symbol)

    # Hexadecimal
    elif call.data == "show_convert_hexadecimal":
        chexadecimal.show_convert_hexadecimal(chat_id, message_id)
    elif call.data == "convert_hexadecimal_decimal":
        msg = bot.send_message(
            call.message.chat.id,
            "Send me a hexadecimal number that you want to convert to decimal:",
        )
        bot.register_next_step_handler(msg, chexadecimal.convert_hexadecimal_decimal)
    elif call.data == "convert_hexadecimal_octal":
        msg = bot.send_message(
            call.message.chat.id,
            "Send me a hexadecimal number that you want to convert to octal:",
        )
        bot.register_next_step_handler(msg, chexadecimal.convert_hexadecimal_octal)
    elif call.data == "convert_hexadecimal_binary":
        msg = bot.send_message(
            call.message.chat.id,
            "Send me a hexadecimal number that you want to convert to binary:",
        )
        bot.register_next_step_handler(msg, chexadecimal.convert_hexadecimal_binary)
    elif call.data == "convert_hexadecimal_symbol":
        msg = bot.send_message(
            call.message.chat.id,
            "Send me a hexadecimal number that you want to convert to Symbol:",
        )
        bot.register_next_step_handler(msg, chexadecimal.convert_hexadecimal_symbol)

    # Binary
    elif call.data == "show_convert_binary":
        cbinary.show_convert_binary(chat_id, message_id)
    elif call.data == "convert_binary_decimal":
        msg = bot.send_message(
            call.message.chat.id,
            "Send me a binary number that you want to convert to decimal:",
        )
        bot.register_next_step_handler(msg, cbinary.convert_binary_decimal)
    elif call.data == "convert_binary_octal":
        msg = bot.send_message(
            call.message.chat.id,
            "Send me a binary number that you want to convert to octal:",
        )
        bot.register_next_step_handler(msg, cbinary.convert_binary_octal)
    elif call.data == "convert_binary_hexadecimal":
        msg = bot.send_message(
            call.message.chat.id,
            "Send me a binary number that you want to convert to hexadecimal:",
        )
        bot.register_next_step_handler(msg, cbinary.convert_binary_hexadecimal)
    elif call.data == "convert_binary_symbol":
        msg = bot.send_message(
            call.message.chat.id,
            "Send me a binary number that you want to convert to Symbol:",
        )
        bot.register_next_step_handler(msg, cbinary.convert_binary_symbol)

    # Symbol
    elif call.data == "show_convert_symbol":
        csymbol.show_convert_symbol(chat_id, message_id)
    elif call.data == "convert_symbol_decimal":
        msg = bot.send_message(
            call.message.chat.id,
            "Send me a symbol number that you want to convert to decimal:",
        )
        bot.register_next_step_handler(msg, csymbol.convert_symbol_decimal)
    elif call.data == "convert_symbol_octal":
        msg = bot.send_message(
            call.message.chat.id,
            "Send me a symbol number that you want to convert to octal:",
        )
        bot.register_next_step_handler(msg, csymbol.convert_symbol_octal)
    elif call.data == "convert_symbol_hexadecimal":
        msg = bot.send_message(
            call.message.chat.id,
            "Send me a symbol number that you want to convert to hexadecimal:",
        )
        bot.register_next_step_handler(msg, csymbol.convert_symbol_hexadecimal)
    elif call.data == "convert_symbol_binary":
        msg = bot.send_message(
            call.message.chat.id,
            "Send me a symbol number that you want to convert to Symbol:",
        )
        bot.register_next_step_handler(msg, csymbol.convert_symbol_binary)

    ##########################################################################
    elif call.data == "menu_helpers":
        hp_menu.menu_helpers(bot, call, types)
    # -----------------------------------
    # Sub menu helpers
    # -----------------------------------
    elif call.data == "show_decimal":
        hp_decimal.show_decimal(bot, chat_id, message_id, types)
    elif call.data == "helpers_decimal_control":
        hp_decimal.helpers_decimal_control(bot, call)
        show_main_menu(call.message)
    elif call.data == "helpers_decimal_printable":
        hp_decimal.helpers_decimal_printable(bot, call)
        show_main_menu(call.message)
    elif call.data == "helpers_decimal_extended":
        hp_decimal.helpers_decimal_extended(bot, call)
        show_main_menu(call.message)
    elif call.data == "helpers_decimal_all":
        hp_decimal.helpers_decimal_all(bot, call)
        show_main_menu(call.message)

    # Octal
    elif call.data == "show_octal":
        hp_octal.show_octal(bot, chat_id, message_id, types)
    elif call.data == "helpers_octal_control":
        hp_octal.helpers_octal_control(bot, call)
        show_main_menu(call.message)
    elif call.data == "helpers_octal_printable":
        hp_octal.helpers_octal_printable(bot, call)
        show_main_menu(call.message)
    elif call.data == "helpers_octal_extended":
        hp_octal.helpers_octal_extended(bot, call)
        show_main_menu(call.message)
    elif call.data == "helpers_octal_all":
        hp_octal.helpers_octal_all(bot, call)
        show_main_menu(call.message)

    # Hexadecimal
    elif call.data == "show_hexadecimal":
        hp_hexadecimal.show_hexadecimal(bot, chat_id, message_id, types)
    elif call.data == "helpers_hexadecimal_control":
        hp_hexadecimal.helpers_hexadecimal_control(bot, call)
        show_main_menu(call.message)
    elif call.data == "helpers_hexadecimal_printable":
        hp_hexadecimal.helpers_hexadecimal_printable(bot, call)
        show_main_menu(call.message)
    elif call.data == "helpers_hexadecimal_extended":
        hp_hexadecimal.helpers_hexadecimal_extended(bot, call)
        show_main_menu(call.message)
    elif call.data == "helpers_hexadecimal_all":
        hp_hexadecimal.helpers_hexadecimal_all(bot, call)
        show_main_menu(call.message)

    # Binary
    elif call.data == "show_binary":
        hp_binary.show_binary(bot, chat_id, message_id, types)
    elif call.data == "helpers_binary_control":
        hp_binary.helpers_binary_control(bot, call)
        show_main_menu(call.message)
    elif call.data == "helpers_binary_printable":
        hp_binary.helpers_binary_printable(bot, call)
        show_main_menu(call.message)
    elif call.data == "helpers_binary_extended":
        hp_binary.helpers_binary_extended(bot, call)
        show_main_menu(call.message)
    elif call.data == "helpers_binary_all":
        hp_binary.helpers_binary_all(bot, call)
        show_main_menu(call.message)

    # Symbol
    elif call.data == "show_symbol":
        hp_symbol.show_symbol(bot, chat_id, message_id, types)
    elif call.data == "helpers_symbol_printable":
        hp_symbol.helpers_symbol_printable(bot, call)
        show_main_menu(call.message)


# Process the text received after pressing the Encode button
@bot.message_handler(
    func=lambda message: bot.get_state(message.from_user.id) == "waiting_for_encode"
)
def process_encode_step(message):
    """Encode"""
    try:
        text = message.text
        encoded = encode.encode(text)
        bot.reply_to(message, f"Encoded: {encoded}")
        bot.set_state(message.from_user.id, None)

        # Show menu again
        show_main_menu(message)
    except IndexError:
        bot.reply_to(message, "Please provide text to encode. Example: /encode hello")
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")


def process_decode_step(message):
    """Decode"""
    try:
        text = message.text
        original_type = int(text)
        decoded = decode.decode(original_type)
        bot.reply_to(message, f"Decoded: {decoded}")

        # Show menu again
        show_main_menu(message)
    except IndexError:
        bot.reply_to(message, "Please provide text to decode. Example: /decode xyz")
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")


def process_division_step(message):
    """Division"""
    try:
        text = message.text
        base = text.split("/")
        a = int(base[0])
        b = int(base[1])
        ab_float = a / b
        ab_integer = int(a / b)
        rest = a - (ab_integer * b)
        bot.reply_to(
            message,
            f"Decimal part: {ab_float} \n Integer part: {ab_integer} \n Rest of the division: {rest}",
        )
        # Show menu again
        show_main_menu(message)
    except ValueError:
        bot.reply_to(message, "Please provide number to divide. Example: /divide x/y")
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")


# +---------------------------------------------------------------------------------
# Commands
# +---------------------------------------------------------------------------------


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
        original_type = int(text)
        decoded = decode.decode(original_type)
        bot.reply_to(message, f"Decoded: {decoded}")
    except IndexError:
        bot.reply_to(message, "Please provide text to decode. Example: /decode xyz")
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")


# Keep the bot running
if __name__ == "__main__":
    bot.remove_webhook()
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f"Polling error: {e}")
            time.sleep(5)  # wait before retrying
