from django.apps import AppConfig


class NewsModelsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news_models'


    def ready(self):
        import news_models.signals