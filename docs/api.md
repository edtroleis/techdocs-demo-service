# API

A especificação completa está em `openapi.yaml` e também aparece na entidade
**demo-api** do catálogo (aba *Definition*).

## Endpoints

| Método | Caminho | Descrição |
|--------|---------|-----------|
| `GET` | `/health` | Health check |
| `GET` | `/items` | Lista os itens |
| `POST` | `/items` | Cria um item |
| `GET` | `/items/{id}` | Busca um item pelo id |

## Exemplos

### Criar item

```bash
curl -X POST http://localhost:8080/items \
  -H 'Content-Type: application/json' \
  -d '{"name": "caneta", "quantity": 3}'
```

```json
{"id": 1, "name": "caneta", "quantity": 3}
```

### Buscar item inexistente

```bash
curl -i http://localhost:8080/items/999
```

```text
HTTP/1.1 404 Not Found
{"detail": "item not found"}
```
