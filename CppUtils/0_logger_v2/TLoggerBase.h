#ifndef TLOGGERBASEHEADER_
#define TLOGGERBASEHEADER_

#define LOG_MACRO_BODY(pLogWriter, logLevel, logMessage) if(pLogWriter){char title[200]; sprintf(title,"%s\t%d\t",__FUNCTION__,__LINE__); (pLogWriter)->writeLog(title, logLevel,logMessage);}

#define LOG_INFO(pLogWriter, logMessage)  LOG_MACRO_BODY(pLogWriter,0, logMessage)
#define LOG_WARNING(pLogWriter, logMessage)  LOG_MACRO_BODY(pLogWriter, 1, logMessage)
#define LOG_ERROR(pLogWriter, logMessage)  LOG_MACRO_BODY(pLogWriter, 2, logMessage)	
	
#define UILOG_INFO(pLogWriter, logMessage)  LOG_MACRO_BODY(pLogWriter,10, logMessage)
#define UILOG_WARNING(pLogWriter, logMessage)  LOG_MACRO_BODY(pLogWriter, 11, logMessage)
#define UILOG_ERROR(pLogWriter, logMessage)  LOG_MACRO_BODY(pLogWriter, 12, logMessage)	

class TLoggerBase
{
public:
	virtual bool writeLog(const char *pTitle, int level, const char *pLog) = 0;
};

#endif // TLOGGERBASEHEADER_