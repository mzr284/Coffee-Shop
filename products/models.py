from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    parent = models.ForeignKey(to="self",verbose_name=_("parent") , blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(_("title"), max_length=20, unique=True, error_messages= {
                                                "unique": _("this title already exist!"),
                                                },)
    avatar = models.ImageField(_("avatar"), upload_to="categories/", blank=True)

    class  Meta:
        db_table = "categories"
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.title


class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    title = models.CharField(_("title"), max_length=30, unique=True,
                             error_messages={"error": "this product already exist"})
    count = models.IntegerField(_("count"))
    avatar = models.ImageField(_("avatar"), upload_to="products/")
    description = models.TextField(_("description"), blank=True)
    is_enable = models.BooleanField(_("is exists"), default=True)

    class Meta:
        db_table = "products"
        verbose_name = _("product")
        verbose_name_plural = _("products")

    def __str__(self):
        return self.title

