from setuptools import setup

setup(
    name="yahoo_historical",
    packages=["yahoo_historical"],
    version="1.0.0",
    description="Fetches historical EOD (end of day) prices from yahoo finance",
    author="Andrew Porter",
    author_email="porter.r.andrew@gmail.com",
    license="MIT License",
    url="https://github.com/AndrewRPorter/yahoo-historical",
    download_url="https://github.com/AndrewRPorter/yahoo-historical/releases",
    install_requires=["setuptools", "pandas", "requests"],
)
