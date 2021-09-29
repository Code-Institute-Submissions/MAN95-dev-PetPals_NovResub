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
    - [Existing Features](#existing-features)
        - [Elements on every Page](#elements-on-every-page)
        - [Home Page](#home-page)
        - [Dogs Page](#dogs-page)
        - [Cats Page](#cats-page)
        - [Small Pets Page](#small-pets-page)
        - [Birds Page](#birds-page)
        - [Fish Page](#fish-page)
        - [Reptiles Page](#reptiles-page)
        - [On Sale Page](#on-sale-page)
        - [Register Page](#register-page)
        - [Login Page](#login-page)
        - [Profile Page](#profile-page)
	- [Product Management Page](#product—management-page)
        - [Log out Page](#log-out-page)
        - [Cart Page](#cart-page)
        - [Checkout](#checkout)
    - [Features for Future Releases](#features-for-future-releases)

5. [Information Architecture](#information-architecture)
    - [Database choice](#database-choice)
    - [Data Models](#data-models)
        - [User](#user)
        - [Products App Model](#products-app-model)
        - [Cart App Models](#cart-app-models)

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

As a visitor to The House of Mouse website I expect/want/need:

1. To easily find what I am looking for, I want the layout of the site to make sense so I am not confused or put off using it. 

1. The information I am presented with to be laid out in a way that is easy for me to navigate and digest, so that I find what I need quickly and efficiently.

1. The ability to search through small amounts of information to find what I need, and then be able to easily click to get more detailed information when I need it.

1. The site to be easily navigable from any device, desktop, tablet or phone. For the content to look good and be useable on all of these devices.

1. To learn more about the shop owner and their process, so that I can be assured I am buying from a small handmade business. 

1. To be able to read reviews of this shop from previous customers, to build trust in my purchase.

1. For all information and images to be laid out in a clear and easy to understand way, on whatever size screen I am viewing the website on.

1. Plenty of high quality images of the products for sale, so I have a clear idea of what I am buying and can see the quality of the products up close.

1. To be able to easily find out all the information I need to make an informed purchase. I expect information about materials, measurements, safety and packaging to be available on every listing page.

1. To be informed if I try to order more items than are available in stock.

1. For recorded stock levels to be accurate, so there are no delays in receiving my order.

1. A text search function so that I can quickly narrow down my search when looking for something specific.

1. A clear terms and conditions and privacy policy.

1. There to be a frequently asked questions page for any further questions I might have about my order.

1. To be able to see a summary of my order on every page of the checkout process.

1. That once I am logged in I can access my account details and update them if I need to. 

1. To be able to find information on my past orders and how to cancel an order. 

1. To be able to connect to the businesses social media channels and/or newsletter, to keep up to date with new listings on the site. 

1. To be able to easily get in contact with the shop owner via a contact form.

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

# Testing 

Testing information can be found in separate [TESTING.md](TESTING.md) file

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