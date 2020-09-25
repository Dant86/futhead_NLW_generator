import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="futhead-NLW-generator-Dant86",
    version="0.0.1",
    author="Vedant Pathak",
    author_email="vpathak@uchicago.edu",
    description="A Fifa NLW generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dant86/futhead_NLW_generator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
