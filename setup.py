
from setuptools import setup

setup(name='ccdl',
      version='0.1',
      description='Comedy Central downloader',
      url='http://github.com/xabgesagtx/ccdl',
      author='xabgesagtx',
      author_email='xabgesagtx@riseup.net',
      license='MIT',
      packages=['ccdl'],
      install_requires=[
         'youtube-dl',
         'colorama'
      ],
      scripts= [
         'bin/cc-dl'
      ],
      zip_safe=False)
