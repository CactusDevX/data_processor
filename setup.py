from setuptools import setup, find_packages

with open("readme.md", "r") as f:
    long_description = f.read()

setup(name = 'processor',
      version='0.0.1',
      description='data_processor2',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Ivan Matešić',
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      include_package_data=True,
      install_requires=['sqlalchemy', 'pandas', 'requests', 'pyexcel', 'pyexcel-xls', 'pyexcel-xlsx', 'zipp',
                        'xlrd', 'bs4', 'unidecode' , 'psutil', 'xlsxwriter', 'openpyxl', 'wheel'],
      scripts=[]
      )