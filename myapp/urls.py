from django.conf.urls import url
from myapp.views import home, roulette, loading, l_out, quiz, postanswer

urlpatterns = [
    url(r'^$', home, name='myapp-home'),
    url(r'^loading$', loading, name='myapp-load'),
    url(r'^roulette$', roulette, name='myapp-roulette'),
    url(r'^(?P<filename>[^/]+)/$', quiz, name='myapp-quiz'),
    url(r'^(?P<filename>[^/]+)/post/$', postanswer, name='myapp-post'),
    url(r'^logout$', l_out, name='myapp-logout')
]
