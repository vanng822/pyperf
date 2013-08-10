#include <Python.h>
#include "soe.c"

static PyObject* _find(PyObject* self, PyObject* args) {
	int n;
	if (!PyArg_ParseTuple(args, "i", &n))
		return NULL;

    return Py_BuildValue("i", find(n));
}

static PyMethodDef methods[] = {
    {"find", _find, METH_VARARGS, "c sieve of eratosthenes"},
    {NULL, NULL, 0, NULL}
};


PyMODINIT_FUNC
initcsoe(void)
{
    (void) Py_InitModule("csoe", methods);
}
