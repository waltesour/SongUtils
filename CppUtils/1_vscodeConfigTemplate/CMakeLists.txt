cmake_minimum_required(VERSION 3.21) # 与当前平台版本有关
# 项目名称
project(test)
# 添加c++ 11标准支持
#set( CMAKE_CXX_FLAGS "-std=c++11" )
# 设置debug调试还是Release模式
SET(CMAKE_BUILD_TYPE "Debug")
# Add OpenCV headers location to your include paths
include_directories(C:/opencv3416/build/x64/MinGW/install/include)
include_directories(C:/opencv3416/build/x64/MinGW/install/include/opencv)
include_directories(C:/opencv3416/build/x64/MinGW/install/include/opencv2)
# 配置opencv库
set(OpenCV_LIBS
    C:/opencv3416/build/x64/MinGW/lib/libopencv_calib3d3416.dll.a
    C:/opencv3416/build/x64/MinGW/lib/libopencv_core3416.dll.a
    C:/opencv3416/build/x64/MinGW/lib/libopencv_dnn3416.dll.a
    C:/opencv3416/build/x64/MinGW/lib/libopencv_features2d3416.dll.a
    C:/opencv3416/build/x64/MinGW/lib/libopencv_flann3416.dll.a
    C:/opencv3416/build/x64/MinGW/lib/libopencv_highgui3416.dll.a
    C:/opencv3416/build/x64/MinGW/lib/libopencv_imgcodecs3416.dll.a
    C:/opencv3416/build/x64/MinGW/lib/libopencv_imgproc3416.dll.a
    C:/opencv3416/build/x64/MinGW/lib/libopencv_ml3416.dll.a
    C:/opencv3416/build/x64/MinGW/lib/libopencv_objdetect3416.dll.a
    C:/opencv3416/build/x64/MinGW/lib/libopencv_photo3416.dll.a
    C:/opencv3416/build/x64/MinGW/lib/libopencv_shape3416.dll.a
    C:/opencv3416/build/x64/MinGW/lib/libopencv_stitching3416.dll.a
    C:/opencv3416/build/x64/MinGW/lib/libopencv_superres3416.dll.a
    C:/opencv3416/build/x64/MinGW/lib/libopencv_ts3416.a
    C:/opencv3416/build/x64/MinGW/lib/libopencv_video3416.dll.a
    C:/opencv3416/build/x64/MinGW/lib/libopencv_videoio3416.dll.a
    C:/opencv3416/build/x64/MinGW/lib/libopencv_videostab3416.dll.a
)
# 指定生成目标
add_executable(test test.cpp)
# Link your application with OpenCV libraries
target_link_libraries(test ${OpenCV_LIBS} )