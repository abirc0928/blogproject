from .forms import SearchForm

def search_form(request):
    search_form = SearchForm()
    return {'SearchForm': search_form}