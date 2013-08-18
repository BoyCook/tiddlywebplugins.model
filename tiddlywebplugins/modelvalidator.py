from tiddlywebplugins.utils import do_html
from tiddlywebplugins.utils import replace_handler
from tiddlyweb.model.bag import Bag
from tiddlyweb.model.recipe import Recipe
from tiddlyweb.control import filter_tiddlers
from tiddlyweb.store import Store
from tiddlyweb.config import config
from tiddlyweb import control
from Loader import Loader
from ScheduledLoad import ScheduledLoad
from MyLifestream import MyLifestream

SUCCESS_RESPONSE = ['<html><body><h1>Done</h1></body></html>']

def init(init_config):
    selector = init_config['selector']
    replace_handler(selector, '/', GET=home_page)
    selector.add('/loadall', GET=load_all)
    store = Store(config['server_store'][0], config['server_store'][1], environ={'tiddlyweb.config': config})
    

@do_html()
def home_page(environ, start_response):
    start_response('200', [('Content-Type', 'text/html; charset=UTF-8')])
    return SUCCESS_RESPONSE    

# get_model_for_tiddler
