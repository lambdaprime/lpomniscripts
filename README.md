**lpomniscripts** - scripts for [Omniverse](https://www.nvidia.com/en-us/omniverse/)

# Requirements

- Omniverse code-2022.3.1

# Download

[Release versions](https://github.com/lambdaprime/lpomniscripts/tree/main/lpomniscripts/release/CHANGELOG.md)

# Install

- Download `lpomniscripts` package and extract it some folder
- Run `link_app` inside the folder. This will link **lpomniscripts** with Omniverse code available in the system. It is required because **lpomniscripts** relies on certain extensions provided by Omniverse Code. 

# Usage

```
./lp.omniscripts.sh --exec "scripts/<SCRIPT_NAME> <ARGS>"
```

Where:

`SCRIPT_NAME` - name of script to run. See list of available scripts below

`ARGS` - list of arguments to the script


# Available scrips

`convert2usd` - converts OBJ files to USD format.

# Documentation

[Development](DEVELOPMENT.md)

# Contributors

lambdaprime <intid@protonmail.com>
