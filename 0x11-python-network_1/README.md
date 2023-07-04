Python - Network #1
====================

This project involved learning how to use the urllib and requests Python libraries to send and receive HTTP messages to URL's. I practiced sending GET and POST requests, fetching JSON resources, and interacting with API's (the Star Wars API, GitHub API, and Twitter API).

Tasks
=====

0. What's my status? #0

0-hbtn_status.py: Python script that fetches https://intranet.hbtn.io/status.
Uses urllib.

1. Response header value #0

1-hbtn_header.py: Python script that displays the X-Request-Id response header variable of a request to a given URL.
Usage: ./1-hbtn_header.py <URL>
Uses urllib.

2. POST an email #0

2-post_email.py: Python script that sends a POST request to a given URL with a given email, and displays the response body.
Usage: ./2-post_email.py <URL> <email>.
Uses urllib.

3. Error code #0

3-error_code.py: Python script sends a request to a given URL and displays the response body.
Handles HTTP errors.
Uses urllib.

4. What's my status? #1

4-hbtn_status.py: Python script that fetches https://intranet.hbtn.io/status.
Uses requests.
