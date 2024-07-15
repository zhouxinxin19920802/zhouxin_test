TOPIC通信

A.如何进行编译？
1. 进入CATKIN_WS
2. catkin_make 编译



B.如何创建包？
1. catkin_create_pkg test_pkg roscpp rospy std_msgs

C.修改什么文件，如何进行修改？
1. CMakeLists.txt和package.xml
2. CMakeLists.txt
```
    CMakeLists.txt
    find_package(catkin REQUIRED COMPONENTS
    roscpp
    std_msgs
    message_generation  #需要添加的地方
    )

    ------------------------------------------------
    add_message_files(FILES gps.msg)
    #catkin在cmake之上新增的命令，指定从哪个消息文件生成，要根据实际修改
    ------------------------------------------------

    ------------------------------------------------
    generate_messages(DEPENDENCIES std_msgs)
    ------------------------------------------------

    #catkin新增的命令，用于生成消息
    #DEPENDENCIES后面指定生成msg需要依赖其他什么消息，由于gps.msg用到了float32这种ROS标准消息，因此需
    要再把std_msgs作为依赖


    运行python脚本，最后需要添加这个
    -----------------------------------------------
    catkin_install_python(PROGRAMS
        scripts/pytalker.py
        scripts/pylistener.py
        DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
    )
    -----------------------------------------------

```
``` 
    package.xml
    -----------------------------------------------
    <build_depend>message_generation</build_depend>
    <run_depend>message_runtime</run_depend>
    -----------------------------------------------



```


D.如何运行

1. source ~/catkin_ws/devel/setup.bash #刷新坏境
2. rosrun test_pkg pylistener.py 添加包名
