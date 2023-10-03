# from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('posts/(?P<slug>.+)/', views.PostDetail.as_view(), name='post_detail'),
    path('service/(?P<slug>.+)/', views.DepartmentDetail.as_view(), name='department_detail'),
    path('services/', views.DepartmentList.as_view(), name='departments'),
    path('department/(?P<user>.+)/', views.ProfileDetail.as_view(), name='profile_detail')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

