from setuptools import setup, find_packages

setup(name='MODEL1303140000',
      version=20140916,
      description='MODEL1303140000 from BioModels',
      url='http://www.ebi.ac.uk/biomodels-main/MODEL1303140000',
      maintainer='Stanley Gu',
      maintainer_url='stanleygu@gmail.com',
      packages=find_packages(),
      package_data={'': ['*.xml', 'README.md']},
    )