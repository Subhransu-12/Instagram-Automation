from instabot import Bot

# Initialize the bot
bot = Bot()

bot.login(username="_4uemerson_", password="Emerson@12")
followers = bot.get_user_followers("_4uemerson_")

for follower in followers:
    # Get information about each follower
    follower_info = bot.get_user_info(follower)
    print(follower_info)