# zhouxin_test
**测试仓库，用于学习和测试github各种功能**

**作为非计算机专业的，之前代码和文件都是通过一个一个版本的文件夹管理的，不会用版本管理工具，自从会科学上网和用了github感觉发现了一个新大陆，github是一个快速学习和记录自己历程的地方，此仓库主要用于熟悉github使用。**

# 1.常用git命令
  * git fetch git reset --hard origin/master 
     - 使用场景：自己多台设备之间同步，由于仓库内可能有一些非git可以比较差异的内容，如anylogic的数据，当在另一台设备中进行了仿真，改变了数据，git pull会失败，此时就必须用远程仓库强制覆盖本地仓库。首先进行git fetch获取远程仓库，然后git checkout 本地分支，执行git reset --hard origin/master，就可用远程分支强制覆盖本地分支。
  * git pull git push
     - push之前要首先git pull获取远程仓库最新更新，进行合并或冲突解决，再进行远程推送git push，其中git pull之前要进行git add和git push否则会出现over written的问题。那么只能用git reset放弃修改或者git stash暂存修改。

# 2.常用github用法
----------
![github快捷键](https://img-blog.csdnimg.cn/d1e55767a7fa432c9d721dbe54b07851.png)

**2.1** 在项目里.可以直接打开编辑器,T可以快速查找文件，L可以快速定位行,B可以快速查看源码修改记录。

**2.2** 在项目中，项目地址前加"https://gitpod.io/#/" + 项目地址可以调用在线编辑器运行。

**2.3** **.gitattibute**是一个文本文件，它用于给git仓库中的不同文件或路径指定属性。.gitattributes 文件中的每个属性由一个或多个行组成，每行指定一个或多个文件或路径及其相应的属性。文件可以被放置在 Git 存储库的任何目录中，Git 会自动递归地查找它并将其应用于该目录及其子目录中的所有文件。

**2.4** 特别注意 **?** 的使用，**?** 可以快速调出快捷键的使用帮助。

**2.5** sync fork命令, 对于一个forked的项目，进入自己仓库的fork的项目中，点击sync fork，可与原项目保持同步，从而阅读最新状态的项目。

**2.6** git stash是必要的，因为开发本地开发的时候，是不确定远程基底是否发生更改的，但此时本地的开发的的代码又不可能放弃掉，因此需要用git stash存起来，先解决冲突将本地更新和远程一样，再进一步将stash的代码和本地代码合并。然后再进行push.

```shell
1.查看已存储的 stash 列表
git stash list
2.应用stash(不删除)
	只有一个stash记录
	git stash apply
    如果存在有多个 stash 记录，可以选择应用特定的 stash 记录	
    git stash apply stash@{n}
3.应用stash(删除)
    只有一个stash记录     
	git stash pop
	如果你有多个 stash 记录，可以选择应用特定的 stash 记录
	git stash pop stash@{n}

4. 删除stash记录
   删除特定记录
   git stash drop stash@{n}
   删除所有stash记录
   git stash clear 
```



**2.7** git diff 返回的@@- ,+ @@的含义,以@@ -2,5 +2,6 @@的含义:

![git diff](https://img-blog.csdnimg.cn/82f1c6be20634c69a4a52027be3e5b0b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA5ZCO5Y6C5p2R6Lev6JSh5b6Q5Z2k,size_8,color_FFFFFF,t_70,g_se,x_16)

-2,5：终端所展示的文本，在旧文件中，所处于第2到5行
+2,6：终端所展示的文本，在新文件中，所处于第2到6行

对于每个修改的文件，你可以查看文件的差异，并显示行级别的代码更改。这包括被添加的行（绿色）、被删除的行（红色）以及被修改的行（黄色）。

**2.8** git rm --cache 1.txt 从暂存区删除
    1.txt 未提交的更改，更改会被丢弃
    1.txt 已经至暂存区，则会将最后一次暂存区的文件还原到工作区

**2.9** git reset将会从暂存区撤回

**2.10** 当新建分支，第一次上传push时，要执行
     git push --set-upstream origin v1
     通过 --set-upstream origin v1 来在远程github建立分支

**2.11** tags的应用

```bash
git tag v1.0
git push --tags
```

​	第一行是用来创建tag，第二行是用来提交tag

**2.12**  当git文件夹中将其它模块视为子系统模块，github中显示带箭头的白色文件夹不能代开

```shell
1、删除文件夹里面的.git文件夹

2、执行git rm --cached [文件夹名]

3、执行git add [文件夹名]

4、执行git commit -m "msg"

5、执行git push origin [branch_name] 
```



**2.13** git checkout .

用于取消对工作目录中所有修改的更改。具体而言，它会将工作目录中所有文件的更改还原到最后一次提交的状态。



2.14 git checkout . 和 git reset --hard区别

`git checkout .` 和 `git reset --hard` 都可以用于丢弃工作目录中的修改，但它们的实现方式和影响略有不同：

a.**git checkout .:**

- 用于取消工作目录中所有已修改的文件。
- 不会影响已经添加到暂存区的文件。
- 不会修改当前分支的指针位置，也就是说，不会影响提交历史。

```shell
git checkout .
```

b. **git reset --hard:**

- 可以用于重置当前分支的 HEAD、暂存区和工作目录。
- 将当前分支的 HEAD 移动到指定的提交，暂存区也会被重置为该提交，工作目录的文件会被替换为该提交的版本。
- 会丢弃所有的本地修改，包括已暂存和未暂存的。

```
git reset --hard HEAD
```

总的来说，如果你只是想取消工作目录中的修改而不影响提交历史，可以使用 `git checkout .`。如果需要完全重置工作目录、暂存区和提交历史，包括已提交的内容，可以使用 `git reset --hard`。请谨慎使用 `git reset --hard`，因为它会永久性地删除未提交的本地修改和已提交的历史



**2.15** git reset --hard真正危险的地方

`git reset --hard` 会修改分支指针和提交历史，将分支指针移动到指定的提交，并删除该提交之后的所有提交。这可能会改变分支的历史。比如提交历史a,b,c,d,e,f 当git reset --hard 到提交点c时会把d,e,f都删掉。



**2.16** 用远程分支强制覆盖本地分支

```shell
git checkout main
git fetch
git reset --hard origin/main
```



**2.17 给本地的仓库添加远程仓库**

```shell
初始本地仓库
git init

添加远程仓库
git remote add origin https://github.com/username/repository.git

查看远程仓库
git remote -v

推送代码到远程仓库
git push origin master

更改远程仓库URL
git remote set-url origin https://github.com/username/new-repository.git
```

**2.18 查看历史提交**

方法一:创建临时分支

```shell
查看历史提交
git log

切换到特定提交并创建临时分支
git checkout -b temp-branch <commit-hash>

查看完毕后删除临时分支并切换回原分支
git checkout <branch-name>
git branch -d temp-branch
```

方法二：使用 `git checkout` 切换到提交并返回到分支

```shell
查看历史提交
git log

切换到特定提交并创建临时分支
git checkout <commit-hash>

查看完毕后删除临时分支并切换回原分支
git checkout <branch-name>
```
2.19

fatal: refusing to merge unrelated histories 错误通常在你试图将两个没有共同历史的独立 Git 仓库合并时出现。这个问题通常出现在以下情况下：

1.你在一个已经存在的远程仓库中初始化了一个新的本地仓库并试图推送。

2.你在本地和远程分别创建了不同的初始提交。
```
合并不同历史
git pull origin main --allow-unrelated-histories
# 解决冲突并提交
git add .
git commit -m "Merge unrelated histories"
git push origin main
或者
重新初始化本地仓库并推送，初始化本地仓库，进行远程覆盖
rm -rf .git
git init
git remote add origin https://github.com/zhouxinxin19920802/Couzin_ros_test.git
git add .
git commit -m "Initial commit"
git push -u origin main --force

```





# 3 git出现冲突的情况

Git 通常在以下情况下会出现冲突：

1.合并分支时：当你试图将一个分支合并到另一个分支时，如果两个分支都修改了同一个文件的相同部分，就会出现冲突。提交代码时：当两个或多个人同时在同一个文件的相同部分进行修改并尝试提交代码时，就会出现冲突。

2.重命名或移动文件时：如果你重命名或移动一个文件，而其他人也对该文件进行了修改，就会出现冲突。

3.同时修改多个文件时：如果多个人在同一时间对同一个文件夹中的多个文件进行修改，就会出现冲突。

4.本地工作区存在未暂存的修改时，git pull也会报错，因为git pull会同时更新版本库和工作区，工作区未暂存或者提交的话，工作区会被覆盖，因此会报错，报错的提示为:
>error: Your local changes to the following files would be overwritten by merge:pom.xml,Please commit your changes or stash them before you merge.

>    <<<<<<< ======= >>>>>>>

>    <<<<<<<和=======之间的所有内容都是你的本地修改。 这些修改还没有在远程版本库中。=======和>>>>>>>之间的所有行都是来自远程版本库或另一个分支的修改。

> 可以看出冲突往往发生在不同分支上，或者同一分支不同操作
> * 不同分支的情况，例如原来版本为a，A拉取修改a+b变成了c,此时分支C, B拉取a+d变成了e，此时分支为D，此时分支C和D合并就会出现冲突，因为基底已经发生了变化
> * 想同分支的情况，例如原来版本为a，A拉取修改a+b变成了c，B拉取a+d变成了e，B上传，需要首先进行

，因为基底发生了变化，所以会发生冲突
> ---------------------------
> 冲突的根本在于基底发生了变化，所以单人单分支操作的话，往往是不会发生冲突的
> 如果当前分支的每一个提交(commit)都已经存在另一个分支里了，git 就会执行一个“快速向前”(fast forward)操作,git 不创建任何新的提交(commit)，只是将当前分支指向合并进来的分支

# 4.github学习资料
4.1 [github漫游指南](https://github.phodal.com/#/chapter/Github%E6%BC%AB%E6%B8%B8%E6%8C%87%E5%8D%97)
