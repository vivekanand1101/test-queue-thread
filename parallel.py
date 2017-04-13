#!/usr/bin/env python
# coding=utf-8

import Queue
import signal
from threading import Thread

import requests
from requests import ReadTimeout

class URLThread(Thread):
    ''' Make each request in a different thread '''
    def __init__(self, queue, output):
        ''' Instantiate the thread object '''
        super(URLThread, self).__init__()
        self.queue = queue
        self.output = output
        self.response = None

    def run(self):
        ''' Run the thread, request is made here '''
        while True:
            # auth will be None except for Twitter
            website, url, auth = self.queue.get()
            try:
                self.response = requests.get(url, auth=auth, timeout=0.9)
                self.output['results'][website]['text'] = self.response.json()
            except ReadTimeout, ConnectTimeout:
                self.output['results'][website]['text'] = 'Request taking too long'
                # Status code for partial content
                self.output['status_code'] = 206
            self.queue.task_done()


def make_parallel_requests(urls_info, output):
    ''' Make parallel requests using thread '''

    queue = Queue.Queue()
    for url in urls_info:
        t = URLThread(queue, output)
        t.setDaemon(True)
        t.start()
        # the args includes only the auth in case of twitter
        queue.put((url, urls_info[url].get('url'), urls_info[url].get('args')))

    queue.join()
