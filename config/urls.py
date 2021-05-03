"""config URL Configuration

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
from django.contrib import admin
from django.urls import include, path
from schedule import views


urlpatterns = [
    path('admin/', admin.site.urls),
    # トップページ
    path('', views.IndexView.as_view(), name='index'),
    # 予定一覧
    path('schedule', views.ScheduleListView.as_view(), name='schedule_list'),
    path('schedule/create', views.ScheduleCreateView.as_view(), name='schedule_create'),
    path('schedule/edit/<int:pk>', views.ScheduleEditView.as_view(), name='schedule_edit'),
    path('schedule/delete/<int:pk>', views.ScheduleDeleteView.as_view(), name='schedule_delete'),
    # お知らせ一覧
    path('info', views.InfoListView.as_view(), name='info_list'),
    path('info/create', views.InfoCreateView.as_view(), name='info_create'),
    path('info/edit/<int:pk>', views.InfoEditView.as_view(), name='info_edit'),
    path('info/delete/<int:pk>', views.InfoDeleteView.as_view(), name='info_delete'),
    # メモ一覧
    path('note', views.NoteListView.as_view(), name='note_list'),
    path('note/create', views.NoteCreateView.as_view(), name='note_create'),
    path('note/edit/<int:pk>', views.NoteEditView.as_view(), name='note_edit'),
    path('note/delete/<int:pk>', views.NoteDeleteView.as_view(), name='note_delete'),
    # 持ち出し＆補充一覧
    path('sc', views.StockControlListView.as_view(), name='sc_list'),
    path('sc/create', views.StockControlCreateView.as_view(), name='sc_create'),
    path('sc/edit/<int:pk>', views.StockControlEditView.as_view(), name='sc_edit'),
    path('sc/delete/<int:pk>', views.StockControlDeleteView.as_view(), name='sc_delete'),
]
