from setuptools import setup, find_packages


setup(
    name='icorn',
    version='0.1dev0',
    description='icon generator',
    author='TakesxiSximada',
    author_email='sximada+icorn@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'jumon',
        'pillow',
    ],
    entry_points="""\
    [console_scripts]
    icorn = icorn.commands:main
    """,
)
