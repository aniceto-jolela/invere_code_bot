from inverse_code.convert import cbin
from token_bot import bot, types


def show_convert_binary(chat_id, message_id):
    """Show convert Binary"""
    markup = types.InlineKeyboardMarkup(row_width=2)

    item1 = types.InlineKeyboardButton(
        "Convert binary to decimal", callback_data="convert_binary_decimal"
    )
    item2 = types.InlineKeyboardButton(
        "Convert binary to octal", callback_data="convert_binary_octal"
    )
    item3 = types.InlineKeyboardButton(
        "Convert binary to hexadecimal", callback_data="convert_binary_hexadecimal"
    )
    item4 = types.InlineKeyboardButton(
        "Convert binary to symbol", callback_data="convert_binary_symbol"
    )
    back = types.InlineKeyboardButton("« Back", callback_data="menu_convert")

    markup.add(item1, item2, item3, item4)
    markup.add(back)
    bot.edit_message_text("ℹ️ Convert Menu:", chat_id, message_id, reply_markup=markup)


def convert_binary_decimal(message):
    """convert_binary_decimal"""
    try:
        text = message.text
        cv = cbin.cbin_decimal(text)
        bot.reply_to(message, f"Decimal: {cv}")
    except ValueError:
        bot.reply_to(
            message,
            "Please provide correct binary number in the interval from 00000000-11111111. Example: /Binary 11111110",
        )
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")


def convert_binary_octal(message):
    """convert_binary_octal"""
    try:
        text = message.text
        cv = cbin.cbin_octal(text)
        bot.reply_to(message, f"Octal: {cv}")
    except ValueError:
        bot.reply_to(
            message,
            "Please provide correct binary number in the interval from 00000000-11111111. Example: /Binary 10100001",
        )
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")


def convert_binary_hexadecimal(message):
    """convert_binary_hexadecimal"""
    try:
        text = message.text
        cv = cbin.cbin_hexadecimal(text)
        bot.reply_to(message, f"Hexadecimal: {cv}")
    except ValueError:
        bot.reply_to(
            message,
            "Please provide correct binary number in the interval from 00000000-11111111. Example: /Binary 00001111",
        )
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")


def convert_binary_symbol(message):
    """convert_binary_symbol"""
    try:
        text = message.text
        cv = cbin.cbin_symbol(text)
        bot.reply_to(message, f"Symbol: {cv}")
    except ValueError:
        bot.reply_to(
            message,
            "Please provide correct binary number in the interval from 00100000-01111111. Example: /Binary 01001101",
        )
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")
