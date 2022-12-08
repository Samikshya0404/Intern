from todo_app.views import StaticView
from django.conf.urls import patterns

urlpatterns = patterns("todo_app.views", (r'^static/$', StaticView.as_view()),)