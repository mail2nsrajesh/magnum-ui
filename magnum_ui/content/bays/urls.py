#  Copyright 2015 Cisco Systems
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from django.conf.urls import include
from django.conf.urls import url
from magnum_ui.content.bays.containers import urls as containers_urls
from magnum_ui.content.bays.views import IndexView


urlpatterns = [
    url(r'^containers/', include(containers_urls, namespace='containers')),
    url(r'^[0-9a-f\-]{36}$', IndexView.as_view(), name='detail'),
    url(r'^$', IndexView.as_view(), name='index'),
]