Como baixar:
$ git clone https://github.com/inzpiron/PIM_fingerprint

$ cd PIM_fingerprint

Modo de usar  o makefile (main.py):

$ python2 main.py {arg1} {arg2} {salvar | buscar} {arg3}
arg1: É o tipo da imagem, no caso, o tipo das imagens que estão na pasta 'img' são jpg.
arg2: É o nome da imagem.
arg3: É o nome da pessoa, é utilizado somente quando o argumento anterior for 'salvar'.

Exemplos:

$ python2 main.py jpg digital salvar leonardo
$ python2 main.py jpg digital1 salvar ariel
$ python2 main.py jpg digital3 salvar rogerio

Exemplos de busca no BD:

$ python2 main.py jpg digital3- buscar

Outras informações:

As imagens normalizadas ficarão em uma pasta com o nome 'img*'.
Necessário usar python2, e ter instalado as bibliotecas 'scipy', 'numpy', 'matplotlib'.
Quando usado o argumento 'salvar', será ilustrado o mapa de orientações da digita.
Quando usado o argumento 'buscar', será informado uma lista, referente ao banco de dados, da digital mais para menos semelhante da digital analisada.

