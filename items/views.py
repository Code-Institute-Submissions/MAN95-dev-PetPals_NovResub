from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Item, Type
from .forms import ItemForm
from reviews.models import Review
from reviews.forms import ReviewForm
from profiles.models import UserProfile

# Create your views here.

def all_items(request):
    """ A view to show all items, including sorting and search queries """
    

    items = Item.objects.all()
    query = None
    types = Type.objects.all()
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
            types= request.GET['type'].split(',')
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
        'current_types': types,
        'current_sorting': current_sorting,
    }

    return render(request, 'items/items.html', context)


def item_detail(request, item_id):
    """ A view to show individual item details """

    item = get_object_or_404(Item, pk=item_id)
    reviews_raw = Review.objects.filter(item=item)
    reviews = reviews_raw.order_by('-date_created')
    review_form = ReviewForm()

    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)
        try:
            # Check if the user has already left a review
            item_review = Review.objects.get(user=user, item=item)
            edit_review_form = ReviewForm(instance=item_review)
            # If so they will not be able to leave another
            review_form = None
        except Review.DoesNotExist:
            edit_review_form = None
    else:
        edit_review_form = None
  
    context = {
        'item': item,
        'reviews': reviews,
        'review_form': review_form,
        'edit_review_form': edit_review_form,
    }

    return render(request, 'items/item_detail.html', context)


@login_required
def add_item(request):
    """ Add an item to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
        
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            messages.success(request, 'Successfully added item!')
            return redirect(reverse('item_detail', args=[item.id]))
        else:
            messages.error(request, 'Failed to add item. Please ensure the form is valid.')
    else:
        form = ItemForm()
        
    template = 'items/add_item.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_item(request, item_id):
    """ Edit an item in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated item!')
            return redirect(reverse('item_detail', args=[item.id]))
        else:
            messages.error(request, 'Failed to update item. Please ensure the form is valid.')
    else:
        form = ItemForm(instance=item)
        messages.info(request, f'You are editing {item.name}')

    template = 'items/edit_item.html'
    context = {
        'form': form,
        'item': item,
    }

    return render(request, template, context)


@login_required
def delete_item(request, item_id):
    """ Delete an item from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    messages.success(request, 'Item deleted!')
    return redirect(reverse('items'))



