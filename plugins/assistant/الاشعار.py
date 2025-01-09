import re
from telethon import Button
from .. import callback, HNDLR

STRINGS = {
    1: """🎇 **مرحبًا بك في سورس HELLAS!** 
يبدو أنك قد اخترت الطريق الصحيح باستخدام السورس 😎

❃ إليك بعض التعليمات الأساسية للتعرف على سورس   .""",
    
    2: """🎉 **ما هو السورس ؟**
🧿 سورس HELLAS هو بوت يدمج أوامر مخصصه في حسابك الشخصي من خلال كود السيشن.  

تم تطويره لإكمال العديد من المهام في حسابات تيليجرام الشخصية، مثل إدارة المجموعات، الرد التلقائي على الرسائل، وتنفيذ أوامر محددة.  
**سورس HELLAS هو الأفضل من حيث الخصوصية**، فلا يمكن حتى للمطور الوصول إلى حسابك، مما يضمن أمانك التام.

📢 تابع قناة السورس  **@SourceHELLAS**""",
    
❃ شكرًا لك على قراءة المعلومات حتى النهاية! 🤍""",
}

@callback(re.compile("initft_(\\d+)"))
async def init_depl(e):
    CURRENT = int(e.data_match.group(1))
    if CURRENT == 5:
        return await e.edit(
            STRINGS[5],
            buttons=Button.inline("<< رجوع", "initbk_4"),
            link_preview=False,
        )

    await e.edit(
        STRINGS[CURRENT],
        buttons=[
            Button.inline("<<", f"initbk_{str(CURRENT - 1)}"),
            Button.inline(">>", f"initft_{str(CURRENT + 1)}"),
        ],
        link_preview=False,
    )

@callback(re.compile("initbk_(\\d+)"))
async def ineiq(e):
    CURRENT = int(e.data_match.group(1))
    if CURRENT == 1:
        return await e.edit(
            STRINGS[1],
            buttons=Button.inline("بدأ مجددًا", "initft_2"),
            link_preview=False,
        )

    await e.edit(
        STRINGS[CURRENT],
        buttons=[
            Button.inline("<<", f"initbk_{str(CURRENT - 1)}"),
            Button.inline(">>", f"initft_{str(CURRENT + 1)}"),
        ],
        link_preview=False,
    )
