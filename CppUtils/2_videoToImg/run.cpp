#include <iostream>
#include "fstream"
#include <dirent.h>
#include <stdio.h>
#include <string>
#include <windows.h>
#include <opencv2/opencv.hpp>
using namespace std;
using namespace cv;

//判断字符串是否以指定字符串结尾
bool hasEnding (std::string const &fullString, std::string const &ending) {
    if (fullString.length() >= ending.length()) {
        return (0 == fullString.compare (fullString.length() - ending.length(), ending.length(), ending));
    } else {
        return false;
    }
}

void videoToImg(string videoName,string savePath)

{
        //打开视频文件：其实就是建立一个VideoCapture结构
    VideoCapture capture(videoName);
    //检测是否正常打开:成功打开时，isOpened返回ture
    if ( !capture.isOpened( ) )
        cout << "fail toopen!" << endl;
    //获取整个帧数
    long totalFrameNumber = capture.get( CV_CAP_PROP_FRAME_COUNT );
    // cout << "整个视频共" << totalFrameNumber << "帧" << endl;
    Mat frame;
	capture >> frame;
    DWORD t_end;
    string pureName = videoName.substr(0, videoName.rfind("."));
    while(!frame.empty())
    {
        t_end = GetTickCount();//操作系统启动所经历的毫秒数
        string output = savePath + to_string(t_end) + ".jpg";
        imwrite(output, frame);                    //显示该图像
        std::cout<<"saving img: "<<output<<std::endl;
        capture >> frame;
    }
}
int main()
{
    DIR * dir;
    struct dirent * ptr;
    char file_list[100][40];
    int i=0;
    char srcFile1[1][100];
    string rootdirPath = "video/";
    string savePath="image/";
    string x,dirPath;
    dir = opendir((char *)rootdirPath.c_str()); //打开一个目录
    while((ptr = readdir(dir)) != NULL) //循环读取目录数据
    {
        x=ptr->d_name;
        dirPath = rootdirPath + x;
        printf("d_name : %s\n", dirPath.c_str()); //输出文件绝对路径
        if(hasEnding (dirPath.c_str(), ".mp4"))
            videoToImg(dirPath.c_str(), savePath);

        if ( ++i>=100 ) break;
    }
    closedir(dir);//关闭目录指针
}