from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from viberbot.api.viber_requests import ViberConversationStartedRequest, ViberMessageRequest, ViberSubscribedRequest, ViberUnsubscribedRequest
from viberbot.api.messages.text_message import TextMessage
from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration

from viber.models import ViberUser

bot_configuration = BotConfiguration(
    name='happyshop',
    avatar='https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg',
    auth_token='4a26d3d64067d12f-3bad0647a89b0e46-bc25cd57eae1b2c',
    )

viber = Api(bot_configuration)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        viber_request = viber.parse_request(request.body)
        #user_data = viber.get_user_details(viber_request.sender.id)
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
            print(viber_request.user.id)
        elif isinstance(viber_request, ViberSubscribedRequest):
            pass
        elif isinstance(viber_request, ViberUnsubscribedRequest):
            v_user, created = ViberUser.objects.update_or_create(
                viber_id=viber_request.user_id,
                defaults={
                    "is_active": False
                }
            )

    return HttpResponse(200)


def set_webhook(request):
    viber.set_webhook('https://cc341262.ngrok.io/viber/callback')
    return HttpResponse(200)


def unset_webhook(request):
    viber.unset_webhook()
    return HttpResponse(200)
