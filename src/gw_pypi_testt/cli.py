"""Command line interface for gw_pypi_testt."""

import argparse
import sys

from gw_pypi_testt import __version__


def parse_args(args=None):
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="t")
    parser.add_argument(
        "--version", action="store_true", help="Show version and exit"
    )
    
    return parser.parse_args(args)


def main(args=None):
    """Run the main program."""
    args = parse_args(args)
    
    if args.version:
        print(f"gw_pypi_testt v{__version__}")
        return 0
    
    # Add your code here
    print("Hello from gw_pypi_testt!")
    print(args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
