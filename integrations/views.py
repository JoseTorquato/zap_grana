from typing import Any
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from integrations.models import Integration
from core.api.whatsapp import WhatsApp
from user.models import Profile


class WebhookActiveCampaign(APIView):
    def post(self, request, id):
        try:
            print(request)
            data = self._process_data(request.data.dict())
            phone_number = data.get("phone", "")
            formatted_phone = self._format_phone_number(phone_number)
            formatted_message = f'{data.get("list", "")}:\nNome: {data.get("first_name", "")}\nContato: {data.get("phone", "")}\nhttps://wa.me/+55{formatted_phone}'

            #TODO: Enviar para a fila
            user = Profile.objects.get(uuid=id)
            response = WhatsApp().send_message(formatted_message, user.phone)

            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("DATA =>", data)
            print("USER =>", user)
            return Response({ "body": str(e)}, status=status.HTTP_200_OK)

    def _process_data(self, data):
        return {
            "list": data["list"],
            "id": data["contact[id]"],
            "email": data["contact[email]"],
            "first_name": data["contact[first_name]"],
            "last_name": data["contact[last_name]"],
            "phone": data["contact[phone]"],
            "ip": data["contact[ip]"],
            "tags": data["contact[tags]"]
        }

    def _format_phone_number(self, phone_number):
        cleaned_phone = phone_number.replace("(", "").replace(")", "").replace(
            " ", "").replace("-", "").replace("+55", "")
        return cleaned_phone


class WebhookHotmart(APIView):
    def post(self, request, id):
        try:
            print(request.data)
            data = self._process_data(request.data)
            phone_number = data.get("phone", "")
            formatted_phone = self._format_phone_number(phone_number)
            formatted_message = f'{data.get("product", "")}:\nNome: {data.get("name", "")}\nContato: {data.get("phone", "")}\nhttps://wa.me/+55{formatted_phone}'

            #TODO: Enviar para a fila
            user = Profile.objects.get(uuid=id)
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

    def _format_phone_number(self, phone_number):
        cleaned_phone = phone_number.replace("(", "").replace(")", "").replace(" ", "").replace("-", "").replace("+55", "")
        return cleaned_phone


class WebhookEduzz(APIView):
    def post(self, request, id):
        try:
            print(request.data)
            data = self._process_data(request.data)
            phone_number = data.get("phone", "") if data.get("phone", "")[0] != '0' else data.get("phone", "")[1:]
            formatted_phone = self._format_phone_number(phone_number)
            formatted_message = f'{data.get("product", "")}:\nNome: {data.get("name", "")}\nContato: {data.get("phone", "")}\nhttps://wa.me/+55{formatted_phone}'

            #TODO: Enviar para a fila
            user = Profile.objects.get(uuid=id)
            response = WhatsApp().send_message(formatted_message, user.phone)

            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("DATA =>", data)
            print("USER =>", user)
            return Response({ "body": str(e)}, status=status.HTTP_200_OK)

    def _process_data(self, data):
        return {
            "product": data["product[title]"],
            "id": data["identifier"],
            "email": data["customer[email]"],
            "name": data["customer[name]"],
            "phone": data["customer[phone]"]
        }

    def _format_phone_number(self, phone_number):
        cleaned_phone = phone_number.replace("(", "").replace(")", "").replace(" ", "").replace("-", "").replace("+55", "")
        return cleaned_phone


@login_required(login_url='/login')
def integration_view(request):
    if request.method == 'POST':
        btn = request.POST.get('btn')
        schema_integration = request.POST.get('integration')
        uuid = request.user.profile.uuid
        url = f"http://15.228.146.110/integrations/{request.user.profile.uuid}/{schema_integration}"

        try:
            integration = Integration.objects.get(
                user_uuid=request.user.profile.uuid)
            if btn == 'Desativar':
                integration.delete()
        except:
            integration = Integration(user_uuid=uuid, url=url, status='Ativo')
            integration.save()

    try:
        integration = Integration.objects.get(
            user_uuid=request.user.profile.uuid)

        webhook_context = {
            "status": integration.status,
            "url": integration.url,
            "countCalls": integration.call_count
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
        context={"weebhook": webhook_context})
