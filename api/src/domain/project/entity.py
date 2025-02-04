from dataclasses import dataclass
from datetime import datetime
from src.domain.validators.validators import DataVerifier
from django.core.files import File
from typing import Optional

@dataclass
class ProjectEntity:
    name: str
    logo: Optional[File]
    description: str
    status: str
    participants: list
    date_created: datetime
    responsible_id: int

    def verify_data(self):
        return DataVerifier.verify_max_value(self.name, 100)


@dataclass
class FeaturesEntity:
    name: str
    description: str
    importance: int
    tags: list
    participants: list
    responsible_id: int
    project_id: int
    status: str

    def verify_data(self):
        return DataVerifier.verify_max_value(self.name, 100)