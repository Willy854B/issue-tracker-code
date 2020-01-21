[![Build Status](https://travis-ci.org/Willy854B/issue-tracker-code.svg?branch=master)](https://travis-ci.org/Willy854B/issue-tracker-code)         ___        ______     ____ _                 _  ___  

# Issue Tracker
## Overview
This website is the third of three projects I'm building as a portfolio to present to prospective employers. In this project, a range of new technologies were used to create a website that showcases how all the knowledge I have gained from the third module is put together to render a more complex product.
## UX
### What is this app for?
This is a bug fixing and feature development service app. Users are able to post descriptions of bugs that are causing problems in their system, which will eventually get reconfigured for free. Users can also request new feature development implementatiton for their software. However, they will be charged thirty dollars everytime a new feature is requested.
### What does it do?
This app will allow users to submit bug reports and feature requests so that developers can use that information to fix any bug related errors or add a new feature to the user's application. All bug reports and feature requests are privided by the user through a ticketing system, which displays important information within the ticket. In addition, this app provides log in, log out, and payment funtionalities to the user. 
### How does it work
This app uses a combination of technologies to manipulate the data available in the database, this data has previously been collected from different forms available to the user in the application. All that information is then rendered according to the user's needs by clicking on specific buttons. When the user opens the home page, all the tickets are displayed with the most relevant information, but certain functionalities such as ticket creation, feature request, and payment can only be done after the user has logged in. 
### Basic website image layout
See the project mock-ups [on Google Presentation]
https://docs.google.com/presentation/d/e/2PACX-1vSjmwlBeb4ShUFwHj3YxPiN4gaZLx_AnMf2VbE3PCNrq5CPA2L3386Yk20JlFmRdN7TznhW1dWsFKr7/pub?start=false&loop=false&delayms=3000
## Features
### Existing Features
- **Registration**

	Allows the user to provide personal information into the registration form. The data entered by the user is then saved in the database for authentication and authorization purposes.
- **Log in/Sign in**

	This piece of functionality is carry out when the user wants to make modifications to a specific ticket or to make a payment. Therefore, privacy and security must be implemented by verifying the user's personal data, so that he/she can be authorized to make changes and payments.
- **Log out/Sign out**

	Once the user has entered new information or made changes to his/her account, the log out functionality ensures that no one else but the user who created this unique account can make further adjustments.	
- **Ticketing/Posting System**

	This part of the application allows the user to post bug reports describing any problem in the code he/she may be experiencing. In addition, a feature request is another option available to the user only if a $30 payment is proccessed through Stripe's API.  
- **Payment/Checkout**

	This website was built with checkout functionality. It proccesses the payment of the service/product that the user wants to purchase. All payments are carry out using Stripe, which is a US company allowing businesses to accept payments over the Internet.
- **Mobile responsive design**

	This website was built to automatically adjust and adapt to any device the user is operating. It has the ability to optimize the screen size, whether it is a desktop, a laptop, a tablet, or a mobile phone.
- **Forms**

	Intuitive structure design was used to create different forms for data collection. Form validation is one of the features present in these forms.

### Features Left to Implement
- **User Based Features**

	- Sorting of tickets
	- Ticket deletion functionality 

## Tech Used
### Some of the tech used includes:
- **HTML**

	I used **Hypertext Markup Language** to structure and format the content of each page for this particular website.

- **CSS**

	I used **Cascading Style Sheets** to separate formatting and layout from content, and to give the website its unique look.	

- **[Django Web Framework](https://www.djangoproject.com)**

	This tecnology was used to host python framework. It facilitates the development of websites by taking care of some of the hassles involved in the coding proccess and enables users to focus on developing components needed for their application.

- **[Bootstrap](https://getbootstrap.com/)** 

   	I used **Bootstrap** to give this project a simple, responsive layout where mobile first approach is implemented throughout the site.

- **[JQuery](https://jquery.com/)** 

   	This JavaScript library was used to simplify the use of JavaScript on this website. It wrapped many lines of code into methods that can later be called with a single line of code.

- **[Font Awesome](https://fontawesome.com)** 

   	I used **Font Awesome** to add icons and style fonts. The **i** and **span** elements were used to insert the scripts required to render these icons and give this project a simple yet elegant look throughout the site.

- **[PostgreSQL](https://www.postgresql.org)**

	Although [SQLite](https://www.sqlite.org/index.html) is available in Django, I used PostgreSQL to save the data needed for this project. PostgreSQL is a general-purpose object-relational database management system.

## Testing
The following tests have been executed to make sure this project functions as expected:

1. Different browsers such as Opera, internet explorer, Firefox, and Google were used to render this site on the computer. I modified the screen display to different sizes making sure that page layout, specially the menu bar, adapts to any device the user may be operating. 

2. To test the code locally on my computer, I logged into **AWS Console**, opened **Cloud9**, activated the environment I was working on, and made sure ```python3 manage.py runserver $IP:$C9_PORT``` was running. This allowed me to make any adjustments to the code, and get the data back from the database.
	
3. Links were tested by clicking on each one of them, and making sure each button is coded properly and takes us to the right place.

4. Forms were tested as follows:

	- I supplied information that doesn't match the expected format or pattern that should be entered, which showed some error messages when I pressed the submit button. That confirms that the code is working properly.

	- I supplied information that matches the expected format or pattern that should be entered, and no error messages were shown when I pressed the submit button. This proves the code is validating the forms as it should.

5. I used Chrome's inspect tool to open the console and check for any errors in the code. It also allowed me to open the Network tab and check for important local or external links needed to run the application.   

6. I used **Django's Admin Panel** to verify that the tables were properly created and that the information entered in some of the forms available in different pages was actually being stored in the database.

7. To test the final product, I logged in to Heroku, selected **issue-tracker-application**, and clicked on "Open app". This allowed me to see if all aspects of this project were working as planned.
## Contributing
### Getting the code up and running
clone this repository into the editor you normally use by typing ```git clone https://github.com/Willy854B/issue-tracker-code``` command in your terminal. To cut ties with this Github repository, type ```git remote rm origin``` in the terminal.

To run the code on your computer, you need to:

1. Although you can install and use Django in your computer to locally modify and partially run the code, I used AWS Cloud9 for this purpose. Cloud9 simplifies the development process all the way to deployment, which in this case was done by linking Cloud9 with GitHub and Heroku.

2. Create a Heroku repository with a Postgres database within the new environment. Open the settings page and make sure that all the necessary configuration variables are properly typed so that Heroku can connect to Cloud9 and Stripe.

3. Open your workspace/environtment within Cloud9, and select the ```settings.py``` file. In there, you need to make sure that all AWS, Stripe, and Django secret keys have the right key-value pairs in the code.

4. Create a new Stripe account and install it by typing ```sudo pip3 install stripe``` in Cloud9's terminal window. 

5. Install **gunicorn** to run the HTTP server. In our case, we are using **Ubuntu** server. You can use ```sudo pip3 install gunicorn```, but make sure that the virtualenv for this project is activated.

6. Add all the **dependencies** to the **requirements.txt** file by opening the terminal in Cloud9, activating virtualenv, and running the following command: ```pip freeze --local > requirements.txt```.

7. Create a **Procfile** under the issue-tracker-code project folder and add ```web: gunicorn itracker.wsgi:application```.

8. Make any other necessary adjustments in yor code and run the following commands in the terminal:
```
git add <directories/files_to_be_added>
git commit -m "Message"
git push 
```
Now just run the heroku open command and the website will open in the browser.

## Credits
### Content
- Although most of the code in this website was created by me, I took some ideas from Bruno Bord who also credited Paul Bissex for his work. The content this app is intended to be the third part of a series of three projects.

### Media
- The home page logo was found using images tab in [Google Search](https://developers.google.com/search/).
- Social media link images were found and embedded into this project from [Fontaweson](https://fontawesome.com/?from=io).

### Acknowledgements
- In general, this portfolio site was created by me using the information I've learned from the **Fullstack Web Developer Program** offered by **[Code Institute](https://codeinstitute.net)**.
   