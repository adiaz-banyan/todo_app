from django.apps import AppConfig


class TodoAppBaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'todo_app_base'
