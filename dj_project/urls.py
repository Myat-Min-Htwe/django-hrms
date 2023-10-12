
from django.contrib import admin
from django.urls import path,include

from payrow import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('attendance.urls')),
    path('extant/',include('extant.urls')),
    path('payrow/', include('payrow.urls')),

    path('login/',views.loginView,name="login"),
    path('logout/',views.logoutView,name="logout"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
