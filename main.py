import sys
from subprocess import call

nomeImg = sys.argv[2]
tipoImg = sys.argv[1]
opc     = sys.argv[3]
if(opc == 'salvar'):
    nome    = sys.argv[4]

print 'Exec cinza.py'
call(['python2','src/cinza.py',tipoImg,nomeImg])
print ''

print 'Exec normaliza.py'
call(['python2','src/normaliza.py',tipoImg,nomeImg])
print ''

print 'Exec orienta.py'
if(opc == 'salvar'):
    call(['python2','src/orienta.py',tipoImg,nomeImg,'salvar',nome])
else:
    call(['python2','src/orienta.py',tipoImg,nomeImg,'buscar'])
