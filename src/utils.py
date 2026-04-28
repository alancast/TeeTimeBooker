import yaml
from pathlib import Path
from loguru import logger
from datetime import datetime


def load_config() -> dict:
    """Load configuration from settings.yaml"""
    config_path = Path("config/settings.yaml")
    
    if not config_path.exists():
        logger.warning("settings.yaml not found, using default config")
        return {"dry_run": True}

    with open(config_path, encoding="utf-8") as f:
        config = yaml.safe_load(f) or {}

    # Merge with environment variables if needed
    config["dry_run"] = config.get("dry_run", True)
    return config


def take_screenshot(page, name: str = "screenshot"):
    """Take screenshot for debugging"""
    screenshots_dir = Path("screenshots")
    screenshots_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = screenshots_dir / f"{name}_{timestamp}.png"
    page.screenshot(path=path)
    logger.info(f"📸 Screenshot saved: {path}")


def save_trace(context, name: str = "trace"):
    """Save Playwright trace for debugging"""
    traces_dir = Path("traces")
    traces_dir.mkdir(exist_ok=True)
    
    path = traces_dir / f"{name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    context.storage_state(path=path)  # You can also use tracing.start() for full trace
    logger.info(f"🔍 Trace saved: {path}")
