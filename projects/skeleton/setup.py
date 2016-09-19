try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
'description':'My Project',
'author':'lane',
'url':'121.40.54.115',
'download_url':'121.40.54.115',
'author_email':'xyf2424094@gmail.com',
'version':'0.1',
'install_requeries':['nose'],
'packages':['NAME'],
'scripts':[],
'name':'testskeleton'
}

setup(**config)

