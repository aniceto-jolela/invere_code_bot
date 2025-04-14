from inverse_code.convert import coct
from token_bot import bot, types


def show_convert_octal(chat_id, message_id):
    """Show convert Octal"""
    markup = types.InlineKeyboardMarkup(row_width=2)

    item1 = types.InlineKeyboardButton(
        "Convert octal to decimal", callback_data="convert_octal_decimal"
    )
    item2 = types.InlineKeyboardButton(
        "Convert octal to hexadecimal", callback_data="convert_octal_hexadecimal"
    )
    item3 = types.InlineKeyboardButton(
        "Convert octal to binary", callback_data="convert_octal_binary"
    )
    item4 = types.InlineKeyboardButton(
        "Convert octal to symbol", callback_data="convert_octal_symbol"
    )
    back = types.InlineKeyboardButton("« Back", callback_data="menu_convert")

    markup.add(item1, item2, item3, item4)
    markup.add(back)
    bot.edit_message_text("ℹ️ Convert Menu:", chat_id, message_id, reply_markup=markup)


def convert_octal_decimal(message):
    """convert_octal_decimal"""
    try:
        text = message.text
        original_type = int(text)
        cv = coct.coct_decimal(original_type)
        bot.reply_to(message, f"Octal: {cv}")

    except ValueError:
        bot.reply_to(
            message,
            "Please provide correct decimal number in the interval from 0 to 377. Example: /Octal 20",
        )
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")


def convert_octal_hexadecimal(message):
    """convert_octal_hexadecimal"""
    try:
        text = message.text
        original_type = int(text)
        cv = coct.coct_hexadecimal(original_type)
        bot.reply_to(message, f"Hexadecimal: {cv}")
    except ValueError:
        bot.reply_to(
            message,
            "Please provide correct decimal number in the interval from 0 to 377. Example: /Octal 15",
        )
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")


def convert_octal_binary(message):
    """convert_octal_binary"""
    try:
        text = message.text
        original_type = int(text)
        cv = coct.coct_binary(original_type)
        bot.reply_to(message, f"Binary: {cv}")
    except ValueError:
        bot.reply_to(
            message,
            "Please provide correct decimal number in the interval from 0 to 377. Example: /Octal 213",
        )
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")


def convert_octal_symbol(message):
    """convert_octal_symbol"""
    try:
        text = message.text
        original_type = int(text)
        cv = coct.coct_symbol(original_type)
        bot.reply_to(message, f"Symbol: {cv}")
    except ValueError:
        bot.reply_to(
            message,
            "Please provide correct decimal number in the interval from 32 to 126. Example: /Octal 46",
        )
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")
