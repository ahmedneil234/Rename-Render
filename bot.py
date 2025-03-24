# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01

import logging
import logging.config
from pyrogram import Client 
from config import API_ID, API_HASH, BOT_TOKEN, FORCE_SUB, PORT
from aiohttp import web
from plugins.web_support import web_server

logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.DEBUG)  # INFO থেকে DEBUG করুন
logging.getLogger("pyrogram").setLevel(logging.ERROR)


class Bot(Client):

    def __init__(self):
        super().__init__(
            name="WebX-Renamer",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
        try:
            await super().start()
            me = await self.get_me()
            self.mention = me.mention
            self.username = me.username 
            self.force_channel = FORCE_SUB
            if FORCE_SUB:
                try:
                    link = await self.export_chat_invite_link(FORCE_SUB)                  
                    self.invitelink = link
                except Exception as e:
                    logging.error(f"Force Sub Channel Error: {e}")  # এই লাইন যোগ করুন
                    self.force_channel = None
            logging.info(f"Bot Started Successfully as {me.first_name}")
        except Exception as e:
            logging.error(f"Error in start: {e}")  # এই লাইন যোগ করুন
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()
        logging.info(f"{me.first_name} ✅✅ BOT started successfully ✅✅")
      

    async def stop(self, *args):
      await super().stop()      
      logging.info("Bot Stopped 🙄")
        
bot = Bot()
bot.run()
