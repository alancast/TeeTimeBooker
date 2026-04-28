from playwright.sync_api import sync_playwright, Page
from loguru import logger
import os

from src.utils import take_screenshot, save_trace


class ForeUpBooker:
    def __init__(self, config: dict):
        self.config = config
        self.dry_run = config.get("dry_run", True)
        self.headless = config.get("headless", True)

        # Get credentials with explicit None checks
        self.email: str = os.getenv("FOREUP_EMAIL") or ""
        self.password: str = os.getenv("FOREUP_PASSWORD") or ""

        if not self.email or not self.password:
            raise ValueError(
                "❌ FOREUP_EMAIL and FOREUP_PASSWORD must be set in .env file"
            )

    def run(self):
        """Main execution flow"""
        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=self.headless,
                slow_mo=500 if not self.headless else 0,
            )

            context = browser.new_context(
                viewport={"width": 1440, "height": 900},
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
            )

            page = context.new_page()

            try:
                self.login(page)
                self.navigate_to_tee_sheet(page)
                self.search_and_book(page)

                logger.success("✅ Process completed successfully!")
            except Exception as e:
                logger.error(f"❌ Error during booking: {e}")
                take_screenshot(page, "error")
                save_trace(context, "error_trace")
            finally:
                browser.close()

    def login(self, page: Page):
        """Login to ForeUp"""
        logger.info("🔑 Logging into ForeUp...")

        page.goto("https://foreupsoftware.com/index.php/booking/login")

        # Wait for login form
        page.wait_for_selector('input[type="email"], input[name="email"]', timeout=15000)

        page.fill('input[type="email"], input[name="email"]', self.email)
        page.fill('input[type="password"], input[name="password"]', self.password)

        page.click('button[type="submit"], input[type="submit"]')

        page.wait_for_load_state("networkidle")
        logger.success("✅ Logged in successfully")

    def navigate_to_tee_sheet(self, page: Page):
        """Navigate to the tee time booking page"""
        logger.info("📅 Navigating to tee time sheet...")

        # TODO: Replace with your actual Mangrove Bay ForeUp booking URL
        booking_url = "https://foreupsoftware.com/index.php/booking/YOUR_COURSE_ID_HERE"

        page.goto(booking_url)
        page.wait_for_load_state("networkidle", timeout=20000)
        logger.info("✅ Arrived at tee time booking page")

    def search_and_book(self, page: Page):
        """Search for desired tee times and book"""
        logger.info("🔍 Searching for available tee times...")

        if self.dry_run:
            logger.info("🛑 DRY RUN MODE — Stopping before any booking")
            take_screenshot(page, "dry_run_final_view")
            return

        logger.warning("⚠️  Booking logic not implemented yet")
