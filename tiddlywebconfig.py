# A basic configuration.
# `pydoc tiddlyweb.config` for details on configuration items.
import mangler

config = {
    'system_plugins': ['tiddlywebplugins.model'],
    'secret': '150d9eabe2bd925c536ef4451afe3c345cebdb2b',
    'twanager_plugins': ['tiddlywebwiki'],
	'static_url_dir': 'static',
	'static_file_dir': './static',    
    'log_level': 'DEBUG',
}
