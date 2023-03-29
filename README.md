# zhouxin_test
**测试仓库，用于学习和测试github各种功能**

**作为非计算机专业的，之前代码和文件都是通过一个一个版本的文件夹管理的，不会用版本管理工具，自从会科学上网和用了github感觉发现了一个新大陆，感觉github这是一个快速学习和记录自己历程的地方，此仓库主要用于熟悉github使用。**

# 1.常用git命令
  * git fetch git reset --hard origin/master 
     - 使用场景：自己多台设备之间同步，由于仓库内可能有一些非git可以比较差异的内容，如anylogic的数据，当在另一台设备中进行了仿真，改变了数据，git pull会失败，此时就必须用远程仓库强制覆盖本地仓库。首先进行git fetch获取远程仓库，然后git checkout 本地分支，执行git reset --hard origin/master，就可用远程分支强制覆盖本地分支。
  * git pull git push
     - push之前要首先git pull获取远程仓库最新更新，进行合并或冲突解决，再进行远程推送git push。

# 2.常用github用法
----------
![github快捷键](https://img-blog.csdnimg.cn/d1e55767a7fa432c9d721dbe54b07851.png)

2.1 在项目里.可以直接打开编辑器,T可以快速查找文件，L可以快速定位行,B可以快速查看源码修改记录。

2.2 在项目中，项目地址前加"https://gitpod.io/#/" + 项目地址可以调用在线编辑器运行。

2.3 **.gitattibute**是一个文本文件，它用于给git仓库中的不同文件或路径指定属性。.gitattributes 文件中的每个属性由一个或多个行组成，每行指定一个或多个文件或路径及其相应的属性。文件可以被放置在 Git 存储库的任何目录中，Git 会自动递归地查找它并将其应用于该目录及其子目录中的所有文件。


![github漫游指南](https://github.phodal.com/#/chapter/Github%E6%BC%AB%E6%B8%B8%E6%8C%87%E5%8D%97?id=%e8%8e%b7%e5%be%97%e4%b8%80%e4%bb%bd%e5%b7%a5%e4%bd%9c)
