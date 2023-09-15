import logging
from buttons import *



API_TOKEN = '5939160792:AAE_1G0NBWbrFRCsKAXPaa4Uic_Etz3WTqM'


logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# Start
@dp.message_handler(commands=['start', 'menu'])
async def send_welcome(message: types.Message):

    await message.reply("Salom\nMars it botga xush kelibsiz \n",reply_markup=bosh_menu)

# Profil
@dp.message_handler(text = 'Profil')
async def send_welcome(message: types.Message):

    await message.reply("""Ism: Kamoliddin
Familiya: Fazliddinov
Til: uz
Telefon: 940025234
Shahar: Toshkent
Ta’lim markazi: YUNUSABAD""",reply_markup=profil)
    
@dp.message_handler(text = 'Ism')
async def send_welcome(message: types.Message):

    await message.reply(text= "Kamoliddin")

@dp.message_handler(text = 'Familiya')
async def send_welcome(message: types.Message):

    await message.reply(text= "Fazliddinov")

@dp.message_handler(text = 'Telefon')
async def send_welcome(message: types.Message):

    await message.reply(text= "940025234")

@dp.message_handler(text = 'Shahar')
async def send_welcome(message: types.Message):

    await message.reply(text= "Toshkent")

@dp.message_handler(text = 'Ta’lim markazi')
async def send_welcome(message: types.Message):

    await message.reply(text= "YUNUSABAD")

@dp.message_handler(text = 'Til')
async def send_welcome(message: types.Message):

    await message.reply(text= "uz")


# Mening tangalarim
@dp.message_handler(text = 'Mening tangalarim')
async def send_welcome(message: types.Message):

    await message.reply(text= "Mening mars tangalarim: 123")

# Space Shop
@dp.message_handler(text = 'Space shop')
async def send_welcome(message: types.Message):

    await message.reply(text= "Menu",reply_markup=space)

@dp.message_handler(text = "Mars notebook")
async def echo(message: types.Message):
    await message.answer_photo(photo="https://t.me/fhdjhfjdhh/3?single",
                               caption="200 coins",reply_markup=ortga)

@dp.message_handler(text = "Mars pen")
async def echo(message: types.Message):
    await message.answer_photo(photo="https://t.me/fhdjhfjdhh/4",
                               caption="25 coins",reply_markup=ortga)

@dp.message_handler(text = "Usb fleshka")
async def echo(message: types.Message):
    await message.answer_photo(photo="https://t.me/fhdjhfjdhh/5",
                               caption="150 coins",reply_markup=ortga)
    
@dp.message_handler(text = "Keyboard")
async def echo(message: types.Message):
    await message.answer_photo(photo="https://t.me/fhdjhfjdhh/6",
                               caption="350 coins",reply_markup=ortga)

@dp.message_handler(text = "Mouse")
async def echo(message: types.Message):
    await message.answer_photo(photo="https://t.me/fhdjhfjdhh/7",
                               caption="250 coins",reply_markup=ortga)
    
@dp.message_handler(text = "Mars chocolate")
async def echo(message: types.Message):
    await message.answer_photo(photo="https://t.me/fhdjhfjdhh/8",
                               caption="50 coins",reply_markup=ortga)
    
@dp.message_handler(text = "Strobar")
async def echo(message: types.Message):
    await message.answer_photo(photo="https://t.me/fhdjhfjdhh/9",
                               caption="30 coins",reply_markup=ortga)
    
@dp.message_handler(text = "Mars mini")
async def echo(message: types.Message):
    await message.answer_photo(photo="https://t.me/fhdjhfjdhh/10",
                               caption="25 coins",reply_markup=ortga)
    
@dp.message_handler(text = "Mars sticker")
async def echo(message: types.Message):
    await message.answer_photo(photo="https://t.me/fhdjhfjdhh/11",
                               caption="70 coins",reply_markup=ortga)
    
@dp.message_handler(text = "Mars rug")
async def echo(message: types.Message):
    await message.answer_photo(photo="https://t.me/fhdjhfjdhh/12",
                               caption="100 coins",reply_markup=ortga)

# Sharh qoldiring
@dp.message_handler(text = "Sharh qoldiring")
async def echo(message: types.Message):
    await message.answer_photo(photo="https://t.me/fhdjhfjdhh/13",
                               caption="Izoh qoldiring")





@dp.message_handler(text = 'Ortga')
async def send_welcome(message: types.Message):

    await message.reply(text= ".",reply_markup=bosh_menu)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)