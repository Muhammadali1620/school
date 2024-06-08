from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from apps.groups.views import home, set_language


urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls', namespace='users')),
    path('notice/', include('apps.notices.urls', namespace='notices')),
    path('exam/', include('apps.exams.urls', namespace='exams')),
    path('attendance/', include('apps.attendances.urls', namespace='attendances')),
    path('groups/', include('apps.groups.urls', namespace='student_groups')),
    path('subject/', include('apps.subjects.urls', namespace='subjects')),
    path('payment/', include('apps.payments.urls', namespace='payments')),
    path('additional/', include('apps.additionals.urls', namespace='additionals')),

    path('setlang/', set_language, name='set_language'),
    path('ckeditor5/', include('django_ckeditor_5.urls'), name='ck_editor_5_upload_file'),
    path('__debug__/', include('debug_toolbar.urls')),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += i18n_patterns(
    path('', home, name='home')
)