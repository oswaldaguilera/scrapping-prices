from setuptools import setup

setup(
    name="scrapping-prices",
    version='0.1',
    py_modules=["scrapping-prices"],
    install_requires=[
        'Click',
        'requests',
        'beautifulsoup4'
    ],
    entry_points='''
        [console_scripts]
        scrapping-prices=main:cli
    ''',
)