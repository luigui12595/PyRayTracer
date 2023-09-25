from setuptools import setup, find_packages

with open('README.md') as _f:
    _README_MD = _f.read()

_VERSION = '0.1'

setup(
    name='rayTracer', # TODO: rename. 
    version=_VERSION,
    description='A basic Ray Tracer based on the book "The Ray Tracer Challenge" by James Buck',
    long_description=_README_MD,
    classifiers=[
        # TODO: typing.
        "Typing :: Typed"
    ],
    packages=find_packages(include=['project*']),  # TODO.
    test_suite="testing",
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"],
    install_requires=["neuraxle"],
    include_package_data=True,
)

