from dagster import (
    load_assets_from_modules,
    Definitions,
    define_asset_job,
    ScheduleDefinition,
)
from github_stars import assets

defs = Definitions(
    assets=load_assets_from_modules([assets]),
    schedules=[
        ScheduleDefinition(
            job=define_asset_job(name="daily_refresh", selection="*"),
            cron_schedule="@daily",
        )
    ],
)