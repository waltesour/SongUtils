# 需要使用git bash运行.sh文件
cd build
rm *
cmake -G "MinGW Makefiles" ..
mingw32-make.exe