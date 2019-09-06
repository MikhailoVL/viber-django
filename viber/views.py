from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from viberbot.api.viber_requests import ViberConversationStartedRequest, ViberMessageRequest, ViberSubscribedRequest, \
    ViberUnsubscribedRequest
from viberbot.api.messages import TextMessage, KeyboardMessage, RichMediaMessage
from viberbot import Api
from django.conf import settings

from .viber_config import bot_configuration
from viber.models import ViberUser, FAQ
from viber.utils import Keyboard, Button

viber = Api(bot_configuration)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        viber_request = viber.parse_request(request.body)
        print(viber_request)
        print("1")
        if isinstance(viber_request, ViberConversationStartedRequest):
            #print(viber_request.user.id)
            v_user, created = ViberUser.objects.get_or_create(
                viber_id=viber_request.user.id,
                defaults=
                {
                    "name": viber_request.user.name,
                    "country": viber_request.user.country,
                    "language": viber_request.user.language,
                    "viber_api_version": viber_request.user.api_version,
                }
            )
            if created:
                welcome_message = {
                    "sender": {
                        "name": " Чебуратор",
                        "avatar": "https://i.ytimg.com/vi/zpqghz36wfg/maxresdefault.jpg"
                    },
                    "tracking_data": "tracking data",
                    "type": "text",
                    "text": "Welcome to our bot!",
                    "keyboard": {
                        "Type": "keyboard",

                        "Buttons": [
                            {
                                "ActionType": "reply",
                                "ActionBody": "reply to me",
                                "Text": "Подписаться",
                                "TextSize": "regular",
                                "BgColor": "#780000",
                            }
                        ]
                    }
                }
                return JsonResponse(welcome_message)
            viber.send_messages(v_user.viber_id, [TextMessage(text="Привет снова")])

        elif isinstance(viber_request, ViberMessageRequest):
            viber_user, created = ViberUser.objects.get_or_create(
                viber_id=viber_request.sender.id,
                defaults={
                    "name": viber_request.sender.name,
                    "country": viber_request.sender.country,
                    "language": viber_request.sender.language,
                    "viber_api_version": viber_request.sender.api_version,
                }
            )
            viber.send_messages(viber_user.viber_id, [TextMessage(text="I listen you", min_api_version=1)])
            faq = FAQ.objects.all()
            if viber_request.message.text.startswith("faq"):
                idd = viber_request.message.text.replace("faq", "")
                fa = faq.get(id=int(idd))
                print(fa.answer)
                print(viber_request.message.text)
            keyb_faq = Keyboard()
            for faq_line in faq:
                action_body = f"faq{faq_line.id}"
                but = Button(text=faq_line.question, action_type="reply", action_body=action_body, col=6, row=1)
                keyb_faq.add_button(but)
            keyb_faq = keyb_faq.to_dict()

            viber.send_messages(
                viber_user.viber_id,
                [KeyboardMessage(keyboard=keyb_faq, min_api_version=6)],
            )



        elif isinstance(viber_request, ViberSubscribedRequest):
            user_id = viber_request.user.id
            viber_user, created = ViberUser.objects.update_or_create(
                viber_id=user_id,
                defaults={
                    "is_active": True
                }
            )
            if viber_user.is_blocked:
                viber.send_messages(user_id, [TextMessage(text="Fuck off")])
            if hasattr(viber_user, 'user') and not hasattr(viber_user.user, 'phone_nomber'):
                key_number = Keyboard()
                but_num = Button(text="give num", action_type="share-phone", action_body="give me you phone number",
                                 col=6, row=1)
                key_number.add_button(but_num)
                key_number = key_number.to_dict()  # !!!!

                viber.send_messages(
                    user_id,
                    [KeyboardMessage(keyboard=key_number, min_api_version=3)],
                )
        elif isinstance(viber_request, ViberUnsubscribedRequest):
            v_user = ViberUser.objects.update_or_create(
                viber_id=viber_request.user_id,
                defaults={
                    "is_active": False
                }
            )

    return HttpResponse(200)


def set_webhook(request):
    viber.set_webhook('https://7706597a.ngrok.io/viber/callback/', webhook_events=["subscribed", "unsubscribed",
                                                                                   "conversation_started"])

    return HttpResponse(200)


def unset_webhook(request):
    viber.unset_webhook()
    return HttpResponse(200)
