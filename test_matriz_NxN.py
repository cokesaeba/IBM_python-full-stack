from matriz_NxN import print_matriz, create_matriz, suma_filas, suma_columnas
import pytest

# Comprobamos que se crea una matriz de NxN
def test_create_matriz():
    N = 3
    matriz = create_matriz(N)
    assert len(matriz) == N
    for i in range(N):
        assert len(matriz[i]) == N

# Comprobamos que N debe ser > 0 (si no, debería haber una excepción de ValueError)
def test_create_matriz_nula():
    N = 0
    AssertionError("N debe ser mayor que 0")
    with pytest.raises(ValueError):
        matriz = create_matriz(N)

# Testamos casos tipo a ver si el resultado coincide con lo esperado 
@pytest.mark.parametrize("matriz, expected", 
[
    ([[0]], [0]),
    ([[9, 5], [5, 8]], [14, 13]),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [6, 15, 24])
])
def test_suma_filas(matriz, expected):
    assert suma_filas(matriz) == expected

@pytest.mark.parametrize("matriz, expected",
[
    ([[0]], [0]),
    ([[9, 5], [5, 8]], [14, 13]),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [12, 15, 18])
])
def test_suma_columnas(matriz, expected):
    assert suma_columnas(matriz) == expected
