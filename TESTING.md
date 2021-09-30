# PetPals - Testing details

[Main README.md file](README.md)

[View website on Heroku](ttps://petpals-milestone-4.herokuapp.com/)

## Table of Contents

1. [Automated Testing](#automated-testing)
    - [Validation](#validation)
2. [User Stories Testing](#user-stories-testing)
3. [Manual Testing](#manual-testing)
    - [Testing undertaken on desktop](#testing-undertaken-on-desktop)
    - [Testing undertaken on tablet and phone devices](#testing-undertaken-on-tablet-and-phone-devices)
4. [Bugs discovered](#bugs-discovered)
    - [Solved bugs](#solved-bugs)
    - [Unsolved bugs](#unsolved-bugs)
5. [Further Testing](#further-testing)


## Automated Testing

### Validation

CSS - Validated using [Jigsaw](https://jigsaw.w3.org/css-validator/) with no errors found.

| Page | Test | 
--- | --- | 
base.css | PASS
checkout.css | PASS
profile.css | PASS

HTML - Validated using [W3C](https://validator.w3.org/#validate_by_input).

| Page | Test | 
--- | --- | 
index.html |PASS
items.html | PASS
item_detail.html | PASS
add_item.html | PASS
edit_item.html | PASS
profile.html | PASS
reviews.html | PASS
checkout.html | PASS
checkout_success.html | PASS
cart.html | PASS

Javascript - Validated using [JSHint Validator](https://jshint.com/) with no errors found.

Python - Validated using [PEP 8](http://pep8online.com/) with no errors found with one exception: - settings.py (the Django settings file has a known issue, but is acceptable to not force a line break) - line too long (> 79 characters) - AUTH_PASSWORD_VALIDATORS = [{}] x 

## User Stories Testing

The following section goes through the user stories identified in the [Ux section of README.md](README.md#UX) to check that the site meets those needs.

**As a visitor to The House of Mouse website I expect/want/need:**

1. **To easily find what I am looking for, I want the layout of the site to make sense so I am not confused or put off using it.**
    - Arrangement of site elements such as navbar, footer, icons, carousels, products lists, search, contact, FAQs and forms conform to expected placement. Breadcrumbs are provided on pages where the user has moved deeper into the hierarchical data structure of the website to make it easier for the user to tell where they are and how they can return to previous pages they were on.
    - The key pages of the site can be accessed from both the navigation bar and the footer, which can be found on all pages of the site (except the checkout pages).

## Manual Testing
Below is a detailed account of all the manual testing that has been done to confirm all areas of the site work as expected. 

### Testing undertaken on desktop

All steps on desktop were repeated in browsers: Firefox, Chrome and Internet Explorer and on two different desktop screen sizes.

#### Elements on every page

1. Navbar 
    - Clicked each link in the navbar to confirm that it leads to the correct page.
    - Confirm that when logged out the options "Register" and "Log in" are visible and that "Account" and "Log out" are not.
    - Log into the site, confirm that options "Account" and "Log out" are visible and that "Register" and "Log in" are not.
    - Click the "Shop" link in the navbar, confirm that all sections of the shop are listed in the dropdown menu.
    - Add an item to the users cart, confirm that the counter appears over the shopping cart icon with the correct number of items displays.
    - Add more than 10 items to the cart, confirm that the counter shows `9+`.
    - Delete all items from the users cart, confirm that the counter is no longer visible in the navbar.

2. Footer
    - Click subscribe button, confirmed it opens a new tab and takes the user to the correct subscription page on the MailChimp website.
    - Hover over links in the footer, confirm the color change animation works as expected.
    - Click all links in the footer, confirm that they take the user to the relevant pages within the site.
    - Click the facebook icon, confirm that it opens a new tab and takes the user to The House of Mouse facebook page.
    - Check date of copyright information, confirm year displayed matches the current year.

#### Home Page

1. Hero Slider
    - Click slider buttons, confirm that they work as expected.
    - Adjust width of browser window, confirm image is always cropped in an attractive way.

2. Call to action buttons
    - Hover over all buttons, confirm the color change and shadow on hover appear as expected.
    - Click all buttons, confirm they take the user to the correct links and open new tabs when links go away from the website.

3. Shop section images
    - Hover over each section image, confirm shadow size increases and image looks as it if is being lifted up on the page.
    - Confirm all titles laid over on images can be easily read.

4. Testimonials carousel
    - Click carousel buttons, confirm that they work as expected.
    - Check each slide to be sure the elements fit within the slider.
    - Confirm all text can be easily read.

5. Featured listings
    - Confirm that on desktop 4 featured listings are visible in one row.
    - Confirm that on tablet 6 featured listings are visible over two rows.
    - Reload the page, confirm that a new random selection of featured listings are shown.
    - Click each listing picture, confirm that it takes the user to the relevant listing detail page.

#### Shop Page

1. Breadcrumbs
    - Click breadcrumb links, confirm they work and go to the correct locations.

2. Shop section buttons
    - Hover over section buttons, confirm the hover effects work as expected.
    - Click all section buttons, confirm they work and take the user to the correct pages.

3. Sorting options
    - Select the different sorting options from the menu one by one, confirm that the products are sorted in the orders selected.

4. Product cards
    - Hover over product cards, confirm the hover effect works as expected.
    - Confirm that the photos, images and prices displayed are correct.
    - Click multiple products, confirm that the user is taken to the correct product listing pages.
    - Confirm that one of each product is displayed in total. 
    - Check that there are no duplicates or missing products.

5. Pagination
    - Click all pagination links, confirm that they work as desired.

#### Search Page

1. Breadcrumbs
    - Click breadcrumb links, confirm they work and go to the correct locations.

2. Search bar
    - Load search page, confirm that the search bar is visible and no product listing results are shown.
    - Enter a search word that applies to many listings. 
        - Confirm that the listing returned match the search term.
        - Confirm that the results are paginated and that the pagination works correctly.
    - Enter a search word that does not apply to any listings. Confirm that the message "There are currently no listings that match this search" is displayed when hitting enter.

3. Footer on search page
    - Confirm that footer stays stuck to the bottom of the screen even when there are no listings to fill up the space.

#### Listing Page

1. Listing breadcrumbs
    - Check that breadcrumbs show the relevant category of the product listing in them.
    - Click all breadcrumb links, confirm that they take the user to the correct pages.

2. Listing details
    - Confirm that the listing title, price, and description match those in the database for the product.

3. Listing photographs
    - Click the thumbnails provided for extra images of the product. Confirm that the large photograph is updated to reflect the thumbnails clicked.
    - Confirm that the standard photograph of the product packaging, and the one provided to show scale are visible with the other listing photographs.

4. Listing information
    - Confirm that all information on measurements, materials, safety and customisations can be found on the listing detail page under the description. 
    - Click the contact page link in the listing info, confirm it takes the user to the contact page.

5. More like this
    - Check that the listings featured in the "more like this" section are from the same category as the listing detail currently open.
    - Check that the current listing is excluded from the selection of products shown.
    - Click the products in this section, confirm that their links and hover effects work as expected.
    - Click the "browse more" button, confirm it takes the user to the correct category section of the shop.

6. Quantity selection
    - Click the quantity selection. Confirm that the highest number available to select matches the number in stock of this product.

7. Add to cart button
    - Click the "add to cart" button. Confirm that the applicable modal is launched, stating the name of the product added to the cart, and that the cart counter in the navigation bar is updated to reflect the new quantity.
    - Confirm that the modal provides two buttons to the user: to go to cart or to continue shopping. Click both to confirm they operate as expected.
    - Add more to the cart from the same product, making the total go over the max number in stock. Confirm that the modal alerting the user to too many of the product in their cart is launch. Confirm that the quantity in the cart is reset to the max number in stock.

#### About Page

- Go to account page, confirm that the title and subheading displays as expected. 
- Check that the photograph is on the left side of the screen and the text on the right. 
- Check that the proportions of the page are as expected.
- Click the "visit shop" call to action button, confirm it takes the user to the main shop page.

#### FAQs Page

- Go to FAQs page. Confirm that each question is in the main heading font and pink, to make it easy for users to scan the questions to find the ones relevant to their needs.
- Check that the questions are clear and the answers given are sufficient.
- Click the "contact" and "subscribe" links provided on this page, confirm they take the user to the contact page.

#### Contact Page

- Go to the contact page. Confirm that the contact form is laid out as expected.
- Confirm that for a logged in user the email address field has already been populated. 
- Confirm that for a user who is not logged in the email address field is blank.
- Try to send the form with no fields filled in, confirm that the user is alerted to fill in the required fields.
- Try to enter a non-email address into the email field, confirm that the user is alerted to fill in an email address.
- Send a complete form, confirm that the message is sent to my email address with all the information included.

#### Register Page

- Try to go to the register url when already logged in, confirm that the user is redirected to the home page.
- Log out then go to the register page again. Confirm that the register form is displayed as expected.
- Fill in the form with a username already in the database, confirm that the user is informed that they must use a unique username.
- Fill in the email input with a non-email address, confirm the user is shown an error asking the to use an email address.
- Go into devtools, change the `type` attribute on the email form to `text`, attempt to send the form. confirm that the Django validation catches the error and tells the user to enter an email address.
- Fill in the form with two different passwords, confirm the error is caught again and the user is informed of their mistake.
- Fill in the registration for correctly, confirm that the user is automatically directed to the login page, and the message "Your account has been created `<username>`. You can now log in." is displayed above the login page. 

#### Login Page

- Reload the login page, confirm that the message for a new account is not visible.
- Attempt to log in with a username not in the database, confirm the relevant error message is shown.
- Attempt to log in with a correct username but wrong password, confirm the relevant error message is shown.
- Log in with a correct username and password, confirm that the user is logged in and that they are redirected to their cart page.
- Try to return to the login page url when already logged in, confirm that the user is redirected to the cart page.

#### Account Page

- Go to the account page of a newly created user. Confirm that te profile info form is populated with the users username and email address.
- Confirm that the first name and last name fields are also available.
- Fill in the form with a non-email address, confirm that the applicable error is shown to the user
- Fill in the form correctly, confirm that the "Your account info has been updated." message is shown to the user and that the reloaded form is now populated with the new data.
- Confirm that a user with no previous orders has the "no orders to show" text in the Orders section.
- Make 2 separate orders on the website. 
- Return to the account page, confirm that the orders are displayed in the Orders section of the account page. With the top order being the most recent and open to show the full details. Confirm that all orders after it in the list are closed accordions, but that can be opened with a click.
- Confirm that all data in the orders on the account page is accurate.
- Go into the admin panel, mark one of the orders as shipped. Confirm that the information to the user in their account page is updated to show that the order selected has been shipped.

#### Log Out Page

- Add a new product to the users cart. Click the "log out" link in the navigation bar. Confirm that the user is logged out and their cart has been cleared.
- Click the "Log in again" link on this page, confirm that the user is taken back to the login page.
- Confirm that the footer stays stuck to the bottom of the screen even when there is not enough content on the page to push it down.

#### Cart Page

- Go to the cart page when not logged in to the site, confirm that the user is taken to the login page to sign in.
- Log in and go to the cart page with nothing in the cart. Confirm that the message "Your cart is empty!" is shown and the call to action button "Let's go shopping" is provided.
- Click the button and confirm it takes the user to the main shop page.
- Add items to the cart and return to the cart page, confirm that all items in the cart are displayed correctly, with the correct amounts requested by the user.
- Adjust the quantity field, confirm that the shopping cart subtotal is updated to reflect the change.
- Adjust the quantity field up higher than the number of that item in stock. Confirm that a modal alerts the user to the maximum number available and adjust the cart to reflect that amount.
- Click the `x` delete button on a listing, confirm that the cart page is reloaded with that item removed from the cart.
- Delete all items from the cart, confirm that the cart page is reloaded to reflect the empty cart.

#### Checkout Pages

- Navigate to the checkout page urls without anything in the cart. Confirm that the user is redirected to the cart page.

##### Info Page

- Go to the info page with items in users cart. Confirm that the items are displayed correctly in the order summary, that the subtotal is correct, and that the "change" link on the order summary returns the user to the cart page if clicked.
- Confirm that the progress bar at the top of the page highlights the correct stage in the checkout process.
- Try to click the "continue to shipping" button without adding any information to the shipping info form. Confirm that the appropriate error message is given to the user.
- Try to send the form without all the required fields filled in. Confirm that the appropriate error message is given to the user.
- Click the "My country is not in the list?" link, confirm that the information modal is launched and that the buttons on this modal work as expected.
- Click the links at the bottom of the page, confirm that they work as expected.
- After adding shipping information and going to the next page, return to the Info page and confirm that the shipping info is populated in the form.

##### Shipping Page

- Go to the shipping page. Confirm that the items are displayed correctly in the order summary and that the "change" link on the order summary returns the user to the cart page if clicked.
- Confirm that the shipping price is correct for the country selected, and has now been added to the total. 
- Test the shipping price by changing the country destination to different areas that have different prices.
- Confirm that the progress bar at the top of the page highlights the correct stage in the checkout process.
- Check that the email address of the user is displayed and is correct. 
- Check that the address given by the user is also displayed correctly.
- Click the links at the bottom of the page, confirm that they work as expected.
- Click the "Continue to payment" button, confirm it takes the user to the Stripe checkout page.

##### Payment Page

- Cancel the payment, confirm that the user is taken back to the all products page of the website.
- Return to the payment page , use the stripe checkout test [card numbers](https://stripe.com/docs/testing) to check the various responses to different errors.
- Make a successful payment. Confirm that the user is returned to The House of Mouse website and the confirm order page.

##### Confirmation Page

- Check that the conformation page loads as expected.
- Confirm that the progress bar at the top of the page highlights the correct stage in the checkout process. 
- Check that the shipping address provided by the user is also correct.
- Check that the estimated shipping time given is correct for the country selected by the user.
- Check that the links provided on this page work as expected.
- Click the "return to shop" button, confirm that the user is taken back to the main shop page.

#### Terms and Conditions Page

- Check that the page loads and displays as expected. Confirm that the links in the text work as needed.

#### Privacy Policy Page

- Check that the page loads and displays as expected. Confirm that the links in the text work as needed.


### Testing undertaken on tablet and phone devices
All steps below were repeated to test mobile and tablet specific elements on my Samsung phone and tablet, in both the firefox browser and samsung internet browser.

Responsive design was also tested in the Chrome Developer Tools device simulators on all options and orientations.

#### Elements on every page

1. Navbar 
    - Open the website on mobile, confirm that the navbar is collapsed into a burger icon
    - click the burger icon, confirm that the navbar list appears are expected.
    - Click the "Shop" dropdown menu, confirm that the shop sections are displayed. 
    - Add something to the cart, confirm that the user shopping cart icon counter appears and displays correctly.

2. Footer
    - Scroll to the bottom of the page, confirm that the footer contents is displayed as expected with the bootstrap grid.
    - No content squashed or squeezed or disproportionate in size.
    - Confirm that all links and buttons in footer are easy to click with a finger on the smallest screen sizes.

3. Shop pages
    - Confirm that the product list is displayed one on top of each other on mobile, and 3 to a row on tablet.
    - Confirm that all clicks and swipes operate as expected on touch screen.

4. Checkout pages
    - Confirm that the order summary is displayed as a closed accordion, and can be opened with a click.
    - Check that the display of elements matches the expected layout for mobile and tablet devices.

5. All pages
    - Navigate to all pages on the site, check that the layout is as expected for the screen size.
    - Check that all buttons, menus, forms and other elements are the correct proportions and easily clickable with a finger.

## Bugs discovered: 
### Solved bugs

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

### Unsolved bugs

1. **Sorting category results with pagination**
    - Getting the operation of pagination in shop categories in combination with the sort function throws multiple bugs and errors. The first pagination page will show correctly, but when the user tries to go to the next page the results are either reset as if the page was never sorted, or throws an error.
    - Given that the number of listings in the largest shop section is 15 - which is only 3 more than the usual pagination number of 12 - I decided to remove pagination in the shop sections and leave tackling this bug for a future release. 

## Further testing: 
1. Asked fellow students, friends and family to look at the site on their devices and report any issues they found.
2. The House of Mouse viewed on all devices and orientations available in Chrome DevTools, as well at a local tech store.