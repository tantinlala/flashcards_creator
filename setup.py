from setuptools import setup, find_packages

setup(
    name='flashcards_creator',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'genanki',
        'google-genai',
        'argparse',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'create_flashcards=create_flashcards.main:main',
        ],
    },
    author='Nicholas Tantisujjatham',
    author_email='nicholas.tantisujjatham@gmail.com',
    description='A Python package to generate Anki flashcards using genanki and generative AI',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/tantinlala/flashcards_creator',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)