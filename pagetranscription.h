#ifndef PAGETRANSCRIPTION_H
#define PAGETRANSCRIPTION_H

#include <QWidget>

namespace Ui {
class PageTranscription;
}

class PageTranscription : public QWidget
{
    Q_OBJECT

public:
    explicit PageTranscription(QWidget *parent = nullptr);
    ~PageTranscription();

private:
    Ui::PageTranscription *ui;
};

#endif // PAGETRANSCRIPTION_H
