from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from viberbot import Api
from viberbot.api.bot_configuration import BotConfiguration

bot_configuration = BotConfiguration(
    name='happyshop',
    avatar='https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg',
    auth_token='4a26d3d64067d12f-3bad0647a89b0e46-bc25cd57eae1b2c'
)

viber = Api(bot_configuration)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        #viber_request = viber.parse_request(request.body)
        #user_data = viber.get_user_details(viber_request.sender.id)
        #print(user_data)
        print(type(request.body))
        pass
    return HttpResponse(200)

# Create your views here.
