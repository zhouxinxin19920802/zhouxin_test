![一幅美丽的画](img/背景图.jpg)
# zhouxin_test
**测试仓库，用于学习和测试github各种功能**

**作为非计算机专业的，之前代码和文件都是通过一个一个版本的文件夹管理的，不会用版本管理工具，自从会科学上网和用了github感觉发现了一个新大陆，感觉github这是一个快速学习和记录自己历程的地方，此仓库主要用于快速熟悉github使用。**

# 常用git命令
  * git fetch git reset --hard origin/master 
     - 使用场景：自己多台设备之间同步，由于仓库内可能有一些非git可以比较差异的内容，如anylogic的数据，当在另一台设备中进行了仿真，改变了数据，git pull会失败，此时就必须用远程仓库强制覆盖本地仓库。首先进行git fetch获取远程仓库，然后git checkout 本地分支，执行git reset --hard origin/master，就可用远程分支强制覆盖本地分支。
  * git pull git push
     - push之前要首先git pull获取远程仓库最新更新，进行合并或冲突解决，再进行远程推送git push。

# 常用github用法
