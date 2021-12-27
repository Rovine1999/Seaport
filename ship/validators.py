from django.core.exceptions import ValidationError


def validate_file(value):
    value= str(value)
    if value.endswith(".pdf") != True: 
        raise ValidationError("Only PDF Documents can be uploaded")
    else:
        return value

def validate_file_extension(value):
  import os
  ext = os.path.splitext(value.name)[1]
  valid_extensions = ['.pdf','.doc','.docx']
  if not ext in valid_extensions:
    raise ValidationError(u'File not supported!')