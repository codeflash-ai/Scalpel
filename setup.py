from distutils.core import setup

setup(name='Scalpel',
      version='1.0',
      description='Scalpel: A Python Program Analysis Framework',
      author='Jiawei Wang',
      author_email='jiawei.wang1@monash.edu',
      url='https://www.monash.edu',
      packages=['scalpel', 'scalpel.call_graph', 'scalpel.import_graph'],
     )
