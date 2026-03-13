#include "pagetranscription.h"
#include "ui_pagetranscription.h"

PageTranscription::PageTranscription(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::PageTranscription)
{
    ui->setupUi(this);
}

PageTranscription::~PageTranscription()
{
    delete ui;
}
