from lolka import Interaction, app_commands
from ..context import BotContext

def setup(ctx: BotContext):
    @ctx.tree.command(name="reload", description="Перечитать конфиг")
    async def reload(interaction: Interaction):
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("нет прав", ephemeral=True)
            return
        try:
            ctx.reload_config()
        except Exception as e:      # битый JSON не должен ронять бота
            await interaction.response.send_message(f"ошибка: {e}", ephemeral=True)
            return
        await interaction.response.send_message("конфиг перечитан", ephemeral=True)