from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext

from .models import Document
from .forms import DocumentForm


def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()
            return render(request, 'upload/success.html')
    else:
        form = DocumentForm()

    documents = Document.objects.all()
    return render_to_response('upload/upload.html',
            {
                'documents': documents,
                'form': form,
            },
            context_instance=RequestContext(request)
    )


