from setuptools import setup, find_packages

setup(
    name='CS2APY',
    version='0.1',
    author='James Li',
    author_email='jamesli196q@gmail.com',
    description='A high-level Python3 wrapper module for the Counter-Strike: 2 Premier Leaderboards API.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/j4mesli/cs2leaderboard-APY',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['maps.json', 'scoreboard.proto'],
    },
    scripts=['CS2APY.py', 'index.py', 'test.py'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
