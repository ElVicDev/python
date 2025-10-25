""" Día 98: API C
Estudie la API C de Python y los módulos de extensión. """

import ctypes
# Definir una función C simple que suma dos enteros
c_code = """
#include <Python.h>
static PyObject* add(PyObject* self, PyObject* args) {
    int a, b;
    if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
        return NULL;
    }
    return PyLong_FromLong(a + b);
}
static PyMethodDef MyMethods[] = {
    {"add", add, METH_VARARGS, "Suma dos enteros."},
    {NULL, NULL, 0, NULL}
};
static struct PyModuleDef mymodule = {
    PyModuleDef_HEAD_INIT,
    "mymodule",
    NULL,
    -1,
    MyMethods
};
PyMODINIT_FUNC PyInit_mymodule(void) {
    return PyModule_Create(&mymodule);
}
"""
# Guardar el código C en un archivo temporal
with open("mymodule.c", "w") as f:
    f.write(c_code)
# Compilar el módulo C
import os
os.system("gcc -shared -o mymodule.so -fPIC $(python3-config --cflags) mymodule.c $(python3-config --ldflags)")
# Cargar el módulo C compilado
mymodule = ctypes.CDLL("./mymodule.so")
# Llamar a la función add del módulo C
result = mymodule.add(3, 5)
print(f"Resultado de la suma desde el módulo C: {result}")
""" Resultados esperados:
El programa imprimirá el resultado de la suma de dos enteros (3 + 5 = 8)
utilizando una función definida en un módulo C. """
# Nota: Este código demuestra cómo crear y utilizar un módulo de extensión C
# en Python. Asegúrese de tener un compilador C instalado para ejecutar este código.
# Puede ejecutar este código en cualquier entorno Python con soporte para C.
# Limpieza del archivo temporal
os.remove("mymodule.c")
os.remove("mymodule.so")