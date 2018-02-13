
from django.conf.urls import url

from .views import (
    ProductListView,
    ProductDetailSlugView,
    )

urlpatterns = [
    url(r'^products/$', ProductListView.as_view()),
    url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),
]
