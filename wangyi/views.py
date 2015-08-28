import datetime
from django.shortcuts import render


from .models import WangyiArticle

def show(request):
    yesterday = datetime.date.today() + datetime.timedelta(days=-1)
    toutiao = WangyiArticle.objects.filter(mtime__lt=datetime.date.today())\
            .filter(mtime__gte=yesterday)\
            .filter(parent_id='T1348647909107')\
            .order_by('-comments_number')[:10]
    yule = WangyiArticle.objects.filter(mtime__lt=datetime.date.today())\
            .filter(mtime__gte=yesterday)\
            .filter(parent_id='T1348648517839')\
            .order_by('-comments_number')[:10]
    tiyu = WangyiArticle.objects.filter(mtime__lt=datetime.date.today())\
            .filter(mtime__gte=yesterday)\
            .filter(parent_id='T1348649079062')\
            .order_by('-comments_number')[:10]
    caijing = WangyiArticle.objects.filter(mtime__lt=datetime.date.today())\
            .filter(mtime__gte=yesterday)\
            .filter(parent_id='T1348648756099')\
            .order_by('-comments_number')[:10]
    junshi = WangyiArticle.objects.filter(mtime__lt=datetime.date.today())\
            .filter(mtime__gte=yesterday)\
            .filter(parent_id='T1348648141035')\
            .order_by('-comments_number')[:10]
    return render(request, 'wangyi/show.html',
            {
                'toutiaos': toutiao,
                'yules': yule,
                'caijings': caijing,
                'tiyus': tiyu,
                'junshis': junshi,
            }
    )


