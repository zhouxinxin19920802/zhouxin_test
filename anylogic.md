# Anylogic 一些常用注意点
---------------------
1.自定义试验的，设置随机发生器代码
```java
    engine.setDefaultRandomGenerator(new Random());
```
上述代码可以设置随机种子，使自带随机的函数生成的值具有随机性，每次都不一样

针对java自带的Math.random(),设置随机发生器的代码为:
```java
    long seed = 12345L; // 设置种子为12345
    Random rand = new Random(seed); // 创建一个使用指定种子的随机数生成器
    System.out.println(rand.nextDouble());
```



