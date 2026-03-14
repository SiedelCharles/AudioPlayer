cmake_minimum_required(VERSION 3.16)

project(AudioPlayer VERSION 0.1 LANGUAGES CXX)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(QT NAMES Qt6 Qt5 REQUIRED COMPONENTS Widgets Multimedia)
find_package(Qt${QT_VERSION_MAJOR} REQUIRED COMPONENTS Widgets Multimedia)

set(PROJECT_SOURCES
        main.cpp
        mainwindow.cpp
        mainwindow.h
        mainwindow.ui
        widgettitle.cpp
        widgettitle.h
        widgetside.cpp
        widgetside.h
        itemsidelistwidget.cpp
        itemsidelistwidget.h
        setting.h
        stackwidgetfordisplay.cpp
        stackwidgetfordisplay.h
        delegateside.cpp
        delegateside.h
        pagedisplay.cpp
        pagedisplay.h
        pagedisplay.ui
        pagetranscription.cpp
        pagetranscription.h
        pagetranscription.ui
        pagetranslation.cpp
        pagetranslation.h
        pagetranslation.ui
        pagesynthesis.cpp
        pagesynthesis.h
        pagesynthesis.ui
        filetreeitem.cpp
        filetreeitem.h
        filetreewidget.cpp
        filetreewidget.h
        filetreethread.cpp
        filetreethread.h
        audioplaypage.cpp
        audioplaypage.h
        audioplaythread.cpp
        audioplaythread.h
        resource.qrc
)

# set(FFMPEG_DIR "D:/VisualStudio_Created/VisualStudio_Resource/Download_Exe/ffmpeg-8.0.1-full_build-shared")
# set(FFMPEG_SOURCES
#     ${FFMPEG_DIR}/libavcodec/jni.h
# )

set(app_icon_resource_windows "${CMAKE_CURRENT_SOURCE_DIR}/favicon.rc")

include_directories(${CMAKE_CURRENT_SOURCE_DIR}/ffmpeg/include)
link_directories(${CMAKE_CURRENT_SOURCE_DIR}/ffmpeg/lib)

if(${QT_VERSION_MAJOR} GREATER_EQUAL 6)
    qt_add_executable(AudioPlayer
        MANUAL_FINALIZATION
        ${PROJECT_SOURCES}
        ${app_icon_resource_windows}
    )
# Define target properties for Android with Qt 6 as:
#    set_property(TARGET AudioPlayer APPEND PROPERTY QT_ANDROID_PACKAGE_SOURCE_DIR
#                 ${CMAKE_CURRENT_SOURCE_DIR}/android)
# For more information, see https://doc.qt.io/qt-6/qt-add-executable.html#target-creation
else()
    if(ANDROID)
        add_library(AudioPlayer SHARED
            ${PROJECT_SOURCES}
        )
# Define properties for Android with Qt 5 after find_package() calls as:
#    set(ANDROID_PACKAGE_SOURCE_DIR "${CMAKE_CURRENT_SOURCE_DIR}/android")
    else()
        add_executable(AudioPlayer
            ${PROJECT_SOURCES}
            favicon.rc
        )
    endif()
endif()

target_link_libraries(AudioPlayer PRIVATE Qt${QT_VERSION_MAJOR}::Widgets)

# Qt for iOS sets MACOSX_BUNDLE_GUI_IDENTIFIER automatically since Qt 6.1.
# If you are developing for iOS or macOS you should consider setting an
# explicit, fixed bundle identifier manually though.
if(${QT_VERSION} VERSION_LESS 6.1.0)
  set(BUNDLE_ID_OPTION MACOSX_BUNDLE_GUI_IDENTIFIER com.example.AudioPlayer)
endif()
set_target_properties(AudioPlayer PROPERTIES
    ${BUNDLE_ID_OPTION}
    MACOSX_BUNDLE_BUNDLE_VERSION ${PROJECT_VERSION}
    MACOSX_BUNDLE_SHORT_VERSION_STRING ${PROJECT_VERSION_MAJOR}.${PROJECT_VERSION_MINOR}
    MACOSX_BUNDLE TRUE
    WIN32_EXECUTABLE TRUE
)

include(GNUInstallDirs)
install(TARGETS AudioPlayer
    BUNDLE DESTINATION .
    LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
    RUNTIME DESTINATION ${CMAKE_INSTALL_BINDIR}
)

target_link_libraries(AudioPlayer PRIVATE Qt${QT_VERSION_MAJOR}::Widgets
    Qt6::Multimedia
    avcodec
    avformat
    avutil
    swresample
    # scale
    # avdevice
    # avfilter
)

if(QT_VERSION_MAJOR EQUAL 6)
    qt_finalize_executable(AudioPlayer)
endif()
