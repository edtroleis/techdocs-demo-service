# Runbook

## Deploy

Nesta PoC não há deploy automatizado. Em produção, o pipeline segue o
[golden path de CI/CD](http://localhost:3000/docs/default/component/wiki-golden-path/ci-cd/).

## Health check

```bash
curl -s http://localhost:8080/health
# {"status":"ok"}
```

## Alertas

| Alerta | Condição | Ação |
|--------|----------|------|
| `DemoServiceDown` | `/health` falha por 2 min | Ver logs; reiniciar o processo |
| `DemoServiceHighLatency` | p95 > 500 ms por 5 min | Verificar carga; escalar réplicas |

## Troubleshooting

??? question "A API responde 404 para itens que acabei de criar"
    O armazenamento é em memória. Se o processo reiniciou, os itens foram perdidos.

??? question "Porta 8080 em uso"
    Rode com outra porta: `uvicorn app.main:app --port 8081`.

## Rollback

Reimplantar a versão anterior da imagem/tag. Não há migração de dados a reverter.
