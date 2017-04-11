from setuptools import setup

setup(
    name='tripadvisor_convert',
    version='0.1',
    url='',
    license='',
    author='Nicholas A. Del Grosso',
    author_email='delgrosso.nick@gmail.com',
    description='Short Package and CLI used to parse the JSON Tripadvisor data set into a more convenient Pandas DataFrame format.',
    install_requires=[
        'pandas',
        'lxml',
        'bs4',
    ],
    py_modules=['tripadvisor_convert'],
    entry_points = '''
            [console_scripts]
            tsc=tripadvisor_convert:to_csv
    ''',
)
