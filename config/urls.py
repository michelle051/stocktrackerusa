from django.contrib import admin
from django.urls import path, include
from stocktrackerusa import views
from stocktrackerusa.views import base_views, chartfinder_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stocktrackerusa/', include('stocktrackerusa.urls')),
    path('common/', include('common.urls')),
    path('', base_views.index, name='index'),  # '/' 에 해당되는 path
    path('stockbacktest/', chartfinder_views.stockbacktest, name='stockbacktest'),
    path('stockpathdetail/', chartfinder_views.stockpathdetail, name='stockpathdetail'),
    path('pathdetailinfo/', chartfinder_views.pathdetailinfo, name='pathdetailinfo'),
]
