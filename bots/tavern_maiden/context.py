from dataclasses import dataclass, field
from lolka import Client, Guild, Object, app_commands
from core.app_config import AppConfig
import asyncio
from typing import Callable


@dataclass
class BotContext:
    client: Client
    settings: object
    config: AppConfig
    tree: app_commands.CommandTree
    _guild: Guild | None = None
    _config_lock: asyncio.Lock = field(default_factory=asyncio.Lock, init=False, repr=False)


    @property
    def guild_id(self) -> int:
        return self.config.params["guild_id"]

    @property #хз зач, это клод навалил
    def guild_obj(self) -> Object:
        return Object(id=self.guild_id)

    async def get_guild(self) -> Guild:
        if self._guild is None:
            self._guild = self.client.get_guild(self.guild_id) \
                          or await self.client.fetch_guild(self.guild_id)
        return self._guild

    def reload_config(self):
        old_intents = self.config.params.get("intents")
        self.config.reload()
        #self._guild = None          # guild_id мог поменяться — сбрасываем кэш  #да не, не мог
        if self.config.params.get("intents") != old_intents:
            print("intents изменились — нужен полный перезапуск бота")

    
    async def update_config(self, mutate: Callable[[dict], None]):
        async with self._config_lock:
            self.config.reload()          # подхватить ручные правки файла, если были
            mutate(self.config.params)
            self.config.save()
            