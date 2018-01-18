import versioneer
from setuptools import setup

setup(name='krtc',
      version=versioneer.get_version(),
      cmdclass=versioneer.get_cmdclass(),
      description='A small utility class for using Kerberos authentication with Python requests',
      url='https://github.com/slaclab/krtc.git',
      author='Murali Shankar',
      author_email='mshankar@slac.stanford.edu',
      license='MIT',
      packages=['krtc'],
      zip_safe=False)
