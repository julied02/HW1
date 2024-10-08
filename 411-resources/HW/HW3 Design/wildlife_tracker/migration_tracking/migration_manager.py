from typing import Optional

from wildlife_tracker.migration_tracking.migration import Migration
from wildlife_tracker.migration_tracking.migration_path import MigrationPath

class MigrationManager:
    def __init__(self,
                start_date: str) -> None:
        migrations: dict[int, Migration] = {}
        paths: dict[int, MigrationPath] = {}
        status: str = "Scheduled"
        self.start_date = start_date

def cancel_migration(migration_id: int) -> None:
    pass

def get_migrations() -> list[Migration]:
    pass

def get_migration_paths() -> list[MigrationPath]:
    pass

def get_migrations_by_current_location(current_location: str) -> list[Migration]:
    pass

def get_migrations_by_migration_path(migration_path_id: int) -> list[Migration]:
    pass

def get_migrations_by_start_date(start_date: str) -> list[Migration]:
    pass

def get_migrations_by_status(status: str) -> list[Migration]:
    pass

def remove_migration_path(path_id: int) -> None:
    pass

def schedule_migration(migration_path: MigrationPath) -> None:
    pass
