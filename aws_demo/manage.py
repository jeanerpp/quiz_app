"""Package-installed management command for aws_demo."""

import os
import sys


def main() -> None:
    """Run Django administrative tasks using project settings."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aws_demo.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Ensure dependencies are installed in this environment."
        ) from exc

    argv = sys.argv[:]
    if argv:
        argv[0] = "aws-demo-manage"
    else:
        argv = ["aws-demo-manage"]

    execute_from_command_line(argv)
