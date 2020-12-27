from transitions.extensions import GraphMachine
from transitions import Machine
from utils import *
# from utils import send_text_message, send_button_message, send_location_message, send_image_url


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):

        self.machine = GraphMachine(model=self, **machine_configs)
    
    def is_going_to_fsm(self,event):
        text = event.message.text
        return text.lower() == "fsm"

    def on_enter_fsm(self,event):   
        send_image_url(event.reply_token, "https://i.imgur.com/49sGo6f.png")
        self.go_back()

    def is_going_to_q1(self, event):
        text = event.message.text
        return text.lower() == "start"

    def on_enter_q1(self, event):
        buttons_template = TemplateSendMessage(
        alt_text = 'buttons template',
        template = ButtonsTemplate(
            title = 'Q1',
            text = '今天天氣如何?',
            actions=[                              
                MessageTemplateAction(
                    label='偏熱',
                    text='偏熱',
                ),
                MessageTemplateAction(
                    label='偏冷',
                    text='偏冷',
                ),
            ]
        )
        )
        send_button_message(event.reply_token,buttons_template)

    def is_going_to_q2(self, event):
        text = event.message.text
        return text.lower() == "偏冷"
    
    def on_enter_q2(self, event):
        buttons_template = TemplateSendMessage(
        alt_text = 'buttons template',
        template = ButtonsTemplate(
            title = 'Q2',
            text = '現在心情好嗎?',
            actions=[                              
                MessageTemplateAction(
                    label='還不錯',
                    text='還不錯',
                ),
                MessageTemplateAction(
                    label='不好',
                    text='不好',
                ),
            ]
        )
        )
        send_button_message(event.reply_token,buttons_template)

    def is_going_to_q3(self, event):
        text = event.message.text
        return text.lower() == "不好"
    
    def on_enter_q3(self, event):
        buttons_template = TemplateSendMessage(
        alt_text = 'buttons template',
        template = ButtonsTemplate(
            title = 'Q3',
            text = '看到吉娃娃',
            actions=[                              
                MessageTemplateAction(
                    label='盆栽要剪，小吉要扁',
                    text='盆栽要剪，小吉要扁',
                ),
                MessageTemplateAction(
                    label='摸摸可愛小吉><',
                    text='摸摸可愛小吉><',
                ),
            ]
        )
        )
        send_button_message(event.reply_token,buttons_template)

    def is_going_to_q4(self, event):
        text = event.message.text
        return text.lower() == "偏熱"

    def on_enter_q4(self, event):
        buttons_template = TemplateSendMessage(
        alt_text = 'buttons template',
        template = ButtonsTemplate(
            title = 'Q4',
            text = '馬老師',
            actions=[                              
                MessageTemplateAction(
                    label='我大意了阿，沒有閃',
                    text='我大意了阿，沒有閃',
                ),
                MessageTemplateAction(
                    label='年輕人不講武德',
                    text='年輕人不講武德',
                ),
            ]
        )
        )
        send_button_message(event.reply_token,buttons_template)

    def is_going_to_q5(self, event):
        text = event.message.text
        return text.lower() == "摸摸可愛小吉><" or text.lower() == "我大意了阿，沒有閃"

    def on_enter_q5(self, event):
        buttons_template = TemplateSendMessage(
        alt_text = 'buttons template',
        template = ButtonsTemplate(
            title = 'Q5',
            text = '雪莉?',
            actions=[                              
                MessageTemplateAction(
                    label='哇！珍妮佛羅培茲！',
                    text='哇！珍妮佛羅培茲！',
                ),
                MessageTemplateAction(
                    label='妳剛攻擊我的村莊？',
                    text='妳剛攻擊我的村莊？',
                ),
            ]
        )
        )
        send_button_message(event.reply_token,buttons_template)

    def is_going_to_q6(self, event):
        text = event.message.text
        return text.lower() == "盆栽要剪，小吉要扁" or text.lower() == "還不錯"

    def on_enter_q6(self, event):
        buttons_template = TemplateSendMessage(
        alt_text = 'buttons template',
        template = ButtonsTemplate(
            title = 'Q6',
            text = '枯藤老樹昏鴉，小橋流水人家，',
            actions=[                              
                MessageTemplateAction(
                    label='古道西風瘦馬。',
                    text='古道西風瘦馬。',
                ),
                MessageTemplateAction(
                    label='古道梅子綠茶。',
                    text='古道梅子綠茶。',
                ),
            ]
        )
        )
        send_button_message(event.reply_token,buttons_template)

    def is_going_to_q7(self, event):
        text = event.message.text
        return text.lower() == "年輕人不講武德" or text.lower() == "哇！珍妮佛羅培茲！"

    def on_enter_q7(self, event):
        buttons_template = TemplateSendMessage(
        alt_text = 'buttons template',
        template = ButtonsTemplate(
            title = 'Q7',
            text = '殘酷二選一',
            actions=[                              
                MessageTemplateAction(
                    label='香菜',
                    text='香菜',
                ),
                MessageTemplateAction(
                    label='芋頭',
                    text='芋頭',
                ),
            ]
        )
        )
        send_button_message(event.reply_token,buttons_template)

    def is_going_to_q8(self, event):
        text = event.message.text
        return text.lower() == "妳剛攻擊我的村莊？" or text.lower() == "古道梅子綠茶。"

    def on_enter_q8(self, event):
        buttons_template = TemplateSendMessage(
        alt_text = 'buttons template',
        template = ButtonsTemplate(
            title = 'Q8',
            text = '媽媽叫你買5顆橘子，如果看到蘋果就買1顆',
            actions=[                              
                MessageTemplateAction(
                    label='買1顆橘子',
                    text='買1顆橘子',
                ),
                MessageTemplateAction(
                    label='買5顆橘子+1顆蘋果',
                    text='買5顆橘子+1顆蘋果',
                ),
            ]
        )
        )
        send_button_message(event.reply_token,buttons_template)

    def is_going_to_q9(self, event):
        text = event.message.text
        return text.lower() == "古道西風瘦馬。" or text.lower() == "香菜"

    def on_enter_q9(self, event):
        buttons_template = TemplateSendMessage(
        alt_text = 'buttons template',
        template = ButtonsTemplate(
            title = 'Q9',
            text = '世界上可分為10種人，你是',
            actions=[                              
                MessageTemplateAction(
                    label='懂二進位的人',
                    text='懂二進位的人',
                ),
                MessageTemplateAction(
                    label='不懂二進位的人',
                    text='不懂二進位的人',
                ),
            ]
        )
        )
        send_button_message(event.reply_token,buttons_template)

    def is_going_to_q10(self, event):
        text = event.message.text
        return text.lower() == "芋頭"

    def on_enter_q10(self, event):
        buttons_template = TemplateSendMessage(
        alt_text = 'buttons template',
        template = ButtonsTemplate(
            title = 'Q10',
            text = 'ouo',
            actions=[                              
                MessageTemplateAction(
                    label='A',
                    text='A',
                ),
                MessageTemplateAction(
                    label='peko',
                    text='peko',
                ),
            ]
        )
        )
        send_button_message(event.reply_token,buttons_template)

    def is_going_to_a1(self, event):
        text = event.message.text
        return text.lower() == "買1顆橘子"

    def on_enter_a1(self, event):
        reply_token = event.reply_token
        title = "杯子社 CROOK TEA SHOP 東安店"
        address = "701台南市東區東安路101號"
        latitude = "22.993081"
        longitude = "120.226439"
        send_location_message(reply_token, title, address, latitude, longitude)
        self.go_back()

    def is_going_to_a2(self, event):
        text = event.message.text
        return text.lower() == "買5顆橘子+1顆蘋果"

    def on_enter_a2(self, event):
        print("A2222")
        reply_token = event.reply_token
        title = "Silver Coin 銀兩"
        address = "700台南市北區北門路一段123巷21號"
        latitude = "22.994849"
        longitude = "120.210859"
        send_location_message(reply_token, title, address, latitude, longitude)
        self.go_back()

    def is_going_to_a3(self, event):
        text = event.message.text
        return text.lower() == "懂二進位的人"

    def on_enter_a3(self, event):
        reply_token = event.reply_token
        title = "海鷗茶館"
        address = "700台南市中西區青年路96號"
        latitude = "22.991863"
        longitude = "120.208398"
        send_location_message(reply_token, title, address, latitude, longitude)
        self.go_back()

    def is_going_to_a4(self, event):
        text = event.message.text
        return text.lower() == "不懂二進位的人"

    def on_enter_a4(self, event):
        reply_token = event.reply_token
        title = "八里亭茶飲"
        address = "701台南市東區青年路265號"
        latitude = "22.991578"
        longitude = "120.212974"
        send_location_message(reply_token, title, address, latitude, longitude)
        self.go_back()

    def is_going_to_a5(self, event):
        text = event.message.text
        return text.lower() == "a"

    def on_enter_a5(self, event):
        reply_token = event.reply_token
        title = "初牧乳飲製造所（台南友愛店）"
        address = "700台南市中西區友愛街249號"
        latitude = "22.992030"
        longitude = "120.196646"
        send_location_message(reply_token, title, address, latitude, longitude)
        self.go_back()

    def is_going_to_a6(self, event):
        text = event.message.text
        return text.lower() == "peko"

    def on_enter_a6(self, event):
        reply_token = event.reply_token
        title = "注春國際人文茶飲 台南永華店"
        address = "70253台南市南區永華路一段233巷1號"
        latitude = "22.988123"
        longitude = "120.191141"
        send_location_message(reply_token, title, address, latitude, longitude)
        self.go_back()