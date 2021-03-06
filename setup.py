from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='krz.labjs',
      version=version,
      description="LABjs integration for Plone",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='labjs integration scripts',
      author='Roman Kozlovskyi',
      author_email='krzroman@gmail.com',
      url='https://github.com/kroman0/krz.labjs/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['krz'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.transformchain',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
