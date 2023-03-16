from django.urls import path
# Импортируем созданные нами представления
from .views import NewsList, PostDetail, NewsCreate, NewsUpdate, NewsDelete, ArticlesCreate, ArticlesUpdate, \
    ArticlesDelete, subscribe, unsubscribe

urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым. Т.к. наше объявленное
    # представление является классом, а Django ожидает функцию, нам надо представить этот класс в виде view.
    # Для этого вызываем метод as_view.
    path('', NewsList.as_view(), name='news_list'),
    # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    # int — указывает на то, что принимаются только целочисленные значения
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),

    path('news/edit/', NewsCreate.as_view(), name='news_edit'),
    path('news/<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
    path('news/<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),

    path('articles/edit/', ArticlesCreate.as_view(), name='articles_edit'),
    path('articles/<int:pk>/update/', ArticlesUpdate.as_view(), name='articles_update'),
    path('articles/<int:pk>/delete/', ArticlesDelete.as_view(), name='articles_delete'),

    path('<int:pk>/subscribe/', subscribe, name='subscribe'),
    path('<int:pk>/unsubscribe/', unsubscribe, name='unsubscribe'),
    ]
