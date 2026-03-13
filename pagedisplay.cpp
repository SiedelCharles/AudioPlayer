#include "pagedisplay.h"
#include "ui_pagedisplay.h"

#include <QMenu>
#include <QAction>
#include <QMenuBar>
#include <QFileDialog>

#include "filelistwidget.h"

PageDisplay::PageDisplay(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::PageDisplay)
{
    ui->setupUi(this);
    _menu = new QMenuBar(this);

    QMenu *file_menu = _menu->addMenu("File(&F)");
    QAction *file_action = new QAction("Open File", this);
    file_action->setIcon(QIcon(":/resource/130180068_p0_master1200.jpg"));
    file_menu->addAction(file_action);
    connect(file_action, &QAction::triggered, this, &PageDisplay::slot_OpenFile);

    _file_list = new FileListWidget(this);
    connect(this, &PageDisplay::Sig_OpenFile, dynamic_cast<FileListWidget*>(_file_list), &FileListWidget::slot_OpenFile);
    _menu->setSizePolicy(QSizePolicy::Expanding, QSizePolicy::Fixed);
    _menu->setFixedHeight(_menu->sizeHint().height());
    ui->file_layout->insertWidget(0, _menu, 0, Qt::AlignTop);
    ui->file_layout->addWidget(_file_list);
}

PageDisplay::~PageDisplay()
{
    delete ui;
}

void PageDisplay::slot_OpenFile(bool checked)
{
    QFileDialog file_dialog;
    file_dialog.setFileMode(QFileDialog::Directory);
    file_dialog.setWindowTitle("choose file");
    file_dialog.setDirectory(QDir::currentPath());
    file_dialog.setViewMode(QFileDialog::Detail);
    QStringList fileNames;
    if(file_dialog.exec()){
        fileNames = file_dialog.selectedFiles();
    }
    if(fileNames.size()<=0) {
        return ;
    }
    QString import_path = fileNames.at(0);
    // emit Sig_OpenProject(import_path);
    emit  Sig_OpenFile(import_path);
}
