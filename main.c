#include <Python.h>

#define THE_FILE "main.py"

int main(int argc, char* argv[])
{
    FILE* fp;
    int res;
    Py_Initialize();
    PyRun_SimpleString("import sys; sys.path.insert(0, '');");
    fp = fopen(THE_FILE, "r");
    if (!fp)
        return 1;
    while (1) {
        res = PyRun_SimpleFile(fp, THE_FILE);
        if (res != -1)
            break;
        rewind(fp);
    }
    Py_Finalize();
    fclose(fp);
    printf("%d\n", res);
    return 0;
}
