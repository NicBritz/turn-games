![](https://img.shields.io/badge/Django-3.1-orange)


## Overview 
[![Home page](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,w_512/v1601467361/f7355fb508f84512843864bb5a26ba30_1_1920_y9dqug.jpg)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601467361/f7355fb508f84512843864bb5a26ba30_1_1920_y9dqug.jpg)

[![turn games](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,f_auto,w_209/v1601468661/turn_games_logo_cn5k5t.png)](https://turn-games.herokuapp.com/) is an e-commerce digital video game store, the site offers a wide variety of visual entertainment content. Users can browse the sites extensive inventory and filter down the content for easier navigation. Users are also able to search the site by use of a search bar that is always readily available. 

The landing page will show any content that the site owner has added to the featured or discounted sections. It will randomly select ten titles to display on the main page image slider.

Users are easily able to view more information about the game simply by selecting the content card. In the game inspection area a user can either rate a game with a thumbs up or a thumbs down and add the game to their basket for purchase once they have finished browsing. You can view the site by following [this link.](https://turn-games.herokuapp.com/)


## Table of Contents

- [Overview](#Overview)
- [UX](#ux)
  - [user](#User)
  - [design](#design)
  - [Wireframes](#wireframes)
   - [Home page](#Home-page)
  - [Trello](#Trello)
  - [Database Schema](#Database-Schema)
- [Features](#Features)
  - [The navigation bar](#The-navigation-bar)
  - [Main Slider](#Main-Slider)
  - [Game cards](#Game-cards)
  - [Pagination](#Pagination)
  - [Footer](#Footer)
  - [Sign-in](#Sign-in)
  - [Registration](#Registration)
  - [Game view](#Game-view)
  - [Error handling](#Error-handling)
  - [Code structure](#Code-structure)
  - [Features Left to Implement](#Features-Left-to-Implement)
- [Technologies Used](#Technologies-Used)
  - [Other Tools](#Other-Tools)
- [Testing](#Testing)
 - [W3C Markup](#W3C-Markup)
 - [W3C CSS](#W3C-CSS)
 - [Autoprefixer](#Autoprefixer)
 - [Unit Testing](#Unit-Testing)
 - [CI/CD](#CI/CD)
 - [Google Lighthouse](#Google-Lighthouse)
 - [Browser and Device Testing](#Browser-and-Device-Testing)
 - [User Testing](#User-Testing)
- [Deployment](#Deployment)
 - [Prerequisites](#Prerequisites)
 - [Development](#Development)
 - [Cloning](#Cloning)
 - [Requirements](#Requirements)
 - [Environment Variables](#Environment-Variables)
 - [Contribution](#Contribution)
- [Deployment](#Deployment)
 - [Credits](#Credits)
   - [Content](#Content)
   - [Media](#Media)
    - [Images](#Images)
 - [Acknowledgements](#Acknowledgements)
   - [Inspiration](#Inspiration)
   - [code](#code)

----



## UX

### User Stories

#### Viewing and Navigation
| Done | As a... | I would like to be able to... | So that I may...|
| ---- | ------- | ----------------------------- | --------------- |
| &checkmark; | user | view a list of available games.  | Select some to purchase.|
| &checkmark; | user | view individual game details.  | view the price, description, game rating.|
| &checkmark; | user | quickly identify discounts and special offers. | take advantage of savings on games that id like to purchase.|
| &checkmark; | user | easily View the total of my cart at any time. | avoid over spending.|

#### Registration and User Accounts
| Done | As a... | I would like to be able to... | So that I may...|
| ---- | ------- | ----------------------------- | --------------- |
| &checkmark; | user | easily register for an account. | have a personal account to be able to view my profile.|
| &checkmark; | user | easily login or logout. | access my personal account information.|
| &checkmark; | user | log into my account using Google. | easily access my profile without site registration.|
| &checkmark; | user | easily recover my password. | recover access to my account if I forget my credentials.|
| &checkmark; | user | receive an email confirmation after registering. | verify that my account registration was successful.|
| &checkmark; | user | have a personalized user profile. | view my personal order history and order confirmations, and save my payment information.|

#### Scrolling and Searching
| Done | As a... | I would like to be able to... | So that I may...|
| ---- | ------- | ----------------------------- | --------------- |
| &checkmark; | user | sort the list of available games. | easily identify the best rated, best priced games.|
| &checkmark; | user | sort by a specific genre of game. | find the best-priced or best-rated product in a specific genre.|
| &checkmark; | user | sort by a specific category of game. | find the best-priced or best-rated product in a specific category.|
| &checkmark; | user | sort by a specific game tag. | find the best-priced or best-rated product with a specific tag.|
| &checkmark; | user | search for a product by name or description. | find a specific product I would like to purchase.|
| &checkmark; | user | easily see what I have searched for and the number of results. | quickly decide whether the product I want is available.|

#### Purchasing and Checkout
| Done | As a... | I would like to be able to... | So that I may...|
| ---- | ------- | ----------------------------- | --------------- |
| &checkmark; | user | easily add or remove the game I want purchase. | easily make changes to my purchase before checkout.|
| &checkmark; | user | view items in my bag to be purchased. | identify the total cost of my purchase and all the games I will receive.|
| &checkmark; | user | easily enter my payment information. | checkout quickly with no hassles.|
| &checkmark; | user | feel my personal and payment information is safe and secure. | confidently provide the needed information to make a purchase.|
| &checkmark; | user | view an order confirmation after checkout. | verify that I have not made any errors.|
| &checkmark; | user | receive an email confirmation after checking out. | keep the confirmation of what I have purchased for my records.|

#### Admin and Store Management
| Done | As a... | I would like to be able to... | So that I may...|
| ---- | ------- | ----------------------------- | --------------- |
| &checkmark; | user | add a game. | add new games to my store.|
| &checkmark; | user | edit a game. | change product prices, descriptions, images and other criteria.|
| &checkmark; | user | delete a game. | remove games that are no longer for sale.|
| &checkmark; | user | have access to an admin dashboard. | manage users games and orders.|
| &checkmark; | user | view any previous order made. | see what was purchased and when.|
| &checkmark; | user | see a chart with the past 30 days sales. | see how the site is doing financially.|




### Design

The goal of this project was to create a digital game e-commerce store that makes use of Django as its primary technology. The site is designed to be responsive and neat without compromising on the primary goal of selling games. There are subtle visual elements added to purposely attract the eye to important things like discounts and price total.

### Wireframes
Before starting the project I used [figma](https://www.figma.com/) to create the wireframe mockups for the project. This was an instrumental step to ensure a clear design direction. The site did not end up looking exactly like the mockups in the end but the general design is visible in the final result.

#### Home page

[![Home page](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,w_512/v1601465525/Wireframe_Home_Page_zncp8i.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601465525/Wireframe_Home_Page_zncp8i.png)

#### All Games

[![All Games](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,w_512/v1601465525/Wireframes_Games_arjtyd.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601465525/Wireframes_Games_arjtyd.png)

#### Game Details

[![Game Details](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,w_512/v1601465525/Wireframes_Details_ebw9mf.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601465525/Wireframes_Details_ebw9mf.png)


### Trello

To keep track of the project I made use of a Trello board. The board was used to keep track of progress add ideas when they spring to mind and keep track of online resources. You can view the board [here](https://trello.com/b/dRoiHJLF/milestone-4-turn-games)

[![Trello Board](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,w_512/v1601467944/Trello_bdvuax.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601467944/Trello_bdvuax.png)


### Database Schema
The database used for development of the project was [SQLite](https://www.sqlite.org/index.html) which was later moved to [Heroku](https://www.heroku.com/) using the postgres addon. Below is a visualisation of the database schema.
[![Trello Board](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,w_1024/v1601470354/Database_Diagram_mvltor.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601470354/Database_Diagram_mvltor.png)

## Features

### The navigation bar


I created a favicon ![favicon](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,f_auto,w_24/v1601471645/turn-games-favicon_yjuqcj.png) with the logo that I designed for the site, it feel it just gives the site a more finished look. 

[![NAv Menu](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,w_1024/v1601471156/Navbar_vzeonj.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601471156/Navbar_vzeonj.png)

The navigation bar was designed to look neat and only show the minimum amount of menu items possible. In a desktop environment this navigation menu has the logo which is also a link to the home page. I added small coloured icons to give the site a 'gamey feel', as I felt it would be suitable for the sites intended audience. There are dropdown menus to navigate the site and filter through the various game categories and genres. I have also added the account menu here for easy access as well as a shopping cart button that shows the current value if the items in the cart.

[![NAv Mobile](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,h_50/v1601472692/mobile_Nav_uc2dp9.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601472692/mobile_Nav_uc2dp9.png)
[![Mobile Menu](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,h_172/v1601473355/mobile_menu_l0u2ys.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,w_172/v1601473355/mobile_menu_l0u2ys.png)

When viewing the website on a mobile device the menu completely collapses into an animated hamburger menu. There are some slight changes to the items in the menu on mobile devices, this was a decision made to keep the site neat.

### Account Menu

[![Account Menu](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,h_172/v1601473834/account_menu_znxppe.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601473834/account_menu_znxppe.png)

The account menu changes dynamically depending on the following factors:

- User not logged in
    - Menu displays: `login` & `Register`
    
- Standard user logged in
    - Title displays: `your-usersname`
    - Menu displays: `Profile` & `Logout`

- Admin user logged in
    - Title displays: `your-usersname`
    - Menu displays: `Admin Dashboard` & `Profile` & `Logout` 

### Shopping Cart button

[![Account Menu](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,h_250/v1601474862/cart_fr7k19.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601474862/cart_fr7k19.png)

When choosing to purchase items from the site they will get added to your shopping cart. The button will update its label to display the current value of the games in your cart. 

Hovering over the menu on a desktop will present the above pictured menu, here you can preview the items currently in your cart as well a select an item to link back to it. I decided to exclude this feature fom the mobile versions as it was looking a bit cluttered.

### Home Page Slider

[![MAin Slider](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,w_1024/v1601475345/slider_yf5mvc.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601475345/slider_yf5mvc.png)

Using a css library called [Flickety](https://flickity.metafizzy.co/) I implemented a slider for the home page. I wanted it not only to be responsive but also make use of the ability to drag through slides on mobile devices. 

Hovering over a slide will also stop the slides from scrolling automatically. The layout of this slider will also change depending on the device its viewed on, again this was a decision based on keeping the site looking neat. 

### Game Cards

[![Game Card](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601476112/card_o80dfe.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601476112/card_o80dfe.png)

The game cards are the main way a game is chosen to be purchased. I tried to keep them looking as simple as possible. The cards are also direct links to the more detailed game view. The ratings are clearly displayed on the footer of each card as well as the prices. If a card has a discount attached to it there will be a ribbon in the top right corner indicating the discount percent. There will also be a red price indicating the old / new prices.

### Content Filtering

[![Game Card](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,w_512/v1601476847/filtering_wxoc3p.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601476847/filtering_wxoc3p.png)

If a users chooses any filers in the main navigation menu or chooses to search the site for a particular game, they will be presented with a new view. This is essentially a view that contains all the games and it can be sorted in various ways using th sort dropdown. There is also an indication on the current filter ie: Adventure as above picture indicates. Here you will also see the number of results found under the current search criteria by pressing the red cross users can clear all filters. 

### Game Details

[![Game Details](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,w_1024/v1601477446/details_f2ekjo.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601477446/details_f2ekjo.png)

The game details page gives the user a final overview of the game. This includes things the description, developer information and any associated tags. These tags, categories and genres are also links so that a user can easily view more games like the one they are currently interested in. This is also where the Buy button resides. clicking this will of course add the game you the cart. If a user tries to add more than one of the same game in the cart they will be presented with a message that the game is already in the cart. This is by design as this is essentially a digital app store so you would not buy a game you already own.   

In the case of a site administrator using the detailed game view will show an edit button so that the game can easily be edited without having to access the game through the administrator dashboard. 

### Footer

[![Footer](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,w_1024/v1601478449/footer_wt7ejk.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601478449/footer_wt7ejk.png)

The footer is simple by design and only contains some social links. hovering over the links will change their colours to the correct brand specific colours. Clicking them will open the relevant social page in a new tab. 

On mobile devices the footer has been moved inside the hamburger menu to make use of maximum screen space for site content.

### Sign-in

[![Sign in](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,h_250/v1601478940/Sign_in_ldzvxz.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601478940/Sign_in_ldzvxz.png)

The site makes use of Django allauth to handle its user login authentication. I have styled all the standard allauth templates to align with the sites design. I have also implemented the ability to sign in with your Google account. This makes site registration and login very simple. 

### User Profile

[![Profile](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,h_512/v1601479205/profile_louz26.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601479205/profile_louz26.png)

The profile page features the ability to add your personal information to make the checkout process faster. From here users can also view all their previous orders and update their email and password. By selecting the order number a user can see a more detailed view of the order. 

### Shopping cart 

[![Cart](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,h_512/v1601479575/shopping_cart_aqjqbc.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601479575/shopping_cart_aqjqbc.png)

The shopping cart view displays all the games in your cart in detail. from this view you can start the checkout process or go back to browse the store. Games can also be removed from your cart in this view by selecting the red cross situated to the left of the games image. There is also an indication oof the total value of the items in the cart taking the tax percentage into account. 

There is a step indication at he top of the view to show the current progress ing the checkout process. By selecting the secure checkout button a user can begin the checkout process.

#### Checkout View

[![Checkout](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,h_512/v1601480219/Checkout_qtof8r.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601480219/Checkout_qtof8r.png)

Here a user can fill in their information to make payment for the items in their cart. Required information is indicated with a red astrix. The credit card section makes use of [stripe](https://stripe.com/) as the payment technology. 

If all the information is correct and the user chooses to submit, then the payment intent will be sent to stripe for processing. There is a webhook implemented as a precaution against errors during this process. The submit button is disabled and replaced with a loading indicator to show there is an action in progress. 

### Checkout Success

[![Checkout](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,h_512/v1601481147/success_jophri.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601481147/success_jophri.png)

Upon successful completion of the order a user will be presented with the above success screen. The customer will get an email also at this point confirming their order. If the user is logged in as a registered user a copy of the order will also mow be available in their profile page. This is also the same page layout used when viewing any previous orders.

### Administrator Dashboard

[![Checkout](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,h_512/v1601486394/dashboard_ppi6tt.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601486394/dashboard_ppi6tt.png)

The Administrator Dashboard acts as a central hub for site administrators to manage the site. The dashboard page features a chart that shows the value of sales over the past 30 days. I used a JS library to achieve this and display it in a canvas element. Here you are also able to see the last 10 database logs with icons that indicate weather it was an edit, delete, add or just general information. 

Just below the heading section there are four cards indicating some site information. 

Here you are able to see: 
- The current number of registered site users.
- The total amount of games currently in the database.
- The number of orders to date.
- The total value of all sales.

These are also links to the relevant management views, these links can also be found in the management dropdown in the main nav-bar.

### User Management

[![Checkout](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,h_512/v1601487178/users_vgqosg.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601486394/dashboard_ppi6tt.png)

In this section of the admin dashboard, site admins can see all currently registered users. Administrators can search for users by name using the searchbar at the top of the table to filter the list. From this view you can see the username, date last seen and you can delete users by selecting the trash can to the right of the user you would like to delete. I have disabled the delete functionality in this view for site admins to avoid accidental deletions.

### Game Management

[![Checkout](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,h_512/v1601487281/game_management_vh6jsb.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601487281/game_management_vh6jsb.png)

The game management page allows the admin user to manage the current games in the database. This view also features a search bar for filtering game titles. Game are listed in a table with an edit button to the left of each row for easy game editing and delete button to the right tp delete the game from the database. 

On the top left of the table there is an add button where an admin can add a new game to the database.

### Add or Edit Game

[![Checkout](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,h_512/v1601487775/edit_t4eenz.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601487775/edit_t4eenz.png)

Adding or editing a gme is done in the the same way. Administrators are presented with the form view pictured above. Here they are able to fill in or edit game details. Games marked with the featured checkmark or discounted checkmark will be added to the home pages and may be randomly selected to be featured on the main page slider. 

[![upload](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,h_150/v1601488118/cloudinary_ffmlsl.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601488118/cloudinary_ffmlsl.png)

I am using Cloaudinary(https://cloudinary.com/) ad my CDN to manage the sites media. For this site I have implemented their media upload widget as it is a very powerful javascript tool. I have set the tool up to resize any images to the correct size for the website.   

### Error handling

[![404](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,h_512/v1601488938/404_xuo7jx.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601488938/404_xuo7jx.png)

I have implemented custom error pages to keep with the site theme, images are from [Drlinkcheck](https://www.drlinkcheck.com/blog/free-http-error-images).

### Code structure

Below is an outline of the file and folder structure of the project as a whole. I have tried to keep things as organised as possible although the amount on files are overwhelming at times.

``` txt
.
├── cart
│   ├── apps.py
│   ├── contexts.py
│   ├── __init__.py
│   ├── migrations
│   ├── templates
│   │   └── cart
│   │       └── cart.html
│   ├── tests
│   │   ├── __init__.py
│   │   └── test_views.py
│   ├── urls.py
│   └── views.py
├── checkout
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0006_order_user_profile.py
│   │   ├── __init__.py
│   ├── models.py
│   ├── signals.py
│   ├── static
│   │   └── checkout
│   │       ├── css
│   │       │   └── checkout.css
│   │       └── js
│   │           └── stripe_elements.js
│   ├── templates
│   │   └── checkout
│   │       ├── checkout.html
│   │       ├── checkout_success.html
│   │       └── confirmation_emails
│   │           ├── confirmation_body.txt
│   │           └── confirmation_subject.txt
│   ├── tests
│   │   ├── __init__.py
│   │   ├── test_forms.py
│   │   ├── test_models.py
│   │   └── test_views.py
│   ├── urls.py
│   ├── views.py
│   ├── webhook_handler.py
│   └── webhooks.py
├── custom_storages.py
├── dashboard
│   ├── apps.py
│   ├── forms.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   ├── static
│   │   └── dashboard
│   │       ├── css
│   │       │   └── dashboard.css
│   │       └── js
│   │           ├── cloudinary.js
│   │           └── dashboard.js
│   ├── templates
│   │   ├── dashboard
│   │   │   ├── add_game.html
│   │   │   ├── dashboard_base.html
│   │   │   ├── dashboard.html
│   │   │   ├── edit_game.html
│   │   │   ├── games_management.html
│   │   │   ├── order_management.html
│   │   │   ├── order_view.html
│   │   │   └── user_management.html
│   │   └── includes
│   │       ├── dashboard_nav.html
│   │       └── info_tiles.html
│   ├── tests
│   │   ├── __init__.py
│   │   ├── test_forms.py
│   │   └── test_views.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── games
│   ├── admin.py
│   ├── apps.py
│   ├── fixtures
│   │   ├── categories.json
│   │   ├── games.json
│   │   ├── genres.json
│   │   └── tags.json
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0025_game_price_discounted.py
│   │   ├── __init__.py
│   ├── models.py
│   ├── static
│   │   └── games
│   │       └── js
│   │           └── games.js
│   ├── templates
│   │   ├── games
│   │   │   ├── game_detail.html
│   │   │   └── games.html
│   │   └── includes
│   │       └── sort_dropdown.html
│   ├── tests
│   │   ├── __init__.py
│   │   ├── test_models.py
│   │   └── test_views.py
│   ├── urls.py
│   └── views.py
├── home
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── __init__.py
│   ├── static
│   │   └── home
│   │       ├── css
│   │       │   ├── flickity.css
│   │       │   └── home.css
│   │       └── js
│   │           ├── flickity.pkgd.min.js
│   │           └── home.js
│   ├── templates
│   │   └── home
│   │       └── index.html
│   ├── tests
│   │   ├── __init__.py
│   │   └── test_views.py
│   ├── urls.py
│   └── views.py
├── htmlcov
│   ├── coverage_html.js
│   ├── index.html
│   ├── status.json
│   └── style.css
├── manage.py
├── media
│   └── header.jpg
├── Procfile
├── profiles
│   ├── apps.py
│   ├── forms.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   ├── models.py
│   ├── static
│   │   └── profiles
│   │       └── css
│   │           └── profile.css
│   ├── templates
│   │   └── profiles
│   │       └── profile.html
│   ├── tests
│   │   ├── __init__.py
│   │   ├── test_forms.py
│   │   ├── test_models.py
│   │   └── test_views.py
│   ├── urls.py
│   └── views.py
├── README.md
├── requirements.txt
├── static
│   ├── css
│   │   ├── all_auth.css
│   │   └── base.css
│   ├── images
│   │   ├── turn-games-full-logo.webp
│   │   ├── turn-games-logo.svg
│   │   ├── turn-games-text.png
│   │   └── turn-games-text.webp
│   └── js
│       └── base.js
├── templates
│   ├── 404.html
│   ├── 500.html
│   ├── allauth
│   │   ├── account
│   │   │   ├── account_inactive.html
│   │   │   ├── base.html
│   │   │   ├── email
│   │   │   │   ├── email_confirmation_message.txt
│   │   │   │   ├── email_confirmation_signup_message.txt
│   │   │   │   ├── email_confirmation_signup_subject.txt
│   │   │   │   ├── email_confirmation_subject.txt
│   │   │   │   ├── password_reset_key_message.txt
│   │   │   │   └── password_reset_key_subject.txt
│   │   │   ├── email_confirm.html
│   │   │   ├── email.html
│   │   │   ├── login.html
│   │   │   ├── logout.html
│   │   │   ├── messages
│   │   │   │   ├── cannot_delete_primary_email.txt
│   │   │   │   ├── email_confirmation_sent.txt
│   │   │   │   ├── email_confirmed.txt
│   │   │   │   ├── email_deleted.txt
│   │   │   │   ├── logged_in.txt
│   │   │   │   ├── logged_out.txt
│   │   │   │   ├── password_changed.txt
│   │   │   │   ├── password_set.txt
│   │   │   │   ├── primary_email_set.txt
│   │   │   │   └── unverified_primary_email.txt
│   │   │   ├── password_change.html
│   │   │   ├── password_reset_done.html
│   │   │   ├── password_reset_from_key_done.html
│   │   │   ├── password_reset_from_key.html
│   │   │   ├── password_reset.html
│   │   │   ├── password_set.html
│   │   │   ├── signup_closed.html
│   │   │   ├── signup.html
│   │   │   ├── snippets
│   │   │   │   └── already_logged_in.html
│   │   │   ├── verification_sent.html
│   │   │   └── verified_email_required.html
│   │   ├── base.html
│   │   └── socialaccount
│   │       ├── authentication_error.html
│   │       ├── base.html
│   │       ├── connections.html
│   │       ├── login_cancelled.html
│   │       ├── messages
│   │       │   ├── account_connected_other.txt
│   │       │   ├── account_connected.txt
│   │       │   ├── account_connected_updated.txt
│   │       │   └── account_disconnected.txt
│   │       ├── signup.html
│   │       └── snippets
│   │           ├── login_extra.html
│   │           └── provider_list.html
│   ├── base.html
│   └── includes
│       ├── footer.html
│       ├── main-nav.html
│       ├── messages
│       │   ├── message_error.html
│       │   ├── message_info.html
│       │   ├── message_success.html
│       │   └── message_warning.html
│       └── messages.html
└── turn_games
    ├── asgi.py
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

90 directories, 398 files
```

### Stripe Payments

[![stripe](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,h_512/v1601498410/stripe_p1kqus.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601498410/stripe_p1kqus.png)

Using [Stripe](https://stripe.com/) I was able to implement a payment system, the above image shows the successful transaction history.

### Features Left to Implement

This project was a lot of fun and there are just so many features i would like to have implemented but ran short on time, I listed some of the key features below.

- setting up cards to all fave a fixed max size
- more work on rating system and user profile areas
- avatars for user profiles
- more charts and greater control of content in the admin dashboard
- printing of order forms


[Contents](#Table-of-Contents)

---

## Technologies Used

The following is a list of tools and technologies I used to create this website:


- [Python 3.8.3](https://www.python.org/)
  - Used for backend data manipulation
- [Django 3.1.1](https://www.djangoproject.com/)
  - Used as main python framework
- [Jinja2 2.11.2](https://pypi.org/project/Jinja2/)
  - Used as the main templating language for template manipulation
- [Cloudinary 1.21.0](https://cloudinary.com/)
  - Used to access the Cloudinary CDN server for image management
- [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
  - Used as the main language for the templates
- [CSS3](https://www.w3.org/Style/CSS/current-work.en.html)
  - Used for styling the webpage
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
  - Used for some front end functionality
- [Git](https://git-scm.com/)
  - Used for version control
- [Google fonts](https://fonts.google.com/)
  - Used for website fonts
- [Font Awesome](https://fontawesome.com/)
  - Used for some icons on the website
- [Heroku](https://www.heroku.com/)
  - Used to host the website
- [GitHub](https://github.com/)
  - Used to store my project source code
- [Bulma](https://bulma.io/)
  - Used as the sites main css framework
- [Flickety](https://flickity.metafizzy.co/)
  - Used to create the main slider on the homepage
- [Stripe](https://stripe.com/)
  - Used for secure credit card payments
- [Kaggel](https://www.kaggle.com/nikdavis/steam-store-games)
  - Used to get some data for the site

### Other Tools

- [Pycharm](https://www.jetbrains.com/pycharm/)
  - This is the main IDE I used to build the website.
- [Pixlr](https://pixlr.com/)
  - Used to manipulate and create content for the website.
- [Grammarly](https://www.grammarly.com/)
  - Used to double-check all my spelling and grammar.
- [W3C Markup](https://validator.w3.org/)
  - Used this to check my HTML for errors and typos.
- [W3C CSS](https://jigsaw.w3.org/css-validator/)
  - Used this to check the validity of my CSS.
- [jshint](https://jshint.com/)
  - Used to validate JavaScript.
- [black](https://black.readthedocs.io/en/stable/)
  - Used for formatting python code.
- [Autoprefixer](https://autoprefixer.github.io/)
  - I used this tool to make sure I did not miss any prefixing in my code.

[Contents](#Table-of-Contents)

------

## Testing

Testing and error checking was undertaken throughout the development process. With the aid of the following tools and the help of human testers, I was able to catch and fix errors and bugs in my code.

#### [W3C Markup](https://validator.w3.org/)

Even though using this validator would understandably show errors for the jinja code I managed to catch some small mistakes by validating all the individual html files.

####  [W3C CSS](https://jigsaw.w3.org/css-validator/)

I tested all the CSS files in the project using W3C CSS validator with no errors as per image below.

#### [Autoprefixer](https://autoprefixer.github.io/)

After finishing up my CSS and before the validation of CSS I used this tool to make sure I had not left out any prefixing in my code.

#### Unit Testing

[![testing](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,w_512/v1601490544/tests_dwe31t.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601490544/tests_dwe31t.png)

[![Coverage](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,h_250/v1601490781/coverage_rr9wpm.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601490781/coverage_rr9wpm.png)

With the use of Django unit tests and coverage I created tests for my codebase, interestingly I discovered some bugs when implementing the tests that I believe I would have otherwise missed. 

#### Google Lighthouse

[![lighthouse](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601491051/lighthouse_eimfjg.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601491051/lighthouse_eimfjg.png)

Using the development tools inside chrome and google lighthouse I was able to fix some of my sites performance issues. 

#### Browser and Device Testing

| **Browser** | **Device** | **Compatibility** | **Version**| **Notes**|
|-------------| ---------- | ----------------- | ---------- |-------|
| Google Chrome | Desktop  | &#9733;&#9733;&#9733;&#9733;&#9733; | Version 85.0.4183.121  |
| Firefox | Desktop  | &#9733;&#9733;&#9733;&#9733;&#9733; | Version 81.0  |
| Edge| Desktop  | &#9733;&#9733;&#9733;&#9733;&#9733; | Version 85.0.564.63  |
| Samsung Internet | Galaxy S8  | &#9733;&#9733;&#9733;&#9733;&#9733; | Version 12.1.2.5  |
| Safari | iPhone 8  | &#9733;&#9733;&#9733;&#9733;&#9734; | Version 14.0  | Some small styling differences & google sign in incompatibility|


- [x] Test links to all pages
- [x] Test errors by typing in random page redirects
- [x] Try to access the user area without signing in
- [x] Test filtering dropdowns
- [x] Test searching
- [x] Test clearing search
- [x] Test card links
- [x] Test social links
- [x] Test ratings
- [x] Test adding and removing items from cart
- [x] Test checkout process
- [x] Test user login
- [x] Test editing user profile
- [x] Test dashboard view
- [x] Test add game
- [x] Test edit game
- [x] Test delete game
- [x] Test add featured and discounted game


#### User Testing

This was probably the most useful of all, I had a number of friends and family test the application. This helped me get feedback and find bugs I had missed. Some included styling issues on different devices to some UX ideas to make it a bit more intuitive. Unfortunately I could not implement all the suggested features in time but the feedback was invaluable. Below are some of the feedback images I received and consequently fixed.

[![error](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,h_250/v1601495309/IMG-20200920-WA0007_l1yzpo.jpg)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601495309/IMG-20200920-WA0007_l1yzpo.jpg)
[![error](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,h_250/v1601495309/IMG-20200920-WA0006_t4yrmg.jpg)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601495309/IMG-20200920-WA0006_t4yrmg.jpg)
[![error](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,h_250/v1601495309/IMG-20200920-WA0011_ejothe.jpg)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601495309/IMG-20200920-WA0011_ejothe.jpg)
[![error](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,h_250/v1601495309/IMG-20200920-WA0026_rdhqen.jpg)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601495309/IMG-20200920-WA0026_rdhqen.jpg)
[![error](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,h_250/v1601495589/IMG-20200930-WA0003_djlgsh.jpg)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601495589/IMG-20200930-WA0003_djlgsh.jpg)


[Contents](#Table-of-Contents)

------



### Deployment

The Deployment of this site uses the following web technology therefore you will need the appropriate accounts:

- [GitHub](https://github.com/) - For hosting this site's Repository
- [Heroku](https://www.heroku.com/) - To host the website
- [Postgresql](https://www.postgresql.org/) - To host the database though addon in Heroku
- [AWS S3](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Categories=categories%23storage&trk=ps_a134p000004f2XNAAY&trkCampaign=acq_paid_search_brand&sc_channel=PS&sc_campaign=acquisition_EMEA&sc_publisher=Google&sc_category=Storage&sc_country=EMEA&sc_geo=EMEA&sc_outcome=acq&sc_detail=aws%20s3&sc_content=S3_e&sc_matchtype=e&sc_segment=468762436981&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Storage|S3|EMEA|EN|Text|xx|EU&s_kwcid=AL!4422!3!468762436981!e!!g!!aws%20s3&ef_id=CjwKCAjw2dD7BRASEiwAWCtCbwYYQwQbIMou2UIrjOgrezSe1BPJF1YLrthdwDUBmz35GRk4gDL2YRoCTLoQAvD_BwE:G:s&s_kwcid=AL!4422!3!468762436981!e!!g!!aws%20s3) - Storage for the sites static files
- [Cloudinary](https://cloudinary.com/) - For hosting the websites images.
- [Stripe](https://stripe.com/) - For the payment system.



#### Prerequisites

In order to contribute to this repository you will need to have the following installed:

- [Python](https://www.python.org/) 3.8.3 or higher
- [Git](https://git-scm.com/) version control
- Code editor - [Pycharm](https://www.jetbrains.com/pycharm/) or [VS Code](https://code.visualstudio.com/) is recommended

#### Development
There are a number of steps required to deploy a local version of this project.

##### Cloning

[![code](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,h_150/v1601496664/code_btn_rpimid.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601496664/code_btn_rpimid.png)

- At the top of the repository click on the Code button as shown above.
- Copy the path to the repo [https://github.com/Frozenaught/turn-games.git](https://github.com/Frozenaught/turn-games.git).
- In your command-line, navigate to the folder where you would like to make a copy of this repository ie: `c:\MyRepos>` or `~/Documents ❯ `.
- Type the following to clone the repo `c:\MyRepos> git clone https://github.com/Frozenaught/turn-games.git` or `~/Documents ❯ git clone https://github.com/Frozenaught/turn-games.git`
- Now you can navigate to the newly created directory `c:\MyRepos\turn-game>` or `~/Documents/turn-games ❯` 

##### Requirements.txt

Next you will need to install all the projects dependencies type `pip install -r requirements.txt` or `pip3 install -r requirements.txt`. If you add or update any packages in the project or add any new ones then use `pip freeze --local > requirements.txt` to update the [requirements.txt](https://github.com/Frozenaught/turn-games/blob/master/requirements.txt) file with the new dependencies.


##### Environment Variables

You will need to setup the following environment variables on your system.

| Variable name         | Used for                 | Notes                                                        |
| --------------------- | ------------------------ | ------------------------------------------------------------ |
| EMAIL_HOST_USER |  Sending notification emails | Can be created under the security tab inside a gmail account |
| EMAIL_HOST_PASSWORD | Sending notification emails | Can be created under the security tab inside a gmail account |
| STRIPE_PUBLIC_KEY | Needed for the stripe payment system | Can be created under the developer tab on your stripe dashboard |
| STRIPE_SECRET_KEY | Needed for the stripe payment system | Can be created under the developer tab on your stripe dashboard |
| STRIPE_WH_SECRET | Needed for the stripe payment system | Can be created under the developer tab on your stripe dashboard |
| AWS_ACCESS_KEY_ID | Needed for the S3 Bucket static files | available when creating the S3 bucket |
| AWS_SECRET_ACCESS_KEY | Needed for the S3 Bucket static files | available when creating the S3 bucket |
| AWS | Deployment only - to tell django to use s3 instead of local static files | Should be used in deployment and set to True |
| DATABASE_URL | Deployment only - sets hosted postgres database | Found in heroku under resources/ Heroku Postgres / Settings |
| SECRET_KEY | used by Django as a salt to generate hashes | can easily be generated [here](https://miniwebtool.com/django-secret-key-generator/)|

##### Contribution

- If you choose to make changes to the website I would recommend using separate branches so that you can go back to the original master branch if the changes don't work as expected.
- Use `git checkout -b <brancname>` to create a new branch and edit the files accordingly.
- If you are happy with the changes to use `git commit -m "my commit message of changes I have made"` to commit the changes.
- Use `git push `to push the changes to the repository.
- As these changes are on a different branch they will not be available on the deployed site until you merge them to the master branch.
- To merge the new branch to the master branch switch to the new branch on GitHub using the branch selector dropdown menu.
- create a new pull request and state what changes were made in the comment section.
- submit the pull request and switch back to the master branch.
- now I will have the option to merge the pull request and you will be done.

##### Deployment

[![code](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,h_150/v1601499589/deploy_tvl4yh.png)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601499589/deploy_tvl4yh.png)

The easiest way to deploy the project to Heroku is to set your connect method to GitHub and link the repository master branch. If you set the project up for automatic deploys it will deploy once the master branch is updated.

[Contents](#Table-of-Contents)

------

## Credits

The bulk of the credits should really go to the documentation of the various technologist I used and of course to teh excellent course content provided by the code institute.

### Content

The content on the site all comes from this [dataset](https://www.kaggle.com/nikdavis/steam-store-games) that was found on [Kaggel](https://www.kaggle.com/), I had to clean it up and take only what I needed to allow fixtures to easily load the data into my models. I created this [fixture_scripts]() folder with some python scripts to achieve this, it will only work for this purpose but it can be adapted for any dataset with a bit more time.

### Media

#### Images

### Acknowledgements

Along the development process I saved all references I used to the References area in my [Trello Board](https://trello.com/b/dRoiHJLF/milestone-4-turn-games)

#### Inspiration

- Used to help with ideas for web design
 

#### Code

[Contents](#Table-of-Contents)
