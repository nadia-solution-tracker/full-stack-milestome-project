### Online Book Store Ecommerce Website(https://online-book-store-ecommerce.herokuapp.com//)

**Table of Contents**

[TOC]

### Overview of the project
- The main objective of this Ecommerce Website is to manage the details of Books, Stock, Customer, Order and Payment.
- The Online book store also allows users to search and purchase a book online based on title, author and other keywords. 
- The selected books are displayed in a tabular format in a cart and the user can order their books online through credit card payment. Using this Website the user can purchase a book online instead of going out to a book store and wasting time.

![IMAGE](static/images/homepagesnapshot.jpg)

## UX
### Insights of the project
- Customer can purchase books online. 
- Through this web browser the customers can search for a book by its title or author, or specific keywords.
- Sorting feature based on price both ascending and descending is also provided to ease search of a product
- Allows users to see specific details about a book like book title, price, author name, description, instock and total views. 
- Using Authentication mechanism a user can login using his account details or new customers can set up an account very quickly
- Books can be added to the shopping cart and finally purchase using credit card transaction
- Users have to register to persist their shopping cart between sessions
- The user can also write reviews about a book by giving ratings on a score of five. 
- Pagination feature allows users concentrate on a particular amount of content
- The books are divided into many categories based on subject like Fiction, Comics, Gospel etc.

#### User Stories
**"Rochelle loves books and wants to buy one of her favourites"**
- As a user she can browse through the list of books ,or browse through book based on Authors ,Categories or search keywords. 
Sorting feature can also advance her search if she wishes to browse based on price.
- Pagination feature at the bottom on the page will display particular number of books in pages giving her a to focus on few books at a time.
- As a user she can click the individual book she finds to see more information and even see reviews about the book

**"Rochelle wants to purchase a book"**
- As a user, finding the book of her choice  she can add the book to the cart. The  cart functionality allows her to update quantity or delete the total items she buying 
- As a user , buying the book requires her to register herself and proceed to checkout
- As a user she can use the checkout functionality to process her order and get the book she is interested in.

**"Kate as a returning customer"**
- As a user , she can leave a review about the book by leaving comments and ratings out of 5 for others to see.This would help other customers to make a choice about buying the book or no.

**"John does not find the book instore"**
- As a user ,he can access this website to check if an item is in stock or not, and proceed to buying .
-

- Logout feature is also provided.

#### Design Process

[Schema diagram](https://www.dropbox.com/s/ii6ipaeryhgdlo1/Relational%20schema.jpg?dl=0)<br/>
While working on the application new features and changes were made on the design of the wireframe<br/>
[Wireframes for Desktop](https://www.dropbox.com/s/rl6qirupp6cfna8/Wireframe%20for%20Desktop.pdf?dl=0)<br/>
[Wireframes for IPhone](https://www.dropbox.com/s/6m8o5ha3vz1swoh/Wireframe%20for%20Iphone.pdf?dl=0)<br/>
[Wireframes for IPad](https://www.dropbox.com/s/8a3o977hn0k2nug/Wireframe%20for%20Ipad.pdf?dl=0)<br/>

## Features

#### Existing Features

The following features are added to the application which is geared towards enhancing the user online experience. This multipage application provides a menu to access the various features of the application

**Apps**

Home
Cart
Products
Purchases
Search
Reviews
Accounts

**Home**- serves as an initial landing page for all users. Users are able to access the following :
- A static clickable navigation menu with items like Home, Browse All , Login, Register
- Have a snick peek at the top 3 most popular books as card.
- Clicking an book image in the card opens up the image to have a better look of the book cover
- Add to cart button will add the book to the cart.
- Clicking the book title or the book cover image redirects to book detail page to see more information about the book
- List of existing author and Categories is displayed on the left side of the home Page to advance search
- Search provided at the at the left of the page to Search books on any search keywords
- A Carousal displaying 2 random images from different websites at a set interval.
- If a valid user logs in displays a message "Welcome "

*Pages* : base .html and home.html

**Login** – this creates an entry for returning users with existing accounts
- Provide a link to Register if the user has not yet logged in
- Clicking the login on the menu, directs the user to an input form to enter login details like username and password
- The Login form provides validations for fields that are required and also checks if login is successful
- Signing in the form creates opens the home page and clickable menu which now includes additional features Home, 
- Clicking on the Logout initiates a session time out and the user lands again on the home page with the additional features removed

*Pages* : Login.html

**Browse all**  this page displays a wide collection of books.
*The search section*
- Provides a list for a filtered view based on the following criteria Category and Author
- Search option - search for books by book title, most important by author,categories or specific keywords.
- Sorting feature to sort book based on price low to high and high to low is also provided in form of a drop down

*The book collection section*
- When this page is first time loaded a list of books  are displayed in form of a card  which the user can browse.
- Pagination feature is incorporated so that users do not get lost and can concentrate on a particular amount of content, the page display 6 books at each time. The user can view the list of next 6 books by clicking on the pagination links provided at the bottom of the page.
- Clicking a book card opens up detail information about the book.
- Clicking any card images of the recipe book opens up the image to have a better view of the book cover

**Searched Books**– this page displays list of books based on filtered criteria
- Provides users with book cards of books based on search criteria Results for: Fiction
- The user can also get back to the book page by clicking |browse all” link in the menu.
- Pagination feature is incorporated so that users do not get lost and can concentrate on a particular amount of content, the page display 6 books at each time.
- The user can view the list of next 6 books by clicking on the pagination links provided at the bottom of the page

**Book Detail**
- individual book page accessed through clicking the book image or the book title link provided in the card.
- It uses an entire page to display a full book information with larger text and the book image at its full capacity to the user.
- Upon viewing it increments the book view count. 
- If a valid user has logged in he/she will be able to leave a comment and rating about the book.

*Pages* : product_detail.html

**Review**
- The review form provided in the product detail page allows a valid logged in user to leave a comment and rating out of 5 for the book displayed
- This comment is than added to the list of customer reviews
- If the user has not logged in he/she will be shown a message to loggin to leave a comment however he/she will be able to view other customer reviews


**Cart**
- Adding a book to the cart will display a clickable cart option in the menu displaying the total items in the cart.
- The cart can be viewed by clicking the cart link on the menu bar.
- On opening the cart a tabular display giving information about the item added will be displayed like Book image, book title, number of copies , option to change the quantity or remove the item from the cart.
- Updating the quantity updates the price by the quantity displaying the new total of the cart.

*Pages* : cart.html

**Checkout**
- Clicking the checkout button on the cart page redirects the user to the checkout page again giving the final list of the items with the cart as well as the total amount. This is the order placed by a valid customer
- This page also provided a form to enter payment details like customer information and credit card information
- Submitting an order finally saves the order for the customer for processing (not implemented) as well as updates the quantity in stock for the product.

*Pages* : checkout.html