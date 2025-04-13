from inverse_code.helpers import hexshow


def show_hexadecimal(bot, chat_id, message_id, types):
    """Show hexadecimal"""
    markup = types.InlineKeyboardMarkup(row_width=2)

    item1 = types.InlineKeyboardButton(
        "Control characters 0-37", callback_data="helpers_hexadecimal_control"
    )
    item2 = types.InlineKeyboardButton(
        "Printable characters 20-7f", callback_data="helpers_hexadecimal_printable"
    )
    item3 = types.InlineKeyboardButton(
        "Extended ascii 80-ff", callback_data="helpers_hexadecimal_extended"
    )
    item4 = types.InlineKeyboardButton(
        "All hexadecimal", callback_data="helpers_hexadecimal_all"
    )
    back = types.InlineKeyboardButton("« Back", callback_data="menu_helpers")

    markup.add(item1, item2, item3, item4)
    markup.add(back)
    bot.edit_message_text("ℹ️ Helpers Menu:", chat_id, message_id, reply_markup=markup)


def helpers_hexadecimal_control(bot, call):
    """helpers_hexadecimal_control"""
    helper_hexadecimal = hexshow.control_characters_0_1f()
    bot.send_message(
        call.message.chat.id, f"Control characters 0-1f:\n\n{helper_hexadecimal}"
    )


def helpers_hexadecimal_printable(bot, call):
    """helpers_hexadecimal_printable"""
    helper_hexadecimal = hexshow.printable_characters_20_7f()
    bot.send_message(
        call.message.chat.id, f"Printable characters 20-7f:\n\n{helper_hexadecimal}"
    )


def helpers_hexadecimal_extended(bot, call):
    """helpers_hexadecimal_extended"""
    helper_hexadecimal = hexshow.extended_ascii_80_ff()
    bot.send_message(
        call.message.chat.id, f"Extended ascii 80-ff:\n\n{helper_hexadecimal}"
    )


def helpers_hexadecimal_all(bot, call):
    """helpers_hexadecimal_all"""
    helper_hexadecimal = hexshow.all_hexadecimal()
    bot.send_message(call.message.chat.id, f"All hexadecimal:\n\n{helper_hexadecimal}")
