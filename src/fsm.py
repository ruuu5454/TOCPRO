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
        text = event["message"]["text"]
        return text == "dateInfo"

    def is_going_to_monthExpense(self, event):
        text = event["message"]["text"]
        return text == "monthExpense"

    def is_going_to_monthIncome(self, event):
        text = event["message"]["text"]
        return text == "monthIncome"

    def is_going_to_monthRatio(self, event):
        text = event["message"]["text"]
        return text == "monthRatio"

    def is_going_to_monthAll(self, event):
        text = event["message"]["text"]
        return text == "monthAll"

    def is_going_to_weekExpense(self, event):
        text = event["message"]["text"]
        return text == "weekExpense"

    def is_going_to_weekIncome(self, event):
        text = event["message"]["text"]
        return text == "weekIncome"

    def is_going_to_weekRatio(self, event):
        text = event["message"]["text"]
        return text == "weekRatio"

    def is_going_to_weekAll(self, event):
        text = event["message"]["text"]
        return text == "weekAll"

    def is_going_to_record(self, event):
        text = event["message"]["text"]
        return text == "record"

    def is_going_to_action(self, event):
        text = event["message"]["text"]
        return text == "action"

    def is_going_to_type(self, event):
        text = event["message"]["text"]
        return text == "type"

    def is_going_to_value(self, event):
        text = event["message"]["text"]
        return text == "value"

    def is_going_to_description(self, event):
        text = event["message"]["text"]
        return text == "description"

    ''' on enter state '''

    def on_enter_check(self, event):
        reply_token = event["replyToken"]
        send_text_message(reply_token, "enter check state")

    def on_enter_dateInfo(self, event):
        reply_token = event["replyToken"]
        send_text_message(reply_token, "enter dateInfo state")
        self.go_back()

    def on_enter_monthExpense(self, event):
        reply_token = event["replyToken"]
        send_text_message(reply_token, "enter monthExpense state")
        self.go_back()

    def on_enter_weekExpense(self, event):
        reply_token = event["replyToken"]
        send_text_message(reply_token, "enter weekExpense state")
        self.go_back()

    def on_enter_monthIncome(self, event):
        reply_token = event["replyToken"]
        send_text_message(reply_token, "enter monthIncome state")
        self.go_back()

    def on_enter_weekIncome(self, event):
        reply_token = event["replyToken"]
        send_text_message(reply_token, "enter weekIncome state")
        self.go_back()

    def on_enter_monthRatio(self, event):
        reply_token = event["replyToken"]
        send_text_message(reply_token, "enter monthRatio state")
        self.go_back()

    def on_enter_weekRatio(self, event):
        reply_token = event["replyToken"]
        send_text_message(reply_token, "enter weekRatio state")
        self.go_back()

    def on_enter_monthAll(self, event):
        reply_token = event["replyToken"]
        send_text_message(reply_token, "enter monthAll state")
        self.go_back()

    def on_enter_weekAll(self, event):
        reply_token = event["replyToken"]
        send_text_message(reply_token, "enter weekAll state")
        self.go_back()

    def on_enter_record(self, event):
        reply_token = event["replyToken"]
        send_text_message(reply_token, "enter record state")

    def on_enter_action(self, event):
        reply_token = event["replyToken"]
        send_text_message(reply_token, "enter action state")

    def on_enter_type(self, event):
        reply_token = event["replyToken"]
        send_text_message(reply_token, "enter type state")

    def on_enter_value(self, event):
        reply_token = event["replyToken"]
        send_text_message(reply_token, "enter value state")

    def on_enter_description(self, event):
        reply_token = event["replyToken"]
        send_text_message(reply_token, "enter description state")
        self.go_back()
