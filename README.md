# papybot-fd

Pypybot-fd is an OpenClassrooms student project writen by Frederic DESCHAMPS.
You can ask to a bot to tell you a story and show you a map about a place you wrote in a web page.

How to install it ?
The code is opensource and can be found on GitHub at : https://github.com/fd-developer/papybot-fd.git

This appli had been writen in python3.8, HTML5,CSS3, JQuery and use BootStrap 4 to be responsive. You can find all requirements to install it in requirements.txt file.

Create a virtualEnv 
Download GitHub code in your directory.

You need a Google Key to use API Google. https://console.cloud.google.com/apis/
Your key must be ok for geocoding API and Maps Javascript API
Be carrefull about security please.


You can install the appli on a web server

-> for example on a local web server :
write  pip install requirements.txt  in a console and Enter
Enter your Google Key in an environment variable named  GOOGLE_KEY
write  python3 run.py  to start web server
go to  http://127.0.0.1:5000   and enjoy ;-) 

-> or on HEROKU if you want to use it ONLINE :
create an heroku account
create your app on heroku with their documentation
Enter your Google Key in an environment variable named  GOOGLE_KEY on keroku
write   git push heroku master   on a console and Enter 

go to   https://yourapp/herokuapp.com

to test this appli, go to    https://pappyapp.herokuapp.com

Best regards,
Fred D

