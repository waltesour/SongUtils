# CMAKE generated file: DO NOT EDIT!
# Generated by "MinGW Makefiles" Generator, CMake Version 3.21

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

SHELL = cmd.exe

# The CMake executable.
CMAKE_COMMAND = "C:\Program Files\CMake\bin\cmake.exe"

# The command to remove a file.
RM = "C:\Program Files\CMake\bin\cmake.exe" -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = C:\code\testProject\0_configTemplate

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = C:\code\testProject\0_configTemplate\build

# Include any dependencies generated for this target.
include CMakeFiles/test.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/test.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/test.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/test.dir/flags.make

CMakeFiles/test.dir/test.cpp.obj: CMakeFiles/test.dir/flags.make
CMakeFiles/test.dir/test.cpp.obj: CMakeFiles/test.dir/includes_CXX.rsp
CMakeFiles/test.dir/test.cpp.obj: ../test.cpp
CMakeFiles/test.dir/test.cpp.obj: CMakeFiles/test.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=C:\code\testProject\0_configTemplate\build\CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/test.dir/test.cpp.obj"
	C:\mingw64\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/test.dir/test.cpp.obj -MF CMakeFiles\test.dir\test.cpp.obj.d -o CMakeFiles\test.dir\test.cpp.obj -c C:\code\testProject\0_configTemplate\test.cpp

CMakeFiles/test.dir/test.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test.dir/test.cpp.i"
	C:\mingw64\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E C:\code\testProject\0_configTemplate\test.cpp > CMakeFiles\test.dir\test.cpp.i

CMakeFiles/test.dir/test.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test.dir/test.cpp.s"
	C:\mingw64\bin\g++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S C:\code\testProject\0_configTemplate\test.cpp -o CMakeFiles\test.dir\test.cpp.s

# Object files for target test
test_OBJECTS = \
"CMakeFiles/test.dir/test.cpp.obj"

# External object files for target test
test_EXTERNAL_OBJECTS =

test.exe: CMakeFiles/test.dir/test.cpp.obj
test.exe: CMakeFiles/test.dir/build.make
test.exe: C:/opencv3416/build/x64/MinGW/lib/libopencv_calib3d3416.dll.a
test.exe: C:/opencv3416/build/x64/MinGW/lib/libopencv_core3416.dll.a
test.exe: C:/opencv3416/build/x64/MinGW/lib/libopencv_dnn3416.dll.a
test.exe: C:/opencv3416/build/x64/MinGW/lib/libopencv_features2d3416.dll.a
test.exe: C:/opencv3416/build/x64/MinGW/lib/libopencv_flann3416.dll.a
test.exe: C:/opencv3416/build/x64/MinGW/lib/libopencv_highgui3416.dll.a
test.exe: C:/opencv3416/build/x64/MinGW/lib/libopencv_imgcodecs3416.dll.a
test.exe: C:/opencv3416/build/x64/MinGW/lib/libopencv_imgproc3416.dll.a
test.exe: C:/opencv3416/build/x64/MinGW/lib/libopencv_ml3416.dll.a
test.exe: C:/opencv3416/build/x64/MinGW/lib/libopencv_objdetect3416.dll.a
test.exe: C:/opencv3416/build/x64/MinGW/lib/libopencv_photo3416.dll.a
test.exe: C:/opencv3416/build/x64/MinGW/lib/libopencv_shape3416.dll.a
test.exe: C:/opencv3416/build/x64/MinGW/lib/libopencv_stitching3416.dll.a
test.exe: C:/opencv3416/build/x64/MinGW/lib/libopencv_superres3416.dll.a
test.exe: C:/opencv3416/build/x64/MinGW/lib/libopencv_ts3416.a
test.exe: C:/opencv3416/build/x64/MinGW/lib/libopencv_video3416.dll.a
test.exe: C:/opencv3416/build/x64/MinGW/lib/libopencv_videoio3416.dll.a
test.exe: C:/opencv3416/build/x64/MinGW/lib/libopencv_videostab3416.dll.a
test.exe: CMakeFiles/test.dir/linklibs.rsp
test.exe: CMakeFiles/test.dir/objects1.rsp
test.exe: CMakeFiles/test.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=C:\code\testProject\0_configTemplate\build\CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable test.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles\test.dir\link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/test.dir/build: test.exe
.PHONY : CMakeFiles/test.dir/build

CMakeFiles/test.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles\test.dir\cmake_clean.cmake
.PHONY : CMakeFiles/test.dir/clean

CMakeFiles/test.dir/depend:
	$(CMAKE_COMMAND) -E cmake_depends "MinGW Makefiles" C:\code\testProject\0_configTemplate C:\code\testProject\0_configTemplate C:\code\testProject\0_configTemplate\build C:\code\testProject\0_configTemplate\build C:\code\testProject\0_configTemplate\build\CMakeFiles\test.dir\DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/test.dir/depend

