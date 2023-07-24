from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class WebhookActiveCampaign(APIView):
    def post(self, request, id):
        try:
            data = self._process_data(request.data.dict())
            phone_number = data.get("phone", "")
            formatted_phone = self._format_phone_number(phone_number)
            formatted_message = f'{data.get("list", "")}:\nNome: {data.get("first_name", "")}\nContato: {data.get("phone", "")}\nhttps://wa.me/+55{formatted_phone}'

            # Enviar para a fila do whatsapp
            print("FORMAT", formatted_message)
            return Response(formatted_message, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(e, status=status.HTTP_200_OK)

    def _process_data(self, data):
        return  {
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
        cleaned_phone = phone_number.replace("(", "").replace(")", "").replace(" ", "").replace("-", "").replace("+55", "")
        return cleaned_phone


def integration_view(request):
    webhook_context = { 
        "status": "Desativado",
        "url": "-",#f"http://15.228.146.110/integrations/{request.user.id}/active-campaign",
        "countCalls": 0
    }
    return render(
        request, 
        'pages/integrations/integration.html', 
        context={ "weebhook": webhook_context })
