"""memo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:memo_id>', views.detail, name='detail'),
    path('new_memo', views.new_memo, name='new_memo'),
    path('delete_memo/<int:memo_id>', views.delete_memo, name='delete_memo'),
    path('edit_memo/<int:memo_id>', views.edit_memo, name='edit_memo'),
]

