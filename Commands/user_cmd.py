from Commands import parser_profile_photo_and_name as pars
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram import types, Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram import exceptions
from dotenv import load_dotenv
from database import bd as db
import os


rp = Router()
load_dotenv()
bot = Bot(token = os.getenv("TOKEN_API"))

class router_for_command_brawl_stars(StatesGroup):
    brawl_id = State()
    nume = State()
    user_id = State()

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
    await message.answer("Выбери действие:", reply_markup = markup)

#Парсер фотографии профиля
async def pars_profile_photo(message: Message, profile_id, user_id):
    try:
        await pars.pars_profile_photo(profile_id)
        profile_photo = "D:\Project\Tg-Brawl-Bot\profile_photo.webp"
        await message.answer_photo(photo = types.FSInputFile(path = profile_photo))
        if os.path.exists(profile_photo):
            os.remove(profile_photo)
    except exceptions.TelegramBadRequest:
        await change_brawl_id(message, user_id)

#Функция которая изменяет вибраной Brawl Stars ID
async def change_brawl_id(message: Message, user_id):
    await message.answer("Похоже вы указали не правильный Brawl Stars ID.")
    await message.answer("Напиши еще раз свой Brawl Stars ID(без #):")
    @rp.message(F.text)
    async def profile_bs_id(message: Message):
        brawl_id = str(message.text.upper())
        await db.save_brawl_stars_id_1(user_id, brawl_id)
        await pars_profile_photo(message, brawl_id, user_id)

#-------------------------------------------------------------#
#Обработчики кнопок

#Обработчики команды /Brawl_Stars     
@rp.callback_query(F.data == "photo")
async def batton(call: CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    from battons.battons import brawl_stars_name
    user_id = call.from_user.id
    markup = await brawl_stars_name(user_id)
    await call.message.answer("Выберите Brawl Stars ID из доступных вам:", reply_markup = markup)

@rp.callback_query(F.data == "change")
async def batton(call: CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    pass

#Обработчики кнопки add
@rp.callback_query(F.data.contains("add_brawl_id_"))
async def batton(call: CallbackQuery, state: FSMContext):
    await state.set_state(router_for_command_brawl_stars.brawl_id)
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    user_id = call.from_user.id
    nume = int(call.data.split("_")[-1])
    await call.message.answer("Напиши свой Brawl Stars ID(без #):")
    await db.save_user_id(user_id)
    await state.update_data(nume = nume, user_id = user_id)
@rp.message(router_for_command_brawl_stars.brawl_id)
async def profile_bs_id(message: Message, state: FSMContext):
    await state.update_data(brawl_id = message.text.upper())
    data = await state.get_data()
    nume = data["nume"]
    user_id = data["user_id"]
    brawl_name = await pars.pars_profile_name(data["brawl_id"])
    await db.__getattribute__(f"save_brawl_stars_name_{nume}")(brawl_name, user_id)
    await db.__getattribute__(f"save_brawl_stars_id_{nume}")(user_id, data["brawl_id"])
    await pars_profile_photo(message, data["brawl_id"], user_id)
    await state.clear()

@rp.callback_query(F.data.contains("brawl_id_"))
async def batton(call: CallbackQuery):
    await bot.delete_message(call.message.chat.id, call.message.message_id)
    user_id = call.from_user.id
    nume = int(call.data.split("_")[-1])
    brawl_id = str(await getattr(db, f'get_brawl_id_{nume}')(user_id))
    await pars_profile_photo(call.message, brawl_id, user_id)
