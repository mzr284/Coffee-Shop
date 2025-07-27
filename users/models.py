import random
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):

    user_in_migrations = True
    def _create_user(self, username, phone_number, email, password, is_staff, is_superuser, **extra_field):
        if username is None:
            raise ValueError("username cannot Null")
        email = self.normalize_email(email)
        user = self.model(username=username, phone_number=phone_number, email=email, is_active=True,
                          is_staff=is_staff, is_superuser=is_superuser, data_joined=timezone.now(), **extra_field
                          )
        if not extra_field.get("no_password"):
            user.set_password(password)

        user.save(using=self._db)
        return user


    def create_user(self, username=None, phone_number=None, email=None, password=None, is_staff=None, **extra_field):
        if username is None:
            if phone_number:
                username = str(phone_number)[-7:] + random.choice('abcdefghijklmnopqrstuvwxyz0123456789')
            else:
                if email:
                    username = email.split("@")[0] + random.choice('abcdefghijklmnopqrstuvwxyz0123456789')
        while User.objects.filter(username=username).exists():
            username += str(random.randint(10))

        if is_staff is None:
            is_staff = False

        return self._create_user(username, phone_number, email, password, is_staff, **extra_field)

    def create_superuser(self, username, phone_number, email, password, **extra_field):
        return self._create_user(username, phone_number, email, password, True, True, **extra_field)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_("username"), unique=True, max_length=25,
                                validators= [RegexValidator(regex=r'^(?=.*[a-zA-Z])(?=.*\d).{6,}$',
                                                            message=_("Your username must be contain at least 6 character or number")
                                                            )], help_text="Enter at least 6 character or number for your username",
                                error_messages={"unique": _("this username already exist")},
                                )
    phone_number = models.BigIntegerField(_("phone number"), unique=True, validators= [RegexValidator(regex=r'^989[0-3]\d{8}$',
                                                                        message=_("Your phone number mast be unique and valid"))])
    full_name = models.CharField(_("full name"), max_length=30, blank=True, null=True)
    email = models.CharField(_("email"), max_length=40, blank=True, null=True)
    is_staff = models.BooleanField(_("is staff"), default=False)
    is_active = models.BooleanField(_("is active"), default=True)
    data_joined = models.DateTimeField(_("date join"), auto_now_add=True, blank=True, null=True)
    last_seen = models.DateTimeField(_("last seen"), default=timezone.now()
                                    , blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["phone_number", "email"]

    class Meta:
        db_table = "users"
        verbose_name = _("user")
        verbose_name_plural = _("users")



class UserPofile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE, related_name="user")
    avatar = models.ImageField(_("avatar"), blank=True, null=True, upload_to="users/%Y/%m/%d/")
    birthday = models.DateField(_("birthday"), blank=True, null=True)
    bio = models.TextField(_("bio"), blank=True)
    nick_name = models.CharField(_("nick name"), max_length=20, blank=True)

    class Meta:
        db_table = "users profile"
        verbose_name = _("user profile")
        verbose_name_plural = _("users profile")

    def __str__(self):
        return self.user.username
