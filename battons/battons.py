from aiogram.types import Message, InlineKeyboardMarkup, CallbackQuery, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from Commands.user_cmd import send_profile_photo
from aiogram import types, Router, F, Bot
from dotenv import load_dotenv
from database import bd as db
import os


rp = Router()
load_dotenv()

bot = Bot(token = os.getenv("TOKEN_API"))

#Набор кнопок для команды /Brawl_Stars
async def communication() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text = "Фото профиля", callback_data = "photo"))
    builder.row(InlineKeyboardButton(text = "Изменить Brawl Stars id", callback_data = "change"))
    return builder.as_markup()


async def photo(user_id) -> InlineKeyboardMarkup:
    profile_id_1 = str(await db.get_brawl_id_1(user_id))
    profile_id_2 = str(await db.get_brawl_id_2(user_id))
    profile_id_3 = str(await db.get_brawl_id_3(user_id))

    builder = InlineKeyboardBuilder()
    if profile_id_1 == "False" or profile_id_1 == "None":
        profile_id_1 = "+"
        builder.row(InlineKeyboardButton(text = profile_id_1, callback_data = "add_brawl_id_1"))
    else:
        builder.row(InlineKeyboardButton(text = profile_id_1, callback_data = "brawl_id_1"))
    if profile_id_2 == "False" or profile_id_2 == "None":
        profile_id_2 = "+"
        builder.row(InlineKeyboardButton(text = profile_id_2, callback_data = "add_brawl_id_2"))
    else:
        builder.row(InlineKeyboardButton(text = profile_id_2, callback_data = "brawl_id_2"))
    if profile_id_3 == "False" or profile_id_3 == "None":
        profile_id_3 = "+"
        builder.row(InlineKeyboardButton(text = profile_id_3, callback_data = "add_brawl_id_3"))
    else:
        builder.row(InlineKeyboardButton(text = profile_id_3, callback_data = "brawl_id_3"))

    return builder.as_markup()

async def brawl_stars_name(user_id) -> InlineKeyboardMarkup:
    profile_name_1 = str(await db.get_brawl_name_1(user_id))
    profile_name_2 = str(await db.get_brawl_name_2(user_id))
    profile_name_3 = str(await db.get_brawl_name_3(user_id))

    builder = InlineKeyboardBuilder()
    if profile_name_1 == "False" or profile_name_1 == "None":
        profile_name_1 = "+"
        builder.row(InlineKeyboardButton(text = profile_name_1, callback_data = "add_brawl_id_1"))
    else:
        builder.row(InlineKeyboardButton(text = profile_name_1, callback_data = "brawl_id_1"))
    if profile_name_2 == "False" or profile_name_2 == "None":
        profile_name_2 = "+"
        builder.row(InlineKeyboardButton(text = profile_name_2, callback_data = "add_brawl_id_2"))
    else:
        builder.row(InlineKeyboardButton(text = profile_name_2, callback_data = "brawl_id_2"))
    if profile_name_3 == "False" or profile_name_3 == "None":
        profile_name_3 = "+"
        builder.row(InlineKeyboardButton(text = profile_name_3, callback_data = "add_brawl_id_3"))
    else:
        builder.row(InlineKeyboardButton(text = profile_name_3, callback_data = "brawl_id_3"))

    return builder.as_markup()


