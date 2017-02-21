from django.shortcuts import render

from mezzanine.pages.views import page

from projects.models import Project


def projects_list(*args, **kwargs):
    projects = Project.objects.all()

    return page(*args, extra_context={'projects': projects}, **kwargs)