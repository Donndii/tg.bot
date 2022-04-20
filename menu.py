import telegram
from button import start_b, coffeshop_b

def main_menu_keyboard():
    keyboard = ([
    [
        telegram.KeyboardButton(start_b[0])
    ],
    [
        telegram.KeyboardButton(start_b[1]),
        telegram.KeyboardButton(start_b[2])
    ]
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard= True, one_time_keyboard=False
    )

def coffeshop_keyboard():
    keyboard = ([
    [
        telegram.KeyboardButton(coffeshop_b[0]),
        telegram.KeyboardButton(coffeshop_b[1])
    ],
    [
        telegram.KeyboardButton(coffeshop_b[2]),
        telegram.KeyboardButton(coffeshop_b[3])
    ],
    [ 
        telegram.KeyboardButton(coffeshop_b[4]),
        telegram.KeyboardButton(coffeshop_b[5])
    ]
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard= False
    )