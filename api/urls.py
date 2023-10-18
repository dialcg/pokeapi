from django.urls import path, include

from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

from api.core import urls as api_core_urls


urlpatterns = [
    path('pokemon/', include(api_core_urls)),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "docs/",
        SpectacularSwaggerView.as_view(
            template_name="swagger-ui.html", url_name="schema"
        ),
        name="swagger-ui",
    ),
]


