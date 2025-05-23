from inverse_code.convert import cdec
from token_bot import bot, types


def show_convert_decimal(chat_id, message_id):
    """Show convert Decimal"""
    markup = types.InlineKeyboardMarkup(row_width=2)

    item1 = types.InlineKeyboardButton(
        "Convert decimal to octal", callback_data="convert_decimal_octal"
    )
    item2 = types.InlineKeyboardButton(
        "Convert decimal to hexadecimal", callback_data="convert_decimal_hexadecimal"
    )
    item3 = types.InlineKeyboardButton(
        "Convert decimal to binary", callback_data="convert_decimal_binary"
    )
    item4 = types.InlineKeyboardButton(
        "Convert decimal to symbol", callback_data="convert_decimal_symbol"
    )
    back = types.InlineKeyboardButton("« Back", callback_data="menu_convert")

    markup.add(item1, item2, item3, item4)
    markup.add(back)
    bot.edit_message_text("ℹ️ Convert Menu:", chat_id, message_id, reply_markup=markup)


def convert_decimal_octal(message):
    """convert_decimal_octal"""
    try:
        text = message.text
        original_type = int(text)
        cv = cdec.cdec_octal(original_type)
        bot.reply_to(message, f"Octal: {cv}")

    except ValueError:
        bot.reply_to(
            message,
            "Please provide correct decimal number in the interval from 0 to 255. Example: /Decimal 20",
        )
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")


def convert_decimal_hexadecimal(message):
    """convert_decimal_hexadecimal"""
    try:
        text = message.text
        original_type = int(text)
        cv = cdec.cdec_hexadecimal(original_type)
        bot.reply_to(message, f"Hexadecimal: {cv}")
    except ValueError:
        bot.reply_to(
            message,
            "Please provide correct decimal number in the interval from 0 to 255. Example: /Decimal 15",
        )
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")


def convert_decimal_binary(message):
    """convert_decimal_binary"""
    try:
        text = message.text
        original_type = int(text)
        cv = cdec.cdec_binary(original_type)
        bot.reply_to(message, f"Binary: {cv}")
    except ValueError:
        bot.reply_to(
            message,
            "Please provide correct decimal number in the interval from 0 to 255. Example: /Decimal 213",
        )
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")


def convert_decimal_symbol(message):
    """convert_decimal_symbol"""
    try:
        text = message.text
        original_type = int(text)
        cv = cdec.cdec_symbol(original_type)
        bot.reply_to(message, f"Symbol: {cv}")
    except ValueError:
        bot.reply_to(
            message,
            "Please provide correct decimal number in the interval from 40 to 176. Example: /Decimal 141",
        )
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")
