# LDAP

## Commands

#### ldapsearch
#### ldapadd
    python manage.py ldapadd cn=user1,ou=People,dc=lazyarea,dc=com \
    'top','account','posixAccount','shadowAccount','ldapPublicKey'
    '{"uid":"usr1","gidNumber":"1101","homeDirectory":"/home/usr1","userPassword":"passwd","uidNumber":1101,"sshPublicKey":"aaa"}'

    python manage.py ldapadd cn=gr1,ou=Group,dc=lazyarea,dc=com \
    'posixGroup','top'  '{"cn":"gr1","gidNumber":11000}'

