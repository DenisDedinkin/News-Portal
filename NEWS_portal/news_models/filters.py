from django_filters import FilterSet

from .models import Post


# Создаем свой набор фильтров для модели Post.
# FilterSet, который мы наследуем, должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
    class Meta:
        model = Post  # В Meta классе мы должны указать Django модель, в которой будем фильтровать записи.
        fields = {  # В fields мы описываем по каким полям модели будет производиться фильтрация.
            'title': ['icontains'],
            'post_type': ['exact'],
            'in_time': ['gt'],

        }
