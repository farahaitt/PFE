# from django.urls import path
# from . import views
# from .views import ReactViewSet


# urlpatterns = [
#     path('', views.ReactView.as_view(), name='react'),  # Update to use ReactView from views.py
# ]


from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings
from .views import react_api

urlpatterns = [

    path('react/', react_api , name='react_api'),
    path('react/<int:pk>', views.react_api),
    # path('', views.ReactListView.as_view(), name='react_list'),  # API endpoint for listing and adding forecasts
    # path('', ReactViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='react_detail'),  # Detail API endpoint for CRUD operations on individual forecasts
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

