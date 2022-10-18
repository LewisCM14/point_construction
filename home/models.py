from django.db import models
from django.core.exceptions import ValidationError

class CompanyDetails(models.Model):
    """
    A model containing key company details, used for CMS
    """
    email = models.EmailField(unique=True, max_length=50)
    phone_number = models.CharField(unique=True, max_length=16)
    street_address1 = models.CharField(unique=True, max_length=80)
    street_address2 = models.CharField(unique=True, max_length=80)
    town_or_city = models.CharField(unique=True, max_length=40)
    postcode = models.CharField(unique=True, max_length=20)

    def clean(self):
        """
        cleanup method to ensure only one set of company details are saved
        """
        if CompanyDetails.objects.exists() and not self.pk:
            raise ValidationError("You can only have one set of company details")

    def save(self, *args, **kwargs):
       return super(CompanyDetails, self).save(*args, **kwargs)

    def __str__(self):
        """
        string method definition for the CompanyDetails model
        """
        return self.street_address1

    class Meta:
        """
        name definition for admin panel
        """
        verbose_name_plural = 'Company Details'