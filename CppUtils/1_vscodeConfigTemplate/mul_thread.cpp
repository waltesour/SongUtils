#include<iostream>
#include<thread>
using namespace std;
int main()
{
	std::ios::sync_with_stdio(false); //打消iostream的输入输出缓存,节省cout、cin时间
	std::thread thread_a([]()
    {
        for (int i = 0; i < 100000; i++)
            std::cout << "thread a: " << i << std::endl;
    });
    std::thread thread_b([]()
    {
        for (int i = 0; i < 100000; i++)
            std::cout << "thread b: " << i << std::endl;
    });
    thread_a.detach(); //把这个线程与主线程分离运行
    thread_b.detach();
	// std::this_thread::sleep_for 将某个线程阻塞(block)dur时间段
	// std::chrono::seconds 持续时间以秒为单位
    std::this_thread::sleep_for(std::chrono::seconds(1)); //主线程堵塞1秒
    return 0;
}



