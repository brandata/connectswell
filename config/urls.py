from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from . import views

urlpatterns = [
                  # path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
                  path("", TemplateView.as_view(template_name="pages/index.html"), name="index"),
                  path("about/", TemplateView.as_view(template_name="pages/about.html"), name="about"),
                  path("organizations/", TemplateView.as_view(template_name="pages/organizations.html"),
                       name="organizations"),
                  path("practitioners/", TemplateView.as_view(template_name="pages/practitioners.html"),
                       name="practitioners"),
                  path("how-to/", TemplateView.as_view(template_name="pages/how-to.html"),
                       name="how-to"),
                  path("my-profile/", TemplateView.as_view(template_name="pages/my-profile.html"),
                       name="my-profile"),
                  path("contact/", views.contact_us, name="contact"),
                  path("org-signup/", views.org_contact, name="org-signup"),
                  path("prac-signup/", views.prac_contact, name="prac-signup"),
                  path("signedup/", TemplateView.as_view(template_name="pages/form-redirect.html"), name="signedup"),
                  # Django Admin, use {% url 'admin:index' %}
                  path(settings.ADMIN_URL, admin.site.urls),
                  # User management
                  path("users/", include("connectswell.users.urls", namespace="users")),
                  path("accounts/", include("allauth.urls")),
                  # Your stuff: custom urls includes go here
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
