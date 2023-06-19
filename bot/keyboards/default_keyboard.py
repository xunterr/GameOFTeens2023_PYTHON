from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from bot.model import poll

class PollKeyboard:
    def get_question_kb(self, variants:list, current: int, cd: CallbackData):
        keyboard = InlineKeyboardMarkup()
        for id, v in enumerate(variants):
            variant_bt = InlineKeyboardButton(text=v, callback_data=cd.new(question=current, variant=id))
            keyboard.add(variant_bt)
        return keyboard
    
    def get_finish_kb(self):
        get_results_bt = InlineKeyboardButton(text="😎 Результати", callback_data="finish_poll")
        keyboard = InlineKeyboardMarkup()
        keyboard.add(get_results_bt)
        return keyboard

def get_start_kb():
    github_bt = InlineKeyboardButton(text="👩‍💻 Github", url="https://github.com/xunterr/GameOFTeens2023_PYTHON")
    my_results_bt = InlineKeyboardButton(text="🤯 Підібраний тариф", callback_data="get_tariff")
    find_tariff_bt = InlineKeyboardButton(text="🚀 Підібрати тариф", callback_data="start_poll")
    keyboard = InlineKeyboardMarkup()
    keyboard.add(github_bt).add(my_results_bt).add(find_tariff_bt)
    return keyboard