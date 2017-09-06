from django.shortcuts import render

from django.http import Http404

from loans.models import Loan

def index(request):
	loans = Loan.objects.exclude(money=0)
	return render(request, 'loans/index.html', {
		'loans': loans,
	})

def loan_detail(request,id):
    try:
        loan = Loan.objects.get(id = id)
    except Loan.DoesNotExist:
        raise Http404('There is no loan')
    return render(request,'loans/loan_detail.html',{
        'loan' : loan,
        })
# Create your views here.
