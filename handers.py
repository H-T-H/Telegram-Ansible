from telebot import TeleBot
from telebot.types import Message
import ansible_utils


def start_handler(message: Message, bot: TeleBot) -> None:
    bot.send_message(
            str(message.from_user.id),
            "Hello,World!",
        )

def edit_hosts_hander(message: Message, bot: TeleBot) -> None:
    bot.send_message(message.chat.id, "Please send your hosts file contents via text. You can cancel this by /cancel")
    bot.set_state(message.from_user.id, "WAITING_HOSTS", message.chat.id)

def waiting_hosts_hander(message: Message, bot: TeleBot) -> None:
    hosts_text = message.text
    with open("hosts.ini", "w") as f:
        f.write(hosts_text)
    bot.send_message(message.chat.id, "Hosts editing completed")
    bot.delete_state(message.from_user.id, message.chat.id)

def edit_playbook_hander(message: Message, bot: TeleBot) -> None:
    bot.send_message(message.chat.id, "Please send your playbook file contents via text. You can cancel this by /cancel")
    bot.set_state(message.from_user.id, "WAITING_PLAYBOOK", message.chat.id)

def waiting_playbook_hander(message: Message, bot: TeleBot) -> None:
    playbook_text = message.text
    with open("playbook.yaml", "w") as f:
        f.write(playbook_text)
    bot.send_message(message.chat.id, "playbook editing completed")
    bot.delete_state(message.from_user.id, message.chat.id)

def show_hosts_hander(message: Message, bot: TeleBot) -> None:
    try:
        with open("hosts.ini", "r") as f:
            hosts_text = f.read()
        bot.send_message(message.chat.id, f"```\n{hosts_text}\n```", parse_mode="Markdown")
    except FileNotFoundError:
        bot.send_message(message.chat.id, "hosts.ini miss。")

def show_playbook_hander(message: Message, bot: TeleBot) -> None:
    try:
        with open("playbook.yaml", "r") as f:
            playbook_text = f.read()
        bot.send_message(message.chat.id, f"```\n{playbook_text}\n```", parse_mode="Markdown")
    except FileNotFoundError:
        bot.send_message(message.chat.id, "playbook.yaml miss.")

def run_hander(message: Message, bot: TeleBot) -> None:
    try:
        with open("playbook.yaml", "r") as f:
            playbook_text = f.read()
        bot.send_message(message.chat.id, f"```\n{playbook_text}\n```", parse_mode="Markdown")
        bot.send_message(message.chat.id, "Are you sure to run this?\nyes / no")
        bot.set_state(message.from_user.id, "WAITING_YES", message.chat.id)
        
    except:
        bot.send_message(message.chat.id, "Which")

def cancel_hander(message: Message, bot: TeleBot) -> None:
    try:
        bot.delete_state(message.from_user.id, message.chat.id)
        bot.send_message(message.chat.id, "OK")
    except:
        bot.send_message(message.chat.id, "Which")

def waiting_yes_hander(message: Message, bot: TeleBot) -> None:
    if message.text == "yes":

        bot.delete_state(message.from_user.id, message.chat.id)
        sent_message = bot.send_message(message.chat.id, "wait a minute")
        result = ansible_utils.run_ansible_task()

        bot.edit_message_text(result, chat_id=sent_message.chat.id, message_id=sent_message.message_id)

    else:
        bot.delete_state(message.from_user.id, message.chat.id)
        bot.send_message(message.chat.id, "alright")
