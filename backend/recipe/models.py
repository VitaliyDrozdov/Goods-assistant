from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Ingredient(models.Model):
    class MeasureChoices(models.TextChoices):
        GRAMM = "г", _("Граммы")
        DROP = "капля", _("Капля")
        PIECE = "шт.", _("Штуки")
        BIGPIECE = "кусок", _("Кусок")
        ML = "мл", _("Миллилитры")
        TEASPOON = "ч.л.", _("Чайная ложка")

    name = models.CharField(name="Имя ингредиента", max_length=128)
    measurement_unit = models.CharField(
        name="Единицы измерения", choices=MeasureChoices.choices, max_length=64
    )

    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(name="Имя тэга", max_length=25)
    slug = models.SlugField(name="Слаг", unique=True, max_length=50)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name


class Recipe(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipes", db_index=True
    )
    name = models.CharField(name="Наименование рецепта", max_length=256)
    # поле image нужно будет заменить на другой тип
    image = models.ImageField(
        name="Изображение", upload_to="recipes", null=True, blank=True
    )
    text = models.TextField(name="Описание")
    ingredients = models.ManyToManyField(
        name="Ингредиенты",
        to=Ingredient,
        related_name="recipes",
    )
    tag = models.ManyToManyField(name="Тэг", to=Tag, related_name="recipes")
    cooking_time = models.IntegerField(
        name="Время приготовления", validators=[MinValueValidator(1)]
    )
    is_favorited = models.BooleanField(name="В избранном")
    is_in_shopping_car = models.BooleanField(name="В списке покупок")
    pub_date = models.DateTimeField(
        name="Дата публикации", auto_now_add=True, db_index=True
    )

    class Meta:
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(to=Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(to=Ingredient, on_delete=models.CASCADE)
    amount = models.IntegerField()

    class Meta:
        verbose_name = "RecipeIngredient"
        verbose_name_plural = "RecipeIngredients"


class Favorite(models.Model):
    author = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="favorites"
    )
    recipe = models.ForeignKey(
        to=Recipe, on_delete=models.CASCADE, related_name="favorites"
    )

    class Meta:
        verbose_name = "Favorite"
        verbose_name_plural = "Favorites"

    def __str__(self):
        return "Избранное"


class ShoppingCart(models.Model):
    author = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="shopping_cart"
    )
    recipe = models.ForeignKey(
        to=Recipe, on_delete=models.CASCADE, related_name="shopping_cart"
    )

    class Meta:
        verbose_name = "ShoppingCart"
        verbose_name_plural = "ShoppingCart"

    def __str__(self):
        return "Список покупок"
