import subprocess
import sys

# Função para instalar pacotes usando pip
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Instalar o pacote ucimlrepo
install('ucimlrepo')

from ucimlrepo import fetch_ucirepo

doenca_cardiaca = fetch_ucirepo(id=45)
print('Variáveis disponíveis no dataset de doenças cardíacas da UCI:')
doenca_cardiaca.variables   # exibe as variaveis do dataset importado

X = doenca_cardiaca.data.features
X = X[['age', 'chol', 'cp']]
X.head()