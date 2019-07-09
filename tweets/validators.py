from django.core.exceptions import ValidationError

def validate_content(value):
    content = value
    if content == "":
        raise ValidationError("The content cannot be empty")
    return value