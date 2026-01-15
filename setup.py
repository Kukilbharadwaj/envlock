from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="envlock",
    version="0.1.1",
    author="sazzadur",
    description="Encrypt and decrypt .env files safely for internal teams",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sazzadur/envlock",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Security :: Cryptography",
    ],
    python_requires=">=3.8",
    install_requires=[
        "cryptography>=41.0.0",
    ],
    entry_points={
        "console_scripts": [
            "envlock=envlock.cli:main",
        ],
    },
    keywords=["env", "dotenv", "secrets", "encryption", "cli"],
)
