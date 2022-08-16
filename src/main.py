import os

from dotenv import load_dotenv

from bot import bot


def main(bot):
    bot.run(os.getenv("TOKEN"))


if __name__ == "__main__":
    load_dotenv()
    main(bot)
