from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="wagtail-collectionmodeladmin",
    version="0.1.0",
    description="Model Admin extension that utilizes the Wagtail collections",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Babis Kaidos",
    author_email="ckaidos@intracom-telecom.com",
    url="https://github.com/BabisK/wagtail-collectionmodeladmin",
    install_requires=[
        "wagtail>=2.6"
    ],
    license="BSD",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Framework :: Wagtail :: 2"
    ],
)
