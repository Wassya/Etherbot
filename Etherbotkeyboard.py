from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# main menu
btnMiner = InlineKeyboardButton(text="Статистика", callback_data="stata")
mainmenu = InlineKeyboardMarkup(row_width=2).add(btnMiner)

# подменю "Стата"
btnmain = InlineKeyboardButton(text="В главное меню", callback_data="backtomain")
submenupremium = InlineKeyboardMarkup(row_width=2).add(btnmain)
