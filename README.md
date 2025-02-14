# Activate a nRF Connect toolchain environment

This script activates a [nRF Connect SDK](https://github.com/nrfconnect/sdk-nrf)
toolchain environment. Initial version was written by Jakob Ruhe 2024 and a
polished version was released early 2025.

Feel free to say something if you find the script useful or if you have any
suggestions for improvements!

## Installation

Clone this repository and put it somewhere. In this documentation it is assumed
that you clone it into `~/nrfenv` but you can put it wherever you want.

## Usage

Use the
[nrfutil](https://www.nordicsemi.com/Products/Development-tools/nRF-Util) like
this to get the paths to the installed toolchains:

``` shell
nrfutil toolchain-manager list
```

Example output:

```
  Version  Toolchain
* v2.9.0   /home/jakob/ncs/toolchains/b77d8c1312
```

Now that you have the path to the toolchain you want to activate, you may verify
that there is a file named `environment.json` in that directory.

With this knowledge you can activate the toolchain environment by using this utility:

``` shell
~/nrfenv/nrfenv.py /home/jakob/ncs/toolchains/b77d8c1312/environment.json
```

To deactivate the environment, simply run:

``` shell
exit
```

## License
See the [LICENSE](LICENSE) file for license rights and limitations (MIT).
