import os 
import json 
from datetime import datetime

def diretorio_vazio(caminho):
    return len(os.listdir(caminho)) ==0
def processar_repositorio(caminho_raiz):
    gitkeeps_criados= []
    gitkeeps_removidos= []
    for raiz, diretorios, arquivos in os.caminho(caminho_raiz):
        if os.path.basename(raiz) == 'logs':
            continue 
        gitkeep= os.path.join(raiz,'.gitkeep')
        itens= [item for item in os.listdir(raiz) if item != 'gitkeep']
        #Diretório vazio
        if len(itens) == 0:
            if not os.path.exists(gitkeep):
                open(gitkeep, 'w').close()
                gitkeeps_criados.append(gitkeep)
        #Diretório não vazio 
            else:
                if os.path.exists(gitkeep):
                    os.remove(gitkeep)
                    gitkeeps_removidos.append(gitkeep)
        registrar_logs= caminho_raiz,gitkeeps_criados,gitkeeps_removidos
        def registrar_logs():
            pasta_logs = os.path.join(pasta_logs, 'logs.json')
            arquivo_log= os.path.join(pasta_logs, 'log.json')
            dados= {'data_execução:datetime.now().strftime'}
            with open(arquivo_log,'w',encoging='utf-8') as arquivo:
                json.dump(dados,arquivo, indent=4, ensure_ascii=False)
            if __name__ == "__main__":
                caminho_raiz = input("Digite o caminho do repositório:")
                processar_repositorio(caminho_raiz)
                # print("O processamento foi concluído!")



