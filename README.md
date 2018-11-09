# redditscrape

A collection of simple scripts to scrape data from reddit.

- getThreadLinks.py creates a file of thread links from a given topic.

- getComments.py reads the file created by getThreadLinks.py and scrapes all the posts for each thread. 
The posts for each thread are stored in a separate file. The first line of the file includes the symbol @@@THREAD@@@, the thread link, 
and the text of original post, separated by a \t. The remaining lines include info for the replies to the original post and have the following format:

[level number]\t[username of post creator]\t[point num]\t[post text] 

The level number can be used to determine the parent/child of each post.

Both scripts assume that chromedriver.exe exists in the same folder. 
