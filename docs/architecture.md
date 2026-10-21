# Arquitetura

## Visão de componentes

```mermaid
flowchart LR
    clientes([Clientes])
    subgraph demo-service [demo-service · FastAPI]
        api[Rotas HTTP<br/>app/main.py]
        repo[Repositório]
        api --> repo
    end
    mem[(Armazenamento<br/>em memória)]

    clientes -- HTTP/JSON --> api
    repo --> mem
```

| Componente | Responsabilidade |
|------------|------------------|
| `app/main.py` | Rotas HTTP, validação de entrada (Pydantic) |
| Repositório em memória | Armazena itens durante a vida do processo |

## Fluxo: criar um item

```plantuml
@startuml
actor Cliente
participant "demo-service\n(FastAPI)" as API
database "Memória" as DB

Cliente -> API : POST /items {name, quantity}
API -> API : valida com Pydantic
alt payload inválido
  API --> Cliente : 422 Unprocessable Entity
else payload válido
  API -> DB : salva item
  API --> Cliente : 201 Created {id, name, quantity}
end
@enduml
```

## Dependências

- **Upstream**: nenhuma.
- **Downstream**: qualquer cliente HTTP que consuma a `demo-api`.

## Decisões relevantes

- [ADR 0001: escolha do FastAPI](adr/0001-escolha-fastapi.md)

!!! warning "Limitação conhecida"
    O armazenamento é em memória: os dados se perdem a cada restart. É intencional nesta PoC.
