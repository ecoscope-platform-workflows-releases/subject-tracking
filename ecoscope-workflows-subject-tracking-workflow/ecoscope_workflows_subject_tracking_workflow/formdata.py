# [generated]
# by = { compiler = "ecoscope-workflows-core", version = "9999" }
# from-spec-sha256 = "11deae320a23ad025f16b3c8e871dd15f88933bbc3ccbba60a0d326780d50037"


from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, ConfigDict, Field


class WorkflowDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str = Field(..., description="The name of your workflow", title="Name")
    description: str = Field(..., description="A description", title="Description")
    image_url: Optional[str] = Field("", description="An image url", title="Image Url")


class ErClientName(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    EcoscopeWorkflowsNamedConnection: str = Field(
        ..., description="A named connection.", title="Name"
    )


class TimeRange(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    since: datetime = Field(..., description="The start time", title="Since")
    until: datetime = Field(..., description="The end time", title="Until")


class SubjectObs(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    subject_group_name: str = Field(
        ..., description="Name of EarthRanger Subject", title="Subject Group Name"
    )
    include_inactive: Optional[bool] = Field(
        True,
        description="Whether or not to include inactive subjects",
        title="Include Inactive",
    )


class SubjectTraj(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    max_length_meters: Optional[float] = Field(10000, title="Max Length Meters")
    max_time_secs: Optional[float] = Field(3600, title="Max Time Secs")
    max_speed_kmhr: Optional[float] = Field(120, title="Max Speed Kmhr")


class Td(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    pixel_size: Optional[float] = Field(
        250.0, description="Raster pixel size in meters.", title="Pixel Size"
    )


class Grouper(BaseModel):
    index_name: str = Field(..., title="Index Name")


class Directive(str, Enum):
    field_a = "%a"
    field_A = "%A"
    field_b = "%b"
    field_B = "%B"
    field_c = "%c"
    field_d = "%d"
    field_f = "%f"
    field_H = "%H"
    field_I = "%I"
    field_j = "%j"
    field_m = "%m"
    field_M = "%M"
    field_p = "%p"
    field_S = "%S"
    field_U = "%U"
    field_w = "%w"
    field_W = "%W"
    field_x = "%x"
    field_X = "%X"
    field_y = "%y"
    field_Y = "%Y"
    field_z = "%z"
    field__ = "%%"


class TemporalGrouper(BaseModel):
    index_name: str = Field(..., title="Index Name")
    directive: Directive = Field(..., title="Directive")


class TimeRange1(BaseModel):
    since: datetime = Field(..., title="Since")
    until: datetime = Field(..., title="Until")
    time_format: Optional[str] = Field("%d %b %Y %H:%M:%S %Z", title="Time Format")


class Groupers(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    groupers: List[Union[Grouper, TemporalGrouper]] = Field(
        ...,
        description="            Index(es) and/or column(s) to group by, along with\n            optional display names and help text.\n            ",
        title="Groupers",
    )


class FormData(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    workflow_details: Optional[WorkflowDetails] = Field(
        None, title="Set Workflow Details"
    )
    er_client_name: Optional[ErClientName] = Field(
        None, title="Select EarthRanger Connection"
    )
    groupers: Optional[Groupers] = Field(None, title="Set Groupers")
    time_range: Optional[TimeRange] = Field(None, title="Set Time Range Filters")
    subject_obs: Optional[SubjectObs] = Field(
        None, title="Get Subject Group Observations from EarthRanger"
    )
    subject_traj: Optional[SubjectTraj] = Field(
        None, title="Transform Relocations to Trajectories"
    )
    td: Optional[Td] = Field(None, title="Calculate Time Density from Trajectory")
