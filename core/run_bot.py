import importlib
import lolka
from lolka.http import Route
from lolka.gateway import DiscordWebSocket
import yarl
from pathlib import Path
from core.config import Settings
from core.intents import IntentsFromConf
from core.app_config import AppConfig

def run_bot(bot_dir_name):
    bot_dir_name = Path(bot_dir_name)
    env_path = Path("bots") / bot_dir_name / ".env"
    config_path = Path("bots") / bot_dir_name / "config.json"
    
    settings = Settings(env_path)
    settings.validate()
            
    Route.BASE = settings.route_base
    DiscordWebSocket.DEFAULT_GATEWAY = yarl.URL(settings.default_gateway)
    
    with open(config_path) as config:
        app_config = AppConfig(config.read())
        app_config.reload()
        intents = IntentsFromConf(app_config.params["intents"])
    
    client = lolka.Client(intents=intents.build_intents())

    bot_module = importlib.import_module(f"bots.{bot_dir_name}.bot")
    bot_module.setup(client, settings, app_config.params)

    try:
        client.run(settings.bot_token)
    except Exception as e:
        print("Oshibka na starte")
        raise e
    