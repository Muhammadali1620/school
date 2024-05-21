from django.core.exceptions import ValidationError


def phone_validate(phone_number: str) -> None:
    if len(phone_number) != 13 or not phone_number.startswith('+998') or not phone_number[1:].isdigit():
        raise ValidationError("Telefon nomerda 13 ta raqam bo'ladi") 