**导出虚拟环境**

```
conda env export > environment.yml    导出当前虚拟环境的配置到一个YAML文件
conda env create -f environment.yml   根据YAML文件创建虚拟环境
```



**查看配置**

```shell
config --show
```



**更改默认命令行执行python时默认的python版本(对应的虚拟环境)**

把python.exe所在在的文件夹加入path中即可





