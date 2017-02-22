from copy import deepcopy
from django.contrib import admin
from django.utils.translation import ugettext as _

from mezzanine.pages.admin import PageAdmin
from mezzanine.blog.admin import BlogPostAdmin
from mezzanine.blog.models import BlogPost

from projects.models import Project


blogpost_fieldsets = deepcopy(BlogPostAdmin.fieldsets)
blogpost_fieldsets[0][1]["fields"].insert(-2, _("project",))


class ProjectBlogPostAdmin(BlogPostAdmin):
    fieldsets = blogpost_fieldsets


admin.site.unregister(BlogPost)
admin.site.register(BlogPost, ProjectBlogPostAdmin)

admin.site.register(Project, PageAdmin)

