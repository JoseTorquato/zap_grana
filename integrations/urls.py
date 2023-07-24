from django.urls import path

from .views import integration_view, WebhookActiveCampaign

urlpatterns = [
    path("", integration_view, name="integrations"),

    # WebHooks
    path("<int:id>/active-campaign", WebhookActiveCampaign.as_view(), name="active-campaign")
]
