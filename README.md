# YOFHL DB
#### Video Demo:  TODO
#### Description:
I wrote a web app that organizes and displays data from my fantasy hockey league in ways that our native fantasy platform (Fantrax) cannot using javascript, python and SQL.

The first thing I did was write scraper.py to scrape data from the web. The data I scraped was compiled into several different CSV files, in hindsight, I could've done this with a single CSV.

Once I had the spreadsheets organized the way I liked (irrelevant data removed, columns renamed, etc) I made a database in sqlite (hockey.db) and then wrote data_import.py to import the data in my CSVs to my database.

Once I had my database working I used flask to make my web app. Traffic is routed via my app.py script and all of my html templates are in my templates folder. I am using the helpers.py script from CS50 mostly to make use of the apology function. There is definitely a lot of room for improvement here. If I were going to pay for web hosting to actually keep this site up full-time I would make my search a little more sophisticated rather than the simple LIKE %s% parameters I'm using currently.

I would also make an effort to display team information dynamically. So instead of having a template for each team, I could have a single team template and dynamically generate the team information depending on the team link the user clicks on.

Perhaps I will return to this sometime and action the above changes, but as is, I am pretty happy with the results! The other players in my fantasy hockey league had fun reviewing the highest scorers for each team and all-time career stats. These are data points that were previously not available to us. It's also cool to see the all-time seasons listed among each other, something Fantrax does not allow for.