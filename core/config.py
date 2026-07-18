import os 
from dotenv import load_dotenv


class Settings:
    def __init__(self, env_file: str | None=None):
        self._env_file = env_file
        self.reload()

    def reload(self):
        load_dotenv(self._env_file, override=True)

        self.bot_token = os.getenv("BOT_TOKEN")
        self.log_level = os.getenv("LOG_LEVEL", "INFO")
        self.log_file = os.getenv("LOG_FILE")
        self.route_base = os.getenv("ROUTE_BASE")
        self.default_gateway = os.getenv("DEFAULT_GATEWAY")
        
    def validate(self):
        if not self.bot_token:
            raise ValueError("Нет токена")
        