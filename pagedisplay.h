#ifndef PAGEDISPLAY_H
#define PAGEDISPLAY_H

#include <QWidget>
#include <QMenuBar>

namespace Ui {
class PageDisplay;
}

class PageDisplay : public QWidget
{
    Q_OBJECT
signals:
    void Sig_OpenFile(const QString& path);
public:
    explicit PageDisplay(QWidget *parent = nullptr);
    ~PageDisplay();
public slots:
    void slot_OpenFile(bool checked = false);
private:
    Ui::PageDisplay *ui;
    QMenuBar *_menu;
    QWidget *_file_list;
};

#endif // PAGEDISPLAY_H
