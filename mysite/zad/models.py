from django.db import models
from django.conf import settings
import datetime
from django.utils import timezone
from django.utils.translation import gettext_lazy as T

_ = lambda s: s

def upload_path(instance, filename):
    imagename, extension = filename.split(".")
    title = instance.Ad_title
    return 'post/{}.{}'.format(title, extension)





class AD(models.Model):
    term_choices = ((24, "day"), (48, "tow days"), (72, "three days"))
    categories = (('product', 'product'), ('service', 'service'), ('course', 'course'), ('store', 'store'), ('other', 'other'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE, related_name='adder',
                             verbose_name=T("User:"), help_text=T("User"))

    Ad_title = models.CharField(verbose_name=T("Ad about:"), max_length=50, blank=False, editable=True, null=False,
                                default="null", help_text=T("TITLE:"))
    Ad_details = models.TextField(verbose_name=T("Ad details:"), max_length=500, blank=False, editable=True,
                                  help_text="DETAILS:")
    category = models.CharField(verbose_name=T("category"), blank=False,max_length=30, null=False, help_text="Choose Category:")
    photo = models.ImageField(blank=False, upload_to='post/')
    term = models.IntegerField(choices=term_choices, blank=False, null=False, verbose_name=T("publish for"),
                               help_text="publish for:")
    approved = models.BooleanField(default=False, blank=True, verbose_name=T("is it approved"), help_text="is it approved")
    valid = models.BooleanField(default=True, blank=True, verbose_name=T("is it valid"), help_text="is it valid")
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, default=None, related_name='AD_likes',verbose_name=T("like"))
    created_at = models.DateTimeField(auto_created=True, auto_now_add=True, blank=False, verbose_name=T("create date"),
                                      help_text=T("Created At:"))
    update_at = models.DateTimeField(auto_created=True, auto_now=True, verbose_name=T("update date"),
                                     help_text=T("Updated At:"))
    publish_date = models.DateTimeField(blank=True, null=True, verbose_name=T("publish At"), help_text=_("publish At:"))

    objects = models.Manager()

    class Meta:
        verbose_name = T('AD')
        verbose_name_plural = T('ADS')

    def number_of_likes(self):
        return self.likes.count()


    def make_un_valid(self):

        if self.approved and self.publish_date+datetime.timedelta(hours=self.term)>timezone.now():
            self.valid =False


    def __str__(self):
        return self.Ad_title




