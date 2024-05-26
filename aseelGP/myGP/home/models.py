from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from enum import Enum
from django.utils.html import escape
import magic
# Create your models here.


def validate_age(value):
    if value >= 18:
        return value
    else:
        raise ValidationError("your age should be grater than or equal to 18")


class UserInfo(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    User._meta.get_field('email')._unique = True
    User._meta.get_field('username')._unique = True
    #add

    full_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(validators=[validate_age, ])
    phone_number = models.CharField(validators=[phone_regex], max_length=17, help_text="ex:+9627958742359")
    bio = models.CharField(max_length=200, help_text="enter your bio here")
    failed_login_num = models.IntegerField(default=0)
    is_supervisor = models.BooleanField(default=False)
    pendaccess = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        # Escape the bio content before saving
        self.bio = escape(self.bio)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name


class PostCategoryEnum(Enum):
    SOCIAL = 1
    EDUCATIONAL = 2
    PROGRAMMING = 3
    NETWORKING = 4


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    created_datetime = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    category_enum = models.IntegerField(choices=[(choice.value, choice.name) for choice in PostCategoryEnum])

    show = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Manually sanitize the content before saving
        self.content = escape(self.content)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Post {self.id}"


def validate_file_type_and_size(value):
    # # Check file type
    # allowed_types = ['application/msword', 'application/pdf', 'application/vnd.ms-excel', 'application/vnd.ms-powerpoint']
    # file_mime = magic.Magic()
    # mime_type = file_mime.from_buffer(value.read(1024))  # Read the first 1024 bytes to determine MIME type
    # # if mime_type not in allowed_types:
    # #     raise ValidationError('Invalid file type. Allowed types are Word, PDF, Excel, and PowerPoint.')
    #
    # # Check file size
    max_size = 32 * 1024 * 1024  # 32 MB
    if value.size > max_size:
        raise ValidationError('File size must be no more than 32 MB.')


class UploadedFile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads/', validators=[validate_file_type_and_size])
    created_datetime = models.DateTimeField(auto_now_add=True)
    category_enum = models.IntegerField(choices=[(choice.value, choice.name) for choice in PostCategoryEnum])
    show = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)
    scan_result = models.CharField(max_length=255, blank=True, null=True)


class PendAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    num_access = models.PositiveIntegerField(default=0)


