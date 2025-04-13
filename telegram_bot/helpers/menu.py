def menu_helpers(bot, call, types):
    """Menu Helpers"""
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    markup = types.InlineKeyboardMarkup(row_width=2)

    item1 = types.InlineKeyboardButton("Show Decimal", callback_data="show_decimal")
    item2 = types.InlineKeyboardButton("Show Octal", callback_data="show_octal")
    item3 = types.InlineKeyboardButton(
        "Show Hexadecimal", callback_data="show_hexadecimal"
    )
    item4 = types.InlineKeyboardButton("Show Binary", callback_data="show_binary")
    item5 = types.InlineKeyboardButton("Show Symbol", callback_data="show_symbol")
    back = types.InlineKeyboardButton("« Back", callback_data="main_menu")

    markup.add(item1, item2, item3, item4, item5)
    markup.add(back)
    bot.edit_message_text("ℹ️ Helpers Menu:", chat_id, message_id, reply_markup=markup)
