# Python Avançado

Material gratuito do QG da Engenharia de Dados. Você recebeu porque comentou **AVANCADO**.

## Como usar este material

1. Leia cada tópico abaixo → entenda o conceito
2. Rode [exemplos.py](exemplos.py) → todos os exemplos estão lá funcionando
3. Altere os exemplos → é assim que fixa

```bash
python exemplos.py
```

## 1. Comprehensions

```python
quadrados = [n ** 2 for n in range(5)]                  # lista
pares = {n for n in range(10) if n % 2 == 0}            # set
precos = {"pão": 1.5, "café": 8.0}
com_imposto = {k: v * 1.1 for k, v in precos.items()}   # dicionário
```

## 2. *args e **kwargs

```python
def registrar(*args, **kwargs):
    print(args)    # tupla com os valores sem nome
    print(kwargs)  # dicionário com os valores nomeados

registrar(1, 2, nivel="INFO")
```

## 3. Decorators

Função que envolve outra função para adicionar comportamento.

```python
import time
from functools import wraps

def cronometro(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        print(f"{func.__name__} levou {time.perf_counter() - inicio:.4f}s")
        return resultado
    return wrapper

@cronometro
def processar():
    return sum(range(1_000_000))
```

## 4. Generators

Entregam um item por vez → não carregam tudo na memória.

```python
def ler_em_lotes(itens, tamanho):
    for i in range(0, len(itens), tamanho):
        yield itens[i:i + tamanho]

for lote in ler_em_lotes(list(range(10)), 3):
    print(lote)
```

## 5. Context managers

Abrem e fecham recursos com segurança usando `with`.

```python
from contextlib import contextmanager

@contextmanager
def conexao_fake():
    print("abrindo")
    yield "conexão"
    print("fechando")   # roda mesmo se der erro no bloco

with conexao_fake() as c:
    print("usando", c)
```

## 6. Dataclasses

```python
from dataclasses import dataclass, field

@dataclass
class Pedido:
    id: int
    cliente: str
    itens: list[str] = field(default_factory=list)

p = Pedido(1, "Ana")
print(p)   # Pedido(id=1, cliente='Ana', itens=[])
```

## 7. Type hints

```python
def total(valores: list[float], desconto: float = 0.0) -> float:
    return sum(valores) * (1 - desconto)
```

Ferramentas como `mypy` usam as dicas para achar erros antes de rodar.

## 8. Funções como objetos

```python
operacoes = {"soma": lambda a, b: a + b, "mult": lambda a, b: a * b}
print(operacoes["mult"](3, 4))   # 12
print(sorted(["banana", "kiwi", "uva"], key=len))
```

## QG da Engenharia de Dados

Este material é uma amostra do que você encontra no QG.

→ Trilha completa do zero ao sênior
→ Projetos reais para o portfólio
→ Comunidade para tirar dúvidas

Acesse → [qg-engenharia-de-dados.com.br](https://qg-engenharia-de-dados.com.br)
YouTube → [@gonzagadosdados](https://www.youtube.com/@gonzagadosdados)
