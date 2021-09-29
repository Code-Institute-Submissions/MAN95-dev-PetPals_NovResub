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

The House of Mouse website has an overall child like, joyful feel, with emphasis on the high quality, artisan handmade feel of the products on sale. The following design choices were made with this in mind:

### Fonts
<div align="center">
    <img src="https://i.ibb.co/zP4PPRh/Clipboard01.jpg" alt="Fonts used on The House of Mouse website" aria-label="Fonts used on The House of Mouse website" />
</div>

- The primary font 'Lato' was chosen for the main text of the site because of it clear readability, clean style and complementary contrast with the secondary font. This font also looks good in uppercase with a little extra letter spacing, and so could serve nicely as a sub heading as well.

- The secondary font 'Emilys Candy' was chosen for the main headings because it is whimsical, childlike and the curled ends to some of the letters look like mouse tails.

### Icons
<div align="center">
    <img src="https://i.ibb.co/Cb3k6vM/Clipboard01.jpg" alt="Icons used on The House of Mouse Home Page" aria-label="Icons used on The House of Mouse Home Page" />
</div>

- In order to keep the site uncluttered only a few icons were utilized. 
- The **search** icon and **shopping cart** icons were used in the navigation bar as they are conventionally used in this setting and would be what the user expects to see.
- Yellow **cheese icons** are used as pointers between breadcrumb links on pages that have worked their way deeper into the hierarchical structure of the website information. These were used to add a little humour to a usually boring aspect of a website.
- On the home page the important facts about The House of Mouse are laid out using icons and simple text for quick assimilation of info (see image above).
- **Star icons** are used in the testimonials section of the home page, to emphasize the high level of reviews the shop already has on Etsy.
- The **Facebook logo** icon is included in the footer to lead visitors to The House of Mouse facebook page.

### Colours

- light pink: #FFE4E6
- pink: #FFBABE
- dark grey: #373737
- light grey: #E5E5E5
- light blue: #7ccfff

- The brand colours for this project were chosen because the two shades of pink and two shades of grey are taken from the felt mice ears and standard body color. This helps to pull the colours of the site together with the product photographs. 

- The blue was chosen to provide a highlighting contrast for links, prices and important buttons for the user such as "add to cart" and "checkout now".

### Styling

- Subtle box shadowing and curved corners were applied to elements that needed a little extra emphasis and style. For example on product images, cart summary and form wrappers. 
- In cases where an area is clickable, for example product images or call to action buttons, the shadow size is increased and animated when the user hovers over that element, this was done to make the area more tempting to click.
- Curved corner styling was chosen for its friendly feel, and as it is a common stylistic choice of bootstrap it blends well with styles used from that library on this project.

## Wireframes

These wireframes were created using [Balsamiq](https://balsamiq.com/) during the Scope Plane part of the design and planning process for this project. 

- [Home](/static/images/readme/wireframe-home.png)
- [Items](/static/images/readme/wireframe-items.png)
- [Item Detail](/static/images/readme/wireframe-item-detail.png)