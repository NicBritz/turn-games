![](https://img.shields.io/badge/Django-3.1-orange)

[![turn games](https://res.cloudinary.com/dauzoqnfv/image/upload/f_auto/v1600948601/Turn_GAmes_uquoab.png)](https://turn-games.herokuapp.com/)

------

## Overview 

Turn Games is en e-commerce digital video game store, the site offers a wide variety of visual entertainment content. Users can browse the sites extensive inventory and filter down the content for easier navigation. Users are also able to search the site by use of a search bar that is always readily available. 

The landing page will show any content that the site owner has added to the featured or discounted sections. It will randomly select ten titles to display on the main page image slider.

Users are easily able to view more information about the game simply by selecting the content card. In the game inspection area a user can either rate a game with a thumbs up or a thumbs down and add the game to their basket for purchase once they have finished browsing.

[![Home page](https://res.cloudinary.com/dauzoqnfv/image/upload/c_scale,w_512/v1601467361/f7355fb508f84512843864bb5a26ba30_1_1920_y9dqug.jpg)](https://res.cloudinary.com/dauzoqnfv/image/upload/v1601467361/f7355fb508f84512843864bb5a26ba30_1_1920_y9dqug.jpg)

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

### Database Schema

## Features

### The navigation bar

### Main Slider

### View  filtering

### Game cards

### Footer

### Sign-in

### Registration

#### Image tab

### Game view

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
