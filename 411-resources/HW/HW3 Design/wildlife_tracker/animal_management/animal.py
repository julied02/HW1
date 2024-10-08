from typing import Any, List, Optional

class Animal:
    def __init__(self,
                animal_id: int,
                animals: List[int] = [],
                age: Optional[int] = None,
                health_status: Optional[str] = None) -> None:
        self.age = age
        self.animal_id = animal_id
        self.animals = animals or []
        self.health_status = health_status

def get_animal_by_id(animal_id: int) -> Optional[Animal]:
    pass

def get_animal_details(animal_id) -> dict[str, Any]:
    pass

def update_animal_details(animal_id: int, **kwargs: Any) -> None:
    pass

def assign_animals_to_habitat(habitat_id: int, animals: List[Animal]) -> None:
    pass
