
from dyrogram import devil as app
import asyncio
from asyncio.exceptions import TimeoutError

from pyrogram import Client, filters
from pyrogram.errors import (
    PhoneCodeExpired,
    PhoneCodeInvalid,
    PhoneNumberInvalid,
    SessionPasswordNeeded,
)



@app.on_message(filters.command("genstr") & filters.private)
async def genstr(_, message):
    chat = message.chat
    while True:
        number = await app.ask(
            chat.id, "Sᴇɴᴅ ʏᴏᴜʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ ɪɴ ɪɴᴛᴇʀɴᴀᴛɪᴏɴᴀʟ ғᴏʀᴍᴀᴛ."
        )
        if not number.text:
            continue
        phone = number.text.strip()
        confirm = await app.ask(
            chat.id, f'`Is "{phone}" ᴄᴏʀʀᴇᴄᴛ ?` \n\nSᴇɴᴅ : `y`\nSᴇɴᴅ : `n`'
        )
        if "y" in confirm.text.lower():
            break
    try:
        temp_client = Client(
            ":memory:", api_id=6, api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e"
        )
    except Exception as e:
        await app.send_message(chat.id, f"**Eʀʀᴏʀ :** `{str(e)}`")
        return
    try:
        await temp_client.connect()
    except ConnectionError:
        await temp_client.disconnect()
        await temp_client.connect()
    try:
        code = await temp_client.send_code(phone)
        await asyncio.sleep(2)
    except PhoneNumberInvalid:
        await message.reply_text("Pʜᴏɴᴇ ɴᴜᴍʙᴇʀ ɪs ɪɴᴠᴀʟɪᴅ...")
        return

    try:
        otp = await app.ask(
            chat.id,
            (
                "Aɴ OTP ɪs sᴇɴᴛ ᴛᴏ ʏᴏᴜʀ ᴘʜᴏɴᴇ ɴᴜᴍʙᴇʀ, "
                "Pʟᴇᴀsᴇ ᴇɴᴛᴇʀ OTP ɪɴ `1 2 3 4 5` ғᴏʀᴍᴀᴛ. __(sᴘᴀᴄᴇ ʙᴇᴛᴡᴇᴇɴ ᴇᴀᴄʜ ɴᴜᴍʙᴇʀs!)__"
            ),
            timeout=300,
        )

    except TimeoutError:
        await message.reply_text("Tɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 5 ᴍɪɴ. ᴘʀᴏᴄᴇss ᴄᴀɴᴄᴇʟʟᴇᴅ.")
        return
    otp_code = otp.text
    try:
        await temp_client.sign_in(
            phone, code.phone_code_hash, phone_code=" ".join(str(otp_code))
        )
    except PhoneCodeInvalid:
        await message.reply_text("Iɴᴠᴀʟɪᴅ OTP.")
        return
    except PhoneCodeExpired:
        await message.reply_text("OTP ɪs ᴇxᴘɪʀᴇᴅ.")
        return
    except SessionPasswordNeeded:
        try:
            two_step_code = await app.ask(
                chat.id,
                "Yᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ ʜᴀᴠᴇ ᴛᴡᴏ-sᴛᴇᴘ ᴠᴇʀɪғɪᴄᴀᴛɪᴏɴ.\nPʟᴇᴀsᴇ ᴇɴᴛᴇʀ ʏᴏᴜʀ ᴘᴀssᴡᴏʀᴅ.",
                timeout=300,
            )
        except TimeoutError:
            await message.reply_text("Tɪᴍᴇ ʟɪᴍɪᴛ ʀᴇᴀᴄʜᴇᴅ ᴏғ 5 ᴍɪɴ.")
            return
        new_code = two_step_code.text
        try:
            await temp_client.check_password(new_code)
        except Exception as e:
            await message.reply_text(f"**Eʀʀᴏʀ :** `{str(e)}`")
            return
    except Exception as e:
        await app.send_message(chat.id, f"**Eʀʀᴏʀ :** `{str(e)}`")
        return
    try:
        session_string = await temp_client.export_session_string()
        await temp_client.disconnect()
        await app.send_message(
            chat.id, text=f"**Hᴇʀᴇ Is Yᴏᴜʀ Sᴛʀɪɴɢ Sᴇssɪᴏɴ :**\n```{session_string}```"
        )
    except Exception as e:
        await app.send_message(chat.id, f"**Eʀʀᴏʀ :** `{str(e)}`")
        return




from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from filters import command, other_filters, other_filters2


@Client.on_message(command("start") & other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""🙃 Hɪ {message.from_user.first_name}!
✨ Hᴇʏ, I'ᴀᴍ PɪᴋᴀᴄʜᴜXᴅ Sᴛʀɪɴɢ Gᴇɴᴇʀᴀᴛᴏʀ Bᴏᴛ. 
🥳 I ᴄᴀɴ Gᴇɴᴇʀᴀᴛᴏʀ Sᴛʀɪɴɢ Sᴇssɪᴏɴ ғᴏʀ Yᴏᴜ. 😉
⚜️ Usᴇ ᴛʜᴇsᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ. 👇
🔥 Bᴏᴛ Mᴀᴅᴇ ʙʏ @iTs_Nitric. 🔥
👉 Tʏᴘᴇ /genstr ғᴏʀ Gᴇɴᴇʀᴀᴛᴇ Sᴛʀɪɴɢ Sᴇssɪᴏɴ. 👈""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💚 ʙᴏᴛ ᴏᴡɴᴇʀ", url="https://t.me/iTs_Nitric"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Gʀᴏᴜᴘ", url="https://t.me/PikachuXdSupport"
                    ),
                    InlineKeyboardButton(
                        "Cʜᴀɴɴᴇʟ 🔈", url="https://t.me/PikachuXdUpdates"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "❌ Cʟᴏsᴇ ❌", callback_data="close"
                    )
                ]
            ]
        )
    )




