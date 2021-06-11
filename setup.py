from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='signinghubapi',
    version='0.1.2',
    description='Package with default calls for the SigningHub API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/erwinmintiens/signinghub-api',
    author='Erwin Mintiens',
    author_email='erwin.mintiens@gmail.com',
    keywords=['SigningHub', 'API'],
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=['requests'],
    license_files=('LICENSE',),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License"
    ]
)
