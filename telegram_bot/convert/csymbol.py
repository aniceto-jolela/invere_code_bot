from inverse_code.convert import csymb
from token_bot import bot, types


def show_convert_symbol(chat_id, message_id):
    """Show convert symbol"""
    markup = types.InlineKeyboardMarkup(row_width=2)

    item1 = types.InlineKeyboardButton(
        "Convert symbol to decimal", callback_data="convert_symbol_decimal"
    )
    item2 = types.InlineKeyboardButton(
        "Convert symbol to octal", callback_data="convert_symbol_octal"
    )
    item3 = types.InlineKeyboardButton(
        "Convert symbol to hexadecimal", callback_data="convert_symbol_hexadecimal"
    )
    item4 = types.InlineKeyboardButton(
        "Convert symbol to binary", callback_data="convert_symbol_binary"
    )
    back = types.InlineKeyboardButton("« Back", callback_data="menu_convert")

    markup.add(item1, item2, item3, item4)
    markup.add(back)
    bot.edit_message_text("ℹ️ Convert Menu:", chat_id, message_id, reply_markup=markup)


def convert_symbol_decimal(message):
    """convert_symbol_decimal"""
    try:
        text = message.text
        cv = csymb.csymb_decimal(text)
        bot.reply_to(message, f"Decimal: {cv}")
    except ValueError:
        bot.reply_to(
            message,
            "Please provide correct binary number in the interval from ! to ~. Example: /Symbol A",
        )
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")


def convert_symbol_octal(message):
    """convert_symbol_octal"""
    try:
        text = message.text
        cv = csymb.csymb_octal(text)
        bot.reply_to(message, f"Octal: {cv}")
    except ValueError:
        bot.reply_to(
            message,
            "Please provide correct binary number in the interval from ! to ~. Example: /Symbol =",
        )
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")


def convert_symbol_hexadecimal(message):
    """convert_symbol_hexadecimal"""
    try:
        text = message.text
        cv = csymb.csymb_hexadecimal(text)
        bot.reply_to(message, f"Hexadecimal: {cv}")
    except ValueError:
        bot.reply_to(
            message,
            "Please provide correct binary number in the interval from ! to ~. Example: /Symbol ?",
        )
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")


def convert_symbol_binary(message):
    """convert_symbol_binary"""
    try:
        text = message.text
        cv = csymb.csymb_binary(text)
        bot.reply_to(message, f"Binary: {cv}")
    except ValueError:
        bot.reply_to(
            message,
            "Please provide correct binary number in the interval from ! to ~. Example: /Symbol y",
        )
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")
