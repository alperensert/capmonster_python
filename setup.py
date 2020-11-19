from distutils.core import setup

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
    requires=["requests"],
    classifiers=["Programming Language :: Python :: 3.4"]
)
