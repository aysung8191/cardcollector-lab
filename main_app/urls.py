from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cards/', views.cards_index, name='index'),
    path('cards/<int:card_id>/', views.cards_detail, name='detail'),
    path('cards/create/', views.CardCreate.as_view(), name="cards_create"),
    path('cards/<int:pk>/update/', views.CardUpdate.as_view(), name='cards_update'),
    path('cards/<int:pk>/delete', views.CardDelete.as_view(), name='cards_delete'),
    path('cards/<int:card_id>/add_cleaning/', views.add_cleaning, name='add_cleaning'),
    path('cards/<int:card_id>/assoc_cover/<int:cover_id>/', views.assoc_cover, name='assoc_cover'),
    path('cards/<int:card_id>/disassoc_cover/<int:cover_id>/', views.disassoc_cover, name = 'disassoc_cover'),
    path('covers/', views.CoverList.as_view(), name='covers_index'),
    path('covers/<int:pk>/', views.CoverDetail.as_view(), name='covers_detail'),
    path('covers/create/', views.CoverCreate.as_view(), name='covers_create'),
    path('covers/<int:pk>/update/', views.CoverUpdate.as_view(), name='covers_update'),
    path('covers/<int:pk>/delete/', views.CoverDelete.as_view(), name='covers_delete'),
]