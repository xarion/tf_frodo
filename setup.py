import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tf_frodo_xarion",
    version="0.0.1",
    author="Erdi Calli",
    author_email="erdicalli@gmail.com",
    description="Use FRODO on any tensorflow model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xarion/tf_frodo.git",
    project_urls={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
