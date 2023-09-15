from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# Bosh menu
bosh_menu = ReplyKeyboardMarkup(
    keyboard = [
         [
            KeyboardButton('Profil'),
            KeyboardButton('Mening tangalarim'),
            KeyboardButton('Space shop')
        ],
        [
            KeyboardButton('Maktab haqida'),
            KeyboardButton('Sharh qoldiring')
        ],
    
    ],
    resize_keyboard=True
)


# Profil
profil = ReplyKeyboardMarkup(
    keyboard = [
         [
            KeyboardButton('Ism'),
            KeyboardButton('Familiya'),
        ],
        [
            KeyboardButton('Til'),
            KeyboardButton('Telefon')
        ],
        [
            KeyboardButton('Shahar')
        ],
        [
            KeyboardButton('Ortga')
        ]
    
    ],
    resize_keyboard=True
)

# Space shop
space = ReplyKeyboardMarkup(
    keyboard = [
         [
            KeyboardButton('Mars notebook'),
            KeyboardButton('Mars pen'),
        ],
        [
            KeyboardButton('Usb fleshka'),
            KeyboardButton('Keyboard')
        ],
        [
            KeyboardButton('Mouse'),
            KeyboardButton('Mars chocolate')
        ],
        [
           KeyboardButton('Strobar'),
           KeyboardButton('Mars mini') 
        ],
        [
           KeyboardButton('Mars sticker'),
           KeyboardButton('Mars rug') 
        ],
    
    ],
    resize_keyboard=True
)
ortga = ReplyKeyboardMarkup(
    keyboard = [
         [
            KeyboardButton('Sotib olmoq'),
            KeyboardButton('Ortga')
        ],
    
    ],
    resize_keyboard=True
)