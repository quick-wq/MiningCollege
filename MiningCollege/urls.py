from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from MiningCollege.settings import STATIC_URL, STATIC_ROOT

urlpatterns = [
    path('', include('website.urls')),
    path('authorization/', include('authorization.urls')),
    path('personal_area/', include('personal_area.urls')),
    path('admin/', admin.site.urls)
] + static(STATIC_URL, document_root=STATIC_ROOT)

handler404 = 'website.views.handler404'
handler500 = 'website.views.handler500'
