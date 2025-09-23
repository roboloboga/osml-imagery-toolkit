#  Copyright 2025-2025 General Atomics Integrated Intelligence, Inc.

from typing import Optional

from .coordinates import GeodeticWorldCoordinate
from .elevation_model import ElevationModel, ElevationRegionSummary


class NormalizedElevationModel(ElevationModel):
    """
    An elevation model that auto normalizes input.
    """

    def __init__(
        self,
        inner_elevation_model: ElevationModel,
    ) -> None:
        """
        Create the model using a nested ElevationModel.

        :param inner_elevation_model: the inner model that sets elevation

        :return: None
        """
        self.inner_elevation_model = inner_elevation_model

    def set_elevation(self, world_coordinate: GeodeticWorldCoordinate) -> bool:
        """
        Set elevation using a normalized coordinate for the inner model.

        :param world_coordinate: the coordinate to update

        :return: True if the elevation was updated, else False
        """
        normalized_world_coordinate = world_coordinate.normalized()
        if self.inner_elevation_model.set_elevation(normalized_world_coordinate):
            world_coordinate.elevation = normalized_world_coordinate.elevation
            return True
        return False

    def describe_region(
        self,
        world_coordinate: GeodeticWorldCoordinate,
    ) -> Optional[ElevationRegionSummary]:
        """
        Get a summary of the region near the provided world coordinate

        :param world_coordinate: the coordinate at the center of the region of interest

        :return: the summary information
        """
        return self.inner_elevation_model.describe_region(world_coordinate.normalized())
