#!/usr/bin/env python3
"""
welcome-to-project.py
A friendly onboarding script for new contributors.
"""

import textwrap
import webbrowser
from datetime import datetime

# Project summary (hard-coded, ~200 words)
SUMMARY = """
The Table History Project is designed to make sense of the U.S. Census Bureau’s public API by tracking the history of its tables. Normally, if you want to know when a table first appeared, disappeared, or how its description has changed over time, you’d have to dig through dataset after dataset manually. That’s time-consuming and error-prone.

This project solves that by using Python to automatically access Census API endpoints across all available years. The program collects details about each table—such as when it first appeared, the years it’s missing, and how its name or description has evolved. The result isn’t just raw data: the goal is to produce an HTML page (or set of linked pages) that lets you search for a table ID like B18104 and instantly see its full history at a glance.

We’re working with both ACS 1-year and 5-year datasets to ensure the information is thorough and reliable. The big idea is to save researchers, analysts, and anyone interested in Census data from repetitive manual work—turning table history into a tool that’s easy to use and explore.

Welcome aboard! We’re excited to have you here, and your contributions will help make this vision a reality.
"""

def get_full_data_year():
    """Return the calendar year with both 1 nad 5 year data published."""
    return datetime.now().year - 2

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

    # Build endpoint list with resolved year
    year = get_full_data_year()
    endpoints = [
        ("All datasets (master list)", "https://api.census.gov/data.json"),
        ("ACS 1-Year dataset", f"https://api.census.gov/data/{year}/acs/acs1.json"),
        ("ACS 5-Year dataset", f"https://api.census.gov/data/{year}/acs/acs5.json"),
        ("ACS 1-Year groups", f"http://api.census.gov/data/{year}/acs/acs1/groups.json"),
        ("ACS 5-Year groups", f"http://api.census.gov/data/{year}/acs/acs5/groups.json"),
    ]

    # Show menu
    print(f"Available Census API endpoints (using year = {year}):")
    for i, (label, url) in enumerate(endpoints, start=1):
        print(f"{i}. {url}  <-- {label}")
    print()

    # Interactive loop
    while True:
        choice = input("Enter the number of an endpoint to open, or 'q' to quit: ").strip().lower()
        if choice == "q":
            print("\nThanks for checking out the project! Happy coding 🎉")
            break
        elif choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(endpoints):
                label, url = endpoints[idx - 1]
                print(f"Opening {label} in your browser...")
                webbrowser.open(url)
            else:
                print("Invalid number. Please pick from the list.")
        else:
            print("Invalid input. Please enter a number or 'q'.")

    print("-" * 70)

if __name__ == "__main__":
    main()
