#!/usr/bin/env python
# coding=utf-8


import flask
from flask import Flask

import requests
import requests_oauthlib

from parallel import make_parallel_requests

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def index():
    ''' Endpoint to query from google, ddg and twitter '''
    term = flask.request.args.get('q')

    # twitter
    auth = requests_oauthlib.OAuth1(
        app.config.get('CONSUMER_API_KEY'),
        app.config.get('CONSUMER_SECRET_KEY'),
        app.config.get('ACCESS_TOKEN'),
        app.config.get('ACCESS_TOKEN_SECRET'),
    )
    twitter_url = app.config.get('TWITTER_URL_TEMPLATE') % term

    # google
    google_url = app.config.get('GOOGLE_URL_TEMPLATE') % (
        app.config.get('GOOGLE_API_KEY'),
        app.config.get('CUSTOM_SEARCH_ENGINE'),
        term
    )

    # ddg
    ddg_url = app.config.get('DDG_URL_TEMPLATE') % term

    urls_info = {
        'twitter': {
            'url': twitter_url,
            'args': auth,
        },
        'google': {
            'url': google_url,
            'args': None,
        },
        'duckduckgo': {
            'url': ddg_url,
            'args': None,
        },
    }

    app_url = app.config.get('APP_URL')
    output = {
        'query': term,
        'results': {
            'google': {
                'url': app_url + '?q=' + term,
                'text': None,
            },
            'twitter': {
                'url': app_url + '?q=' + term,
                'text': None,
            },
            'duckduckgo': {
                'url': app_url + '?q=' + term,
                'text': None,
            }
        }
    }

    # make requests parallely
    # each request updates the output - since dict() is mutable
    # Queue library takes care of the locking for us
    make_parallel_requests(urls_info, output)
    response_code = output.get('status_code')
    if response_code:
        output.pop('status_code')
        return flask.jsonify(output), 206

    return flask.jsonify(output)


if __name__ == '__main__':
    app.run(debug=True)
