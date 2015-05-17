from django.shortcuts import render, render_to_response
from django.template import RequestContext

from .forms import AlgorithmForm
from upload.models import Document
from .utils import run_algorithm


def show(request):
    if request.method == 'POST':
        form = AlgorithmForm(request.POST)
        print form
        if form.is_valid():
            algorithm = form.cleaned_data['algorithm']
            minSupport = form.cleaned_data['minSupport']
            minConfidence = form.cleaned_data['minConfidence']
            datafile = form.cleaned_data['datafile']
            print algorithm, minSupport, minConfidence, datafile
            run_algorithm(algorithm, str(minSupport), str(minConfidence), datafile)
            path = 'algorithm/' + datafile.split('/')[-1] + str(minSupport) + str(minConfidence) + '/'
            fp = open(path + 'freq.data', 'r')
            freq = []
            for line in fp:
                freq.append(line)
            fp.close()
            print freq
            fp =open(path + 'rules.data', 'r')
            rules = []
            for line in fp:
                line = line.split('; ')
                rules.append(line)
            return render(request, 'algorithm/success.html',
                    {
                        'algorithm': algorithm,
                        'minS': minSupport,
                        'minC': minConfidence,
                        'datafile': datafile,
                        'freq': freq,
                        'rules': rules,
                    }
            )
    else:
        form = AlgorithmForm()
    documents = Document.objects.all()
    return render_to_response('algorithm/show.html',
            {
                'documents': documents,
                'form': form,
            },
            context_instance=RequestContext(request)
    )




