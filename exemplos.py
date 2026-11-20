"""Todos os exemplos do guia de Python Avançado. Rode: python exemplos.py"""
import time
from contextlib import contextmanager
from dataclasses import dataclass, field
from functools import wraps


# 1. Comprehensions
quadrados = [n ** 2 for n in range(5)]
pares = {n for n in range(10) if n % 2 == 0}
precos = {"pão": 1.5, "café": 8.0}
com_imposto = {k: round(v * 1.1, 2) for k, v in precos.items()}
print("1 →", quadrados, pares, com_imposto)


# 2. *args e **kwargs
def registrar(*args, **kwargs):
    print("2 →", args, kwargs)


registrar(1, 2, nivel="INFO")


# 3. Decorator
def cronometro(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.perf_counter()
        resultado = func(*args, **kwargs)
        print(f"3 → {func.__name__} levou {time.perf_counter() - inicio:.4f}s")
        return resultado
    return wrapper


@cronometro
def processar():
    return sum(range(1_000_000))


processar()


# 4. Generator
def ler_em_lotes(itens, tamanho):
    for i in range(0, len(itens), tamanho):
        yield itens[i:i + tamanho]


print("4 →", list(ler_em_lotes(list(range(10)), 3)))


# 5. Context manager
@contextmanager
def conexao_fake():
    print("5 → abrindo")
    yield "conexão"
    print("5 → fechando")


with conexao_fake() as c:
    print("5 → usando", c)


# 6. Dataclass
@dataclass
class Pedido:
    id: int
    cliente: str
    itens: list[str] = field(default_factory=list)


print("6 →", Pedido(1, "Ana"))


# 7. Type hints
def total(valores: list[float], desconto: float = 0.0) -> float:
    return sum(valores) * (1 - desconto)


print("7 →", total([10.0, 20.0], 0.1))


# 8. Funções como objetos
operacoes = {"soma": lambda a, b: a + b, "mult": lambda a, b: a * b}
print("8 →", operacoes["mult"](3, 4), sorted(["banana", "kiwi", "uva"], key=len))
