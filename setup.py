#from distutils.core import setup
from setuptools import setup

with open("README.md") as f:
  long_description = f.read()

setup(
  name = 'datahandler',
  packages = ['datahandler'], # this must be the same as the name above
  version = '0.1.1',
  description = 'Multipurpose datahandler, read data from source like a Sensor & handle it to send, save, trigger, ... by config.',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Takeyuki UEDA',
  author_email = 'gde00107@nifty.com',
  license='MIT',
  url = 'https://github.com/UedaTakeyuki/datahandler', # use the URL to the github repo
  keywords = ['testing', 'logging', 'example'], # arbitrary keywords
  classifiers = ['Development Status :: 4 - Beta',
                 'Programming Language :: Python',
                 'Topic :: Terminals'
  ],
)
