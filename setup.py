from setuptools import setup, find_packages

setup(
    name='GitReleaseNotesGenerator',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'pystache'
    ],
    entry_points='''
        [console_scripts]
        gitlab_release=GitReleaseNotesGenerator.main:main
    ''',
)
