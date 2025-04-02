from dagster_data_eng.assets import people_asset

import dagster as dg


people_assets = dg.load_assets_from_package_module(people_asset)


defs = dg.Definitions(assets=people_assets)
