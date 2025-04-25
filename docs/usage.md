# Usage

## Installation

 ```bash
 pip install lair-postgis
 ```

## Command Line Interface

 ```bash
 lair-postgis --in path/to/lair.sql [--out path/to/install]
 ```

 **Options**:

 - `--in`: Path to your `lair.sql` file (required).
 - `--out`: Directory to scaffold the project (default: current directory).
 - `--version`: Show version information.

 **Example**:

 ```bash
 lair-postgis --in ./lair.sql --out ./my-project
 ```