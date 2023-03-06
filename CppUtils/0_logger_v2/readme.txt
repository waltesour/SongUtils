该版本Logger工具记录信息多用法如下
用法如下：

#include"TLogger.h"
int main()
{
	TLoggerBase* m_logger;
	//将日志文件存储到log/TodayTime/文件夹下,日志中包含:时间--当前函数名--所在行数--写入的内容
	m_logger = new TLogger("log.txt");
	LOG_INFO(m_logger, (std::string("----------- Logger test-----------")).c_str());
}