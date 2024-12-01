from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('hello/', views.hello, name='hello'),
    
    # ---------- function based view path -----------
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    
    # ---------- class based view path -----------
    path('class_tasks/', views.TaskList.as_view(), name='class_task_list'),
    path('class_tasks/<int:pk>/', views.TaskDetail.as_view(), name='class_task_detail'),
]

router = DefaultRouter()

# ---------- Path for Task -----------
router.register('task', views.TaskViewSet, basename='task')

# ---------- Path for Book and Author -----------
router.register('book', views.BookViewSet, basename='book')
router.register('author', views.AuthorViewSet, basename='author')

urlpatterns += router.urls