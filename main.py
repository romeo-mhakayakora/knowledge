# Root-level entry point for mkdocs-macros-plugin
# Delegates logic to tools/macros/main.py

import os
import sys

# Ensure the project root is in python path
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from tools.macros.main import define_env
