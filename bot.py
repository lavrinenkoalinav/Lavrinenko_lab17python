import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from assistant import Assistant

TOKEN = "7885663600:AAF6qT7h4Sje8nMbW8aWHHSYA5-BmzF-xTA"
assistant = Assistant()
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(msg: types.Message):
    await msg.answer("Привіт! Я нотатковий бот. Команди: /add, /list, /search")

@dp.message(Command("help"))
async def cmd_help(msg: types.Message):
    await msg.answer("Команди:\n/add — додати нотатку\n/list — список нотаток\n/search — пошук нотатки")

@dp.message(Command("add"))
async def cmd_add(msg: types.Message):
    await msg.answer("Введіть текст нотатки:")

    @dp.message()
    async def handle_add_note(note_msg: types.Message):
        assistant.add_note(note_msg.text)
        await note_msg.answer("✅ Нотатку збережено.")
        dp.message_handlers.unregister(handle_add_note)

@dp.message(Command("list"))
async def cmd_list(msg: types.Message):
    notes = assistant.list_notes()
    if notes:
        await msg.answer("\n".join(f"{i+1}. {n}" for i, n in enumerate(notes)))
    else:
        await msg.answer("⚠️ Немає нотаток.")

@dp.message(Command("search"))
async def cmd_search(msg: types.Message):
    await msg.answer("Введіть ключове слово для пошуку:")

    @dp.message()
    async def handle_search(note_msg: types.Message):
        results = assistant.search_notes(note_msg.text)
        if results:
            await note_msg.answer("\n".join(results))
        else:
            await note_msg.answer("🔍 Нічого не знайдено.")
        dp.message_handlers.unregister(handle_search)

async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
