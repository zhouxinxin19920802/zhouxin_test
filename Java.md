**1.java日志的配置**

**MyFormatter**

```java
import java.util.logging.Formatter;
import java.util.logging.LogRecord;
import java.text.SimpleDateFormat;
import java.util.Date;

public class MyFormatter extends Formatter {
    private static final SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");

    @Override
    public String format(LogRecord record) {
        StringBuilder sb = new StringBuilder();

        // 获取时间
        sb.append(dateFormat.format(new Date(record.getMillis())))
          .append(" ");

        // 获取行号
        try {
            // 通过创建一个异常来获取当前的堆栈跟踪
            Throwable t = new Throwable();
            StackTraceElement[] elements = t.getStackTrace();
            for (StackTraceElement element : elements) {
                if (element.getClassName().equals(record.getSourceClassName()) &&
                    element.getMethodName().equals(record.getSourceMethodName())) {
                    sb.append("[")
                      .append(record.getSourceClassName())
                      .append(".")
                      .append(record.getSourceMethodName())
                      .append(":")
                      .append(element.getLineNumber())
                      .append("] ");
                    break;
                }
            }
        } catch (Exception e) {
            // 如果获取行号失败，不添加行号
        }

        // 获取日志级别
        sb.append(record.getLevel().getName())
          .append(" ");

        // 获取记录器名称
        sb.append(record.getLoggerName())
          .append(" - ");

        // 获取日志消息
        sb.append(formatMessage(record))
          .append(System.lineSeparator());

        return sb.toString();
    }
}
```



**logging.properties**

```
# Handlers
handlers = java.util.logging.FileHandler

# Root logger level
.level = ALL

# FileHandler configuration
java.util.logging.FileHandler.level = ALL
java.util.logging.FileHandler.pattern = logs/myapp.log
java.util.logging.FileHandler.append = true
java.util.logging.FileHandler.formatter = MyFormatter
```



**主类**

```java
import java.io.IOException;
import java.util.logging.LogManager;
import java.util.logging.Logger;

public class MyApp {
    // 获取日志
    private static final Logger logger = Logger.getLogger(MyApp.class.getName());

    public static void main(String[] args) {
        // 加载自定义的日志配置文件
        try {
            LogManager.getLogManager().readConfiguration(MyApp.class.getResourceAsStream("/logging.properties"));
        } catch (IOException e) {
            e.printStackTrace();
        }

        logger.info("This is an info message");
        logger.warning("This is a warning message");
        logger.severe("This is a severe message");
    }
}
```

