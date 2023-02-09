from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Card, Cover
from .forms import CleaningForm

# Create your views here.
def home(request):
    # Include an .html file extension - unlike when rendering EJS templates
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cards_index(request):
    cards = Card.objects.all()
    return render(request, 'cards/index.html', {
        'cards': cards
    })

def cards_detail(request, card_id):
    card = Card.objects.get(id=card_id)
    id_list = card.covers.all().values_list('id')
    covers_card_doesnt_have = Cover.objects.exclude(id__in=id_list)
    cleaning_form = CleaningForm()
    return render(request, 'cards/detail.html', {
        'card': card,
        'cleaning_form': cleaning_form,
        'covers': covers_card_doesnt_have
    })

def add_cleaning(request, card_id):
    form = CleaningForm(request.POST)
    if form.is_valid():
        new_cleaning = form.save(commit=False)
        new_cleaning.card_id = card_id
        new_cleaning.save()
    return redirect('detail', card_id=card_id)

class CardCreate(CreateView):
    model = Card
    fields = ['athlete', 'manufacturer', 'set', 'year_manufactured', 'features']

class CardUpdate(UpdateView):
    model = Card
    fields = ['athlete', 'manufacturer', 'set', 'year_manufactured', 'features']

class CardDelete(DeleteView):
    model = Card
    success_url = '/cards'

class CoverList(ListView):
    model = Cover

class CoverDetail(DetailView):
    model = Cover

class CoverCreate(CreateView):
    model = Cover
    fields = '__all__'

class CoverUpdate(UpdateView):
    model = Cover
    fields = '__all__'

class CoverDelete(DeleteView):
    model = Cover
    success_url = '/covers'

def assoc_cover(request, card_id, cover_id):
    Card.objects.get(id=card_id).covers.add(cover_id)
    return redirect('detail', card_id=card_id)

def disassoc_cover(request, card_id, cover_id):
    Card.objects.get(id=card_id).covers.remove(cover_id)
    return redirect('detail', card_id=card_id)