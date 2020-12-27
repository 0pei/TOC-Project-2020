import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message

load_dotenv()

machine = TocMachine(
    states=["user", "fsm", "q1", "q2", "q3", "q4", "q5", "q6", "q7", "q8", "q9", "q10", "a1", "a2", "a3", "a4", "a5", "a6",],
    transitions=[
        {"trigger": "advance", "source": "user", "dest": "fsm", "conditions": "is_going_to_fsm",},  
        {"trigger": "advance","source": "user", "dest": "q1","conditions": "is_going_to_q1",},
        {"trigger": "advance","source": "q1", "dest": "q4","conditions": "is_going_to_q4"},              
        {"trigger": "advance","source": "q1", "dest": "q2","conditions": "is_going_to_q2"},        
        {"trigger": "advance","source": "q2", "dest": "q6","conditions": "is_going_to_q6"},        
        {"trigger": "advance","source": "q2", "dest": "q3","conditions": "is_going_to_q3"},  
        {"trigger": "advance","source": "q3", "dest": "q6","conditions": "is_going_to_q6"},        
        {"trigger": "advance","source": "q3", "dest": "q5","conditions": "is_going_to_q5"},
        {"trigger": "advance","source": "q4", "dest": "q5","conditions": "is_going_to_q5"},        
        {"trigger": "advance","source": "q4", "dest": "q7","conditions": "is_going_to_q7"},
        {"trigger": "advance","source": "q5", "dest": "q7","conditions": "is_going_to_q7"},        
        {"trigger": "advance","source": "q5", "dest": "q8","conditions": "is_going_to_q8"},
        {"trigger": "advance","source": "q6", "dest": "q9","conditions": "is_going_to_q9"},        
        {"trigger": "advance","source": "q6", "dest": "q8","conditions": "is_going_to_q8"}, 
        {"trigger": "advance","source": "q7", "dest": "q9","conditions": "is_going_to_q9"},        
        {"trigger": "advance","source": "q7", "dest": "q10","conditions": "is_going_to_q10"}, 
        {"trigger": "advance","source": "q8", "dest": "a1","conditions": "is_going_to_a1"},        
        {"trigger": "advance","source": "q8", "dest": "a2","conditions": "is_going_to_a2"},
        {"trigger": "advance","source": "q9", "dest": "a3","conditions": "is_going_to_a3"},        
        {"trigger": "advance","source": "q9", "dest": "a4","conditions": "is_going_to_a4"},
        {"trigger": "advance","source": "q10", "dest": "a5","conditions": "is_going_to_a5"},        
        {"trigger": "advance","source": "q10", "dest": "a6","conditions": "is_going_to_a6"},
        {"trigger": "go_back","source": ["fsm", "a1", "a2", "a3", "a4", "a5", "a6"], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = "280a4536aafbc55087af240efcf7d22c"
channel_access_token = "NWeBJJ7+eTJ4HQMMj5dEHner0dmBho2IrqXB1EEIP7Zjqf3jJqL+p6Ez208HpfyrXmSLkyj9kzrBAZbWXcY3dM3FtVC5p+G1d9AlKw1/940Fjnj86yUZUHOa3HoVemaPkZ9u2FllvcxIfjUw/adbDgdB04t89/1O/w1cDnyilFU="
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    # app.logger.info("Request body: " + body)

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


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    # app.logger.info(f"Request body: {body}")

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
        if not isinstance(event.message.text, str):
            continue
        # print(f"\nFSM STATE: {machine.state}")
        # print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        if response == False:
            send_text_message(event.reply_token, "")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm_new.png", prog="dot", format="png")
    return send_file("fsm_new.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
