#!/usr/bin/env python3
"""
welcome-to-project.py
A friendly onboarding script for new contributors.
"""

import textwrap

# Project summary (hard-coded, ~200 words)
SUMMARY = """
The Table History Project is designed to make sense of the U.S. Census Bureau’s public API by tracking the history of its tables. Normally, if you want to know when a table first appeared, disappeared, or how its description has changed over time, you’d have to dig through dataset after dataset manually. That’s time-consuming and error-prone.

This project solves that by using Python to automatically access Census API endpoints across all available years. The program collects details about each table—such as when it first appeared, the years it’s missing, and how its name or description has evolved. The result isn’t just raw data: the goal is to produce an HTML page (or set of linked pages) that lets you search for a table ID like B18104 and instantly see its full history at a glance.

We’re working with both ACS 1-year and 5-year datasets to ensure the information is thorough and reliable. The big idea is to save researchers, analysts, and anyone interested in Census data from repetitive manual work—turning table history into a tool that’s easy to use and explore.

Welcome aboard! We’re excited to have you here, and your contributions will help make this vision a reality.
"""

def main():
    # Print header
    print("=" * 70)
    print("        Welcome to the Table History Project".upper())
    print("=" * 70)
    print()

    # Wrap and print summary
    wrapped = textwrap.fill(SUMMARY, width=70)
    print(wrapped)
    print()

    print("-" * 70)
    print("End of welcome message. Happy coding!")
    print("-" * 70)

if __name__ == "__main__":
    main()
