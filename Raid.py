import discord
from discord.ext import commands
import os
import requests

def main_menu():
    while True:
        print("""\
______          _             __   __          _     _ 
| ___ \        | |            \ \ / /         (_)   | |
| |_/ / __ ___ | |_ ___  _ __  \ V / _ __ __ _ _  __| |
|  __/ '__/ _ \| __/ _ \| '_ \ /   \| '__/ _` | |/ _` |
| |  | | | (_) | || (_) | | | / /^\ \ | | (_| | | (_| |
\_|  |_|  \___/ \__\___/|_| |_\/   \/_|  \__,_|_|\__,_|

                  made by exctasy
""")

        print("\nProtonXraid menu:")
        print("1. Raid with Discord bot")
        print("2. Spam Webhook")
        print("3. Delete Webhook")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
            
        if choice == '1':
            print("This is currently broken and being worked on.")
            #bot_raid()
        elif choice == '2':
            spam_webhook()
        elif choice == '3':
            del_webhook()
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def bot_raid():
    # Prompt for the bot token
    token = input("Please enter your bot token: ").strip()

    # Create the bot instance with necessary intents
    intents = discord.Intents.default()
    intents.guilds = True  # Make sure the bot can access guilds
    intents.messages = True  # To handle messages if needed
    intents.message_content = True  # Required for bots to read messages content in interactions
    bot = commands.Bot(command_prefix='!', intents=intents)

    # Define the bot command for deleting channels
    @bot.command()
    async def delchans(ctx):
        try:
            if not ctx.author.guild_permissions.administrator:
                await ctx.send("You do not have permission to delete channels!")
                return

            for c in ctx.guild.channels:  # Iterating through each guild channel
                if isinstance(c, discord.TextChannel) or isinstance(c, discord.VoiceChannel):  # Check if it's a valid channel type
                    await c.delete()
            await ctx.send("All channels have been deleted.")
        except Exception as e:
            await ctx.send(f"Failed to delete channels: {e}")

    # Run the bot
    try:
        bot.run(token)
    except Exception as e:
        print(f"Failed to start the bot: {e}")

def del_webhook():
    # Ask for webhook url
    url = input("Please enter your webhook url: ").strip()

    # Confirmation for deletion
    confirmation = input(f"Are you sure you want to delete this webhook {url}? (yes/no): ").strip().lower()

    if confirmation == 'yes':
     # Delete Webhook from input
     hook_del = requests.delete(url)
     if hook_del.status_code == 204:
        print("Webhook Successfully deleted!")
     else:
        print(f"Failed to deleted webhook. Status Code: {hook_del.status_code}")
    
    if confirmation == 'no':
        print("Successfully canceled webhook deletion!")

def spam_webhook():
    # Ask for webhook url
    url = input("Please enter your webhook url: ").strip()
    # Ask for spam text
    text = input("Please enter what you would like to spam: ").strip()
    # Times to spam
    spam_ammount = input("Please enter how many times you want the webhook spammed: ").strip()

    # Check if number
    if not spam_ammount.isdigit():
        print("This value is not a number. Please enter a number")
        return
    
    # Convert the input to an int
    spam_ammount = int(spam_ammount)

    # Confirmation for spam
    confirmspam = input(f"Are you sure you want to spam with webhook {url}? (yes/no): ").strip().lower()

    if confirmspam == 'yes':
        for i in range(spam_ammount):
            # Spam webhook
            payload = {"content": f"{text}"}
            
            spam_payload = requests.post(url, json=payload)
            if spam_payload.status_code == 204:
                print("Spammed webhook successfully!")
            else: 
                print(f"Failed to spam webhook. Status Code: {spam_payload.status_code}")


# Run the menu
if __name__ == "__main__":
    main_menu()
