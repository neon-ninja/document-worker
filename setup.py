from setuptools import setup, find_packages


with open('README.md') as f:
    long_description = ''.join(f.readlines())

setup(
    name='document_worker',
    version='2.1.0',
    description='Worker for assembling and transforming documents',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Marek Suchánek',
    keywords='documents worker jinja2 pandoc pdf-generation',
    license='Apache License 2.0',
    url='https://github.com/ds-wizard/document-worker',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Text Processing',
        ],
    zip_safe=False,
    python_requires='>=3.8, <4',
    install_requires=[
        'click',
        'pika',
        'pymongo',
        'jinja2',
        'markdown2',
        'tenacity',
    ],
    entry_points={
        'console_scripts': [
            'docworker=document_worker:main',
        ],
    },
)