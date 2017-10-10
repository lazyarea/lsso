from django.core.management.base import BaseCommand
import datetime
import json
import re
import logging
import pymysql
from django.conf import settings
from ldap3 import Server, Connection, SUBTREE
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "引数で指定した数値の総和を表示します"
    #s = Server('localhost', get_info=ALL)
    s = Server('192.168.56.101')

    def add_arguments(self, parser):
        #parser.add_argument('values', nargs='+', type=str)
        parser.add_argument('values', nargs='*', type=str)

    def handle(self, *args, **options):
        b   = options['values'][0]
        sfilter       = options['values'][1]
        #search_scope = SUBTREE
        attr          = options['values'][2].split(',')
        page        = options['values'][3]
        c  = Connection(settings.LDAP_AUTH_URL, user=settings.LDAP_MANAGER_DN, password=settings.LDAP_AUTH_PASSWD)
        c.bind()
        c.search(search_base = b,
            search_filter = sfilter,
            search_scope = SUBTREE,
            attributes = attr,
            paged_size = page
        )
        print((c.response))
        print(len(c.response))
#        total_entries += len(c.response)
        pass
