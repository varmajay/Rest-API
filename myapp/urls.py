from django.urls import path
from .import views
urlpatterns = [
    path('',views.overviews,name='overviews'),
    path('all-data/',views.all_data,name='all-data'),
    path('one-data/<int:pk>',views.one_data,name='one-data'),
    path('create-data/',views.create_data,name='create-data'),

]
