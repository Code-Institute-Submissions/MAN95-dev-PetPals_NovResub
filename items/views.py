from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Item, Type

# Create your views here.

def all_items(request):
    """ A view to show all items, including sorting and search queries """

    items = Item.objects.all()
    query = None
    type = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                items = items.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            items = items.order_by(sortkey)

        if 'type' in request.GET:
            types = request.GET['type'].split(',')
            items = items.filter(type__name__in=types)
            types = Type.objects.filter(name__in=types)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('items'))
                
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            items = items.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'items': items,
        'search_term': query,
        'current_type': type,
        'current_sorting': current_sorting,
    }

    return render(request, 'items/items.html', context)


def item_detail(request, item_id):
    """ A view to show individual item details """

    item = get_object_or_404(Item, pk=item_id)

    context = {
        'item': item,
    }

    return render(request, 'items/item_detail.html', context)