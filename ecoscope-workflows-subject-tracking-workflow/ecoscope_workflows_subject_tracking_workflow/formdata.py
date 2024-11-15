# [generated]
# by = { compiler = "ecoscope-workflows-core", version = "9999" }
# from-spec-sha256 = "735a0a8a6fd62c9a0010573c318cd3e8552ac07a7e6839c5ca0d332d8d9279c1"


from __future__ import annotations

from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, ConfigDict, Field


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
    since: AwareDatetime = Field(..., description="The start time", title="Since")
    until: AwareDatetime = Field(..., description="The end time", title="Until")


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


class NaPosition(str, Enum):
    first = "first"
    last = "last"


class SortTrajSpeed(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    ascending: Optional[bool] = Field(
        True, description="Sort ascending if true", title="Ascending"
    )
    na_position: Optional[NaPosition] = Field(
        "last", description="Where to place NaN values in the sort", title="Na Position"
    )


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


class TimeRangeModel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    since: AwareDatetime = Field(..., title="Since")
    until: AwareDatetime = Field(..., title="Until")
    time_format: Optional[str] = Field("%d %b %Y %H:%M:%S %Z", title="Time Format")


class WidgetType(str, Enum):
    graph = "graph"
    map = "map"
    text = "text"
    stat = "stat"


class GroupedWidget(BaseModel):
    widget_type: WidgetType = Field(..., title="Widget Type")
    title: str = Field(..., title="Title")
    is_filtered: bool = Field(..., title="Is Filtered")
    views: Dict[str, Union[Path, AnyUrl, str]] = Field(..., title="Views")


class WidgetSingleView(BaseModel):
    widget_type: WidgetType = Field(..., title="Widget Type")
    title: str = Field(..., title="Title")
    is_filtered: bool = Field(..., title="Is Filtered")
    data: Union[Path, AnyUrl, str] = Field(..., title="Data")
    view: Optional[List[List]] = Field(None, title="View")


class WorkflowDetails1(BaseModel):
    name: str = Field(..., title="Name")
    description: str = Field(..., title="Description")
    image_url: Optional[str] = Field("", title="Image Url")


class Groupers(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    groupers: List[Union[Grouper, TemporalGrouper]] = Field(
        ...,
        description="            Index(es) and/or column(s) to group by, along with\n            optional display names and help text.\n            ",
        title="Groupers",
    )


class SubjectTrackingDashboard(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    time_range: TimeRangeModel = Field(
        ..., description="Time range filter", title="Time Range"
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
    sort_traj_speed: Optional[SortTrajSpeed] = Field(
        None, title="Sort Trajetories By Classification"
    )
    td: Optional[Td] = Field(None, title="Calculate Time Density from Trajectory")
    subject_tracking_dashboard: Optional[SubjectTrackingDashboard] = Field(
        None, title="Create Dashboard with Subject Tracking Widgets"
    )
