from dataclasses import dataclass
from dotenv import load_dotenv
import os

load_dotenv()

@dataclass
class Config:
    bot_token: str
    admin_chat_id: int

def load_config() -> Config:
    return Config(
        bot_token=os.getenv("BOT_TOKEN"),
        admin_chat_id=int(os.getenv("ADMIN_CHAT_ID")),
    )
