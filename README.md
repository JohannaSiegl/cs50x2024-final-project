# GAME "BINARY"
### Video Demo:
https://youtu.be/lJKSI6ow2js
### Description:
For my CS50's final project (2024) I decided to create a small game in the style of an old NES game. The goal of the game is to convert a decimal number into a binary number, hence the name of the game "BINARY".

<br/>

### Structure:

+ **Start screen**
<br/> The first thing the user sees is the index page, which shows the titel of the game and a menu to choose between starting the game and other options explained below. In addition, the player's username and high score are displayed at the top of the page.

+ **Playing the game**
<br/> When the player clicks on the START GAME menu item, the game will start. Again, the current score is displayed at the top right of the screen. In the middle, the current level is shown. Below that is a decimal number that the player must convert to binary. To do this, there are buttons labeled with 2^8, 2^7, and so on down to 2^0. Below these buttons are the corresponding decimal numbers. Clicking the button changes the 0 above it to a 1, and clicking it again changes the 1 back to a 0. If the player thinks that the decimal and binary notations represent the same number, the CHECK button is clicked to ckeck. If the binary number is correct, the player is sent to the next level. If it is not correct, the GAME OVER screen will appear with the option to restart or quit the game. Throughout the game there is also an EXIT button available to leave the game at any time.

+ **Level difficulty**
<br/> The first levels start with a very easy setting. During the first four levels, the highest possible number is 8. Up to level 8, the highest possible number is 16. After every 4 levels, the maximum number is doubled. From level 21 on, all numbers up to 256 are accessible. The numbers given here are the highest possible, the actual number is chosen randomly, so smaller numbers can appear in higher levels, too.


+ **Information about binary**
<br/> After clicking on INFORMATION in the menu of the start page, a short text with information about the binary system will be presented to help understand and play the game.

+ **High scores**
<br/> When selecting HIGH SCORES, the ten highest high scores of all players are displayed in a table, together with their place, user name and level number. The current player's high score is shown above the table. This idea was chosen so that the player can compare themselves with others, even if they did not make it into the top ten. If the player is not logged in, the default name PLAYER is used.

+ **User Account**
<br/> Within the USER ACCOUNT menu option, a user account can be created to choose a name and save the high score. Both fields (username and password) must be filled in, otherwise an error message will appear. An error will also occur if an incorrect password is entered. If the user is already logged in, the USER ACCOUNT option will be replaced by the CHANGE PLAYER option in the menu. Clicking this will automatically log the player out. The username, a hash for the password and the high score are stored in a database.

<br/>

### Layout:
The overall layout of the game should feel like an old NES game. Therefore a simple design was chosen and (except for the error messages) only three colors were used: black for the background and white or lavender for the text.

<br/>

### Description of all project files (in alphabetical order):

+ **app.py**
<br/> This Python file is the most important part of the whole program, as it ties all the other files together. The application runs with Flask.
app.py handles which HTML page is displayed and gets the correct value for certain variables shown on those pages, such as the (high) score or username.
It also handles the data that is stored or requested from the database.

+ **dragon.png**
<br/> This image was chosen as a favicon for no particular reason or connection to the topic. The programmer just thought it would be funny.

+ **final.db**
<br/> The database stores each player's username, the hash of the password using the pbkdf2 function, and the corresponding high score.

+ **footer.html**
<br/> Since the footer of some HTML pages is the same, it is stored in a separate file to reduce redundancy.

+ **game.js**
<br/> This file describes the algorithm for the game itself. It is written in JavaScript. It contains variables for the level number, the current score and the random decimal number. As described before, the value of the random number depends on the level. As the level progresses, the decimal number is chosen from a larger range. The actions for clicking the buttons to change the binary numbers or to check the answer are also written here. Finally, a transition from the styles.css is applied when changing levels, and a GAME OVER screen is displayed in case of a wrong answer.

+ **helpers.py**
<br/> This Python file contains some helper functions that are used in the other files. They are placed here to reduce redundancy and improve readability.

+ **high-scores.html**
<br/> This shows the table with the ten highest high scores. The values are accessed through a loop from a dictionary created in app.py that gets its information from the database using SQL queries.

+ **index.html**
<br/> This is the start page that is shown when visiting the website. It shows the user name (if not logged in, the name PLAYER), the high score, the title of the game and a menu with four options to choose from: START GAME, INFORMATION, HIGH SCORES and USER ACCOUNT. If the user is already logged in, the last menu option is CHANGE PLAYER instead.

+ **info1.html**
<br/> The info page shows information about the structure of the binary system compared to the decimal system. A short example should make the description clearer.

+ **layout.html**
<br/> This file contains the general structure of every other HTML page. All other pages extend this template.

+ **password.html**
<br/> Here are two input fields for the username and the password. Clicking the button below will submit the input.

+ **requirements.txt**
<br/> This text file contains the packages needed to run the application.

+ **start.html**
<br/> This file contains the elements needed for the game itself: the current high score, the level, the decimal number, a table with buttons to change the binary numbers and a check button. The JavaScript file to run the game is linked in the script tags.

+ **styles.css**
<br/> All style changes are stored here.

