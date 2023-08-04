from django.urls import path

from .views import integration_view, WebhookActiveCampaign, WebhookHotmart
urlpatterns = [
    path("", integration_view, name="integrations"),

    # WebHooks
    path("<str:id>/active-campaign", WebhookActiveCampaign.as_view(), name="active-campaign"),
    path("<str:id>/hotmart", WebhookHotmart.as_view(), name="hotmart"),
]
