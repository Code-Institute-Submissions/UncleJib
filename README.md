[![Build Status](https://travis-ci.com/Wini996/UncleJib.svg?branch=master)](https://travis-ci.com/Wini996/UncleJib)

# Welcome to Uncle Jib's!
![](static/images/logo2.JPG)
## The Snow Sports Specialists

Here at Uncle Jib's we are a family run retailers who love snow and everything to do with it.
We are all about the experience here at Uncle Jib's and want to bring you the very best experience when using our site. We hope you 
all enjoy browsing and hope to see you again soon.


## Why was this site created?
Uncle Jib's webshop has been designed and built by Libby Winfield as a final project for the Code Institute Full Stack Web Development 
Diploma. The purpose of this shopping site is to allow for new customers to shop on a safe and secure site in order to shop for the latest
snowboards and equipment. Specifically aimed at customers who enjoy being outdoors in the snowy mountains looking for the highest quality 
and stylish snowboards to suit their riding needs.

## UX

### Business Goals
The goals for Uncle Jib's website on a business front are:
- Providing a professional online shop where users can easily find their way around the site.
- There are links to all social media to provide Uncle Jib's with a brand awareness for all it's customers.

### Visitor Goals
- Allows for shoppers to find the best snowboard for them, by providing descriptions and information relevant to each individual snowboard.
- Enjoy browsing for those who like to see what new products are being released.
- Ensures the users know what type of snowboarder they are. They can choose what their riding style is enabling them to find a suitable board.
- Buying from a trustworthy online dealer.

### What users expect, need and want
- The users need to be able to easily find selected items that are shown within the category on the navigation bar. 
- Having a clean and clear layout that allows user to easily navigate around the site.
- Ensure that the site is easy to use, not only on a desktop view but also mobile views and tablets.
- All information and images should be layed out in a clear manour to make easy reading.
- Have a working contact page to allow for users to contact the site owner when they have any questions that need answering.
- To be able to see what items are within their cart.
- Allow for users to log into the site to keep their contact details and payment information.

## Design Choices

## Icons
- There are many icons throughout the entire site to easily show what specific items represent. 
- - Within the footer section of the page there are two icons, Snapchat and Facebook. These two social media links lead the users 
onto those chosen platforms to allow users to spread brand awarenss. 
- - There is a search icon on the navigation bar to show users that they can add anything within the search bar to find a 
specific item. 
- - On the home page, on the 'Select a Snowboard Category' there are two icons, Snowflakes and  Snowman. These icons are placed on the 
snowboard categories to add some character to the cards.  
- - Within the actual site tab itself there is a small icon which represents the website logo.

## Colours
- Specific colours are shown and have been specifically chosen becuase they work well with each other.
- Background colour: #2c2e2f - Dark grey
- Headline colour: #2fb8ce - Light blue
- Text: #c5c5c5c - Dark white / Creme
- The use of dark white / creme on the dark grey background allows for users to easily read the text, as if white/#ffffff had been chosen there 
would be a bright contrast and would strain the users eyes when viewing the site.

## Styling
- There are specific styling additions to the majority of the buttons to allow for users to know when they are hovering on them. These buttons 
will turn from a light blue to dark blue to indicate that these will take you to other pages within the site. 
- Curved edges were chosen on buttons to make the site more user friendly. This is a common styling choice within bootstrap and is commonly 
used on sites such as Facebook and Instagram.

## wireframes
- All wireframes were hand drawn and were made 2/3x over to ensure I could create the best site possible within the assessed time period.
The wireframes can be found within the 'static' file under the name 'wireframes'.

## Pages
### Home Page
- On the Home page, it is designed to have a selection of three images all to do with snowy mountains, to scroll through these images simply press 
the indication arrows on the left and right side of the images. Below there is information about Uncle Jib's. Further down the pages shows 
all of the categories of snowboard riding styles which people can select from to suit their own needs. It states the category name, 
description, image and a button to direct the user to that specific category. At the bottom of this page, is a simple icon row which simply states 
there is 'Fast and Free Shipping', '24hr Customer Service' and 'Free Returns on all Orders'. 

### Nav bar
- Within the Nav bar there are selected pages I'd like the user to go to. These are the specific snowboard categories, which will provide a 
dropdown and render the specific categories. Besides this is the Contact page, where users can email the site provider. The About page is vital for 
users to know more about how the site originated and who is behind selling their goods. I decided to add the shopping cart as just an icon as it 
allowed for a more simple and minimal approach to the site. Within the middle of the nav bar is the registration/profile/login/logout.
These too have icons next to ther title to add an artistic approach. Finally there is the search bar. This is located to the far right of the 
navigation bar as it is set out of the way from the main navigation.

### Products 
- When typing into the URL `/products` it will return all the products even though they have a selected category. However, within the product app views.py, 
there are 3 views. `def product` will render a single product in lots of detail, `def all_products` which will only be rendered if /products is added 
into the URL and `category` which renders only the snowboards within a particular categegory which is defined within the products models.py 
under `CHOICE`.

### Cart 
- If the users shopping cart is empty, then the cart will return empty and no number icon on the cart icon. However, when there are items within the basket a 
small yellow icon and number will appear next to the cart to indicate how many items are in the cart. 
- When there are items added to the cart, a table will appear with the product picture, name, price, quantity and price and then the ammendment section for you to adjust your order.
Below this is the checkout station. The user is asked to review their cart order and if correct then proceed to purchase.
- This page has been designed where one item goes below the other. This is due to when ordering snowboards, it is very rare to order more than one.

### Checkout
- Once the user is at the checkout, their product image will appear with the name, price and quantity. They will be told in big text what the total amount to pay is and then be taken
 to the payment details form. Within this form is all the neccessary information for purchasing the products, ie. card details, address information etc. once submitted, there 
 will be a confirmation saying 'your order has been successful'.

### Search
- The search bar will only render an item if the name is spelt correctly and is within the database. If the item is not within the database then it will 
return a page stating 'The product cannot be found'.
- When searching for a specific item, use phrases common to snowboarding, ie. Jib, Camber, Bataleon etc. Try using brand names to filter your 
search (Bataleon, Burton, Salomon etc).

### About
- Here is where users can learn more about Uncle Jib's. There is text about their story and a map providing 
the location of their warehouse/shop for those who want to return items in person.
- At the end there is a section that provides the user with information on environmental features that Uncle jib's adhere to throughout their company.

### Delivery
- On this page, the user can find all the information and policy on delivering their item, if delivery is free and where we deliver within the world.

### Returns
- Users can access all the information on returning an item if needed. 
- At the bottom of the page if there is anything the that isnt specific to the user, there is a contact button below so they may email Uncle Jib's with their specific questions.

### Contact
- This contact service is fully functional and will send the email to the site owners personal email and will aim to get back to the user within 24hrs.

### Reviews
- When creating the reviews section within each individual product I chose to use a ForeignKey instead of a OneToOne relation key.
I chose to add a review system in to add some unique use for the user. They need to create an account and log in inorder to write a review on any 
product. If however, the user is not logged in then they can only see what reviews have been left.

### FAQs
- The most asked questions are highlighten in blue and the answers are beneath them. I used the blue to highlight the questions so users 
could quickly scan the page and find the most relevant question to them. At the bottom of the page I added a link to the contact form, so if a user couldn't find 
their questions they can simply and quickly email Uncle Jib's and get an answer back within 24hrs.

### Register
- Within this page, there is a large title saying 'Create An Account'. A form underneath asks for the user to enter in a valid email address, username, 
password x2. However, there is a link just below the title allowing users with existing acounts to sign in.

### Login
- Here there are simply 2 text forms displaying username and password. If the username and password are not correct it will return an error.

### Logout
- When the logout button is pressed, it logs the user out and renders the index page.

### Covid
- This page just describes what to do during Covid-19 ie. Staying inside, it states that there may be delays in shipping and returning 
items due to the virus.

## furture features
There are many future features I would like to implement as we progress to allow for a better user experience.
- Creating a 'like' system that all products will have. A user can simply 'like' a product and it will be sent to a wish list for future visits to 
the site.
- When a customer has purchased a snowboard from the website, an automatic email shall be sent to ensure them that their order is being 
requested, processed, in production and out for delivery. This should improve customer experience and and give them the satisfaction if they are a first 
time buyer. 
- When the snow seasons come to an end in early may, I would like for the site to have a end of season sale, so users can purchase the same snowboard 
just at a more competetive price. 
- If a user has just signed up to the site, there will be a modal which will pop up and offer them a 10% discount on their first order to try 
and promote more sales and gain more users within the database.
- Create a newsletter for viewers that have accounts to notify them when there are specific sales on and to tell them about any new products at fututre events
which they might have over looked when they were last on the site.
- Allow for users to see order details once they have purchased their order. This will allow the user to ask for any alterations to their 
purchase and ask any question about refund, exchanges and delivery information.

##DATABASE MODELS

### Product model app
Within the `products app`, the product containal all the data for the products within the site.

 | Name | Key in DB | Validation | Field Type |
 | --- | --- | --- | --- |
 | Title | title | max_length=250 | CharField |
 | Image 1 | image_01 | blank=True | ImageField |
 | Price | price | max_digits=6 | DecimalField |
 | Descriptions | description |  | TestField |
 | Size | size | max_length=100 | CharField |
 | Colour | colour | max_length=100 | CharField |
 | Flex | flex | max_length=100 | CharField |
 | Shape | shape | max_length=100 | CharField |
 | Board Profile | board_profile | max_length=100 | CharField |

### Checkout Model
Found within the `checkout app`, shows how the form will appear on the site. 

| Title | Key in DB | Validation | Field Type |
|---|---|---|---|
|  Full Name | full_name  |  max_length=50 | CharField  |
| Phone Number | phone_number  |  max_length=20 |  CharField |
| Country | country | max_length=40 |  CharField |
| Postcode | postcode | max_length=20 | CharField  |
| Town or City |  town_or_city | max_length=40 | CharField  |
| Street Address 1 | street_address1 | max_length=40 | CharField  |
| Street Address 2 | street_address2 |  max_length=40 | CharField  |
| County |  county |  max_length=40 | CharField  |
| Date | date |  default=datetime.date.today | DateField  |

### Order line Checkout Model
Found within the `checkout app`, will show how the form is filled out on the site.

| Title | Key in DB | Validation | Field Type |
|---|---|---|---|
| Order | order | Order, null=False | ForeignKey |
| Products | product | Product, null=False | ForeignKey |
| Quantity | quantity | blank=False | IntegerField |

### Reviews Model
Found within the `reviews app`

| Title | Key in DB | Validation | Field Type |
|---|---|---|---|
| Product | product | on_delete=models.CASCADE | ForeignKey |
| User | user | on_delete=models.CASCADE | ForeignKey |
| Content | content | max_length=500 | CharField |

## Technologies used

- **Django** as a python framework.
- **AWS S3** Bucket to store images which are entered into the database.
- **Stripe** as a payment platform.
- **Heroku** for deployment
- **Pillow** as a python library for processing images.
- **Git** as version control.
- **Github** to allow storing and sharing the project remotely.
- **Whitenoise** allows the web app to have it's own static files.
- **Boto3** to enable management.
- **Sqlite3** for a development database.
- **Bootstrap** to provide simple structure to the website and making it mobile responsive.
- **Font Awesome** to provide the icons for the site.
- **Google Fonts** to style we websites fonts.
- **JQuery** as DOM manipulation.
- **HTML**
- **CSS** - Much of the CSS has been used within the HTML as it was easier to import and use some of the style provided by Bootstrap.
- **Java** Script
- **Python**
- **Gitpod** was used to develop the entire site.
- **Gunicorn** for heroku deployment



## Testing

1. The code below will delete the migrations due to an occuring error which occured multiple
 times. In order to migrate my files, I had to delete migrations and remigrate them 
 to the products model.py.
    1. `find . -path "*/migrations/*.py" -not -name "__init__.py" -delete`
    2. `find . -path "*/migrations/*.pyc"  -delete `  
    3. `python manage.py migrate UncleJibs zero`
    4. `python3 manage.py runserver --run-sync` 

 These few lines of code allowed for me to delete and reimport any migrations I needed to my project. However, countless times I had to manually 
 delete the migrations folders, __pycache__, db.sqlite3 files to ensure that there was a hard reboot and reinstallation of `makemigrations` and `migrate`.
 After finding out this issue, I had to understand how you can allow a translator to translate part of the URL. 

- Some testing was done within the products app to ensure that my spelling for 'products' and 'product' were caught. This kept rendering an error 
trying to get a product out of something that wasn't there due to my spelling mistakes.

- While importing my code within jinja, I came across multiple issues with {{_______}}. My issues came from not opening and closing my jinja correctly 
and due to not understanding that when redirecting to a view to display information a certain singular database item needs to pass in some way of itentifying 
that item. This was through giving an ID to the database item. However I went over this multiple times within the course and got extra help to understand where 
I was going wrong.

- Throughout the project, I commonly forgot that since I was using Gitpod, There was a need to use `pip3` instead of `pip`. Becuase I was using python3 
I soon realised that `pip3` was essential as after installing certain programs didnt work due to this reason.

- During the final few days of coding, I began seeing an error where my previewed site. The site wasnt connecting to my AWS S3 account and created an issue 
where the `STATICFILES_STORAGE = ` needed to be written as `STATIC_FILES_STORAGE = `. Without the first underscore ('_') non of my added CSS or images would render.
- - To resolve this, I tried adding in `<AllowedMethod>HEAD</AllowedMethod>` earlier than when was needed, which still rendered the same error.
- - I tried resetting the CORGS Configurations and the Bucket policy. Neither of these worked.
- - I tried recreating a new User, Group and Policy within AWS to understand where I had gone wrong previously. However, the codes looked identical.
- - After hours of trying, I removed the IAM credential/secret keys. Created a new User, Group, Policy and Bucket. Pushed this to github. 
Ensured that my code was correct and re added everything to my repositoy. I ensured that I always hard rebooted/refreshed the previewed site to delete the cashed data.
This essential worked, after reading over django documentation and using code forums for extra help. However, I am still unsure as to why it didnt work before, which is something that I am going to look into further.

- There is a section dedicated to manual testing located in the `statics` file. 
## Deployment 

### Heroku Deployment
1. Create a `requirements.txt` file in the terminal.
2. Create a `Procfile` in the terminal.
3. Push these new commits to GitHub.
4. Create a new app on the Heroku site.
5. Click 'Deploy', select the deployment method to GitHub.
6. Click onto Herokus dashboard, select 'Settings' 'Reveal Config Var'.
7. Set the following config vars... 

| Key | Value |
|---|---|
| STRIPE_PUBLISHABLE | "yourpersonalisedsecretkey"  |
| STRIPE_SECRET | "yourpersonalisedsecretkey"  |
| DATABASE_UR | "yourpersonalisedsecretkey"  |
| SECRET_KEY | "yourpersonalisedsecretkey"  |
| AWS_ACCESS_KEY_ID |  "yourpersonalisedsecretkey" |
| AWS_SECRET_ACCESS_KEY | "yourpersonalisedsecretkey"  |
| DISABLE_COLLECTSTATIC | 1 |

- ^ the DISABLE_COLLECSTATIC should be set to 1 to disable the static files being accessed from github instead of AWS.

8. Within the terminal make sure you have installed 'gunicorn' and added that 
program to the requirements.txt file.
9. Create a Procfile at the root of your directory.
10. In Heroku, click 'Deploy', 'Manual Deploy' and select the master branch 'Deploy Branch'
11. Once the build has completed, click the 'Open App' button provided in the top right hand corner.

### When commiting to Github, follow theres steps...
1. Ensure you are on the /environment/ in your ternimal.
2. If not, use `cd ..` to got back one file at a time till you reach 'environment'.
3. Enter `git add .` to add all content to github.
4. `git commit -m "Initial commit"` This code will commit your code and add a a small description.
5. `git push` will upload this file to a remote repository.

## Content
- The descriptions and images for the snowboard and descriptions were all taken from www.absolute-snow.co.uk.
This site sells everything to do with the outdoors from hiking, wakeboarding and snowboarding. 
- Big thanks to W3Schools for allowing me to understand certain concepts and use small snippets of their code to push the limits of this site.
- Big thanks to Scott Kipp for allowing me to take information form your previous MS4 and providing me with inspiration for the categories to products, products to product design for the site. 
- The accounts app was taken from a previous project that we were taught and had been incorporated into this project, 
to allow me to spend more time on more inportant aspects of the site which I seemed to struggle with ie. products models.

## Acknowledgements
- I received inspiration for this project from multiple shopping sites such as ridestore.com, absolute-snow.co.uk and many more.
- Many thanks to all the tutors at CI who helped me fix numerous bugs within my products/models.py file when it started to error out saying there 
was already a products table there when there wasn't. 
- Shout out to my mentor Brian Macharia, for the help tutoring me throughout the course!
