from .models import CompanyDetails

def get_company_details_context(request):
    """
    CompanyDetails model allows only one object.
    Collect this object and return details as context for use in templates
    """
    company_details = CompanyDetails.objects.get(id=1)

    context = {
        'company_email': company_details.email,
        'company_phone_number': company_details.phone_number,
        'company_address1': company_details.street_address1,
        'company_address2': company_details.street_address2,
        'company_town_or_city': company_details.town_or_city,
        'company_postcode': company_details.postcode,
    }

    return context