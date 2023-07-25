from django.db import models
import uuid

class Integration(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.URLField()
    user_uuid = models.UUIDField()
    status = models.CharField(max_length=20)
    call_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"ID: {self.id}, URL: {self.url}, User UUID: {self.user_uuid}, Status: {self.status}, Call Count: {self.call_count}"
    