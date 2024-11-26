# Documentação do Projeto: Sistema de Gestão de Alvos

Este é um projeto Django com integração ao PostgreSQL para gerenciamento de alvos. A aplicação oferece uma API para manipulação de dados, inclui um painel de administração via Django Admin e teste unitários.

![Home screen](https://i.imgur.com/lTexAgW.png)

## Sumário

- [Descrição do Projeto](#descrição-do-projeto)
- [Pré-requisitos](#pré-requisitos)
- [Iniciando o Projeto](#iniciando-o-projeto)
  - [Passo 1: Clonando o Repositório](#passo-1-clonando-o-repositório)
  - [Passo 2: Configurando o Docker](#passo-2-configurando-o-docker)
  - [Passo 3: Rodando o Projeto](#passo-3-rodando-o-projeto)
- [API: Endpoints](#api-endpoints)
  



---

## Descrição do Projeto

Este projeto foi desenvolvido para gerenciar informações de "alvos". Ele é composto por:

- Um **back-end** construído com **Django** e exposto via uma API com operações de CRUD.
- O **banco de dados PostgreSQL** roda em um container Docker, permitindo fácil escalabilidade e portabilidade.
- O projeto inclui um painel de administração Django para gerenciamento de alvos e usuários.

---

## Pré-requisitos

Antes de começar, você precisa ter as seguintes ferramentas instaladas no seu sistema:

- **Docker**: Para rodar os containers e o banco de dados.
- **Docker Compose**: Para orquestrar a criação e o gerenciamento dos containers.
- **Python 3.x**: Para rodar o Django e a aplicação localmente.
- **Git**: Para clonar o repositório do projeto.

---

## Iniciando o Projeto

### Passo 1: Clonando o Repositório

Clone o repositório com o seguinte comando:

```bash
git clone <URL_DO_REPOSITORIO>
cd <PASTA_DO_REPOSITORIO>
```

### Passo 2: Configurando o Docker

Este projeto usa Docker para configurar a infraestrutura de banco de dados. Antes de rodar a aplicação, você precisa construir e rodar os containers Docker.


1. **Criar a rede do Docker e os containers**:
   No diretório raiz do projeto, rode o comando:
    ```bash
   docker-compose up --build
   ```
   Isso irá construir as imagens do Docker e iniciar os containers de banco de dados PostgreSQL e Django

2. **Verificar se os containers estão rodando**:
   Para garantir que tudo foi configurado corretamente, execute o comando:
    ```bash
   docker ps
   ```

### Passo 3: Rodando o Projeto
Depois que os containers estiverem rodando, a aplicação Django estará disponível em **http://localhost:8000**. 

O Docker também estará configurado para persistir o banco de dados no volume postgres_data, garantindo que os dados não sejam perdidos quando os containers forem reiniciados ou apagados.

---

## api endpoints

Base URL: http://127.0.0.1:8000/api/alvos/

Admin url: http://127.0.0.1:8000/admin/

(login: admin password: hOfYDKspW1ecZ2Y)

Campos dos Alvos
Abaixo está a estrutura dos objetos de alvo:
```json
[
    {
        "id": int,
        "nome": string,
        "latitude": float,
        "longitude": float,
        "identificador": string,
        "data_expiracao": datetime
    }
]
```
Operações Disponíveis
1.  **Listar Todos os Alvos (GET)**

    Descrição: Retorna uma lista de todos os alvos cadastrados.

2. **Criar um Novo Alvo (POST)**

    Descrição: Permite criar um novo alvo.

3. **Atualizar um Alvo Existente (PUT)**

    Descrição: Atualiza um alvo existente pelo ID.

4. **Excluir um Alvo (DELETE)**

    Descrição: Exclui um alvo existente pelo ID.