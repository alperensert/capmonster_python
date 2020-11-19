from distutils.core import setup

with open("README.md", "r") as rmf:
    readme = rmf.read()

setup(
    name="capmonster_python",
    version="1.2",
    packages=["python_capmonster"],
    url="https://github.com/alperensert/python_capmonster",
    download_url="https://github.com/alperensert/python_capmonster/archive/v1.2.tar.gz",
    license="MIT",
    author="Alperen Sert",
    author_email="alperenssrt@gmail.com",
    description="Unofficial capmonster.cloud library for Python",
    long_description= str(readme),
    requires=["requests"],
    classifiers=["Programming Language :: Python :: 3.4"]
)
