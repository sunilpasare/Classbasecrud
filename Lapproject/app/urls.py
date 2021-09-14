from django.urls import path
from .views import LaptopListview,LaptopCreateview,LaptopUpdateview,LaptopDeleteview

urlpatterns=[
    path('list/',LaptopListview.as_view(),name='listview'),
    path('create/',LaptopCreateview.as_view(),name='create'),
    path('update/<int:pk>',LaptopUpdateview.as_view(),name='update'),
    path('delete/<int:pk>',LaptopDeleteview.as_view(),name='delete'),
]