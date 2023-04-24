
# Python tips
-------------------
![python图灵书单](./img/python图灵书单.png)

1. python通过MingW调用C/C++, 编写C/C++,用gcc或者g++调用生成dll文件，通过ctypes包进行调用，代码示例如下:
``` python
import ctypes
dll = ctypes.CDLL('test.dll',winmode=0) #加载动态链接库
f=dll.add #提取函数
f.argtypes=[ctypes.c_double,ctypes.c_double] #定义参数类型
f.restype=ctypes.c_double #定义函数返回值类型
cons = f(2.5,3.5) #计
print(cons)
```

