from setuptools import setup

try:
    with open('LICENSE.txt', 'r') as f:
        _license = f.read()
except:
    _license = ''

try:
    with open('README.rst', 'r') as f:
        _readme = f.read()
except:
    _readme = ''

setup(
  name='yahoo_historical',
  packages=['yahoo_historical'],
  version='0.1.4',
  description='Fetches historical EOD (end of day) prices from yahoo finance',
  author='Andrew Porter',
  author_email='porter.r.andrew@gmail.com',
  license=_license,
  long_description=_readme,
  url='https://github.com/AndrewRPorter/yahoo-historical',
  download_url='https://github.com/AndrewRPorter/yahoo-historical/releases',
  install_requires=['setuptools', 'pandas', 'requests'],
 )
