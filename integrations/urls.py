from django.urls import path

from .views import integration_view, WebhookActiveCampaign, WebhookEduzz, WebhookGuru, WebhookHotmart, WebhookKiwify
urlpatterns = [
    path("", integration_view, name="integrations"),

    # WebHooks
    path("<str:id>/active-campaign", WebhookActiveCampaign.as_view(), name="active-campaign"),
    path("<str:id>/eduzz", WebhookEduzz.as_view(), name="eduzz"),
    path("<str:id>/guru", WebhookGuru.as_view(), name="guru"),
    path("<str:id>/hotmart", WebhookHotmart.as_view(), name="hotmart"),
    path("<str:id>/kiwify", WebhookKiwify.as_view(), name="kiwify"),
]
