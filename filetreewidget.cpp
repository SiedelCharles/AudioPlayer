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

// void FileTreeWidget::slot_PlayMusic(QTreeWidgetItem *item, int column)
// {
//     if (!item) return;
//     QString file_path = item->data(0, Qt::ToolTipRole).toString();
//     if (!file_path.isEmpty()) {
//         qDebug() << "slot_PlayMusic is executed. ";
//         emit SigPlayMusic(item, column);
//     }
// }
