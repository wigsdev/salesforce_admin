#!/usr/bin/env python
"""
Force Re-Seed Script for Lumina Dashboard

This script forces a complete re-seed of the Lumina dashboard data,
updating all doc_path values that are currently NULL.

Usage:
    python scripts/force_reseed.py
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.seed_data import seed_data


def main():
    print("\n" + "=" * 80)
    print("🔄 FORCE RE-SEED: Lumina Dashboard")
    print("=" * 80 + "\n")

    print("⚠️  This will UPDATE all existing tasks with corrected doc_path values.")
    print("⚠️  Existing task completion status will be PRESERVED.\n")

    # Confirm
    response = input("Continue? (yes/no): ")
    if response.lower() != "yes":
        print("\n❌ Aborted.")
        return

    print("\n🚀 Starting re-seed...\n")

    try:
        seed_data()
        print("\n" + "=" * 80)
        print("✅ RE-SEED COMPLETED SUCCESSFULLY")
        print("=" * 80 + "\n")
        print("📄 All doc_path values have been updated.")
        print("🔄 Refresh the dashboard to see file icons.\n")
    except Exception as e:
        print("\n" + "=" * 80)
        print("❌ RE-SEED FAILED")
        print("=" * 80 + "\n")
        print(f"Error: {e}\n")
        raise


if __name__ == "__main__":
    main()
