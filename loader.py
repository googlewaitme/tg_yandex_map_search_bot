#!/usr/bin/env python
# encoding: utf-8
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config

import asyncio

from utils.search_api import Searcher


loop = asyncio.get_event_loop()


bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

searcher = Searcher(
    url=config.YANDEX_URL,
    token=config.YANDEX_TOKEN
)

