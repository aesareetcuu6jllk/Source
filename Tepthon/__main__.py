from . import *

import contextlib
import os
import sys
import time
from .core.helper import time_formatter#, bash
from .load_plug import load
from telethon.errors import SessionRevokedError
from .utils import (
    join_dev,
    main_process,
)


jmubot.me.phone = None

if not jmubot.me.bot:
    jmdB.set_key("OWNER_ID", jmubot.me.id)
    jmdB.set_key("NAME", jmubot.full_name)


LOGS.info("جاري تثبيت سورس HELLAS...")


try:
    LOGS.info("- يتم إعـداد الإعدادات .......")
    jmubot.loop.run_until_complete(main_process())
    LOGS.info("تم إعداد إعدادات سورس HELLAS ✅")
except Exception as meo:
    LOGS.error(f"- {meo}")
    sys.exit()

jmubot.loop.create_task(join_dev())

async def load_plugins():
    load(path=["plugins/basic", "plugins/assistant","plugins/account","plugins/fun","plugins/group"])

jmubot.run_in_loop(load_plugins())


LOGS.info(f"⏳ تم استغراق {time_formatter((time.time() - start_time) * 1000)}  HELLAS ميللي ثانية لبدء تشغيل سورس.")

LOGS.info(
    """
    ╔══════════════════════════════════════════╗
    ║       ✅ تم تنصيب وتشغيل سورس HELLAS بنجاح             ║ 
    ║       تابع آخر التحديثات من خلال قناة @SourceHELLAS            ║
    ╚══════════════════════════════════════════╝
    """
)

    
try:
    asst.run()
    LOGS.info(f"تم بنجاح تشغيل البوت المساعد من @SourceHELLAS")
except SessionRevokedError:
    LOGS.info(f"جلسة البوت المساعد [@{asst.me.username}] فشلت لكن سيتم تشغيل سورس الحساب فقط")
    jmubot.run()

