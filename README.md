# clonar repositorio pela primeira vez
```bash
git clone https://kaiomudkt:COLOCA_SEU_TOKEN@github.com/kaiomudkt/tensorflow.git
```

# tensorflow

estudando tensorflow

# Ambiente Docker com Jupyter e GitHub
exemplo de arquivo docker-compose.yml já configurado

txt
version: '3'

services:
  jupyter:
    image: quay.io/jupyter/scipy-notebook:2024-03-14
    container_name: jupyter
    ports:
      - 8888:8888
    volumes:
       - .:/home/jovyan
    environment:
      - .env
    command: >
      /bin/bash -c "
      if [ ! -d /home/jovyan/inteligencia_artificial/.git ]; then
          git config --global user.name ${GITHUB_USERNAME} &&
          git config --global user.email ${GITHUB_USEREMAIL} &&
          git config --global credential.helper store &&
          git clone https://${GITHUB_USER}:${GITHUB_TOKEN}${GITHUB_REPO}
      fi &&
      jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root
      "


* desta forma temos um arquivo docker-compose.yml, onde ter um serviço baseado na imagem jupyter quay.io, 
onde executa na porta 8888. 
* no "comand" é clonado o repositorio github
* "volumes" é mapeado um diretorio dentro do seu computador que correponde ao mesmo diretorio dentro do container, ou seja é compartilhado, assim quando desligar o container não irá perder os arquivos salvos no HD
    * obs: . (ponto) representa diretorio corrente, então a partir do diretorio corrente mapeia o diretorio "jupter"
* e dentro do diretorio "./jupyter/inteligencia_artificial/" está o repositório git clonado
* autenticação github por "Personal access tokens" (Tokens de acesso pessoal)
