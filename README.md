# TweakZipper

just a dead simple deb/dylib -> trollfools zip converter.

for some reason, you can't inject debs into apps installed from the appstore? at least that's what i understand from the [Limitations](https://github.com/Lessica/TrollFools?tab=readme-ov-file#limitations) tab:

> Encrypted App Store applications with bare dynamic library

this does what you'd expect, just pass a deb and it'll extract the necessary files and add them to the zip.

some code taken from [cyan/cgen](https://github.com/asdfzxcvbn/pyzule-rw).

# installation

just the usual platforms supported: linux/WSL & macOS

again, like usual, you need the `ar` and `tar` commands installed on your system.

then:

1. install and setup [pipx](https://github.com/pypa/pipx?tab=readme-ov-file#install-pipx)

2. `pipx install --force https://github.com/asdfzxcvbn/TweakZipper/archive/main.zip`

