# [generated]
# by = { compiler = "ecoscope-workflows-core", version = "9999" }
# from-spec-sha256 = "ce99aa75b964ef05abbda6aaf04196155783e7be46b4194b23de1ec97f12a9ea"


from __future__ import annotations

from enum import Enum
from typing import Any, Dict, List, Optional, Union

from pydantic import AwareDatetime, BaseModel, ConfigDict, Field


class WorkflowDetails(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    name: str = Field(..., description="The name of your workflow", title="Name")
    description: str = Field(..., description="A description", title="Description")
    image_url: Optional[str] = Field("", description="An image url", title="Image Url")


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
    client: str = Field(
        ..., description="A named EarthRanger connection.", title="Client"
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
    min_length_meters: Optional[float] = Field(0.1, title="Min Length Meters")
    max_length_meters: Optional[float] = Field(10000, title="Max Length Meters")
    max_time_secs: Optional[float] = Field(3600, title="Max Time Secs")
    min_time_secs: Optional[float] = Field(1, title="Min Time Secs")
    max_speed_kmhr: Optional[float] = Field(120, title="Max Speed Kmhr")
    min_speed_kmhr: Optional[float] = Field(0.0, title="Min Speed Kmhr")


class ColormapTrajSpeed(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    input_column_name: str = Field(
        ...,
        description="The name of the column with categorical values.",
        title="Input Column Name",
    )
    output_column_name: Optional[str] = Field(
        None,
        description="The dataframe column that will contain the color values.",
        title="Output Column Name",
    )


class TrajMapWidgetsSingleViews(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    title: str = Field(..., description="The title of the widget", title="Title")


class ColormapTrajNight(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    input_column_name: str = Field(
        ...,
        description="The name of the column with categorical values.",
        title="Input Column Name",
    )
    output_column_name: Optional[str] = Field(
        None,
        description="The dataframe column that will contain the color values.",
        title="Output Column Name",
    )


class TrajMapDaynightWidgetsSv(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    title: str = Field(..., description="The title of the widget", title="Title")


class MeanSpeed(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    column_name: str = Field(
        ..., description="Column to aggregate", title="Column Name"
    )


class MeanSpeedSvWidgets(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    title: str = Field(..., description="The title of the widget", title="Title")


class MaxSpeed(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    column_name: str = Field(
        ..., description="Column to aggregate", title="Column Name"
    )


class MaxSpeedSvWidgets(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    title: str = Field(..., description="The title of the widget", title="Title")


class NumLocationSvWidgets(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    title: str = Field(..., description="The title of the widget", title="Title")


class DaynightRatioSvWidgets(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    title: str = Field(..., description="The title of the widget", title="Title")


class TotalDistance(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    column_name: str = Field(
        ..., description="Column to aggregate", title="Column Name"
    )


class TotalDistanceSvWidgets(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    title: str = Field(..., description="The title of the widget", title="Title")


class TotalTime(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    column_name: str = Field(
        ..., description="Column to aggregate", title="Column Name"
    )


class TotalTimeSvWidgets(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    title: str = Field(..., description="The title of the widget", title="Title")


class Td(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    pixel_size: Optional[float] = Field(
        250.0, description="Pixel size for raster profile.", title="Pixel Size"
    )
    crs: Optional[str] = Field("ESRI:102022", title="Crs")
    nodata_value: Optional[Union[float, str]] = Field("nan", title="Nodata Value")
    band_count: Optional[int] = Field(1, title="Band Count")
    max_speed_factor: Optional[float] = Field(1.05, title="Max Speed Factor")
    expansion_factor: Optional[float] = Field(1.3, title="Expansion Factor")
    percentiles: Optional[List[float]] = Field(
        [50.0, 60.0, 70.0, 80.0, 90.0, 95.0], title="Percentiles"
    )


class TdMapWidget(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    title: str = Field(..., description="The title of the widget", title="Title")


class NsdChartWidget(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    title: str = Field(..., description="The title of the widget", title="Title")


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
    since: AwareDatetime = Field(..., title="Since")
    until: AwareDatetime = Field(..., title="Until")
    time_format: Optional[str] = Field("%d %b %Y %H:%M:%S %Z", title="Time Format")


class FisherJenksArgs(BaseModel):
    k: Optional[int] = Field(5, title="K")


class MaxBreaksArgs(BaseModel):
    k: Optional[int] = Field(5, title="K")
    mindiff: Optional[float] = Field(0, title="Mindiff")


class NaturalBreaksArgs(BaseModel):
    k: Optional[int] = Field(5, title="K")
    initial: Optional[int] = Field(10, title="Initial")


class QuantileArgs(BaseModel):
    k: Optional[int] = Field(5, title="K")


class SharedArgs(BaseModel):
    k: Optional[int] = Field(5, title="K")


class StdMeanArgs(BaseModel):
    multiples: Optional[List[int]] = Field([-2, -1, 1, 2], title="Multiples")
    anchor: Optional[bool] = Field(False, title="Anchor")


class Unit(str, Enum):
    m = "m"
    km = "km"
    s = "s"
    h = "h"
    d = "d"
    m_s = "m/s"
    km_h = "km/h"


class LegendDefinition(BaseModel):
    label_column: Optional[str] = Field(None, title="Label Column")
    color_column: Optional[str] = Field(None, title="Color Column")
    labels: Optional[List[str]] = Field(None, title="Labels")
    colors: Optional[List[str]] = Field(None, title="Colors")


class Placement(str, Enum):
    top_left = "top-left"
    top_right = "top-right"
    bottom_left = "bottom-left"
    bottom_right = "bottom-right"
    fill = "fill"


class LegendStyle(BaseModel):
    placement: Optional[Placement] = Field("bottom-right", title="Placement")


class NorthArrowStyle(BaseModel):
    placement: Optional[Placement] = Field("top-left", title="Placement")
    style: Optional[Dict[str, Any]] = Field({"transform": "scale(0.8)"}, title="Style")


class LineWidthUnits(str, Enum):
    meters = "meters"
    pixels = "pixels"


class RadiusUnits(str, Enum):
    meters = "meters"
    pixels = "pixels"


class PointLayerStyle(BaseModel):
    filled: Optional[bool] = Field(True, title="Filled")
    get_fill_color: Optional[str] = Field(None, title="Get Fill Color")
    get_line_color: Optional[str] = Field(None, title="Get Line Color")
    get_line_width: Optional[float] = Field(1, title="Get Line Width")
    fill_color_column: Optional[str] = Field(None, title="Fill Color Column")
    line_width_units: Optional[LineWidthUnits] = Field(
        "pixels", title="Line Width Units"
    )
    get_radius: Optional[float] = Field(5, title="Get Radius")
    radius_units: Optional[RadiusUnits] = Field("pixels", title="Radius Units")


class PolygonLayerStyle(BaseModel):
    filled: Optional[bool] = Field(True, title="Filled")
    get_fill_color: Optional[str] = Field(None, title="Get Fill Color")
    get_line_color: Optional[str] = Field(None, title="Get Line Color")
    get_line_width: Optional[float] = Field(1, title="Get Line Width")
    fill_color_column: Optional[str] = Field(None, title="Fill Color Column")
    line_width_units: Optional[LineWidthUnits] = Field(
        "pixels", title="Line Width Units"
    )
    extruded: Optional[bool] = Field(False, title="Extruded")
    get_elevation: Optional[float] = Field(1000, title="Get Elevation")


class PolylineLayerStyle(BaseModel):
    pass


class TileLayer(BaseModel):
    name: str = Field(..., title="Name")
    opacity: Optional[float] = Field(1, title="Opacity")


class Quantity(BaseModel):
    value: Union[int, float] = Field(..., title="Value")
    unit: Optional[Unit] = None


class LineStyle(BaseModel):
    color: Optional[str] = Field(None, title="Color")


class PlotStyle(BaseModel):
    xperiodalignment: Optional[str] = Field(None, title="Xperiodalignment")
    marker_colors: Optional[List[str]] = Field(None, title="Marker Colors")
    textinfo: Optional[str] = Field(None, title="Textinfo")
    line: Optional[LineStyle] = Field(None, title="Line")


class Groupers(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    groupers: List[Union[Grouper, TemporalGrouper]] = Field(
        ...,
        description="            Index(es) and/or column(s) to group by, along with\n            optional display names and help text.\n            ",
        title="Groupers",
    )


class ClassifyTrajSpeed(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    input_column_name: str = Field(
        ..., description="The dataframe column to classify.", title="Input Column Name"
    )
    output_column_name: Optional[str] = Field(
        None,
        description="The dataframe column that will contain the classification values.",
        title="Output Column Name",
    )
    labels: Optional[List[str]] = Field(
        None,
        description="Labels of classification bins, uses bin edges if not provied.",
        title="Labels",
    )
    classification_options: Optional[
        Union[
            SharedArgs,
            StdMeanArgs,
            MaxBreaksArgs,
            NaturalBreaksArgs,
            QuantileArgs,
            FisherJenksArgs,
        ]
    ] = Field({"k": 5}, title="Classification Options")


class SpeedmapLegendWithUnit(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    input_column_name: str = Field(
        ..., description="The column name to map.", title="Input Column Name"
    )
    output_column_name: str = Field(
        ..., description="The new column name.", title="Output Column Name"
    )
    original_unit: Optional[Unit] = Field(
        None, description="The original unit of measurement.", title="Original Unit"
    )
    new_unit: Optional[Unit] = Field(
        None, description="The unit to convert to.", title="New Unit"
    )
    decimal_places: Optional[int] = Field(
        1,
        description="The number of decimal places to display.",
        title="Decimal Places",
    )


class TrajEcomap(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    tile_layers: Optional[List[TileLayer]] = Field(
        [],
        description="A list of named tile layer with opacity, ie OpenStreetMap.",
        title="Tile Layers",
    )
    static: Optional[bool] = Field(
        False, description="Set to true to disable map pan/zoom.", title="Static"
    )
    north_arrow_style: Optional[NorthArrowStyle] = Field(
        default_factory=lambda: NorthArrowStyle.model_validate(
            {"placement": "top-left", "style": {"transform": "scale(0.8)"}}
        ),
        description="Additional arguments for configuring the North Arrow.",
        title="North Arrow Style",
    )
    legend_style: Optional[LegendStyle] = Field(
        default_factory=lambda: LegendStyle.model_validate(
            {"placement": "bottom-right"}
        ),
        description="Additional arguments for configuring the legend.",
        title="Legend Style",
    )


class TrajDaynightEcomap(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    tile_layers: Optional[List[TileLayer]] = Field(
        [],
        description="A list of named tile layer with opacity, ie OpenStreetMap.",
        title="Tile Layers",
    )
    static: Optional[bool] = Field(
        False, description="Set to true to disable map pan/zoom.", title="Static"
    )
    north_arrow_style: Optional[NorthArrowStyle] = Field(
        default_factory=lambda: NorthArrowStyle.model_validate(
            {"placement": "top-left", "style": {"transform": "scale(0.8)"}}
        ),
        description="Additional arguments for configuring the North Arrow.",
        title="North Arrow Style",
    )
    legend_style: Optional[LegendStyle] = Field(
        default_factory=lambda: LegendStyle.model_validate(
            {"placement": "bottom-right"}
        ),
        description="Additional arguments for configuring the legend.",
        title="Legend Style",
    )


class AverageSpeedConverted(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    original_unit: Optional[Unit] = Field(
        None, description="The original unit of measurement.", title="Original Unit"
    )
    new_unit: Optional[Unit] = Field(
        None, description="The unit to convert to.", title="New Unit"
    )


class MaxSpeedConverted(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    original_unit: Optional[Unit] = Field(
        None, description="The original unit of measurement.", title="Original Unit"
    )
    new_unit: Optional[Unit] = Field(
        None, description="The unit to convert to.", title="New Unit"
    )


class TotalDistConverted(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    original_unit: Optional[Unit] = Field(
        None, description="The original unit of measurement.", title="Original Unit"
    )
    new_unit: Optional[Unit] = Field(
        None, description="The unit to convert to.", title="New Unit"
    )


class TotalTimeConverted(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    original_unit: Optional[Unit] = Field(
        None, description="The original unit of measurement.", title="Original Unit"
    )
    new_unit: Optional[Unit] = Field(
        None, description="The unit to convert to.", title="New Unit"
    )


class TdEcomap(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    tile_layers: Optional[List[TileLayer]] = Field(
        [],
        description="A list of named tile layer with opacity, ie OpenStreetMap.",
        title="Tile Layers",
    )
    static: Optional[bool] = Field(
        False, description="Set to true to disable map pan/zoom.", title="Static"
    )
    north_arrow_style: Optional[NorthArrowStyle] = Field(
        default_factory=lambda: NorthArrowStyle.model_validate(
            {"placement": "top-left", "style": {"transform": "scale(0.8)"}}
        ),
        description="Additional arguments for configuring the North Arrow.",
        title="North Arrow Style",
    )
    legend_style: Optional[LegendStyle] = Field(
        default_factory=lambda: LegendStyle.model_validate(
            {"placement": "bottom-right"}
        ),
        description="Additional arguments for configuring the legend.",
        title="Legend Style",
    )


class NsdChart(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    group_by: str = Field(
        ..., description="The dataframe column to group by.", title="Group By"
    )
    x_axis: str = Field(
        ..., description="The dataframe column to plot in the x axis.", title="X Axis"
    )
    y_axis: str = Field(
        ..., description="The dataframe column to plot in the y axis.", title="Y Axis"
    )
    plot_style: Optional[PlotStyle] = Field(
        None,
        description="Style arguments passed to plotly.graph_objects.Scatter.",
        title="Plot Style",
    )


class Params(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
    )
    workflow_details: Optional[WorkflowDetails] = Field(
        None, title="Set Workflow Details"
    )
    groupers: Optional[Groupers] = Field(None, title="Set Groupers")
    time_range: Optional[TimeRange] = Field(None, title="Set Time Range Filters")
    subject_obs: Optional[SubjectObs] = Field(
        None, title="Get Subject Group Observations from EarthRanger"
    )
    subject_traj: Optional[SubjectTraj] = Field(
        None, title="Transform Relocations to Trajectories"
    )
    classify_traj_speed: Optional[ClassifyTrajSpeed] = Field(
        None, title="Classify Trajectories By Speed"
    )
    colormap_traj_speed: Optional[ColormapTrajSpeed] = Field(
        None, title="Apply Color to Trajectories By Speed"
    )
    speedmap_legend_with_unit: Optional[SpeedmapLegendWithUnit] = Field(
        None, title="Format Speedmap Legend Label"
    )
    traj_ecomap: Optional[TrajEcomap] = Field(
        None, title="Draw Ecomaps for each trajectory group"
    )
    traj_map_widgets_single_views: Optional[TrajMapWidgetsSingleViews] = Field(
        None, title="Create Map Widgets for Trajectories"
    )
    colormap_traj_night: Optional[ColormapTrajNight] = Field(
        None, title="Apply Color to Trajectories By Day/Night"
    )
    traj_daynight_ecomap: Optional[TrajDaynightEcomap] = Field(
        None, title="Draw Ecomaps for each trajectory group"
    )
    traj_map_daynight_widgets_sv: Optional[TrajMapDaynightWidgetsSv] = Field(
        None, title="Create Map Widgets for Trajectories"
    )
    mean_speed: Optional[MeanSpeed] = Field(
        None, title="Calculate Mean Speed Per Group"
    )
    average_speed_converted: Optional[AverageSpeedConverted] = Field(
        None, title="Convert Average Speed units"
    )
    mean_speed_sv_widgets: Optional[MeanSpeedSvWidgets] = Field(
        None, title="Create Single Value Widgets for Mean Speed Per Group"
    )
    max_speed: Optional[MaxSpeed] = Field(None, title="Calculate Max Speed Per Group")
    max_speed_converted: Optional[MaxSpeedConverted] = Field(
        None, title="Convert Max Speed units"
    )
    max_speed_sv_widgets: Optional[MaxSpeedSvWidgets] = Field(
        None, title="Create Single Value Widgets for Max Speed Per Group"
    )
    num_location_sv_widgets: Optional[NumLocationSvWidgets] = Field(
        None, title="Create Single Value Widgets for Number of Location Per Group"
    )
    daynight_ratio_sv_widgets: Optional[DaynightRatioSvWidgets] = Field(
        None, title="Create Single Value Widgets for Day/Night Ratio Per Group"
    )
    total_distance: Optional[TotalDistance] = Field(
        None, title="Calculate Total Distance Per Group"
    )
    total_dist_converted: Optional[TotalDistConverted] = Field(
        None, title="Convert total distance units"
    )
    total_distance_sv_widgets: Optional[TotalDistanceSvWidgets] = Field(
        None, title="Create Single Value Widgets for Total Distance Per Group"
    )
    total_time: Optional[TotalTime] = Field(
        None, title="Calculate Total Time Per Group"
    )
    total_time_converted: Optional[TotalTimeConverted] = Field(
        None, title="Convert total time units"
    )
    total_time_sv_widgets: Optional[TotalTimeSvWidgets] = Field(
        None, title="Create Single Value Widgets for Total Distance Per Group"
    )
    td: Optional[Td] = Field(None, title="Calculate Time Density from Trajectory")
    td_ecomap: Optional[TdEcomap] = Field(None, title="Draw Ecomap from Time Density")
    td_map_widget: Optional[TdMapWidget] = Field(
        None, title="Create Time Density Map Widget"
    )
    nsd_chart: Optional[NsdChart] = Field(None, title="Draw NSD Scatter Chart")
    nsd_chart_widget: Optional[NsdChartWidget] = Field(
        None, title="Create NSD Plot Widget"
    )


class LayerDefinition(BaseModel):
    geodataframe: Any = Field(..., title="Geodataframe")
    layer_style: Union[PolylineLayerStyle, PointLayerStyle, PolygonLayerStyle] = Field(
        ..., title="Layer Style"
    )
    legend: LegendDefinition
