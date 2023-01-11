from setuptools import setup

setup(name='chandu',
      version='0.1',
      description='thinxview device core package for decode the sensor or gateway packets',
      author='thinxview',
      author_email='subramani.krishnan@gndsolutions.com',
      license='MIT',
      packages=['py_thinxview_core'],
      scripts=['.bin/test.py'],
      zip_safe=False)
