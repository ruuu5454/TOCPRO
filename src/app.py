import os
import sys
import json

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()


machine = TocMachine(
    states=["user",
            "check",
            "dateInfo",
            "monthExpense",
            "monthIncome",
            "monthRatio",
            "monthAll",
            "weekExpense",
            "weekIncome",
            "weekRatio",
            "weekAll",
            "record",
            "action",
            "type",
            "value",
            "description"
            ],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "check",
            "conditions": "is_going_to_check",
        },
        {
            "trigger": "advance",
            "source": "check",
            "dest": "dateInfo",
            "conditions": "is_going_to_dateInfo",
        },
        {
            "trigger": "advance",
            "source": "check",
            "dest": "monthExpense",
            "conditions": "is_going_to_monthExpense",
        },
        {
            "trigger": "advance",
            "source": "check",
            "dest": "weekExpense",
            "conditions": "is_going_to_weekExpense",
        },
        {
            "trigger": "advance",
            "source": "check",
            "dest": "monthIncome",
            "conditions": "is_going_to_monthIncome",
        },
        {
            "trigger": "advance",
            "source": "check",
            "dest": "weekIncome",
            "conditions": "is_going_to_weekIncome",
        },
        {
            "trigger": "advance",
            "source": "check",
            "dest": "monthRatio",
            "conditions": "is_going_to_monthRatio",
        },
        {
            "trigger": "advance",
            "source": "check",
            "dest": "weekRatio",
            "conditions": "is_going_to_weekRatio",
        },
        {
            "trigger": "advance",
            "source": "check",
            "dest": "monthAll",
            "conditions": "is_going_to_monthAll",
        },
        {
            "trigger": "advance",
            "source": "check",
            "dest": "weekAll",
            "conditions": "is_going_to_weekAll",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "record",
            "conditions": "is_going_to_record",
        },
        {
            "trigger": "advance",
            "source": "record",
            "dest": "action",
            "conditions": "is_going_to_action",
        },
        {
            "trigger": "advance",
            "source": "action",
            "dest": "type",
            "conditions": "is_going_to_type",
        },
        {
            "trigger": "advance",
            "source": "type",
            "dest": "value",
            "conditions": "is_going_to_value",
        },
        {
            "trigger": "advance",
            "source": "value",
            "dest": "description",
            "conditions": "is_going_to_description",
        },
        {"trigger": "go_back",
         "source": ["dateInfo",
                    "monthExpense",
                    "monthIncome",
                    "monthRatio",
                    "monthAll",
                    "weekExpense",
                    "weekIncome",
                    "weekRatio",
                    "weekAll",
                    "description"
                    ],
         "dest": "user"
         },
    ],
    initial="user",
    auto_transitions=False,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


def webhook_parser(webhook):
    event = webhook["events"][0]
    reply_token = event["replyToken"]
    return event, reply_token


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    webhook = json.loads(request.data.decode("utf-8"))
    if(len(webhook["events"]) > 0):
        event, reply_token = webhook_parser(webhook)
        response = machine.advance(event)
        # check if message is valid or not
        if response == False:
            if machine.state == 'user':
                send_text_message(reply_token, "So tired")

    return "OK"


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
