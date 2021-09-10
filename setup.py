from distutils.core import setup
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="capmonster_python",
    packages=["capmonster_python"],
    url="https://github.com/alperensert/capmonster_python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    author="Alperen Sert",
    author_email="mail@alperenn.com",
    description="capmonster.cloud library for Python",
    requires=["requests"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    use_scm_version=True,
    test_suite="tests",
    setup_requires=["setuptools_scm", "wheel"],
    install_requires=["requests", "six"],
    python_requires=">=3",
    project_urls={
        "Documentation": 'https://github.com/alperensert/capmonster_python/wiki/',
        "Source": 'https://github.com/alperensert/capmonster_python/',
        "Tracker": 'https://github.com/alperensert/capmonster_python/issues',
    },
)