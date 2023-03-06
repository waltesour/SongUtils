#include "TLogger.h"
#include <string>
#include <chrono>
#include <fstream>

#ifndef _WIN32
#include <sys/stat.h>
#include <unistd.h>
#include <cstring>
#define MKDIR(dir) 	if (access(dir, F_OK) == -1) mkdir(dir, S_IRWXU | S_IRUSR | S_IWUSR | S_IXUSR | S_IRWXG | S_IRWXO);
#else
#include <direct.h>
#include <sys/stat.h>
#define MKDIR(dir) 	_mkdir(dir);
#endif

#define WRITE_FILE

#define MAX_PATH 256

static const unsigned int maxfilesize = 10 * 1024 * 1024;

TLogger::TLogger(const char* filename)
{
	m_opened = false;
	m_lastFlush = 0;
	m_callback_ = NULL; 
	m_callbackcontext_ = NULL;
	if (filename)
	{
		setLogFile(filename);
	}
}

TLogger::~TLogger(void)
{
	if (m_opened)
	{
		m_opened = false;
		m_logFile.close();
	}
}

void TLogger::setLogFile(const char *fileName, const char *filePath, const char *subPath)
{
#ifndef WRITE_FILE
	m_opened = true;
	m_fileName = std::string(fileName);
	return;
#endif
	m_curTime = "";

	if (subPath != NULL)
	{
		m_fileSubPath = std::string(subPath);
	}

	if (filePath != NULL)
	{
		m_filePath = std::string(filePath);
	}
	else
	{
		char  strConvertPath[MAX_PATH];
		memset(strConvertPath, 0, sizeof(strConvertPath));
#ifndef _WIN32
		getcwd(strConvertPath, sizeof(strConvertPath));
#else
		_getcwd(strConvertPath, sizeof(strConvertPath));
#endif // DEBUG

		m_filePath = std::string(strConvertPath) + std::string("/log/");
	}
	if (fileName != NULL)
	{
		m_fileName = std::string(fileName);
	}
	else
	{
		m_fileName = "default";
	}

	CheckTime();
}

void TLogger::setCallback(WriteLogCallback callback, void* context)
{
	m_callback_ = callback;
	m_callbackcontext_ = context;
}

std::string  TLogger::getTime()
{
	auto now = std::chrono::system_clock::now();
	uint64_t dis_millseconds = std::chrono::duration_cast<std::chrono::milliseconds>(now.time_since_epoch()).count()
		- std::chrono::duration_cast<std::chrono::seconds>(now.time_since_epoch()).count() * 1000;
	time_t tt = std::chrono::system_clock::to_time_t(now);
	auto time_tm = localtime(&tt);

	char timedata[MAX_PATH];
	memset(timedata, 0, sizeof(timedata));
	sprintf(timedata, "%02u:%02u:%02u:%03u\t", time_tm->tm_hour, time_tm->tm_min, time_tm->tm_sec, (int)dis_millseconds);
	return std::string(timedata);
}

bool TLogger::CheckTime()
{
	bool changed = false;

	char timeTemp[9];
	memset(timeTemp,0,sizeof(timeTemp));

	auto now = std::chrono::system_clock::now();
	time_t tt = std::chrono::system_clock::to_time_t(now);
	tm* t = localtime(&tt);
	sprintf(timeTemp, "%04u%02u%02u", t->tm_year + 1900, t->tm_mon + 1, t->tm_mday);

	std::string strtime = std::string(timeTemp);
	if (strtime != m_curTime)
	{
		m_curTime = strtime;
		if (CreateLogFile() >= 0)
		{
			changed = true;
		}
	}
	return changed;
}

void TLogger::CheckFileSize(size_t newdatasize)
{
	m_filesize += newdatasize;
	m_filesize += 38;
	if (m_filesize > maxfilesize)
	{
		CreateLogFile();
		m_filesize = 0;
	}
}

int TLogger::CreateLogFile()
{
	char strPath[MAX_PATH];
	memset(strPath, 0, sizeof(strPath));

	auto now = std::chrono::system_clock::now();
	uint64_t dis_millseconds = std::chrono::duration_cast<std::chrono::milliseconds>(now.time_since_epoch()).count()
		- std::chrono::duration_cast<std::chrono::seconds>(now.time_since_epoch()).count() * 1000;
	time_t tt = std::chrono::system_clock::to_time_t(now);
	auto time_tm = localtime(&tt);

	sprintf(strPath, "%s-%02u.%02u.%02u.%03u.txt", m_fileName.c_str(), time_tm->tm_hour, time_tm->tm_min, time_tm->tm_sec, (int)dis_millseconds);

	//std::lock_guard<std::mutex> lock(m_writeMutex);

	std::string path = m_filePath + "/";
	MKDIR(path.c_str());

	path += std::string(m_curTime) + "/";
	MKDIR(path.c_str());

	if (!m_fileSubPath.empty())
	{
		path += std::string(m_fileSubPath) + "/";
		MKDIR(path.c_str());
	}

	path += std::string(strPath);

	if (m_opened)
	{
		m_opened = false;
		m_logFile.close();
	}

	m_logFile.open(path, std::ios::app);
	m_opened = m_logFile.is_open();
	m_filesize = 0;
	return 0;
}

bool TLogger::writeLog(const char *pTitle, int level, const char *pLog)
{
#ifdef WRITE_FILE
	if (!m_opened)
	{
		return false;
	}
#endif
	auto now = std::chrono::system_clock::now();
	uint64_t dis_millseconds = std::chrono::duration_cast<std::chrono::milliseconds>(now.time_since_epoch()).count()
		                      - std::chrono::duration_cast<std::chrono::seconds>(now.time_since_epoch()).count() * 1000;
	time_t tt = std::chrono::system_clock::to_time_t(now);
	auto time_tm = localtime(&tt);

	char timedata[MAX_PATH];
	memset(timedata, 0, sizeof(timedata));
	sprintf(timedata, "%02u:%02u:%02u:%03u\t", time_tm->tm_hour, time_tm->tm_min, time_tm->tm_sec, (int)dis_millseconds);

	std::lock_guard<std::mutex> lock(m_writeMutex);
	std::string loglevel = "Info\t";
	if (level%10 == 1)
	{
		loglevel = "Warning\t";
	}
	else if (level%10 == 2)
	{
		loglevel = "Error\t";
	}
	std::string loginfo = std::string(timedata).append(pTitle).append(loglevel).append(pLog);

//#ifndef WRITE_FILE
	//std::cout<<m_fileName.c_str()<<"\t"<<loginfo<<std::endl;
//#else
	m_logFile << loginfo << std::endl;
	if (m_lastFlush != time_tm->tm_min)
	{
		m_lastFlush = time_tm->tm_min;
		m_logFile.flush();
	}

	CheckTime();
	CheckFileSize(loginfo.size());
//#endif
	if (m_callback_)
	{
		m_callback_(level, loginfo.c_str(), m_callbackcontext_);
	}
	return true;
}

bool TLogger::writeLog(std::vector<std::string> &log)
{
#ifdef WRITE_FILE
	if (!m_opened)
	{
		return false;
	}
#endif
	size_t datasize = 0;
	for (auto& loginfo : log)
	{
		datasize += log.size();
		m_logFile << loginfo << std::endl;
	}

	time_t tt = std::chrono::system_clock::to_time_t(std::chrono::system_clock::now());
	auto time_tm = localtime(&tt);
	if (m_lastFlush != time_tm->tm_min)
	{
		m_lastFlush = time_tm->tm_min;
		m_logFile.flush();
	}

	CheckTime();
	CheckFileSize(datasize);
}
