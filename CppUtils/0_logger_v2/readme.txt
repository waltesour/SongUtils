�ð汾Logger���߼�¼��Ϣ���÷�����
�÷����£�

#include"TLogger.h"
int main()
{
	TLoggerBase* m_logger;
	//����־�ļ��洢��log/TodayTime/�ļ�����,��־�а���:ʱ��--��ǰ������--��������--д�������
	m_logger = new TLogger("log.txt");
	LOG_INFO(m_logger, (std::string("----------- Logger test-----------")).c_str());
}