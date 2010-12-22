from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='dolmen.app.metadatas',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='',
      author_email='',
      url='',
      license='GPL',
     packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['dolmen', 'dolmen.app'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'dolmen.app.layout',
          'dolmen.app.security',
          'dolmen.content',
          'dolmen.menu',
          'setuptools',
          'zeam.form.base',
          'zeam.form.composed',
          'zeam.form.layout',
          'zeam.form.ztk',
          'zope.dublincore',
          'grokcore.viewlet',
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
