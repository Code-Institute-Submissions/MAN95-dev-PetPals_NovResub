<div align="center">
    <img src="/static/images/readme/mock-up.png" target="_blank" rel="noopener" alt="PetPals" aria-label="PetPals"/>
</div>


[PetPals](https://petpals-milestone-4.herokuapp.com/) is an e-commerce site, built using HTML, CSS, JavaScript, Python, and Django. The shop sells a range of pet food and accessories.

DISCLAIMER: This website is for educational purposes only and uses products and content from existing brands. Please see the credits section for full information.

Test card details:
* Card Number: 4242 4242 4242 4242
* Expiration Date: 04 / 24
* CVC: 424
* ZIP: 42424

## Table of Contents

1. [Project Summary](#project-summary)
	- [Site Purpose](#site-purpose)

2. [UX](#ux)
    - [Goals](#goals)
        - [Site Owner Goals](#site-owner-goals)
        - [Site User Goals](#site-user-goals)
    - [User Stories](#user-stories)
    - [Design Choices](#design-choices)
    - [Wireframes](#wireframes)

3. [Features](#features)
    - [Common Features](#common-features)
    - [Page Features](#page-features)

5. [Information Architecture](#information-architecture)
    - [Database choice](#database-choice)
    - [Data Models](#data-models)

6. [Technologies Used](#technologies-used)
    - [Tools](#tools)
    - [Databases](#databases)
    - [Libraries](#libraries)
    - [Languages](#languages)

7. [Testing](#testing)
    - See separate [TESTING.md](TESTING.md) file.

8. [Deployment](#deployment)
    - [How to run this project locally](#how-to-run-this-project-locally)
    - [Heroku Deployment](#heroku-deployment)

9. [Credits](#credits)
    - [Content](#content)
    - [Images](#images)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)

----

# Project Summary 

This project is my fourth and final milestone project (Full Stack Frameworks With Django) for the Code Institute Diploma in Software Development.

The purpose of the project is to build a full-stack site based around business logic used to control a centrally-owned dataset , setting up an authentication mechanism and providing paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.

## Site Purpose 

The purpose of the site is to sell pet items and accessories on an online store call PetPals. Customers can purchase items and user engagement is encouraged through the ability to leave reviews and comments and to create user profiles.

The site is intended to be visually appealing, and easy to navigate. It has a responsive design so that it can be viewed easily on mobile and desktop.

# UX

## Goals

### Site Owner Goals

As a site owner I want to be able to:

- Create a visually appealing site with a strong brand identity.
- Add products on the website so I can add new items to my stores.
- Edit existing products in my store so I can change product prices, descriptions, images and other product information.
- Delete products on the website so I can remove items from my store.
- Have links that direct users to our social sites for further engagement.
- Keep track of sales data to inform future product choices.

### Site User Goals

The central target audience for PetPals are:

- People who own pets. 
- People who would like to own a pet. 
- People who would like the ease of shopping online for pets.
- People who value door to door delivery.

As a site user I want to be able to:

- Find items needed for my pet. 
- Enjoy browsing all the pet items.
- Be able to navigate the shop easily, find what I need and make a safe and secure purchase.
- Buy from a trustworthy online shop. 


## User Stories

As a visitor to the PetPals website I expect/want/need:

1. To easily find what I am looking for, I want the layout of the site to make sense so I am not confused or put off using it. 

1. The ability to search through small amounts of information to find what I need, and then be able to easily click to get more detailed information when I need it.

1. The site to be easily navigable from any device, desktop, tablet or phone. For the content to look good and be useable on all of these devices.

1. To be able to read reviews of items bought from previous customers, to build trust in my purchase.

1. Leave a review on a product so that I can inform other shoppers about whether it was a good purchase or not.

1. For all information and images to be laid out in a clear and easy to understand way, on whatever size screen I am viewing the website on.

1. To be able to easily find out all the information I need to make an informed purchase. I expect information about the description, ingredients, and instructions where necessary. 

1. A text search function so that I can quickly narrow down my search when looking for something specific

1. To be able to see a summary of my order during the checkout process.

1. That once I am logged in I can access my account details and update them if I need to. 

1. To be able to find information on my past orders. 

1. To be able to connect to the businesses social media channels, to keep up to date with new items and deals on the site. 

1. To be able to easily get in contact with the shop owner via a telephone number or email.

1. Feedback from the website I am using when I interact with it, I expect pop ups and modals to inform me when my forms have been completed and sent correctly. Or to let me know when an error has ocurred and what to do next.

## Design Choices

### Fonts

- The primary font 'Lato' was chosen for the main text of the site because of it clear readability, clean style and complementary contrast with the secondary font. 

- The secondary font 'Fredoka One' was chosen for the website name, as it is fun and bold. The rounded edges compliment those of the buttons used in the website. 

### Colors
- The colour scheme for this site was rendered on [Cooler](https://coolors.co/) and can be seen below:

<div align="center">
    <img src="/static/images/readme/color-palette.png" alt="Colors used in the PetPals website" aria-label="Colors used in the PetPals website"/>
</div>

- light grey: #CCCCCC
- cadet blue crayola: #AAB7C4
- sapphire blue: #006994
- capri: #00BFFF
- gold web golden: #FFD700
- rossso corsa: #D80000

- The sapphire blue was chosen as the brand color for PetPals, as it provides a strong presence and is a fun color. 

- The yellow was chosen to provide a highlighting contrast for the logo and buttons. 

- The red was chosen to highlight prices and on sale items.

- The greys were chosen for this project to provide a neutral background color to information, making a clear seperation from the white background. 

### Styling

- Subtle box shadowing and curved corners were applied to buttons and form elements. 
- Curved corner styling was chosen for its friendly feel, and as it is a common stylistic choice of bootstrap it blends well with styles used from that library on this project.

## Wireframes

These wireframes were created using [Balsamiq](https://balsamiq.com/) during the Scope Plane part of the design and planning process for this project. 

- [Home](/static/images/readme/wireframe-home.png)
- [Items](/static/images/readme/wireframe-items.png)
- [Item Detail](/static/images/readme/wireframe-item-detail.png)

# Features

### Common Features 

#### Navbar

- The navigation bar is sticky to the top of the window so that it can be accessed at all times
- All of the main pages (other than the individual product pages) can be accessed from the navigation links
- On smaller screen sizes, all of the navigation links can be accessed via the hamburger button
- The brand logo will redirect the user back to the homepage when clicked
- The search bar allows users to search for items. 

#### Footer 

- The footer is displayed at the bottom of the page for all content sizes. 
- It contains links to socials, however these will just redirect to the website home pages for this project. The links open in a new page so as not the close the site page.

#### Toasts

- Toasts have been used to provide feedback to users, displaying success, error, info and warning messages.
- A toast is also used to display the current cart to the user when items are added to it.
- The cart toast will fade out automatically or can be dismissed using the close button. 

#### Admin - Features that are only available to admin accounts

- Admin's have an additional option available from the user icon dropdown in the navigation bar:
    - Item Management (used to add an item to the site).
- On individual item detail pages, buttons to edit and delete an item from the UI appear for admin users only.
    - The edit button will open a form containing the current item information
    - The delete button will delete the item. 
- Access to all the following are available via the Django admin site:
    - User Profiles
    - Item types
    - Items
    - Orders
    - Item reviews

### Page Features 

#### Home Page

- The home page displays 3 carousel images of pets. 
- Below the carousel images are the On Sale items, of which 8 are displayed on the home page. Below the On Sale items, is a button "See All On Sale", that will take the user to the "All Items On Sale" page. 
- The last section is "Shop by pet" which displays a button for each pet, that PetPals is selling items for. If you hover over the button, it displays the pet name, along with the icon. 

#### Items Page

- Users can select to view specific types of items from the navigation bar's dropdown link for each pet, or by using the tag buttons. 
- The pet item pages also contain a dropdown that allow users to sort by:
    - Name (A-Z)
    - Name (Z-A)
    - Category (A-Z)
    - Category (Z-A)
    - Price (Low - High)
    - Price (High - Low)

#### Item Details Page

- Item details include the item image, name, price and description. The description appears in a tab below the image and "Add to Cart" button. The tab has the option of showing ingredients, instructions, and FAQs, depending on whether the item has them. Description, Reviews and Write a review automatically appear for every item. 
- The reviews tab shows the reviews, which include the date created, review title, username of reviewer, and the review subject. 
- The Write a review tab, if the site user is not signed in, they will be prompted to log in or sign up. If the user is already signed in, this tab will contain a form allowing them to leave a review
- The quantity selector allow users to select 1-20 of a product.
- An "Add to Cart" button adds the item (with quantity) to the cart.

#### Cart Page

- Users can see all of the items that are in their cart
- The quantity of an item in the cart can be updated by updating the quantity and then clicking the "Update" button. This will reload the page, and update the cart totals.
- An item can be deleted from the cart by clicking the "Delete" button.
- There is a cart summary card which shows the Subtotal, Delivery and Total Amount. The delivery charge is automatically populated as 10% of the order charge. If the cart total is above the delivery threshold of "$50" then the delivery charge is set to 0. If the cart total is below the delivery threshold, the user is informed of how much more they need to spend to reach it.
- If the cart is empty, the "Secure Checkout" button is removed.

#### Checkout Page

- This page contains a form where users can enter their personal, delivery and card information.
- A summary of the order is shown so that users are reminded of what they are purchasing.
- At the bottom of the screen are two buttons allowing the user to either "Adjust cart" or "Complete Order".
- Underneath the "Complete Order" button, the user is reminded that their card will be charged $[ Order Amount ].

#### User Profile Page

- Users can use the "Default Information" form to submit default delivery information that will be autofilled next time they check out.
- The "Order History" section provides users with a last of their past orders. Clicking on the order number will direct the user to the order confirmation of that order so that they can see the order details in full.

# Information Architecture

### Database Choice

- As a framework Django works with SQL databases. I worked with the standard **sqlite3** database installed with Django.
- On deployment, the SQL database provided by Heroku is a **PostgreSQL** database. 

### Data Models

This project consists of the following 6 Django apps:

- **Home** - Displays the PetPal home page

- **Items** - Handles item display and individual item views

    - Type Model - Stores the items types


    ```python
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    ``` 

    - Item Model - Stores individual item information


    ```python
    type = models.ForeignKey('Type', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    instructions = models.TextField(null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)
    questions = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    onsale = models.BooleanField(default=False, null=True, blank=True)
    onsale_price = models.DecimalField(null=True, max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    ``` 

- **Cart** - Handles CRUD operations for items in cart

- **Checkout** - Display checkout page and handles payments

    - Order Model - Stores order information


    ```python
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
    ``` 

    - Order Line Model - Stores individual items within an order


    ```python
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    item = models.ForeignKey(Item, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
    ``` 

- **Profiles** - Displays user profile and stores user profile information and order history

    - UserProfile Model - Stores user profile information


    ```python
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)
    ``` 

- **Reviews** - Handles CRUD operations for product reviews

    - Review Model - Stores the review for the product


    ```python
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    ``` 

# Technologies Used

### Tools
- [Django](https://www.djangoproject.com/) as python web framework for rapid development and clean design.
- [Stripe](https://stripe.com) as payment platform to validate and accept credit card payments securely.
- [AWS S3 Bucket](https://aws.amazon.com/) to store images entered into the database.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) to enable creation, configuration and management of AWS S3.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) to style django forms.
- [Django Storages](https://django-storages.readthedocs.io/en/latest/) a collection of custom storage backends with django to work with boto3 and AWS S3.
- [Gunicorn](https://pypi.org/project/gunicorn/) WSGI HTTP Server for UNIX to aid in deployment of the Django project to heroku.
- [Pillow](https://pillow.readthedocs.io/en/stable/) as python imaging library to aid in processing image files to store in database.
- [Psycopg2](https://pypi.org/project/psycopg2/) as PostgreSQL database adapter for Python.
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03) to handle version control.
- [GitHub](https://github.com/) to store and share all project code remotely. 
- [Browserstack](https://www.browserstack.com/) to test functionality on all browsers and devices.
- Heroku for deployment
- [Google Chrome Developer Tools](https://developer.chrome.com/docs/devtools/) used to inspect page elements, test different CSS styles and debug site issues using the console
- [Balsamiq](https://balsamiq.com/) to create the wireframes for this project.

### Databases
- [PostgreSQL](https://www.postgresql.org/) for production database, provided by heroku.
- [SQlite3](https://www.sqlite.org/index.html) for development database, provided by django.

### Libraries
- [JQuery](https://jquery.com) to simplify DOM manipulation.
- [Bootstrap](https://www.bootstrapcdn.com/) to simplify the structure of the website and make the website responsive.
- [FontAwesome](https://www.bootstrapcdn.com/fontawesome/) to provide icons for PetPals website. 
- [Google Fonts](https://fonts.google.com/) to style the website fonts.

### Languages
- This project uses HTML, CSS, JavaScript and Python programming languages.

# Testing 

Testing information can be found in separate [TESTING.md](TESTING.md) file.

# Deployment

## How to run this project locally

To run this project on your own IDE follow the instructions below:

Ensure you have the following tools: 
    - An IDE such as [Visual Studio Code](https://code.visualstudio.com/)

The following **must be installed** on your machine:
    - [PIP](https://pip.pypa.io/en/stable/installing/)
    - [Python 3](https://www.python.org/downloads/)
    - [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)

To allow you to access all functionality on the site locally, ensure you have created free accounts with the following services:
    - [Stripe](https://dashboard.stripe.com/register)
    - [AWS](https://aws.amazon.com/) and [set up an S3 bucket](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)

Please click the links above for documentation on how to set these up and retrieve the necessary environment variables.

### Instructions
1. Save a copy of the github repository located at https://github.com/MAN95-dev/PetPals by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command.
    ```
    git clone https://github.com/MAN95-dev/PetPals
    ```

2. Open your preferred IDE, open a terminal session in the unzip folder or cd to the correct location.

3. A virtual environment is recommended for the Python interpreter, I recommend using Pythons built in virtual environment. Enter the command:
    ```
    python -m .venv venv
    ```  
_NOTE: The `python` part of this command and the ones in other steps below assumes  you are working with a windows operating system. Your Python command may differ, such as `python3` or `py`_

4. Activate the .venv with the command:
    ```
    .venv\Scripts\activate 
    ```
_Again this **command may differ depending on your operating system**, please check the [Python Documentation on virtual environments](https://docs.python.org/3/library/venv.html) for further instructions._

5. If needed, Upgrade pip locally with
    ```
    pip install --upgrade pip.
    ```

6. Install all required modules with the command 
    ```
    pip -r requirements.txt.
    ```

7. Set up the following environment variables within your IDE. 

    - If using VSCode, locate the `settings.json` file within the .vscode directory and add your environment variables as below. Do not forget to restart your machine to activate your environment variables or your code will not be able to see them: 

    ```json
    "terminal.integrated.env.windows": {
        "HOSTNAME": "<enter hostname here>",
        "DEV": "1",
        "SECRET_KEY": "<your secret key>",
        "STRIPE_PUBLIC_KEY ": "<insert stripe public key>",
        "STRIPE_SECRET_KEY": "<insert stripe secret key>",
        "STRIPE_WH_SECRET": "<insert stripe webhook secret>",
        "EMAIL_HOST_PASS": "<insert the gmail password>",
        "EMAIL_HOST_USER": "<insert your email address>",
        "STRIPE_WH_SECRET": "<enter key here>",
        "AWS_ACCESS_KEY_ID": "<enter key here>",
        "AWS_SECRET_ACCESS_KEY": "<enter bucket name here>",
        "USE_AWS": "True",
    }
    ```

    - If using an IDE that includes a `bashrc` file, open this file and enter all the environment variables listed above using the following format: 
    ```
    HOSTNAME="<enter key here>"
    ```
    - `HOSTNAME` should be the local address for the site when running within your own IDE.
    - `DEV` environment variable is set only within the development environment, it does not exist in the deployed version, making it possible to have different settings for the two environments. For example setting DEBUG to True only when working in development and not on the deployed site.

8. If you have restarted your machine to activate your environment variables, do not forget to reactivate your virtual environment with the command used at step 4.

9. Migrate the admin panel models to create your database template with the terminal command
    ```
    python manage.py migrate
    ```

10. Create your superuser to access the django admin panel and database with the following command, and then follow the steps to add your admin username and password:
    ```
    python manage.py createsuperuser
    ```

11. You can now run the program locally with the following command: 
    ```
    python manage.py runserver
    ```

12. Once the program is running, go to the local link provided and add `/admin` to the end of the ur. Here log in with your superuser account and create instances of ShippingDestination and Product within the new database.

13. Once instances of these items exist in your database your local site will run as expected.

## Heroku Deployment

To deploy PetPals to heroku, take the following steps:

1. Create a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Create a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to whichever is applicable for your location.

4. From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

5. Confirm the linking of the heroku app to the correct GitHub repository.

6. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7. Set the following config vars:

| Key | Value |
--- | ---
AWS_ACCESS_KEY_ID | `<insert from the aws csv>`
AWS_SECRET_ACCESS_KEY | `<insert from the aws csv>`
DATABASE_URL | `<your postgres database url>`
EMAIL_HOST_PASS | `<insert the gmail password>`
EMAIL_HOST_USER | `	<insert your email address>`
SECRET_KEY | `<your secret key>`
STRIPE_PUBLIC_KEY | `<insert stripe public key >`
STRIPE_SECRET_KEY | `<insert stripe secret key >`
STRIPE_WH_SECRET | `<insert stripe webhook secret>`
USE_AWS | `True`

8. From the command line of your local IDE:
    - Enter the heroku postres shell 
    - Migrate the database models 
    - Create your superuser account in your new database
    
     Instructions on how to do these steps can be found in the [heroku devcenter documentation](https://devcenter.heroku.com/articles/heroku-postgresql).

9. In your heroku dashboard, click "Deploy". Scroll down to "Manual Deploy", select the master branch then click "Deploy Branch".

10. Once the build is complete, click the "View app" button provided.

11. From the link provided add `/admin` to the end of the url, log in with your superuser account and create instances of ShippingDestination and Product within the new database.

12. Once instances of these items exist in your database your heroku site will run as expected.

# Credits

## Content
- All item content and descriptions were taken from the [EntirelyPets](https://entirelypets.com/) website.

### Images
- All product images were taken from the [EntirelyPets](https://entirelypets.com/) website.
- The carousel images were taken from [shutterstock](https://www.shutterstock.com/).
- The mockup image in the README.md file was created using [Techsini](https://techsini.com/).

## Code
- [Code Institute](https://codeinstitute.net/) - Code learnt during the Full Stack Web Developer course (specifically the Boutique-Ado project) has been implemented in this project.

- The following websites provided inspiration for my website.
    - [EntirelyPets](https://www.entirelypets.com/)
    - [Petco](https://www.petco.com/shop/en/petcostore)
    - [Chewy](https://www.chewy.com/)

- The README file was taken from Anna Greave's 'The House of Mouse' project to use as a template.
    - [The House of Mouse by Anna Greaves ](https://github.com/AJGreaves/thehouseofmouse)
    
## Acknowledgements
- Special thanks to my mentor Moosa, for his time, and guidance with this project.
- Code Institute tutors for helping support and guide me in the right direction with my code.