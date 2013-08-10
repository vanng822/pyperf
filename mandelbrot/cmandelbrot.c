#include <Python.h>
#include "mandelbrot.c"

static PyObject* mandelbrot(PyObject* self, PyObject* args) {
	draw();
    return Py_BuildValue("i", 0);
}

static PyMethodDef methods[] = {
    {"draw", mandelbrot, METH_VARARGS, "Fractal - Mandelbrot"},
    {NULL, NULL, 0, NULL}
};


PyMODINIT_FUNC
initcmandelbrot(void)
{
    (void) Py_InitModule("cmandelbrot", methods);
}
