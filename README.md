# Tax-office Desktop App
[University](https://www.bsuir.by/ "BSUIR") course project "Desktop Tax Office".
This is the complete source code and the build instruction for [Tax-office desktop App.](https://github.com/RuslanAl1mov/tax-officeDesktop "Source code")

[![Version](https://img.shields.io/badge/version-1.0.0-green)](https://github.com/RuslanAl1mov/tax-officeDesktop/releases)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

![Preview of Tax-office Desktop](https://github.com/RuslanAl1mov/tax-officeDesktop/blob/main/Screenshots/add_new_client.jpg "Preview of Tax-office Desktop")

The source code is published under Apache 2.0, the license is available [here][license]

## How to build project (Complicated method)
1. You have to install [Python3.5](https://www.python.org/downloads/release/python-350/ "Python3.5") or later.
2. Download the [source code](https://github.com/RuslanAl1mov/tax-officeDesktop/releases/download/v1.0.0/Source.code.full.rar "Tax-office v1.0.0").
3. Install [pyinstaller 5.1][pyinstaller] to bundle application.
4. Bundles a Python application and all its dependencies into a single package using [pyinstaller 5.1 documentation][pyinstallersdocs]

Simple way to build application is to use command

```sh
pyinstaller path_to_project\Main.py
```

After the folder with applicatin was bundled, add
```sh
AppWidgets
DataBaseFunctions
conf
icons
```
folders into created folder with bundeled application.

More variants of bundeling this project considering security and application size issues you can find using [pyinstaller documentation][pyinstallersdocs].

## How to build project (Simplified method)
1. You have to install [Python3.5](https://www.python.org/downloads/release/python-350/ "Python3.5") or later.
2. Download the [source code](https://github.com/RuslanAl1mov/tax-officeDesktop/releases/download/v1.0.0/Source.code.full.rar "Tax-office v1.0.0").
3. Install [auto-py-to-exe 2.20.1][auto-py-to-exe] and bundle application. <br/>

It is easy to configure bundeling project using [auto-py-to-exe 2.20.1][auto-py-to-exe]. Main reason to this is that [auto-py-to-exe 2.20.1][auto-py-to-exe] has GUI where you can point main issues which you want to have in your application

## Used libraries (Main of libraries)

[PyMySQL 1.0.2](https://pypi.org/project/PyMySQL/ "PyMySQL 1.0.2")<br/>
[PyQt5 5.15.6](https://pypi.org/project/PyQt5/ "PyQt5 5.15.6")<br/>
[configparser 5.2.0](https://pypi.org/project/configparser/ "configparser 5.2.0")

## Supported systems

The latest version is available for

* Windows 7 and above
* macOS 10.12 and above
* OS X 10.10 and 10.11
* Linux static build for 64 bit

## ER Database diagram

![Preview of Tax-office Desktop](Diagrams/Database%20ER.png)


[//]: # (LINKS)
[license]: LICENSE
[pyinstaller]: https://pypi.org/project/pyinstaller/
[pyinstallersdocs]: https://pyinstaller.org/en/stable/
[auto-py-to-exe]: https://pypi.org/project/auto-py-to-exe/
