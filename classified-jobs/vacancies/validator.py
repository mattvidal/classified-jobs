# Created custom validator
from django.core.exceptions import ValidationError


def validate_id_document_length(value):

    #Brazilian CPF or CNPJ only(length = 11 or 14)

    length = len(str(value))

    if length != 11 or length != 14 :
        raise ValidationError(u'%s is not the correct length' % value)