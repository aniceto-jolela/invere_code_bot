from inverse_code.helpers import binshow


def show_binary(bot, chat_id, message_id, types):
    """Show binary"""
    markup = types.InlineKeyboardMarkup(row_width=2)

    item1 = types.InlineKeyboardButton(
        "Control characters 0-11111", callback_data="helpers_binary_control"
    )
    item2 = types.InlineKeyboardButton(
        "Printable characters 100000-01111111", callback_data="helpers_binary_printable"
    )
    item3 = types.InlineKeyboardButton(
        "Extended ascii 10000000-11111111", callback_data="helpers_binary_extended"
    )
    item4 = types.InlineKeyboardButton("All binary", callback_data="helpers_binary_all")
    back = types.InlineKeyboardButton("« Back", callback_data="menu_helpers")

    markup.add(item1, item2, item3, item4)
    markup.add(back)
    bot.edit_message_text("ℹ️ Helpers Menu:", chat_id, message_id, reply_markup=markup)


def helpers_binary_control(bot, call):
    """helpers_binary_control"""
    helper_binary = binshow.control_characters_0_11111()
    bot.send_message(
        call.message.chat.id, f"Control characters 0-11111:\n\n{helper_binary}"
    )


def helpers_binary_printable(bot, call):
    """helpers_binary_printable"""
    helper_binary = binshow.printable_characters_100000_01111111()
    bot.send_message(
        call.message.chat.id,
        f"Printable characters 100000-01111111:\n\n{helper_binary}",
    )


def helpers_binary_extended(bot, call):
    """helpers_binary_extended"""
    helper_binary = binshow.extended_ascii_10000000_11111111()
    bot.send_message(
        call.message.chat.id, f"Extended ascii 10000000-11111111:\n\n{helper_binary}"
    )


def helpers_binary_all(bot, call):
    """helpers_binary_all"""
    helper_binary = binshow.all_binary()
    bot.send_message(call.message.chat.id, f"All binary:\n\n{helper_binary}")
