from inverse_code.helpers import symbshow


def show_symbol(bot, chat_id, message_id, types):
    """Show Symbol"""
    markup = types.InlineKeyboardMarkup(row_width=2)

    item1 = types.InlineKeyboardButton(
        "Printable characters", callback_data="helpers_symbol_printable"
    )

    back = types.InlineKeyboardButton("« Back", callback_data="menu_helpers")

    markup.add(item1)
    markup.add(back)
    bot.edit_message_text("ℹ️ Helpers Menu:", chat_id, message_id, reply_markup=markup)


def helpers_symbol_printable(bot, call):
    """helpers_symbol_printable"""
    helper_symbol = symbshow.printable_characters_32_127()
    bot.send_message(
        call.message.chat.id, f"Printable characters 32-127:\n\n{helper_symbol}"
    )
