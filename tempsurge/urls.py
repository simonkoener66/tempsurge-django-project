from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'tempsurge.views.home', name='home'),
                       # url(r'^login/$', 'tempsurge.views.login', name='login'),
                       # url(r'^$', 'tempsurge.views.home_old', name='home_old'),
                       # url(r'^blog/', include('blog.urls')),

                       (r'^accounts/', include('accounts.urls')),
                       (r'^agencies/', include('agencies.urls')),
                       (r'^employers/', include('employers.urls')),

                       url(r'^admin/', include(admin.site.urls)),

                       (r'^pages/', include('django.contrib.flatpages.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)