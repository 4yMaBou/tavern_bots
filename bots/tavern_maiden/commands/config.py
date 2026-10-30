from lolka import Interaction, Role, app_commands
from ..context import BotContext

def setup(ctx: BotContext):
    group = app_commands.Group(name="settings", description="Настройки бота")

    @group.command(name="autorole", description="Роль, выдаваемая при входе")
    async def autorole(interaction: Interaction, role: Role):
        await ctx.update_config(lambda p: p.setdefault("autorole", {}).update(role_id=role.id))
        await interaction.response.send_message(f"автороль: {role.mention}", ephemeral=True)

    @group.command(name="reactrole_add", description="Привязать эмодзи к роли")
    async def reactrole_add(interaction: Interaction, emoji: str, role: Role):
        await ctx.update_config(lambda p: p["react_role"]["map"].__setitem__(emoji, role.id))
        await interaction.response.send_message(f"{emoji} → {role.mention}", ephemeral=True)

    @group.command(name="reactrole_remove", description="Отвязать эмодзи")
    async def reactrole_remove(interaction: Interaction, emoji: str):
        removed = None
        def mutate(p):
            nonlocal removed
            removed = p["react_role"]["map"].pop(emoji, None)
        await ctx.update_config(mutate)
        msg = f"{emoji} отвязан" if removed else f"{emoji} не найден"
        await interaction.response.send_message(msg, ephemeral=True)

    @group.command(name="reactrole_message", description="Сообщение для ролей по реакциям")
    async def reactrole_message(interaction: Interaction, link: str):
        message_id = int(link.rstrip("/").rsplit("/", 1)[-1])
        await ctx.update_config(lambda p: p["react_role"].update(message_id=message_id))
        await interaction.response.send_message("сообщение обновлено", ephemeral=True)

    @group.command(name="show", description="Текущие настройки")
    async def show(interaction: Interaction):
        p = ctx.config.params
        lines = [f"автороль: <@&{p['autorole']['role_id']}>"]
        lines += [f"{e} → <@&{r}>" for e, r in p["react_role"]["map"].items()]
        await interaction.response.send_message("\n".join(lines), ephemeral=True)

    @group.error
    async def on_error(interaction: Interaction, error):
        await interaction.response.send_message(f"ошибка: {error}", ephemeral=True)

    ctx.tree.add_command(group)