from setuptools import setup, find_packages

VERSION = '1.0.0'

setup (
    name = 'project-name',
    version = VERSION,
    description = 'Description goes here.',
    author = 'First Last',
    author_email = 'user@site.com',
    maintainer = 'First Last',
    maintainer_email = 'user@site.com',
    url = 'https://github.com/user/repo',
    license = 'http://www.apache.org/licenses/LICENSE-2.0',
    platforms = ['any'],
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
)