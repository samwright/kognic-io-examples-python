from __future__ import absolute_import

from pathlib import Path
from typing import List, Optional
from uuid import uuid4

import kognic.io.model.scene.cameras as CM
from kognic.io.client import KognicIOClient
from kognic.io.logger import setup_logging
from kognic.io.model import CreateSceneResponse, Image
from kognic.io.model.scene.metadata.metadata import MetaData

base_dir = Path(__file__).parent.absolute()


def run(
    client: KognicIOClient,
    project: Optional[str],
    annotation_types: Optional[List[str]] = None,
    dryrun: bool = True,
) -> Optional[CreateSceneResponse]:
    print("Creating Cameras Scene...")

    metadata = MetaData(
        **{
            "location-lat": 27.986065,
            "location-long": 86.922623,
            "vehicle_id": "abg",
        }
    )

    cameras = CM.Cameras(
        external_id=f"cameras-example-{uuid4()}",
        frame=CM.Frame(
            images=[
                Image(
                    filename=str(base_dir) + "/resources/img_RFC01.jpg",
                    sensor_name="RFC01",
                ),
                Image(
                    filename=str(base_dir) + "/resources/img_RFC02.jpg",
                    sensor_name="RFC02",
                ),
            ]
        ),
        metadata=metadata,
    )

    # Create scene
    return client.cameras.create(cameras, project=project, annotation_types=annotation_types, dryrun=dryrun)


if __name__ == "__main__":
    setup_logging(level="INFO")
    client = KognicIOClient()

    # Project - Available via `client.project.get_projects()`
    project = "Project-identifier"

    run(client, project)
