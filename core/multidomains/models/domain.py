from django.db import models
from django.contrib.postgres.fields import ArrayField
from utils.validators import domain_validator
class Domain(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE, related_name='domains')
    name = models.CharField(max_length=255, validators=[domain_validator], unique=True)
    zone = models.CharField(max_length=255, blank=True, null=True)
    name_servers = ArrayField(
        models.CharField(max_length=255),
        default=list,
        blank=True,
        null=True,
    )
    is_created = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = [
            "-id",
        ]

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def created(self):
        self.is_created = True
        self.save()
    
    def active(self):
        self.is_active = True
        self.save()