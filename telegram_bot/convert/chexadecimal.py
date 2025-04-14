from inverse_code.convert import chex
from token_bot import bot, types


def show_convert_hexadecimal(chat_id, message_id):
    """Show convert Hexadecimal"""
    markup = types.InlineKeyboardMarkup(row_width=2)

    item1 = types.InlineKeyboardButton(
        "Convert hexadecimal to decimal", callback_data="convert_hexadecimal_decimal"
    )
    item2 = types.InlineKeyboardButton(
        "Convert hexadecimal to octal", callback_data="convert_hexadecimal_octal"
    )
    item3 = types.InlineKeyboardButton(
        "Convert hexadecimal to binary", callback_data="convert_hexadecimal_binary"
    )
    item4 = types.InlineKeyboardButton(
        "Convert hexadecimal to symbol", callback_data="convert_hexadecimal_symbol"
    )
    back = types.InlineKeyboardButton("« Back", callback_data="menu_convert")

    markup.add(item1, item2, item3, item4)
    markup.add(back)
    bot.edit_message_text("ℹ️ Convert Menu:", chat_id, message_id, reply_markup=markup)


def convert_hexadecimal_decimal(message):
    """convert_hexadecimal_decimal"""
    try:
        text = message.text
        cv = chex.chex_decimal(text)
        bot.reply_to(message, f"Decimal: {cv}")

    except ValueError:
        bot.reply_to(
            message,
            "Please provide correct decimal number in the interval from 00 to ff. Example: /Hexadecimal 20",
        )
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")


def convert_hexadecimal_octal(message):
    """convert_hexadecimal_octal"""
    try:
        text = message.text
        cv = chex.chex_octal(text)
        bot.reply_to(message, f"Octal: {cv}")
    except ValueError:
        bot.reply_to(
            message,
            "Please provide correct decimal number in the interval from 00 to ff. Example: /Hexadecimal 10",
        )
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")


def convert_hexadecimal_binary(message):
    """convert_hexadecimal_binary"""
    try:
        text = message.text
        cv = chex.chex_binary(text)
        bot.reply_to(message, f"Binary: {cv}")
    except ValueError:
        bot.reply_to(
            message,
            "Please provide correct decimal number in the interval from 00 to ff. Example: /Hexadecimal fc",
        )
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")


def convert_hexadecimal_symbol(message):
    """convert_hexadecimal_symbol"""
    try:
        text = message.text
        cv = chex.chex_symbol(text)
        bot.reply_to(message, f"Symbol: {cv}")
    except ValueError:
        bot.reply_to(
            message,
            "Please provide correct decimal number in the interval from 20 to 7f. Example: /Hexadecimal 79",
        )
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")
