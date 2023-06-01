# Como executar:

## Crie um ambiente virtual com venv
Caso não tenha o venv instalado você pode fazer isso com:
~~~ bash
sudo apt install python3-venv
~~~
> **atenção:** Apenas em distros debian-based!

Crie o ambiente virtual:
~~~ bash
python3 -m venv venv
~~~
> o segundo ***venv*** é o nome do nosso ambiente, para saber mais você pode procurar informações [aqui](https://docs.python.org/pt-br/3/library/venv.html). 

Ative o ambiente com:

~~~ bash 
source venv/bin/activate
~~~
> você perceberá que no terminal agora aparece algo como: **(venv)** usuário@máquina:

## Instalando as dependências

para instalar as dependências nós iremos utilizar o **pip**

~~~ bash
pip install -r requirements.txt
~~~
após isso estamos preparados para rodar nosso código! (ou quase isso por enquanto)

## Arquivos importantes:
- **function.py**: guarda todas as funções de coleta
- **main.ipynb**: notebook para testes (evitar escrever funções nele)

Ainda estou resolvendo bugs, então o código não está funcionando 100%