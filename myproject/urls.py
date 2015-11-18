from django.conf.urls import include, url
from django.contrib import admin

from myapp import views as MyAppView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^mypage/', MyAppView.DisplayMyPage),
    url(r'^mypage_param/(?P<my_parameter>.+)/(?P<my_parameter2>.+)', MyAppView.DisplayMyPageWithParameter),
    url(r'^post_list/', MyAppView.post_list),
    url(r'^post/(?P<post_id>.+)', MyAppView.post_view),
]
