# IBM_python-full-stack

Ejercicio práctico del curso Python full stack

Alumno: Antonio Javier García Martínez (cokesaeba@gmail.com)

Repositorio: https://github.com/cokesaeba/IBM_python-full-stack


Resultado pruebas unitarias:

<code>
pytest -v
=========================================================== test session starts ===========================================================
platform darwin -- Python 3.10.7, pytest-7.4.0, pluggy-1.2.0 -- /Library/Frameworks/Python.framework/Versions/3.10/bin/python3
cachedir: .pytest_cache
rootdir: /Users/ajgarciam/Library/CloudStorage/Dropbox/Mac/Downloads/CURSOS/IBM/matriz
plugins: anyio-3.7.0
collected 8 items

test_matriz_NxN.py::test_create_matriz PASSED                                                                                       [ 12%]
test_matriz_NxN.py::test_create_matriz_nula PASSED                                                                                  [ 25%]
test_matriz_NxN.py::test_suma_filas[matriz0-expected0] PASSED                                                                       [ 37%]
test_matriz_NxN.py::test_suma_filas[matriz1-expected1] PASSED                                                                       [ 50%]
test_matriz_NxN.py::test_suma_filas[matriz2-expected2] PASSED                                                                       [ 62%]
test_matriz_NxN.py::test_suma_columnas[matriz0-expected0] PASSED                                                                    [ 75%]
test_matriz_NxN.py::test_suma_columnas[matriz1-expected1] PASSED                                                                    [ 87%]
test_matriz_NxN.py::test_suma_columnas[matriz2-expected2] PASSED                                                                    [100%]

============================================================ 8 passed in 0.01s ============================================================
</code>
