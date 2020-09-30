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

## Admin Dashboard

### Code structure


### Code structure


### Features Left to Implement

[Contents](#Table-of-Contents)

---

## Technologies Used

The following is a list of tools and technologies I used to create this website:


- [Python 3.8.3](https://www.python.org/)
  - Used for backend data manipulation
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

### Other Tools

- [Pycharm](https://www.jetbrains.com/pycharm/)
  - This is the main IDE I used to build the website.
- [Adobe Photoshop](https://www.adobe.com/uk/products/photoshop.html?gclid=CjwKCAjwvOHzBRBoEiwA48i6AtbSWstaKzHCUaUKzSlnKYFxv7dELw1rAOJgZhYShhzdXSxrCp3JHxoCnG4QAvD_BwE&sdid=88X75SKR&mv=search&ef_id=CjwKCAjwvOHzBRBoEiwA48i6AtbSWstaKzHCUaUKzSlnKYFxv7dELw1rAOJgZhYShhzdXSxrCp3JHxoCnG4QAvD_BwE:G:s&s_kwcid=AL!3085!3!340669891884!e!!g!!photoshop)
  - Used to manipulate and create content for the website.
- [Grammarly](https://www.grammarly.com/)
  - Used to double-check all my spelling and grammar.
- [W3C Markup](https://validator.w3.org/)
  - Used this to check my HTML for errors and typos.
- [W3C CSS](https://jigsaw.w3.org/css-validator/)
  - Used this to check the validity of my CSS.
- [jshint](https://jshint.com/)
  - Used to validate JavaScript.
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

#### CI/CD

As an extra test I used [github actions](https://github.com/features/actions) to set up continuous integration tests when ever I create a pull request. This was just in case I broke something. It was good to check before merging to the master branch.

#### Google Lighthouse

#### Browser and Device Testing

| **Browser**      | **Device** | **Compatibility**                                            | **Version**            |
| :--------------- | :--------- | :----------------------------------------------------------- | :--------------------- |
| Google Chrome    | PC         | ?????????                                                    | Version 83.0.4103.106  |
     |

- [ ] Test links to all pages
- [ ] Test errors by typing in random page redirects
- [ ] Try to access the user area without signing in
- [ ] Test filtering dropdowns

#### User Testing

[Contents](#Table-of-Contents)

------



### Deployment

#### Prerequisites

#### Development

##### Cloning

##### Requirements

##### Environment Variables

You will need to setup the following environment variables on your system.

| Variable name         | Used for                 | Notes                                                        |
| --------------------- | ------------------------ | ------------------------------------------------------------ |




> Note: you will need to add these environment variable to your GitHub repo in `settings -> secrets` and Heroku  in `settings -> config vars` 

##### Contribution

- If you chose to make changes to the website I would recommend using separate branches so that you can go back to the original master branch if the changes don't work as expected.
- Use `git checkout -b <brancname>` to create a new branch and edit the files accordingly.
- If you are happy with the changes to use `git commit -m "my commit message of changes I have made"` to commit the changes.
- Use `git push `to push the changes to the repository.
- As these changes are on a different branch they will not be available on the deployed site until you merge them to the master branch.
- To merge the new branch to the master branch switch to the new branch on GitHub using the branch selector dropdown menu.
- create a new pull request and state what changes were made in the comment section.
- submit the pull request and switch back to the master branch.
- now I will have the option to merge the pull request and you will be done.

##### Deployment

The easiest way to deploy the project to Heroku is to set your connect method to GitHub and link the repository master branch. If you set the project up for automatic deploys it will deploy once the master branch is updated.

[Contents](#Table-of-Contents)

------

## Credits

The bulk of the credits should really go to the documentation of the various technologist I used, I managed to get most of what I needed from there.

### Content


### Media

#### Images

### Acknowledgements

Along the development process I saved all references I used to the References area in my [Trello Board](https://trello.com/b/dRoiHJLF/milestone-4-turn-games)

#### Inspiration

- Used to help with ideas for web design
 

#### Code

[Contents](#Table-of-Contents)
