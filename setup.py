from distutils.core import setup

setup(
    name="capmonster_python",
    version="1.3.0",
    packages=["capmonster_python"],
    url="https://github.com/alperensert/capmonster_python",
    download_url="https://github.com/alperensert/capmonster_python/archive/v1.3.0.tar.gz",
    license="MIT",
    author="Alperen Sert",
    author_email="alperenssrt@gmail.com",
    description="Unofficial capmonster.cloud library for Python",
    requires=["requests"],
    classifiers=["Programming Language :: Python :: 3.4"]
)