#include "Logger.h"

using namespace std;

namespace songutils {

Logger::Logger(string filename)
{
	logFile.open(filename.c_str(), ios::app);
}

Logger::~Logger(void)
{

}

void Logger::Write(string line)
{
	time_t now; 
	now = time(NULL); 
	struct tm * timeinfo = localtime(&now);  

	logFile << timeinfo->tm_year + 1900 << "-" << timeinfo->tm_mon + 1 << "-" << timeinfo->tm_mday << " ";
	logFile << timeinfo->tm_hour << ":" << timeinfo->tm_min << ":" << timeinfo->tm_sec << ",";

	logFile << line << endl;
}

}