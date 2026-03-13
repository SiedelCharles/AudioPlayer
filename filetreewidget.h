#ifndef FILETREEWIDGET_H
#define FILETREEWIDGET_H

#include <QHeaderView>
#include <QTreeWidget>
#include "filetreethread.h"

class FileTreeWidget : public QTreeWidget
{
    Q_OBJECT
public:
    FileTreeWidget(QWidget *parent = nullptr);
public slots:
    void slot_OpenFile(const QString& path);
private:
    std::shared_ptr<FileTreeThread> _thread_openfiles;
};


#endif // FILETREEWIDGET_H
