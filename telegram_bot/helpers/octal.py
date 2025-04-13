from inverse_code.helpers import octshow


def show_octal(bot, chat_id, message_id, types):
    """Show Octal"""
    markup = types.InlineKeyboardMarkup(row_width=2)

    item1 = types.InlineKeyboardButton(
        "Control characters 0-37", callback_data="helpers_octal_control"
    )
    item2 = types.InlineKeyboardButton(
        "Printable characters 40-177", callback_data="helpers_octal_printable"
    )
    item3 = types.InlineKeyboardButton(
        "Extended ascii 200-377", callback_data="helpers_octal_extended"
    )
    item4 = types.InlineKeyboardButton("All octal", callback_data="helpers_octal_all")
    back = types.InlineKeyboardButton("« Back", callback_data="menu_helpers")

    markup.add(item1, item2, item3, item4)
    markup.add(back)
    bot.edit_message_text("ℹ️ Helpers Menu:", chat_id, message_id, reply_markup=markup)


def helpers_octal_control(bot, call):
    """helpers_octal_control"""
    helper_octal = octshow.control_characters_0_37()
    bot.send_message(
        call.message.chat.id, f"Control characters 0-37:\n\n{helper_octal}"
    )


def helpers_octal_printable(bot, call):
    """helpers_octal_printable"""
    helper_octal = octshow.printable_characters_40_177()
    bot.send_message(
        call.message.chat.id, f"Printable characters 40-177:\n\n{helper_octal}"
    )


def helpers_octal_extended(bot, call):
    """helpers_octal_extended"""
    helper_octal = octshow.extended_ascii_200_377()
    bot.send_message(call.message.chat.id, f"Extended ascii 200-377:\n\n{helper_octal}")


def helpers_octal_all(bot, call):
    """helpers_octal_all"""
    helper_octal = octshow.all_octal()
    bot.send_message(call.message.chat.id, f"All octal:\n\n{helper_octal}")
