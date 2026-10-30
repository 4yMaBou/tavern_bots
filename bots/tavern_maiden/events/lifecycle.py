from ..context import BotContext

def setup(ctx: BotContext):
    client = ctx.client

    @client.event
    async def setup_hook():
        await ctx.tree.sync()

    @client.event
    async def on_ready():
        print(f"ready as {client.application}")