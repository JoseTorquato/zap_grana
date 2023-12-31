from typing import Any
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from integrations.models import CalledWebHook, Integration
from core.api.whatsapp import WhatsApp
from user.models import Profile

import logging

logger = logging.getLogger('django')

def save_count_call(user_uuid, platform, response_data):
    integration = Integration.objects.get(user_uuid=user_uuid, platform=platform)
    integration.call_count += 1
    integration.save()

    webhook_call = CalledWebHook(integration=integration, response_data=response_data)
    webhook_call.save()

def format_phone_number(phone_number):
        cleaned_phone = phone_number.replace("(", "").replace(")", "").replace(" ", "").replace("-", "").replace("+55", "")
        return cleaned_phone

class WebhookActiveCampaign(APIView):
    def post(self, request, id):
        try:
            data = self._process_data(request.data.dict())
            phone_number = data.get("phone", "")
            formatted_phone = format_phone_number(phone_number)
            formatted_message = f'Checkout Active Campaign:\nProduto: {data.get("list", "")}\nNome: {data.get("first_name", "")}\nContato: {data.get("phone", "")}\nhttps://wa.me/+55{formatted_phone}'

            #TODO: Enviar para a fila
            user = Profile.objects.get(uuid=id)
            save_count_call(id, 'activeCampaign')
            response = WhatsApp().send_message(formatted_message, user.phone)

            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            logger.info(e)
            logger.warning(request.data.dict())
            return Response({ "body": str(e)}, status=status.HTTP_200_OK)

    def _process_data(self, data):
        print(data)
        return {
            "list": data.get("list", ''),
            "id": data["contact[id]"],
            "email": data["contact[email]"],
            "first_name": data["contact[first_name]"],
            "last_name": data["contact[last_name]"],
            "phone": data["contact[phone]"]
        }


class WebhookHotmart(APIView):
    def post(self, request, id):
        try:
            print(request.data)
            data = self._process_data(request.data)
            phone_number = data.get("phone", "")
            formatted_phone = format_phone_number(phone_number)
            formatted_message = f'Checkout Hotmart:\nProduto: {data.get("product", "")}\nNome: {data.get("name", "")}\nContato: {data.get("phone", "")}\nhttps://wa.me/+55{formatted_phone}'

            #TODO: Enviar para a fila
            user = Profile.objects.get(uuid=id)
            save_count_call(id, 'hotmart', data)
            response = WhatsApp().send_message(formatted_message, user.phone)

            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("DATA =>", data)
            print("USER =>", user)
            return Response({ "body": str(e)}, status=status.HTTP_200_OK)

    def _process_data(self, data):
        return {
            "product": data["data"]["product"]["name"],
            "id": data["id"],
            "email": data["data"]["buyer"]["email"],
            "name": data["data"]["buyer"]["name"],
            "phone": data["data"]["buyer"]["phone"],
            "country": data["data"]["checkout_country"]["iso"]
        }


class WebhookEduzz(APIView):
    def post(self, request, id):
        try:
            print(request.data)
            data = self._process_data(request.data)
            phone_number = data.get("phone", "") if data.get("phone", "")[0] != '0' else data.get("phone", "")[1:]
            formatted_phone = format_phone_number(phone_number)
            formatted_message = f'Checkout Eduzz:\nProduto: {data.get("product", "")}\nNome: {data.get("name", "")}\nContato: {data.get("phone", "")}\nhttps://wa.me/+55{formatted_phone}'

            #TODO: Enviar para a fila
            user = Profile.objects.get(uuid=id)
            save_count_call(id, 'eduzz', data)
            response = WhatsApp().send_message(formatted_message, user.phone)

            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("DATA =>", data)
            print("USER =>", user)
            return Response({ "body": str(e)}, status=status.HTTP_200_OK)

    def _process_data(self, data):
        return {
            "product": data["product"]["title"],
            "id": data["identifier"],
            "email": data["customer"]["email"],
            "name": data["customer"]["name"],
            "phone": data["customer"]["phone"]
        }


class WebhookGuru(APIView):
    def post(self, request, id):
        try:
            logger.info(request.data)
            data = self._process_data(request.data)
            phone_number = data.get("phone", "") if data.get("phone", "")[0] != '0' else data.get("phone", "")[1:]
            formatted_phone = format_phone_number(phone_number)
            formatted_message = f'Checkout Guru:\nProduto: {data.get("product", "")}\nNome: {data.get("name", "")}\nContato: {data.get("phone", "")}\nhttps://wa.me/+55{formatted_phone}'

            #TODO: Enviar para a fila
            user = Profile.objects.get(uuid=id)
            save_count_call(id, 'guru', data)
            response = WhatsApp().send_message(formatted_message, user.phone)

            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            logger.warning(e)
            logger.warning(id)
            logger.warning(request.data)
            return Response({ "body": str(e)}, status=status.HTTP_200_OK)

    def _process_data(self, data):
        return {
            "product": data["product"]["offer"]["name"],
            "email": data["contact"]["email"],
            "name": data["contact"]["name"],
            "phone": data["contact"]["phone_number"],
            "code": data["contact"]["phone_local_code"]
        }


class WebhookKiwify(APIView):
    def post(self, request, id):
        try:
            print(request.data)
            data = self._process_data(request.data)
            phone_number = data.get("phone", "") if data.get("phone", "")[0] != '0' else data.get("phone", "")[1:]
            formatted_phone = format_phone_number(phone_number)
            formatted_message = f'Checkout Kiwify:\nProduto: {data.get("product", "")}\nNome: {data.get("name", "")}\nContato: {data.get("phone", "")}\nhttps://wa.me/+55{formatted_phone}'

            #TODO: Enviar para a fila
            user = Profile.objects.get(uuid=id)
            save_count_call(id, 'kiwify', data)
            response = WhatsApp().send_message(formatted_message, user.phone)

            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("DATA =>", data)
            print("USER =>", user)
            return Response({ "body": str(e)}, status=status.HTTP_200_OK)

    def _process_data(self, data):
        return {
            "product": data["product_name"],
            "id": data["id"],
            "email": data["email"],
            "name": data["name"],
            "phone": data["phone"],
            "country": data["country"]
        }

class WebhookTicTo(APIView):
    def post(self, request, id):
        try:
            print(request.data)
            data = self._process_data(request.data)
            phone_number = data.get("phone", "") if data.get("phone", "")[0] != '0' else data.get("phone", "")[1:]
            formatted_phone = format_phone_number(phone_number)
            formatted_message = f'Checkout TicTo:\nProduto: {data.get("product", "")}\nNome: {data.get("name", "")}\nContato: {data.get("phone", "")}\nhttps://wa.me/+55{formatted_phone}'

            #TODO: Enviar para a fila
            user = Profile.objects.get(uuid=id)
            save_count_call(id, 'ticto', data)
            response = WhatsApp().send_message(formatted_message, user.phone)

            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            # print(e)
            # print("DATA =>", data)
            # print("USER =>", user)
            return Response({ "body": str(e)}, status=status.HTTP_200_OK)

    def _process_data(self, data):
        return {
            "product": data["item"]["product_name"],
            "email": data["customer"]["email"],
            "name": data["customer"]["name"],
            "phone": f'{data["customer"]["phone"]["ddd"]}{data["customer"]["phone"]["number"]}',
            "ddi": data["customer"]["phone"]["ddi"]
        }


@login_required(login_url='/login')
def integration_view(request):
    if request.method == 'POST':
        btn = request.POST.get('btn')
        platform = request.POST.get('platform')
        schema_integration = request.POST.get('integration')
        uuid = request.user.profile.uuid
        url = f"https://zapgrana.com.br/integrations/{request.user.profile.uuid}/{schema_integration}"

        integration = Integration.objects.filter(
            user_uuid=request.user.profile.uuid)

        if btn == 'Desativar':
            integration_delete = Integration.objects.get(
            user_uuid=request.user.profile.uuid, platform=platform)

            integration_delete.delete()

        if btn == 'Ativar':
            integration = Integration(platform=platform, user_uuid=uuid, url=url, status='Ativo')
            integration.save()

    try:
        integration = Integration.objects.filter(
            user_uuid=request.user.profile.uuid)

        webhook_context = {}
        for i in integration:
            webhook_context[i.platform] = {
                "status": i.status,
                "url": i.url,
                "countCalls": i.call_count,
                "platform": i.platform
            }

    except Integration.DoesNotExist:
        webhook_context = {
            "status": "Desativado",
            "url": '-',
            "countCalls": '-'
        }

    return render(
        request,
        'pages/integrations/integration.html',
        context={"webhook": webhook_context})
