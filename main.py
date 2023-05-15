# coding: utf-8

#!/usr/bin/env python3
import importlib
math = importlib.import_module('math')
print(math.sin(2))

mod = importlib.import_module('urllib.request')
u = mod.urlopen('http://www.python.org')
print(u)