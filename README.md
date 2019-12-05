
1.Executive summary

Goodreads is a social cataloging website where the users can search its database to find book reviews, give ratings and suggestions along with creating their own reading list. A recommender system is an algorithm which uses gradient descent to calculate the ratings which users would have highly rated. My goal for this capstone is to use the ratings and book descriptions for books using unsupervised learning and Natural language processing techniques in order to build a recommender system. 
Pairwise distance and cosine similarities were used to measure the distance between each book against the remaining. The purpose of this is to find a book which has the least distance i.e closer to 0.
Data collection tools used were goodreads API, Selenium and Beautiful Soup, which scraped data from the web page. User based and content based recommender system was able to predict similar books based on user ratings and book description. The limitations for this project was data collection. It is a very slow process and uses a lot of RAM. Thus for the purpose of this capstone I considered a part of my dataset to run the recommender system.

2.Data Collection for book ratings and description

Goodreads API key was not very useful for data collection. Web scraping tools like Selenium and Beautiful Soup had to be used for data collection.Selenium is a web browser automation tool which helps click, fill out information and so on. Sometimes websites ban web scrapers if the requests are very frequent. Thus time was added at regular intervals in the function. ChromeDriver is a separate executable that Selenium WebDriver uses to control Chrome. Once the ChromeDriver is setup we add our goodreads url to the driver in order to get the webpage. Beautiful Soup is a python package for parsing HTML and XMLthat can be used to extract data. The function was created based on this basic concept of selenium in order to get ratings from all the pages. The maximum pages are 10. The scraper breaks when there is no web element and moves on to the next book. This continues until it reached the last book mentioned in the range. Once the data was collected it was saved as a csv file as a dataframe. The same function was used to scrape the description as well.

3.Recommender Systems

3.1.Item-based collaborative recommender system

Collaborative filtering methods to collect and analyze information on user behavior i.e. ratings and then predicts what the users will like based on their similarity to other users. For an item based collaborative recommender we take the weighted sum of ratings of other books.

3.2.Content based recommender system

Content-based recommender system uses characteristics such as the description of the books. We will figure out what kind of books a user likes based on his history. The system groups similar products based on their features. Content-based systems rely on machine learning techniques to calculate the probabilities of user liking. Machine learning techniques include neural networks, decision trees classifiers etc.Same process as the item based recommender system with the exception of  column names and the index values. 

3.3.Hybrid recommender system

This approach takes calculates content based recommender and item based recommender separately at first, then collaborates the outputs to produce a system that considers both the systems.

4.Recommendations and next steps


Collect more data for better results, since the RAM was an issue in my computer, I would run this on AWS instead. Once more data is collected more Natural Language techniques can be used to filter out results in a content based recommender. Next steps would be adding links from amazon to purchase the book on the websites along with links to meet up groups for books. Lastly I would continue to work on user feedbacks if they like the books being recommended.
