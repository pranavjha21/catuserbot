import time
from platform import python_version
import os
import requests

from telethon import version

from . import StartTime, catversion, get_readable_time, hmention, mention, reply_id

# backup

ALIVE_NAME = Config.ALIVE_NAME
PINEAPPLE_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.CUSTOM_ALIVE_TEXT or "✧✧ PINEAPPLE IS RUNNING SUCCESSFULLY ✧✧"
EMOJI = Config.CUSTOM_ALIVE_EMOJI or "➥"
DEFAULT_USER = str(ALIVE_NAME) if ALIVE_NAME else "PineApple"
on = await bot.send_file(yes.chat_id, file=file1)

global ghanti
ghanti = bot.uid
edit_time = 9
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/a0f435a5975c30466e038.jpg"
file2 = "https://telegra.ph/file/f8c3fefef25b1c99ce1d9.jpg"
file3 = "https://telegra.ph/file/ca1df6456be952d0d5f23.jpg"
file4 = "https://telegra.ph/file/c98058f2c192e8ce8c5b6.jpg"
file5 = "https://telegra.ph/file/c866dda4baeacb33752c9.jpg"
file6 = "https://telegra.ph/file/ca71d325120480ca8871f.jpg"
file7 = "https://telegra.ph/file/886a2606a353f59e5a30c.jpg"
file8 = "https://telegra.ph/file/decf1583b93e275041621.jpg"
""" =======================CONSTANTS====================== """

PINEAPPLE_IMG
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if PINEAPPLE_IMG:
        cat_caption = f"<b>{CUSTOM_ALIVE_TEXT}</b>\n\n"
        cat_caption += f"<b>{EMOJI} Boss : {DEFAULT_USER}</b>\n"
        cat_caption += f"<b>{EMOJI} Uptime :</b> <code>{uptime}</code>\n"
        cat_caption += (
            f"<b>{EMOJI} Python Version :</b> <code>{python_version()}</code>\n"
        )
        cat_caption += (
            f"<b>{EMOJI} Telethon version :</b> <code>{version.__version__}</code>\n"
        )
        cat_caption += (
            f"<b>{EMOJI} PineApple Version :</b> <code>{catversion}</code>\n"
        )
        cat_caption += f"<b>{EMOJI} Database :</b> <code>{check_sgnirts}</code>\n\n"
        cat_caption += "    <a href = https://github.com/madboy482/PineApple><b>PineApple</b></a> | <a href = https://telegram.me/PineApple_UB><b>Updates</b></a> | <a href = https://telegram.me/PineApple_UB_OnTopic><b>Support</b></a> | <a href = https://telegram.me/PineApple_UB_Spam><b>Spam</b></a>"
        await alive.client.send_file(
            alive.chat_id,
            PINEAPPLE_IMG,
            caption=cat_caption,
            parse_mode="html",
            reply_to=reply_to_id,
            link_preview=False,
            allow_cache=True,
        )
        await alive.delete()
    else:
        await reply(
            alive,
            f"<b>{CUSTOM_ALIVE_TEXT}</b>\n\n"
            f"<b>{EMOJI} Boss : {DEFAULT_USER}</b>\n"
            f"<b>{EMOJI} Uptime :</b> <code>{uptime}</code>\n"
            f"<b>{EMOJI} Python Version :</b> <code>{python_version()}</code>\n"
            f"<b>{EMOJI} Telethon version :</b> <code>{version.__version__}</code>\n"
            f"<b>{EMOJI} PineApple Version :</b> <code>{catversion}</code>\n"
            f"<b>{EMOJI} Database :</b> <code>{check_sgnirts}</code>\n\n"
            "    <a href = https://github.com/madboy482/PineApple><b>PineApple</b></a> | <a href = https://telegram.me/PineApple_UB><b>Updates</b></a> | <a href = https://telegram.me/PineApple_UB_OnTopic><b>Support</b></a> | <a href = https://telegram.me/PineApple_UB_Spam><b>Spam</b></a>",
            parse_mode="html",
        )
            on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)
    
            await asyncio.sleep(edit_time)
            ok = await bot.edit_message(yes.chat_id, on, file=file1) 

            await asyncio.sleep(edit_time)
            ok2 = await bot.edit_message(yes.chat_id, ok, file=file2)

            await asyncio.sleep(edit_time)
            ok3 = await bot.edit_message(yes.chat_id, ok2, file=file3)
    
            await asyncio.sleep(edit_time)
            ok4 = await bot.edit_message(yes.chat_id, ok3, file=file4)
    
            await asyncio.sleep(edit_time)
            ok5 = await bot.edit_message(yes.chat_id, ok4, file=file5)
    
            await asyncio.sleep(edit_time)
            ok6 = await bot.edit_message(yes.chat_id, ok5, file=file6)
    
            await asyncio.sleep(edit_time)
            ok7 = await bot.edit_message(yes.chat_id, ok6, file=file7)

            await asyncio.sleep(edit_time)
            ok8 = await bot.edit_message(yes.chat_id, ok7, file=file8)
    
            await asyncio.sleep(edit_time)
            ok9 = await bot.edit_message(yes.chat_id, ok8, file=file4)
    
            await asyncio.sleep(edit_time)
            ok10 = await bot.edit_message(yes.chat_id, ok9, file=file1)
    
            await asyncio.sleep(edit_time)
            ok11 = await bot.edit_message(yes.chat_id, ok10, file=file5)
            
            
@bot.on(admin_cmd(outgoing=True, pattern="ialive$"))
@bot.on(sudo_cmd(pattern="ialive$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    tgbotusername = Config.TG_BOT_USER_NAME_BF_HER
    reply_to_id = await reply_id(alive)
    cat_caption = f"**PineApple is Up and Running Successfully.**\n"
    cat_caption += f"**  -Boss :** {DEFAULT_USER}\n"
    cat_caption += f"**  -Python Version :** `{python_version()}\n`"
    cat_caption += f"**  -Telethon version :** `{version.__version__}\n`"
    cat_caption += f"**  -PineApple Version :** `{catversion}`\n"
    results = await bot.inline_query(tgbotusername, cat_caption)  # pylint:disable=E0602
    await results[0].click(alive.chat_id, reply_to=reply_to_id, hide_via=True)
    await alive.delete()


# UniBorg Telegram UseRBot
# Copyright (C) 2020 @UniBorg
# This code is licensed under
# the "you can't use this for anything - public or private,
# unless you know the two prime factors to the number below" license
# 543935563961418342898620676239017231876605452284544942043082635399903451854594062955
# വിവരണം അടിച്ചുമാറ്റിക്കൊണ്ട് പോകുന്നവർ
# ക്രെഡിറ്റ് വെച്ചാൽ സന്തോഷമേ ഉള്ളു..!
# uniborg


def check_data_base_heal_th():
    # https://stackoverflow.com/a/41961968
    is_database_working = False
    output = "No Database is set"
    if not Config.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        # to check database we will execute raw query
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "Functioning"
        is_database_working = True
    return is_database_working, output


CMD_HELP.update(
    {
        "alive": "__**PLUGIN NAME :** Alive__\
      \n\n📌** CMD ➥** `.alive`\
      \n**USAGE   ➥  **To see wether your bot is working or not.\
      \n\n📌** CMD ➥** `.ialive`\
      \n**USAGE   ➥  **__Status of bot will be showed by inline mode with button__."
    }
)
