from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from viberbot.api.viber_requests import ViberConversationStartedRequest, ViberMessageRequest, ViberSubscribedRequest, \
    ViberUnsubscribedRequest
from viberbot.api.messages import TextMessage, KeyboardMessage, RichMediaMessage
from viberbot import Api
from django.conf import settings

from .viber_config import bot_configuration
from viber.models import ViberUser

viber = Api(bot_configuration)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        viber_request = viber.parse_request(request.body)
        # user_data = viber.get_user_details(viber_request.sender.id)
        # print(user_data)
        # print(viber_request)
        print(viber_request)
        if isinstance(viber_request, ViberConversationStartedRequest):
            print(viber_request.user.id)
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

            keyboard = {
                "Type": "keyboard",
                #"DefaultHeight": False,
                'CustomDefaultHeight': 70,
                #'ButtonsGroupColumns': 4,
                'InputFieldState':'hidden',
                "Buttons": [
                    {
                        "Rows": 2,
                        "Columns": 2,
                        "ActionType": "reply",
                        "ActionBody": "give me you phone number",
                        "Text": "предоставить номер",
                        "TextSize": "regular",
                        "BgColor": "#780000",
                    },
                    {
                        "Rows": 1,
                        "Columns":2,
                        "ActionType": "reply",
                        "ActionBody": "give me you phone number",
                        "Text": "предоставить номер",
                        "TextSize": "regular",
                        "BgColor": "#780000",
                    },

                    {
                        "Rows": 2,
                        "Columns": 2,
                        "ActionType": "reply",
                        "ActionBody": "give me you phone number",
                        "Text": "предоставить номер",
                        "TextSize": "regular",
                        "BgColor": "#780000",
                    }
                    ,
                    {
                        "Rows": 2,
                        "Columns": 6,
                        "ActionType": "reply",
                        "ActionBody": "give me you phone number",
                        "Text": "предоставить номер",
                        "TextSize": "regular",
                        "BgColor": "#780000",
                    }

                ]
            }

            # viber.send_messages(
            #     viber_user.viber_id,
            #     [
            #         RichMediaMessage(rich_media=carousel, min_api_version=2)
            #     ]
            # )
            viber.send_messages(
                viber_user.viber_id,
                [KeyboardMessage(keyboard=keyboard, min_api_version=6)],
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
                keyboard = {
                    "Type": "keyboard",
                    "DefaultHeight": True,
                    "Buttons": [
                        {
                            "ActionType": "share-phone",
                            "ActionBody": "give me you phone number",
                            "Text": "предоставить номер",
                            "TextSize": "regular",
                            "BgColor": "#780000",
                        }

                    ]
                }
                viber.send_messages(
                    user_id,
                    [KeyboardMessage(keyboard=keyboard, min_api_version=3)],
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
    viber.set_webhook('https://6c396a0a.ngrok.io/viber/callback/')
    return HttpResponse(200)


def unset_webhook(request):
    viber.unset_webhook()
    return HttpResponse(200)
