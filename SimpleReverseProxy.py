from twisted.Internet import reactor
from twisted.web import proxy, server

site = server.Site(proxy.ReverseProxyResources('www.thehackerway.com', 80, ''))
reactor.listenTCP(8000, site)
reactor.run()