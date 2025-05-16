from setuptools import setup

requires = [
    'pyramid',
    'pyramid_jinja2',
    'sqlalchemy',
    'zope.sqlalchemy',
    'waitress',
    'psycopg2-binary',
]

setup(
    name='manajemen_matakuliah',
    version='0.1',
    description='Aplikasi manajemen matakuliah',
    author='Mychael Daniel',
    author_email='you@example.com',
    keywords='web pyramid sqlalchemy',
    packages=['manajemen_matakuliah'],
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = manajemen_matakuliah:main',
        ],
        'console_scripts': [
            'initialize_db = manajemen_matakuliah.scripts.initializedb:main',
        ],
    },
)
