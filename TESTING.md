# PetPals - Testing details

[Main README.md file](README.md)

[View website on Heroku](https://thehouseofmouse.herokuapp.com/)

## Table of Contents

1. [Automated Testing](#automated-testing)
    - [Validation services](#validation-services)
2. [User Stories Testing](#user-stories-testing)
3. [Manual Testing](#manual-testing)
    - [Testing undertaken on desktop](#testing-undertaken-on-desktop)
    - [Testing undertaken on tablet and phone devices](#testing-undertaken-on-tablet-and-phone-devices)
4. [Bugs discovered](#bugs-discovered)
    - [Solved bugs](#solved-bugs)
    - [Unsolved bugs](#unsolved-bugs)
5. [Further Testing](#further-testing)


## User Stories Testing

The following section goes through the user stories identified in the [Ux section of README.md](README.md#UX) to check that the site meets those needs.

**As a visitor to The House of Mouse website I expect/want/need:**

1. **To easily find what I am looking for, I want the layout of the site to make sense so I am not confused or put off using it.**
    - Arrangement of site elements such as navbar, footer, icons, carousels, products lists, search, contact, FAQs and forms conform to expected placement. Breadcrumbs are provided on pages where the user has moved deeper into the hierarchical data structure of the website to make it easier for the user to tell where they are and how they can return to previous pages they were on.
    - The key pages of the site can be accessed from both the navigation bar and the footer, which can be found on all pages of the site (except the checkout pages).

### Bugs discovered: 
#### Solved bugs

1. **On running the python server, large errors appeared in terminal**
    - Any time a page was loaded, the terminal filled with around 100 lines of errors. This turned out to be a bug with Python 3.7.3 [See bug report on bugs.python.org](https://bugs.python.org/issue27682)
    - Bug was partially resolved by upgrading my version of python to python 3.7.5, although this threw new errors at me.
    - Bug finally fixed by replacing my `python manage.py runserver` command with `python manage.py runserver 8000` (with thanks to Chris Zielinski, Code Institute Mentor for this solution)

2. **Duplicate items added to OrderItems database**
    - As I was using a nested loop to compare the items in my sessions storage cart to the items in the database Order, I was ending up with duplicate items when more than 1 item was already in the database.
    - After multiple different attempts to fix the problem the solution was pretty simple: if the Order already existed I deleted all the OrderItems from the database and rebuilt them from the session variable instead.
```python
order = Order.objects.filter(customer=request.user, paid=False).first()
checkout_cart = request.session['cart']

# if new order, create instance of order
if not order:
    order = Order.objects.create(customer=request.user)

# if unpaid order exists in database already:
else:
    # get items in session storage cart
    session_cart = checkout_cart['orderItems']

    # get items currently in Order
    items_in_order = OrderItem.objects.filter(order=order)

    # delete all order items in the list
    for orderitem in items_in_order:
        orderitem.delete()

    # loop through all cart items and create new instances of OrderItem for them
    for item in session_cart:
        _id = int(item['listingId'])
        quantity = int(item['quantity'])

        # filter out items in session storage that have had their quantities reduced to 0
        if quantity > 0:
            product = Product.objects.filter(id=_id).first()
            order_item = OrderItem(order=order, product=product, quantity=quantity)
            order_item.save()
```

5. **Django code for search vectors not working with sqlite3 database**
    - The more refined search functions from `django.contrib.postgres.search`, such as `SearchQuery, SearchRank, SearchVector` would not work with my local sqlite3 database.
    - Temporarily solved this by using this simpler search code:

    ```python
    from django.db.models import Q
    results = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(tags__icontains=query))
    ```

    - Once my site was deployed, I connected to the postgres database and then replaced the above code with the more robust and accurate django postgres search code.


    ```python
    from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

    vector = SearchVector('title', weight='A') + SearchVector('description', weight='B') + SearchVector('tags', weight='C')
    query = SearchQuery(query)
    results = Product.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gte=0.1).order_by('rank')
    ```

4. **VScode unable to access postgreSQL database for testing**
    - Due to the free Hobby-dev postgres package selected when setting up the heroku database, I was not able to set the permissions necessary to alow Django to create a test database when running `manage.py test`. 
    - To fix this I reverted to accessing my sqlite3 database on my local machine for testing, and checked Travis regularly to check my tests written locally were passing when tested against the production database too.

5. **Duplicate listings showing up in All-Products view**
    - This was initially caused due to trying to sort results from the database by a boolean value (featured), but this turned out to be a known nofix issue with django. 
    - First I attempted to fix this by ordering by random, but the same problem continued.
    - Eventually I used the following code to grab both querysets for featured and not featured and concatenate them into one list to send to the page view.


    ```python
    from itertools import chain

    featured = Product.objects.filter(featured=True)
    not_featured = Product.objects.filter(featured=False)
    queryset = list(chain(featured, not_featured))
    ```

#### Unsolved bugs

1. **Sorting category results with pagination**
    - Getting the operation of pagination in shop categories in combination with the sort function throws multiple bugs and errors. The first pagination page will show correctly, but when the user tries to go to the next page the results are either reset as if the page was never sorted, or throws an error.
    - Given that the number of listings in the largest shop section is 15 - which is only 3 more than the usual pagination number of 12 - I decided to remove pagination in the shop sections and leave tackling this bug for a future release. 


## Further testing: 
1. Asked fellow students, friends and family to look at the site on their devices and report any issues they found.
2. The House of Mouse viewed on all devices and orientations available in Chrome DevTools, as well at a local tech store.