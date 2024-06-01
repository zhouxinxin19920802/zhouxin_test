1. C++日志配置

```shell
安装spdlog和fmt
sudo apt-get install libspdlog-dev
sudo apt-get install libfmt-dev
编译
g++ -std=c++11 -o a.out test1.cpp -lspdlog -lfmt && ./a.out
```



2. C++的日志输出

```c++
#define SPDLOG_ACTIVE_LEVEL SPDLOG_LEVEL_INFO
#include "spdlog/spdlog.h"
#include <iostream>
#include "spdlog/sinks/basic_file_sink.h"


int main()
{
  auto fileLogger = spdlog::basic_logger_mt("zxx", "test.log",true);
  spdlog::set_pattern("[%H:%M:%S][%n][thr %t][%s:%!():%#] %v");
  std::string strURL =  "fengyuzaitu51.cto";
  int nFirstTime = 1;
  SPDLOG_LOGGER_INFO(fileLogger, "Welcome to {} {} time!", strURL, nFirstTime);
  return 0;
}
```



