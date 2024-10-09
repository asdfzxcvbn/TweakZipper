# type: ignore

from setuptools import setup

setup(
  name="TweakZipper",
  version="1.0",
  description="a deb/dylib to trollfools zip converter",
  author="zx",
  author_email="zx@hrzn.email",
  packages=["TweakZipper"],
  python_requires=">=3.9",
  entry_points={
    "console_scripts": [
      "tweakzipper=TweakZipper.__main__:main"
    ]
  }
)

