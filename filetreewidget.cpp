#include "filetreewidget.h"
#include "filetreethread.h"

#include <QDir>

FileTreeWidget::FileTreeWidget(QWidget *parent)
    : QTreeWidget(parent), _thread_openfiles(nullptr)
{

}

void FileTreeWidget::slot_OpenFile(const QString &path)
{
    // TODO:to create a set to store the opened files;
    QDir project_dir(path);
    QString project_name = project_dir.dirName();
    _thread_openfiles = std::make_shared<FileTreeThread>(path, nullptr, this);
    connect(_thread_openfiles.get(), &FileTreeThread::SigOpenFileFinished, this, [this]() {
        _thread_openfiles.reset();
    });
    if(_thread_openfiles!=nullptr) {
       _thread_openfiles->start();
    }
}
