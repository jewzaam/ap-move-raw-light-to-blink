"""
Project-specific configuration constants for ap-move-lights.
These are specific to this tool and not shared across projects.
"""

# Directory name constants (workflow state directories)
DIRECTORY_BLINK = "10_Blink"
DIRECTORY_ACCEPT = "accept"

# File pattern constants
INPUT_PATTERN_ALL = ".*"

# Regex pattern to extract target directory (parent of DATE directory)
# Matches paths like: /path/to/target/DATE_2024-01-01/file.fits
TARGET_DIR_PATTERN = r"(.*)[/\\]DATE.*"

# Progress indicator: print a dot every N files processed
PROGRESS_INTERVAL = 50
