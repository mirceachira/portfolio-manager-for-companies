from django.views.generic import DetailView, ListView
from portfolio_manager.companies.models import Company


class CompanyDetailView(DetailView):
    model = Company
    template_name="companies/company_detail.html"
    
company_detail_view=CompanyDetailView.as_view()    

class CompanyListView(ListView):
    model = Company
    template_name="companies/company_list.html"

company_list_view=CompanyListView.as_view()    


