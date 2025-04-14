def menu_convert(bot, call, types):
    """Menu convert"""
    chat_id = call.message.chat.id
    message_id = call.message.message_id

    markup = types.InlineKeyboardMarkup(row_width=2)

    item1 = types.InlineKeyboardButton("Decimal", callback_data="show_convert_decimal")
    item2 = types.InlineKeyboardButton("Octal", callback_data="show_convert_octal")
    item3 = types.InlineKeyboardButton(
        "Hexadecimal", callback_data="show_convert_hexadecimal"
    )
    item4 = types.InlineKeyboardButton("Binary", callback_data="show_convert_binary")
    item5 = types.InlineKeyboardButton("Symbol", callback_data="show_convert_symbol")
    back = types.InlineKeyboardButton("« Back", callback_data="main_menu")

    markup.add(item1, item2, item3, item4, item5)
    markup.add(back)

    bot.edit_message_text("♻️ Convert Menu:", chat_id, message_id, reply_markup=markup)
