# ex2025_1_PFC-PMPB_Douglas Andrade

Este é um projeto desenvolvido para a pontuação e monitoramento da captura de detentos de uma forma dinâmica.

## Requisitos

Certifique-se de ter os seguintes requisitos instalados:

- Python 3.8.10

## Instalação

1. Clone o repositório:

```bash
git clone https://gitlab.com/repositoriodafabrica/ex2025_1_pfc-pmpb_douglas-andrade.git

cd ex2025_1_pfc-pmpb_douglas-andrade
```

2. Crie e ative um ambiente virtual:
```bash
py -3.8 -m venv venv

.\venv\Scripts\activate
```

3. Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

4. Colete os arquivos estáticos:
```bash
python manage.py collectstatic --noinput
```

5. Aplique as migrações do banco de dados:
```bash
python manage.py makemigrations

python manage.py migrate
```


6. Crie um usuário admin:
```bash
python manage.py createsuperuser
```


7. Inicie o servidor:
```bash
python manage.py runserver
```
