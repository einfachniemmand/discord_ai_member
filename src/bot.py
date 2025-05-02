import discord
import asyncio
import requests

TOKEN = 'YOUR_BOT_TOKEN' # Add the token from the discord developer forum here

def generate_response(prompt: str, custom_prefix: str, server_id: int):
    full_prompt = custom_prefix + prompt
    endpoint = "https://example.user.workers.dev/" # Your cloudflare domain
    headers = {"Content-Type": "application/json"}
    payload = {"content": full_prompt}
    response = requests.post(endpoint, headers=headers, json=payload)
    response.raise_for_status()
    data = response.json()
    response_text = data["candidates"][0]["content"]["parts"][0]["text"].strip()
    return response_text

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.messages = True

client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    await tree.sync()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if client.user.mentioned_in(message):
        history = [msg async for msg in message.channel.history(limit=20, oldest_first=False)] # Set the maximal amount of messages here
        context = "\n".join([f"{msg.author.name}: {msg.content}" for msg in reversed(history)])
        prompt = f"\n{context}\n{message.author.name}:"
        custom_prefix = "Only concentrate on the last/latest message" # Add your prefix here
        async with message.channel.typing():
            response_text = generate_response(prompt, custom_prefix=custom_prefix, server_id=message.guild.id)
            await asyncio.sleep(1)
            await message.channel.send(response_text)

@tree.command(name="summary", description="Summarize the last 80 messages in this channel")
async def summary_command(interaction: discord.Interaction):
    await interaction.response.defer()
    history = [msg async for msg in interaction.channel.history(limit=80, oldest_first=False)] # Set the maximal amount of messages for /summary here
    context = "\n".join([f"{msg.author.name}: {msg.content}" for msg in history])
    prompt = f"Summarize the following Discord chat into a few sentences:\n\n{context}" # Add your prefix for /summary here
    custom_prefix = ""
    summary = generate_response(prompt, custom_prefix=custom_prefix, server_id=interaction.guild.id)
    await interaction.followup.send(summary[:2000])

client.run(TOKEN)
