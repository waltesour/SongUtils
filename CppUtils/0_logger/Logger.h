#pragma once

#include <ctime> 
#include <string>
#include <fstream>
#include <iostream> 

using namespace std;

namespace songutils {

//Logger
class Logger
{
public:
	Logger(string filename);
	~Logger(void);

private:
	ofstream logFile;
	
public:
	void Write(string line);
};

}