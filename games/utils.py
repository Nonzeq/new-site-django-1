from .forms import CommentForm
from .models import *

menu = [
    {'title': 'О сайте', 'ulr_name': 'about'},
    {'title': 'Добавить статью', 'ulr_name': 'add_page'},
    {'title': 'Обратная связь', 'ulr_name': 'contact'},
]


class DataMixin:
    paginate_by = 6
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        user_menu = menu.copy()
        #если юзер авторизован + добавить статью
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context