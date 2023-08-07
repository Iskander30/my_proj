from django.urls import path
from .views import les

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', les),
]
