import datetime

from transitions import Machine
from utils import send_text_message


class TocMachine(object):
    def __init__(self, **machine_configs):
        self.machine = Machine(model=self, **machine_configs)

    ''' is going to state '''

    def is_going_to_check(self, event):
        text = event["message"]["text"]
        return text == "check"

    def is_going_to_dateInfo(self, event):
        # text = event["message"]["text"] if "message" in event else event["postback"]["params"]["date"]
        text = event["message"]["text"]
        return text == "dateinfo"

    ''' on enter state '''

    def on_enter_check(self, event):
        # self.db = Database(event["source"]["userId"])
        reply_token = event["replyToken"]
        send_text_message(reply_token, "enter check state")
        # self.go_back()
        # send_check_menu(reply_token)

    def on_enter_dateInfo(self, event):
        # dateStr = event["message"]["text"] if "message" in event else event["postback"]["params"]["date"]
        # dateInfoStr = self.db.getDateInfo(dateStr)
        reply_token = event["replyToken"]
        send_text_message(reply_token, "enter dateinfo state")
        self.go_back()
