Logger工具用法如下：

#include "Logger.h"
int main()
{
	songutils::Logger logfile("log.txt");
	logfile.Write("message need record");
	return 0;
}