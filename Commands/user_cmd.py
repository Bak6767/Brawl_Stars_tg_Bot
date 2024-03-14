
from aiogram.types import Message, InlineKeyboardMarkup, CallbackQuery, InlineKeyboardButton
from Commands import parser_profile_photo_and_name as pars
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import CommandStart, Command
from aiogram import types, Router, F, Bot
from aiogram import exceptions
from dotenv import load_dotenv
from database import bd as db
import os


rp = Router()
load_dotenv()
bot = Bot(token = os.getenv("TOKEN_API"))

#Обработка команды /start
cmd_list = "\n1. /start - Запустить/перезапустить бота\n2. /Brawl_Stars - Взаимодействие с твоим Brawl Stars id"
@rp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"🚀 Привет! Вот полный список команд, которые сейчас доступны:{cmd_list}")

#Обработка команды /Brawl_Stars
@rp.message(Command("Brawl_Stars"))
async def key(message: types.Message):
    from battons.battons import communication
    markup = await communication()
    await message.answer("Вибери действие:", reply_markup = markup)

#Парсер фотографии профиля
#Состояние ✅
async def pars_profile_photo(message: Message, profile_id, user_id):
    try:
        await pars.pars_profile_photo(profile_id)
        profile_photo = "D:\Project\Tg-Brawl-Bot\profile_photo.jpg"
        await message.answer_photo(photo = types.FSInputFile(path = profile_photo))
        if os.path.exists(profile_photo):
            os.remove(profile_photo)
    except exceptions.TelegramBadRequest:
        await change_brawl_id(message, user_id)

#Функция которая изменяет вибраний Btawl Stars ID
#Состояние ✅
async def change_brawl_id(message: Message, user_id):
    await message.answer("Похоже вы указали не правиьный Brawl Stars ID.")
    await message.answer("Напиши еще раз свой Brawl Stars ID(без #):")
    @rp.message(F.text)
    async def profile_bs_id(message: Message):
        brawl_id = str(message.text.upper())
        await db.save_brawl_stars_id_1(user_id, brawl_id)
        await pars_profile_photo(message, brawl_id, user_id)


#Функция которая проверяет есть лы такой user если да тогда возвращает нужний Brawl Stars ID
#Состояние ✅
async def send_profile_photo(message: Message, user_id, nume):
    profile_id = str(await db.__getattribute__(f"get_brawl_id_{nume}")(user_id))
    if profile_id == "False" or profile_id == "None":
        await message.answer("Напиши свой Brawl Stars ID(без #):")
        await db.save_user_id(user_id)
        @rp.message(F.text)
        async def profile_bs_id(message: Message):
            brawl_id = str(message.text.upper())
            await db.__getattribute__(f"save_brawl_stars_id_{nume}")(user_id, brawl_id)
            await pars_profile_photo(message, brawl_id, user_id)
            
    else:
        await pars_profile_photo(message, profile_id, user_id)


#Функция которая сохраняет вибраний Brawl Stars ID
async def save_brawl_stars_id(message: Message, user_id, nume):
    await message.answer("Напиши свой Brawl Stars ID(без #):")
    @rp.message(F.text)
    async def profile_bs_id(message: Message):
        brawl_id = str(message.text.upper())
        await db.__getattribute__(f"save_brawl_stars_id_{nume}")(user_id, brawl_id)

#-------------------------------------------------------------#
#Обработчики кнопок

#Обработчики команды /Brawl_Stars     
@rp.callback_query(F.data == "photo")
async def batton(call: CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    from battons.battons import photo
    user_id = call.from_user.id
    await photo(user_id)
    markup = await photo(call.from_user.id)
    await call.message.answer("Виберете Brawl Stars ID из доступних вам:", reply_markup = markup)

@rp.callback_query(F.data == "change")
async def batton(call: CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    pass

#Обработчики кнопоки add
@rp.callback_query(F.data == "add_brawl_id_1")
async def batton(call: CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    user_id = call.from_user.id
    nume = 1
    await send_profile_photo(call.message, user_id, nume)
@rp.callback_query(F.data == "brawl_id_1")
async def batton(call: CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    user_id = call.from_user.id
    nume = 1
    await send_profile_photo(call.message, user_id, nume)


@rp.callback_query(F.data == "add_brawl_id_2")
async def batton(call: CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    user_id = call.from_user.id
    nume = 2
    await send_profile_photo(call.message, user_id, nume)
@rp.callback_query(F.data == "brawl_id_2")
async def batton(call: CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    user_id = call.from_user.id
    nume = 2
    await send_profile_photo(call.message, user_id, nume)


@rp.callback_query(F.data == "add_brawl_id_3")
async def batton(call: CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    user_id = call.from_user.id
    nume = 3
    await send_profile_photo(call.message, user_id, nume)
@rp.callback_query(F.data == "brawl_id_3")
async def batton(call: CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    user_id = call.from_user.id
    nume = 3
    await send_profile_photo(call.message, user_id, nume)
