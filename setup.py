from setuptools import setup, find_packages

setup(
    name="trading-tools",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.10",
    install_requires=open("requirements.txt").read().splitlines(),
    description="Algorithmic trading tools and ML models",
)
