#!/usr/bin/env python3
"""
Tee Time Booker - Main Entry Point
Mangrove Bay Golf Club (ForeUp)
"""
import argparse
from dotenv import load_dotenv
from loguru import logger

from src.utils import load_config
from src.booking import ForeUpBooker


def main() -> None:
    # Load environment variables
    load_dotenv()

    # CLI arguments
    parser = argparse.ArgumentParser(description="Mangrove Bay Tee Time Booker")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Run in dry-run mode (no actual booking)",
    )
    parser.add_argument(
        "--headless",
        action="store_true",
        default=True,
        help="Run browser in headless mode",
    )
    args = parser.parse_args()

    # Load configuration
    config = load_config()
    config["dry_run"] = args.dry_run or config.get("dry_run", True)
    config["headless"] = args.headless

    logger.info("🚀 Starting Mangrove Bay Tee Time Booker (ForeUp)")
    if config["dry_run"]:
        logger.warning("🔍 DRY-RUN MODE ENABLED — No bookings will be made")

    try:
        booker = ForeUpBooker(config)
        booker.run()
    except Exception as e:
        logger.error(f"💥 Fatal error: {e}")
        raise


if __name__ == "__main__":
    main()