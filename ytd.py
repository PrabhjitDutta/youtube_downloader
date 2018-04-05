import requests
import click
import os
from bs4 import BeautifulSoup
from pytube import YouTube

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.option('dir', '-d', type=click.Path(exists=True), default=os.getcwd(), help='give you the option to chose '
                                                                                   'directory where you want to '
                                                                                   'save the video')
@click.argument('search_term', type=click.STRING)
def cli(search_term, dir):

    '''
    This command helps you download YouTube videos just by entering the video name

    search_term :- Enter the name of the video.
    '''


    search = "https://www.youtube.com/results"
    params = {"search_query": "youtube " + search_term}

    r = requests.get(search, params=params)
    soup = BeautifulSoup(r.text, 'html5lib')

    result = soup.find('a', {'aria-hidden': 'true'})
    result = result['href']

    os.chdir(dir)
    YouTube("https://www.youtube.com" + result).streams.first().download()
