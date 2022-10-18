from .models import CompanyDetails

def get_company_details_context(request):
    """
    CompanyDetails model allows only one object.
    Collect this object and return details as context for use in templates

    Defaults to initial details if no entry in database exists
    """
    company_details = CompanyDetails.objects.all()

    if company_details.exists():
        company_details = CompanyDetails.objects.get()

        context = {
            'company_email': company_details.email,
            'company_phone_number': company_details.phone_number,
            'company_address1': company_details.street_address1,
            'company_address2': company_details.street_address2,
            'company_town_or_city': company_details.town_or_city,
            'company_postcode': company_details.postcode,
        }

    else:
        context = {
        'company_email': 'sales@point.co.uk',
        'company_phone_number': '0115 971 8909',
        'company_address1': 'Point Construction',
        'company_address2': '15 The Point,',
        'company_town_or_city': 'Nottingham',
        'company_postcode': 'NG1 1LL',
        }

    return context