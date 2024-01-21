1. 将UI文件转成py文件

```
pyuic5 input_file.ui -o output_file.py
示例
pyuic5 menu.ui -o Menu.py
```



2.  布局添加按钮

```python
# 设置布局
layout = QHBoxLayout()
# 布局添加按钮
layout.addWidget(button1)
layout.addWidget(button2)

# 主窗口
main_frame = QWidget()
# 主窗口添加布局
main_frame.setLayout(layout)
```



3. **QWidget**和**QMainWindow**的关系

   `QMainWindow` 是`QWidget`的子类，专门用于创建主窗口。

​       `QWidget`是所有用户界面元素的基类，提供了基本的GUI功能



4. `QApplication`是整个应用程序的管理者，负责初始化和控制整个应用程序的事件循环



5. 初始化窗口类的时候:

   ```python
   # 集成
   class WinForm(QMainWindow):
       # 必须要有这句
       def __init__(self, parent=None):
           super(WinForm, self).__init__(parent)
   ```



6. QtWidgets.QWidget作用

   1.创建空白窗口

   ```python
   my_widget = QtWidgets.QWidget()
   ```

   2.作为其它控件的容器

   ```python
   parent_widget = QtWidgets.QWidget()
   child_button = QtWidgets.QPushButton("Click me", parent_widget)
   ```

   3**.作为应用程序主窗口的中央部件：**

   ```python
   main_window = QtWidgets.QMainWindow()
   central_widget = QtWidgets.QWidget(main_window)
   main_window.setCentralWidget(central_widget)
   ```

   在这个例子中，`central_widget` 被设置为应用程序主窗口的中央部件。它将占据主窗口的中央区域，用于放置其他控件。



7. QtWidgets(学习最主要要学习的模块）

   QtWidgets模块：是PyQt5中最常用和最重要的模块，提供了一系列用户界面控件，如按钮、文本框、标签、表格、菜单、滚动条等。开发者可以利用这些控件快速构建用户界面。

   QWidget是QtWidgets中最主要的类，是gui控件的集合。

   pyqt中widget中类的关系

   ![pyqt_widgets](.\img\pytqt_widgets.webp)