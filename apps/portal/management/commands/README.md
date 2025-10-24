# Script de População e Limpeza do Banco de Dados

## Sumário
- [Descrição Geral](#descrição-geral)
- [Pré-requisitos](#pré-requisitos)
- [Scripts Disponíveis](#scripts-disponíveis)
  - [Script de População do Banco de Dados](#1-script-de-população-do-banco-de-dados-populate_data_devpy)
  - [Script de Limpeza do Banco de Dados](#2-script-de-limpeza-do-banco-de-dados-clear_data_devpy)
  - [Script de Configuração Inicial do Portal](#3-script-de-configuração-inicial-do-portal-portal_seedpy)
- [Aviso](#aviso)

## Descrição Geral

Este documento oferece instruções para a utilização dos scripts que manipulam o banco de dados da aplicação, incluindo a população inicial com dados fictícios, a limpeza segura dos dados e configurações iniciais do portal.

## Pré-requisitos

- O ambiente deve estar configurado em modo DEBUG para evitar execução acidental em produção.

## Scripts Disponíveis

### 1. Script de População do Banco de Dados (`populate_data_dev.py`)

#### Descrição

Popula o banco de dados com dados iniciais, incluindo a criação de gêneros, hierarquias organizacionais, entidades, militares e usuários de teste.

#### Como Executar

Navegue até o diretório raiz do projeto onde o `manage.py` está localizado e execute o comando:

```bash
python manage.py populate_data_dev
```
### 2. Script de Limpeza do Banco de Dados (clear_data_dev.py)

#### Descrição

Deleta todos os registros de modelos especificados de forma segura, tratando as deleções individualmente para evitar erros de integridade.

#### Como Executar

Navegue até o diretório raiz do projeto onde o manage.py está localizado e execute o comando:

```bash
python manage.py clear_data_dev
```
#### Observações

Antes de executar, o script solicitará uma confirmação para prosseguir com a exclusão dos dados. Digite 'yes' para continuar.

### 3. Script de Configuração Inicial do Portal (portal_seed.py)

#### Descrição

Realiza configurações iniciais para o portal, como a criação de grupos essenciais após a instalação.

#### Como Executar

Navegue até o diretório raiz do projeto onde o manage.py está localizado e execute o comando:

```bash
python manage.py portal_seed
```
#### Observações

Este script é utilizado principalmente durante a configuração inicial do projeto ou quando é necessário reconfigurar componentes essenciais do portal.

#### Aviso

Importante: Estes scripts devem somente ser usados em ambientes de desenvolvimento, pois eles modificam diretamente o banco de dados. Nunca execute estes scripts em um ambiente de produção para evitar a perda de dados ou a interrupção do serviço.