""" Model field module."""

from django.db.models import CharField

from django_ibanfield.validators import iban_validator

class IBANField(CharField):

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 35
        super(IBANField, self).__init__(*args, **kwargs)
        self.validators.append(iban_validator)
