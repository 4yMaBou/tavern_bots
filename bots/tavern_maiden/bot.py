def setup(client, settings, config):
    autorole = config.get("autorole") or {}
    role_id = autorole.get("role_id")
    if not role_id:
        raise ValueError("В config.json нужен autorole.role_id")

    @client.event
    async def on_ready():
        print(f"ready as {client.user}")

    @client.event
    async def on_member_join(member):
        role = member.guild.get_role(role_id)
        if role is None:
            print(f"role {role_id} not found in guild {member.guild.id}")
            return
        await member.add_roles(role, reason="autorole on join")