from inverse_code.helpers import decshow


def show_decimal(bot, chat_id, message_id, types):
    """Show Decimal"""
    markup = types.InlineKeyboardMarkup(row_width=2)

    item1 = types.InlineKeyboardButton(
        "Control characters 0-31", callback_data="helpers_decimal_control"
    )
    item2 = types.InlineKeyboardButton(
        "Printable characters 32-127", callback_data="helpers_decimal_printable"
    )
    item3 = types.InlineKeyboardButton(
        "Extended ascii 128-255", callback_data="helpers_decimal_extended"
    )
    item4 = types.InlineKeyboardButton(
        "All decimal", callback_data="helpers_decimal_all"
    )
    back = types.InlineKeyboardButton("« Back", callback_data="menu_helpers")

    markup.add(item1, item2, item3, item4)
    markup.add(back)
    bot.edit_message_text("ℹ️ Helpers Menu:", chat_id, message_id, reply_markup=markup)


def helpers_decimal_control(bot, call):
    """helpers_decimal_control"""
    helper_decimal = decshow.control_characters_0_31()
    bot.send_message(
        call.message.chat.id, f"Control characters 0-31:\n\n{helper_decimal}"
    )


def helpers_decimal_printable(bot, call):
    """helpers_decimal_printable"""
    helper_decimal = decshow.printable_characters_32_127()
    bot.send_message(
        call.message.chat.id, f"Printable characters 32-127:\n\n{helper_decimal}"
    )


def helpers_decimal_extended(bot, call):
    """helpers_decimal_extended"""
    helper_decimal = decshow.extended_ascii_128_255()
    bot.send_message(
        call.message.chat.id, f"Extended ascii 128-255:\n\n{helper_decimal}"
    )


def helpers_decimal_all(bot, call):
    """helpers_decimal_all"""
    helper_decimal = decshow.all_decimal()
    bot.send_message(call.message.chat.id, f"All decimal:\n\n{helper_decimal}")
