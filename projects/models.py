from django.db.models import ImageField, ManyToManyField, ForeignKey
from django.utils.translation import ugettext_lazy as _

from mezzanine.pages.models import Page
from mezzanine.core.models import RichText, RichTextField
from mezzanine.core.fields import FileField
from mezzanine.blog.models import BlogPost
from mezzanine.utils.models import upload_to

from cloudinary.models import CloudinaryField

class Project(Page, RichText):

    featured_image = FileField(verbose_name=_("Featured Image"),
                               upload_to=upload_to("blog.BlogPost.featured_image", "blog"),
                               format="Image", max_length=255, null=True, blank=True)

    authors = RichTextField(_("Authors"), null=True, blank=True)

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")


