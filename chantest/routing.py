from channels.routing import route
from channels import include

channel_routing = [
    include('chtest.routing.datastream', path=r'^/datastream/')
]
