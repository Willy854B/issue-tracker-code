from django.conf.urls import url, include
from .views import all_tickets, single_ticket, add_ticket, add_feature, add_comment


urlpatterns = [
    url(r'^$', all_tickets, name='tickets'),
    url(r'^(?P<ticket_id>\d+)/$', single_ticket, name='ticket'),
    url(r'^add_ticket/$', add_ticket, name='add_ticket'),
    url(r'^add_feature/$', add_feature, name='add_feature'),
    url(r'^(?P<ticket_id>\d+)/comment/$', add_comment, name='add_comment'),
]