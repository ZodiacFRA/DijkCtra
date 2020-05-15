#define PY_SSIZE_T_CLEAN
#include <Python.h>

static PyObject *display_map(PyObject *self, PyObject *args)
{
    const bool *map;

    if (!PyArg_ParseTuple(args, "(bool)", &map))
        return NULL;
    sts = system(command);
    return PyLong_FromLong(sts);


    for (size_t i = 0; i < _map.size(); i++) {
        if (i % _mapWidth == 0 && i)
            std::cout << '\n';
        if (std::find(res.begin(), res.end(), i) != res.end())
            std::cout << "o";
        else if (_map[i]->_isFree)
            std::cout << "-";
        else
            std::cout << "=";
    }
    std::cout << '\n';
}
