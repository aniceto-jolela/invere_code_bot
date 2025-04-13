from inverse_code.convert import cdec


def show_decimal(bot, chat_id, message_id, types):
    """Show Decimal"""
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
    back = types.InlineKeyboardButton("« Back", callback_data="menu_helpers")

    markup.add(item1, item2, item3, item4)
    markup.add(back)
    bot.edit_message_text("ℹ️ Helpers Menu:", chat_id, message_id, reply_markup=markup)


def convert_decimal_octal(bot, message):
    """convert_decimal_octal"""
    try:
        text = message.text
        cv = cdec.cdec_octal(text)
        bot.reply_to(message, f"Octal: {cv}")
        bot.set_state(message.from_user.id, None)
    except IndexError:
        bot.reply_to(message, "Please provide text to decimal. Example: /decimal 20")
    except Exception as e:
        bot.reply_to(message, f"Error: {str(e)}")


def convert_decimal_hexadecimal(bot, call):
    """convert_decimal_hexadecimal"""
    cv = cdec.cdec_hexadecimal("")
    bot.send_message(call.message.chat.id, f"Convert decimal to hexadecimal:\n\n{cv}")


def convert_decimal_binary(bot, call):
    """convert_decimal_binary"""
    cv = cdec.cdec_binary("")
    bot.send_message(call.message.chat.id, f"Convert decimal to binary:\n\n{cv}")


def convert_decimal_symbol(bot, call):
    """convert_decimal_symbol"""
    cv = cdec.cdec_symbol("")
    bot.send_message(call.message.chat.id, f"Convert decimal to symbol:\n\n{cv}")
