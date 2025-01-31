import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="api_gateway_3scale_auth",
    version="0.1",

    description="A deployment of AWS API Gateway and 3scale Auth",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "api_gw"},
    packages=setuptools.find_packages(where="api_gw"),

    install_requires=[
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
