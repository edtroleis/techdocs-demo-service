# ADR 0001: Escolha do FastAPI

- **Status:** aceito
- **Data:** 2026-10-21

## Contexto

Precisamos de um framework HTTP em Python, simples, com validação de entrada e
geração de OpenAPI.

## Decisão

Usar **FastAPI** com Pydantic.

## Consequências

- OpenAPI gerado automaticamente, publicado no catálogo como `demo-api`.
- Suporte nativo a async.
- Mais uma dependência a manter atualizada (ver
  [golden path de segurança](http://localhost:3000/docs/default/component/wiki-golden-path/seguranca/)).
