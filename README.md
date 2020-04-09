# Django IBAN Field


IBANField is an extension for django CharField with special validation for IBAN accounts.

## Install

You can install django-ibanfield with pip as usual o pipenv

```bash
    $> pip install django-ibanfield
```

```bash
    $> pipenv install django-ibanfield
```

## Usage

Use IBANField on your models, like any other django models fields.

```python
    from django_ibanfield.fields import IBANField

    class MyModel(models.Model):

        account = IBANField()
```
