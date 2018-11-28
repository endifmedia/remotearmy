from django.shortcuts import render

from django.core.paginator import Paginator

from .models import Company


def index(request):
    company_list = Company.objects.all()
    paginator = Paginator(company_list, 50)
    page = request.GET.get('page')
    pag_company_list = paginator.get_page(page)

    return render(request, 'index.html', {'company_list': pag_company_list, 'company_count': company_list.count() })


def company(request, company_id):
    c = Company.objects.get(pk=company_id)
    return render(request, 'single-company.html', {'company': c})