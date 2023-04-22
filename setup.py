from setuptools import setup, find_packages

setup(
    name="gpodder-exporter",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add any other required packages here
    ],
    entry_points={
        "console_scripts": [
            "gpodder-exporter = gpodder_exporter.main:main",
        ]
    },
    author="Guvenc USANMAZ",
    author_email="gusanmaz@gmail.com",
    description="A CLI tool to export gPodder podcast titles and RSS URLs to a CSV file",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gusanmaz/gpodder-export",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
