from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from apps.general.views import home, set_language


urlpatterns = [ 
    path('admin/', admin.site.urls),

    path('setlang/', set_language, name='set_language'),
    path('ckeditor5/', include('django_ckeditor_5.urls'), name='ck_editor_5_upload_file'),
    path('__debug__/', include('debug_toolbar.urls')),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += i18n_patterns(
    path('', home, name='home')
)