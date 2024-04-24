import argparse
import telebot
from telebot import TeleBot
from telebot.types import Message

import ansible_utils
import handers

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("tg_token", help="telegram bot token")
    parser.add_argument("user_id", help="your user id")
    options = parser.parse_args()
    print("Arg parse done.")

    # Init bot
    bot = TeleBot(options.tg_token)
    bot.delete_my_commands(scope=None, language_code=None)
    bot.set_my_commands(
        commands=[
            telebot.types.BotCommand("start", "Start"),
            telebot.types.BotCommand("edit_hosts", "edit hosts file"),
            telebot.types.BotCommand("edit_playbook", "edit playbook file"),
            telebot.types.BotCommand("show_hosts","show hosts file"),
            telebot.types.BotCommand("show_playbook","show playbook file"),
            telebot.types.BotCommand("just_shell","run a shell command for a host group"),
            telebot.types.BotCommand("run","run"),
            telebot.types.BotCommand("cancel","cancel current event"),
        ]
    )

    def is_waiting(message, state):
        return bot.get_state(message.from_user.id) == state
    bot.register_message_handler(handers.start_handler,             commands=["start"],                                 pass_bot=True)
    bot.register_message_handler(handers.cancel_hander,             commands=["cancel"],                                pass_bot=True)

    bot.register_message_handler(handers.waiting_yes_hander,        func=lambda m: is_waiting(m, "WAITING_YES"),        pass_bot=True)
    bot.register_message_handler(handers.waiting_hosts_hander,      func=lambda m: is_waiting(m, "WAITING_HOSTS"),      pass_bot=True)
    bot.register_message_handler(handers.waiting_playbook_hander,   func=lambda m: is_waiting(m, "WAITING_PLAYBOOK"),   pass_bot=True)

    bot.register_message_handler(handers.edit_hosts_hander,         commands=["edit_hosts"],                            pass_bot=True)
    bot.register_message_handler(handers.edit_playbook_hander,      commands=["edit_playbook"],                         pass_bot=True)
    bot.register_message_handler(handers.show_hosts_hander,         commands=["show_hosts"],                            pass_bot=True)
    bot.register_message_handler(handers.show_playbook_hander,      commands=["show_playbook"],                         pass_bot=True)
    bot.register_message_handler(handers.run_hander,                commands=["run"],                                   pass_bot=True)

    print("Bot init done.")

    bot.polling(none_stop=True)
if __name__ == '__main__':
    main()