from django.conf.urls import include, url
from django.contrib import admin

from myapp import views as MyAppView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^mypage/', MyAppView.DisplayMyPage),
]
