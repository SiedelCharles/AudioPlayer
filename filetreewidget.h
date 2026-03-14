#ifndef FILETREEWIDGET_H
#define FILETREEWIDGET_H

#include <QHeaderView>
#include <QTreeWidget>
#include "filetreethread.h"

class FileTreeWidget : public QTreeWidget
{
    Q_OBJECT
signals:
    // void SigPlayMusic(QTreeWidgetItem *item, int cloumn);
public:
    FileTreeWidget(QWidget *parent = nullptr);
public slots:
    void slot_OpenFile(const QString& path);
    // void slot_PlayMusic(QTreeWidgetItem *item, int column);
private:
    std::shared_ptr<FileTreeThread> _thread_openfiles;
};


#endif // FILETREEWIDGET_H
