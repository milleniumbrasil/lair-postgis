# src/lair_postgis/cli.py - Entry point for lair-postgis
import argparse
import sys

def main():
    """
    Main entry point for lair-postgis.
    Parses command-line arguments and performs scaffolding.
    """
    parser = argparse.ArgumentParser(
        prog="lair-postgis",
        description="Scaffold a PostGIS project with Docker and init scripts."
    )
    parser.add_argument(
        "--in", dest="input_file", required=True, help="Path to your lair.sql file"
    )
    parser.add_argument(
        "--out", dest="output_dir", default=".", help="Output directory"
    )
    parser.add_argument(
        "--version", action="version", version=__import__("lair_postgis").__version__
    )
    args = parser.parse_args()
    # For now, just echo the inputs
    print(f"lair-postgis called with input: {args.input_file}")
    print(f"Output directory: {args.output_dir}")
    # TODO: implement scaffolding logic
    sys.exit(0)