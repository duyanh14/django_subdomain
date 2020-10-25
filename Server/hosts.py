from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', 'Server.urls_www', name='www'),
    host(r'api', 'Server.urls_api', name='api'),
)