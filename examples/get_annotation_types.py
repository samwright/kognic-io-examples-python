from typing import List, Optional

import kognic.io.client as IOC
from kognic.io import model as IAM
from kognic.io.model.projects import project_batch


def run(client: IOC.KognicIOClient, project: str, batch: Optional[str] = None) -> List[str]:
    print("Listing projects annotation types...")

    return client.project.get_annotation_types(project=project, batch=batch)


if __name__ == "__main__":
    client = IOC.KognicIOClient()

    project = "Project-Identifier"
    annotation_types = run(client, project)
