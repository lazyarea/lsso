# LDAP

## Commands

*ldapsearch
* ldapadd
    `python manage.py ldapadd uid=user1,ou=People,dc=lazyarea,dc=com \
'top','account','posixAccount','shadowAccount' \
'{"cn":"usr1","gidNumber":"1101","homeDirectory":"/home/usr1","userPassword":"passwd","uidNumber":1101}'`

