from typing import Any

from wildlife_tracker.migration_tracking.migration_path import MigrationPath

class Migration:
    def __init__(self, current_date: str,
                current_location: str,
                
                migration_id: int,
                migration_path: MigrationPath,
                species: str) -> None:
        self.current_date = current_date
        self.current_location = current_location
        self.migration_id = migration_id
        self.migration_path = migration_path
        self.species = species

def cancel_migration(migration_id: int) -> None:
    pass

def get_migration_by_id(migration_id: int) -> Migration:
    pass

def get_migration_details(migration_id: int) -> dict[str, Any]:
    pass

def update_migration_details(migration_id: int, **kwargs: Any) -> None:
    pass