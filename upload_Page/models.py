#_*_coding:utf-8 _*_
from django.db import models
import json, time, xlrd, xlwt

# Create your models here.
class ExcelFile(models.Model):
    name = models.CharField(max_length=40, blank=True)
    file = models.FileField(upload_to='meida/')
    upload_time = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = u"Excel File"
        verbose_name_plural = u"Excel File List"

    def __unicode__(self):
        return self.name

    def save_contents(self):
        file = xlrd.open_workbook(file_contents=self.file.read())
        sheet = file.sheets()[0]
        if sheet.nrows:
            for i in range(sheet.nrows):
                tmp = [x.value for x in sheet.row(i)]
                # print list(tmp)
                tmp_row = Rows()
                tmp_row.content = json.dumps(tmp)
                tmp_row.belong_to = self
                tmp_row.save()

    def save(self, *args, **kwargs):
        # super(ExcelFile, self).save(*args, **kwargs)
        if not self.name:
            print self.file.name
            self.name = self.file.name
        super(ExcelFile, self).save(*args, **kwargs)
        self.save_contents()


class Rows(models.Model):
    content = models.TextField(editable=False)
    belong_to = models.ForeignKey(ExcelFile)
    
    class Meta:
        verbose_name = u"Excel Rows"
        verbose_name_plural = u"Excel Rows List"

    def __unicode__(self):
        return self.content
