socialcrawl
=========

Script for fetching profile information from social networks

## Installation

Python 2.7.x is required, plus some python packages which can be installed by typing:

    pip install -r requirements.txt


## Configuration

Create a file for social network authentication at `socialcrawl/auth.py`. A sample file can be
found at `socialcrawl/auth_sample.py`. 

### Twitter

You will need to register an application, generate an OAuth access token for it and define `TWITTER_ACCESS_TOKEN`

### Facebook

You will need to register an app, generate an OAuth access token and define `FACEBOOK_ACCESS_TOKEN`

## Running the scripts

To get twitter profile info for the user 'twitter':

    PYTHONPATH=. python socialcrawl/clients/twitter.py twitter

For the Facebook 'zuck' user:

    PYTHONPATH=. python socialcrawl/clients/facebook.py zuck

## Tests

Test dependencies can be installed by typing:

    pip install -r test_requirements.txt

To run the test suite:

    PYTHONPATH=. nosetests -v -s
