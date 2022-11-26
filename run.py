import os
from main import bot_main


def main():
    TOKEN = os.environ.get("TOKEN")
    bot_main(TOKEN)


if __name__ == '__main__':
    main()
