# 📘 Assignment: Testing FastAPI Applications with pytest

## 🎯 Objective

Escreva testes unitários para a lógica de gerenciamento de tarefas e testes de integração para os endpoints de uma API FastAPI. Use `pytest` e `TestClient` para verificar respostas válidas, erros HTTP e isolamento entre testes.

## 📝 Tasks

### 🛠️ Prepare the Test Environment

#### Descrição
Instale `fastapi`, `pytest` e `httpx`. Use o arquivo `starter-code.py` como aplicação sob teste e crie uma suíte chamada `test_tasks.py`. Como o nome do arquivo contém hífen, carregue-o com `importlib.import_module("starter-code")` e configure o `TestClient` do FastAPI com `starter_code.app`.

#### Requisitos
A suíte de testes deve:

- Executar com `python -m pytest -v`
- Usar uma fixture para restaurar `tasks` e `next_task_id` antes e depois de cada teste
- Manter os testes independentes, sem depender da ordem em que o pytest os executa


### 🛠️ Test the Task Management Logic

#### Descrição
Escreva testes unitários para as funções que localizam, criam, atualizam e removem tarefas. Teste tanto os resultados válidos quanto a exceção lançada quando uma tarefa não existe.

#### Requisitos
Os testes unitários devem:

- Confirmar que a busca retorna a tarefa com o ID solicitado
- Confirmar que uma busca por ID inexistente lança `HTTPException` com status `404`
- Confirmar que criar tarefas atribui IDs únicos e atualiza a coleção
- Confirmar que atualizar altera o título e o estado `completed`
- Confirmar que remover exclui a tarefa da coleção


### 🛠️ Verify the HTTP API Contract

#### Descrição
Use `TestClient` para testar as rotas como um cliente HTTP. Cubra o fluxo CRUD e as respostas para dados inválidos ou IDs que não existem; use `pytest.mark.parametrize` para evitar duplicar testes de casos equivalentes.

#### Requisitos
Os testes de integração devem:

- Verificar `GET /tasks` e `GET /tasks/{task_id}` com status `200` e os dados esperados
- Verificar `POST /tasks` com status `201`, além de `PUT /tasks/{task_id}` e `DELETE /tasks/{task_id}` com os status correspondentes
- Confirmar status `404` ao atualizar, consultar ou remover um ID inexistente
- Confirmar status `422` para um corpo de requisição inválido
- Confirmar status `204` e corpo vazio ao remover uma tarefa existente
