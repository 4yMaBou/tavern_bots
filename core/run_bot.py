import importlib
import lolka
from lolka.http import Route
from lolka.gateway import DiscordWebSocket
import yarl
from pathlib import Path
from core.config import Settings
from core.intents import IntentsFromConf
from core.app_config import AppConfig


def read_config(bot_name):
    bot_dir_path = Path(bot_name)
    env_path = Path("bots") / bot_dir_path / ".env"
    config_path = Path("bots") / bot_dir_path / "config.json"
    settings = Settings(env_path)
    settings.validate()
    settings.reload()
    app_config = AppConfig(config_path)
    app_config.reload()
    intents = IntentsFromConf(app_config.params["intents"])
    return app_config, intents, settings


def run_bot(bot_name):
    app_config, intents, settings = read_config(bot_name)
            
    Route.BASE = settings.route_base
    DiscordWebSocket.DEFAULT_GATEWAY = yarl.URL(settings.default_gateway)
    
    client = lolka.Client(intents=intents.build_intents(), 
                        chunk_guilds_at_startup=False) #убрал подгрузку всех участников гилды при поднятии бота, туду в конфиг
    
    bot_module = importlib.import_module(f"bots.{bot_name}.bot")
    bot_module.setup(client, settings, app_config)

    try:
        client.run(settings.bot_token)
    except Exception as e:
        print("Oshibka na starte")
        raise e

