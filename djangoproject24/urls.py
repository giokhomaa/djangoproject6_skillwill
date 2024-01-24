from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view

urlpatterns = [

    path("api_schema/", get_schema_view(
        title = "SkillWill API schema",
        description = "API schema for our API",
    ), name = "api_schema"),

    path('admin/', admin.site.urls),
    path('api/', include('note.urls'))
]
