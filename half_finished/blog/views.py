from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.conf import settings

from markdown_it import MarkdownIt

from pathlib import Path
import os

# Create your views here.
def blog(request):

    template = loader.get_template('basic.html')
    return HttpResponse(template.render())

def single(request, filename):
    full_path = os.path.join(settings.BASE_DIR, filename, ".md")
    files_dir = "files"
    filename_md = ''.join([filename, ".md"])
    md_glob = Path(os.path.join(settings.BASE_DIR, files_dir)).glob(filename_md, case_sensitive=False)
    md_files = []
    for file in md_glob:
        md_files.append(file)

    if (len(md_files) == 1):
        md_text = md_files[0].read_text()
        md = MarkdownIt()
        html_text = md.render(md_text)
        return HttpResponse(html_text)
    else:
        return HttpResponse("Hmm...")
    
    