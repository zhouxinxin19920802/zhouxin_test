
# Python tips
-------------------
![python图灵书单](./img/python图灵书单.png)

#### 1. python通过MingW调用C/C++, 编写C/C++,用gcc或者g++调用生成dll文件，通过ctypes包进行调用，代码示例如下:
python代码:
``` python
import ctypes
dll = ctypes.CDLL('test.dll',winmode=0) #加载动态链接库
f=dll.add #提取函数
f.argtypes=[ctypes.c_double,ctypes.c_double] #定义参数类型
f.restype=ctypes.c_double #定义函数返回值类型
cons = f(2.5,3.5) #计算
print(cons)
```
cpp代码:
```c
extern "C" {
	__declspec(dllexport) double add(double x,double y);
}

double add(double x,double y){
	return x+y;
}
```
gcc的编译代码:
```shell
g++ -shared -Wl,--kill-at,--output-def,test.def -o test.dll test.cpp
```

#### 2.Python的C扩展可以用ctypes可以利用python.h的头文件，举例如下：
``` C
#include <Python.h>

// 扩展函数
static PyObject* add_numbers(PyObject* self, PyObject* args) {
    int num1, num2, result;

    // 解析参数
    if (!PyArg_ParseTuple(args, "ii", &num1, &num2)) {
        return NULL;
    }

    // 执行计算
    result = num1 + num2;

    // 将结果转换为Python对象并返回
    return Py_BuildValue("i", result);
}

// 扩展模块定义
static PyMethodDef ExampleMethods[] = {
    {"add_numbers", add_numbers, METH_VARARGS, "Add two numbers."},
    {NULL, NULL, 0, NULL}  // 结束标记
};

// 扩展模块初始化函数
static struct PyModuleDef examplemodule = {
    PyModuleDef_HEAD_INIT,
    "example",   // 模块名
    NULL,        // 模块文档
    -1,          // 模块状态
    ExampleMethods
};

// 扩展模块初始化
PyMODINIT_FUNC PyInit_example(void) {
    return PyModule_Create(&examplemodule);
}
```
然后通过:
``` shell
gcc -shared -o example.so example.c -I /usr/include/python3.x/
```
编译成功后，将生成一个名为example.so的共享库文件，导入即可使用。