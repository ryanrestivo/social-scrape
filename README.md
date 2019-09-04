# social-scrape
Quick and easy method to use on the back end to make sure content shared on Facebook has updated title, image and description when shared.

This requires: Python (2.7 or 3+), Requests (`https://2.python-requests.org/en/master/`), Permanent Facebook Token.

How to get a never expiring token `https://stackoverflow.com/questions/17197970/facebook-permanent-page-access-token`

Export this token ID in the shell script and then pass the URL string value into the shell. Scrapes should yield results in less than .0001 seconds, which the requests library handles.

The Graph API version will need to be manually changed, since Facebook does not give a version that can by dynamically changed.
