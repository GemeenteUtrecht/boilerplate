Apache + mod-wsgi configuration
===============================

An example Apache2 vhost configuration follows::

    WSGIDaemonProcess boilerplate-<target> threads=5 maximum-requests=1000 user=<user> group=staff
    WSGIRestrictStdout Off

    <VirtualHost *:80>
        ServerName my.domain.name

        ErrorLog "/srv/sites/boilerplate/log/apache2/error.log"
        CustomLog "/srv/sites/boilerplate/log/apache2/access.log" common

        WSGIProcessGroup boilerplate-<target>

        Alias /media "/srv/sites/boilerplate/media/"
        Alias /static "/srv/sites/boilerplate/static/"

        WSGIScriptAlias / "/srv/sites/boilerplate/src/boilerplate/wsgi/wsgi_<target>.py"
    </VirtualHost>


Nginx + uwsgi + supervisor configuration
========================================

Supervisor/uwsgi:
-----------------

.. code::

    [program:uwsgi-boilerplate-<target>]
    user = <user>
    command = /srv/sites/boilerplate/env/bin/uwsgi --socket 127.0.0.1:8001 --wsgi-file /srv/sites/boilerplate/src/boilerplate/wsgi/wsgi_<target>.py
    home = /srv/sites/boilerplate/env
    master = true
    processes = 8
    harakiri = 600
    autostart = true
    autorestart = true
    stderr_logfile = /srv/sites/boilerplate/log/uwsgi_err.log
    stdout_logfile = /srv/sites/boilerplate/log/uwsgi_out.log
    stopsignal = QUIT

Nginx
-----

.. code::

    upstream django_boilerplate_<target> {
      ip_hash;
      server 127.0.0.1:8001;
    }

    server {
      listen :80;
      server_name  my.domain.name;

      access_log /srv/sites/boilerplate/log/nginx-access.log;
      error_log /srv/sites/boilerplate/log/nginx-error.log;

      location /500.html {
        root /srv/sites/boilerplate/src/boilerplate/templates/;
      }
      error_page 500 502 503 504 /500.html;

      location /static/ {
        alias /srv/sites/boilerplate/static/;
        expires 30d;
      }

      location /media/ {
        alias /srv/sites/boilerplate/media/;
        expires 30d;
      }

      location / {
        uwsgi_pass django_boilerplate_<target>;
      }
    }
