#ifndef TLOGGERHEADER_
#define TLOGGERHEADER_

#include "TLoggerBase.h"
#include <vector>
#include <string>
#include <iostream> 
#include <fstream>
#include <mutex>

typedef  void (*WriteLogCallback)(int, const char*, void*);
class TLogger : public TLoggerBase
{
public:
	TLogger(const char* filename = nullptr);
    virtual ~TLogger();
	void setLogFile(const char *fileName, const char *filePath = nullptr, const char *subPath = nullptr);
	void setCallback(WriteLogCallback callback, void* context);
	static std::string getTime();
private:
	WriteLogCallback m_callback_;
	void* m_callbackcontext_;
	std::mutex m_writeMutex;
	std::ofstream m_logFile;
	bool m_opened;
	int m_lastFlush;
	
	std::string m_curTime;
	std::string m_filePath;		            //�ļ�·��
	std::string m_fileName;		            //�ļ���
	std::string m_fileSubPath;		            //�����µ����ļ���

	//�ļ���С�����ļ�����һ��ֵʱ�������ļ�
	size_t m_filesize;

private:
	//�鿴�����Ƿ���
	bool CheckTime();
	//�鿴��־�ļ���С
	void CheckFileSize(size_t newdatasize);
	//������־�ļ�
	int CreateLogFile();

public:
	virtual bool writeLog(const char *pTitle, int level, const char *pLog) override;
	bool writeLog(std::vector<std::string> &log);
};

#endif // TLOGGERHEADER_
