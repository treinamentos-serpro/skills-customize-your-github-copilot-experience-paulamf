# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construa uma API REST para gerenciar tarefas usando FastAPI. Você vai praticar rotas HTTP, modelos de dados, operações CRUD e respostas de erro para recursos que não existem.

## 📝 Tasks

### 🛠️ Implementar a leitura de tarefas

#### Descrição
Use o starter code para iniciar a API e implemente a rota que busca uma tarefa pelo ID. A rota de listagem já está pronta. Instale as dependências com `python -m pip install fastapi uvicorn` e execute o servidor com `uvicorn starter-code:app --reload`.

#### Requisitos
O programa concluído deve:

- Retornar uma tarefa específica em `GET /tasks/{task_id}` quando o ID existir
- Responder com status `404` quando o ID não corresponder a nenhuma tarefa
- Exibir a documentação interativa da API em `/docs`


### 🛠️ Criar tarefas pela API

#### Descrição
Adicione uma rota para criar tarefas. Cada nova tarefa deve receber um ID único e começar com `completed` igual a `false`.

#### Requisitos
O programa concluído deve:

- Aceitar um título no corpo JSON de `POST /tasks`
- Adicionar a nova tarefa à lista em memória e retornar a tarefa criada
- Responder com status `201` e não reutilizar IDs já atribuídos


### 🛠️ Atualizar e remover tarefas

#### Descrição
Complete as operações CRUD implementando a atualização e a remoção de tarefas existentes. Use a documentação em `/docs` para testar cada operação.

#### Requisitos
O programa concluído deve:

- Atualizar título e estado `completed` com `PUT /tasks/{task_id}`
- Remover uma tarefa com `DELETE /tasks/{task_id}`
- Responder com status `404` ao tentar atualizar ou remover uma tarefa inexistente
- Permitir testar o fluxo completo: criar, listar, consultar, atualizar e remover tarefas