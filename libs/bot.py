# Project Pi Zero Telegram Bot

from telethon import TelegramClient, events
import logging


# Telegram Bot
class TelegramBot:
    # Bot init
    def __init__(self, id, hash, token, session_path, log_path):
        # Logging configuration
        logging.basicConfig(
            format="[%(asctime)s - %(name)s] (%(levelname)s) %(message)s",
            level=logging.INFO,
            filename=log_path   
        )
        # Create log
        self.log = logging.getLogger("bot.app")
        
        # Create new client
        self.client = TelegramClient(session_path, id, hash).start(bot_token=token)
        self.client.parse_mode = "html"


    # Bot core
    def __core(self):
        # Start handler
        @self.client.on(events.NewMessage(pattern="/start"))
        async def start(event: events.NewMessage.Event):
            await event.respond(
                (
                    "<b>Chào mừng đến với Phatcraft Server</b>\n\n"
                    "Tôi là Alice, một bot cung cấp dịch vụ cho Phatcraft Server"
                )
            )

    # Start bot
    def start(self):
        # Register core
        self.__core()

        # Start bot
        self.log.info("App is running ...")
        self.client.run_until_disconnected()