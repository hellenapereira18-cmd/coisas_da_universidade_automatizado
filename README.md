# coisas_da_universidade_automatizado
Desafio 4 da trilha de python. 
Esse projeto foi desenvolvido em Python com o objetivo de automatizar o gerenciamento de diretórios vazios em um repositório git. Como git não versiona diretórios vazios, é necessário utilizar um arquivo chamado 
.gitkeep para permitir que esses diretórios sejam armazenados no repositório. O programa percorre todos os diretórios do projeto e realiza automaticamente a criação ou remoção desse arquivo conforme necessário. 
O programa percorre todos os diretórios do repositório utilizando a função os.walk().
Durante a execução são aplicadas as seguintes regras: 
Se um diretório não possuir arquivos nem subdiretórios, o programa cria um arquivo. gitkeep, caso ele ainda exista.
Se um diretório possuir arquivos ou subdiretórios, o arquivo.gitkeep não deve existir. Caso seja encontrado, ele será removido. 
O diretório logs é ignorado durante a verificação e não sofre alterações. 
Ao final da execução. o programa cria um arquivo log.json dentro do diretório logs. 
Nesse arquivo são armazenadas as seguintes informações:
Data e hora da execução.
Lista de arquivos .gitkeep criados.
Lista de arquivos .gitkeep removidos. 
os - responsável pela navegação entre diretórios, criação e remoção de arquivos,
json - armazena os registros de execução no formato JSON. 
datetime - utilizada para registrar a data e o horário de cada execução do programa. 
diretorio_vazio()
Verifica se um diretório está vazio. 
registrar_logs()
Cria ou atualiza o arquivo log.json contendo o histórico da execução. 
RESPOSTA AS PERGUNTAS TEÓRICAS:
json.dump() grava os dados diretamente em um arquivo JSON. Já o jso.dumps() converte os dados para uma string JSON. 
E o jso.load() lê dados JSON a partir de um arquivo, enquanto o arquivo json.loads() converte uma string JSON em um objeto Python.
