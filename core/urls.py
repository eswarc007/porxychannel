from django.conf.urls import url, include
from rest_framework import routers
from .views import ProxyViewSet, countryView, cityView, RegionView
# from rest_framework_swagger.views import get_swagger_view

router = routers.DefaultRouter()
router.register(r'proxies', ProxyViewSet)
# router.register(r'country', countryViewSet)

# schema_view = get_swagger_view(title='API Docs')
urlpatterns = [
    url(r'^country/$', countryView.as_view()),
    url(r'^city/$', cityView.as_view()),
    url(r'^region/$', RegionView.as_view()),
]
urlpatterns += router.urls