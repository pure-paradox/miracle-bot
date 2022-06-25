from aiohttp import web
import asyncio
import discord 
from discord.ext import commands
import os
        
class Server(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def webserver(self):
        async def handler(request):
            return web.Response(text="Hello, world")

        app = web.Application()
        app.router.add_get('/', handler)
        runner = web.AppRunner(app)
        await runner.setup()
        self.site = web.TCPSite(runner, 'localhost', os.environ.get("PORT"))
        await self.bot.wait_until_ready()
        await self.site.start()

    def __unload(self):
        asyncio.ensure_future(self.site.stop())

def setup(bot):
    server = Server(bot)
    bot.add_cog(server)
    bot.loop.create_task(server.webserver())