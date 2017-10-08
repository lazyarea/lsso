from django.core.management.base import BaseCommand
import datetime
import json
import re
import logging
import pymysql
from django.conf import settings
from ldap3 import Server, Connection, ALL, NTLM
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "引数で指定した数値の総和を表示します"
    s = Server('localhost', get_info=ALL)

    def add_arguments(self, parser):
        #parser.add_argument('values', nargs='+', type=str)
        parser.add_argument('values', nargs='*', type=str)

    def handle(self, *args, **options):
        dn = options['values'][0]
        objclass = options['values'][1].split(',')
        attr     = json.loads(options['values'][2])
        c  = Connection(settings.LDAP_AUTH_URL, user=settings.LDAP_MANAGER_DN, password=settings.LDAP_AUTH_PASSWD)
        c.bind()
        ret = c.add(dn, objclass, attr)
        c.unbind()
        print(ret)
#        return ret
