from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


def integration_view(request):
    return render(request, 'pages/integrations/integration.html')

class WebhookActiveCampaign(APIView):
    def post(self, request, id):
        try:
            print(id)
            print(request.data.dict())
            data = self._process_data(request.data.dict())
            phone_number = data.get("contact[phone]", "")
            formatted_phone = self._format_phone_number(phone_number)
            formatted_message = f'{data.get("list", "")}:\nNome: {data.get("contact[first_name]", "")}\nContato: {data.get("contact[phone]", "")}\nhttps://wa.me/+55{formatted_phone}'

            print("FORMAT", formatted_message)
            return Response(formatted_message, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(e, status=status.HTTP_200_OK)

    def _process_data(self, data):
        contact = {
            "id": data["contact[id]"],
            "email": data["contact[email]"],
            "first_name": data["contact[first_name]"],
            "last_name": data["contact[last_name]"],
            "phone": data["contact[phone]"],
            "ip": data["contact[ip]"],
            "tags": data["contact[tags]"]
        }

        return {
            "list": data["list"],
            "contact": contact
        }

    def _format_phone_number(self, phone_number):
        print("FORMART")
        cleaned_phone = phone_number.replace("(", "").replace(")", "").replace(" ", "").replace("-", "").replace("+55", "")
        return cleaned_phone

