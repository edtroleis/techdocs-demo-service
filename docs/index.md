# Demo Service

O **demo-service** expõe uma API REST simples de itens. Ele existe para demonstrar como a
documentação de um serviço aparece na aba **Docs** da página do componente no Backstage.

| | |
|---|---|
| **Owner** | `platform-team` |
| **System** | `demo-system` |
| **API** | `demo-api` (OpenAPI) |
| **Linguagem** | Python 3.14 / FastAPI |
| **Lifecycle** | experimental |

!!! info "Golden path"
    Este serviço segue o [Golden Path de Arquitetura](http://localhost:3000/docs/default/component/wiki-golden-path).
    Em caso de dúvida sobre estrutura, CI/CD ou observabilidade, consulte-o primeiro.

## Como rodar localmente

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r app/requirements.txt
uvicorn app.main:app --reload --port 8080
```

Depois acesse <http://localhost:8080/docs> para a UI do Swagger.

## Próximos passos

- [Arquitetura](architecture.md): componentes e dependências.
- [API](api.md): endpoints e exemplos.
- [Runbook](runbook.md): operação, alertas e troubleshooting.
