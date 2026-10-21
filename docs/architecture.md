# Arquitetura

## Visão de componentes

```text
┌──────────┐   HTTP/JSON   ┌───────────────┐
│ Clientes │ ────────────▶ │ demo-service  │
└──────────┘               │  (FastAPI)    │
                           │               │
                           │  repositório  │ ──▶ armazenamento em memória
                           └───────────────┘
```

| Componente | Responsabilidade |
|------------|------------------|
| `app/main.py` | Rotas HTTP, validação de entrada (Pydantic) |
| Repositório em memória | Armazena itens durante a vida do processo |

## Dependências

- **Upstream**: nenhuma.
- **Downstream**: qualquer cliente HTTP que consuma a `demo-api`.

## Decisões relevantes

- [ADR 0001: escolha do FastAPI](adr/0001-escolha-fastapi.md)

!!! warning "Limitação conhecida"
    O armazenamento é em memória: os dados se perdem a cada restart. É intencional nesta PoC.
