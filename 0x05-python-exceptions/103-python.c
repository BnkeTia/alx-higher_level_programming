#define PY_SSIZE_T_CLEAN
#include <Python.h>


/**
 * print_python_list - A function that prints some basic info about
 * python lists.
 * @p: a pointer to an object to be compared
 * Return: void
 */
void print_python_list(PyObject *p)
{
	if (!PyList_Check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - A function that prints some basic info about
 * python bytes..
 * @p: a pointer to an object to be compared
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}
	Py_ssize_t size = PyBytes_GET_SIZE(p);
	Py_ssize_t display_size = (size > 10) ? 10 : size;

	printf("[.] Size of the Python Bytes = %ld\n", size);
	printf("[. ]Trying string: %s\n", PyBytes_AsString(p));
	printf("[*] First %ld bytes: ", display_size);
	for (Py_ssize_t i = 0; i < display_size; i++)
	{
		printf("%02x", (unsigned char)PyBytes_AsString(p)[i]);
		if (i + 1 < display_size)
			printf(" ");
	}
	printf("\n");
}
/**
 * print_python_float - A function that prints some basic info about
 * python float objects.
 * @p: a pointer to an object to be compared
 * Return: void
 */
void print_python_float(PyObject *p)
{
	if (!PyFloat_Check(p))
	{
		printf("[ERROR] Invalid Float Object\n");
		return;
	}
	printf("[.] Float object info\n");
	printf(" value: %.17g\n", ((PyFloatObject *)p)->ob_fval);
}
