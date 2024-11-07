# [generated]
# by = { compiler = "ecoscope-workflows-core", version = "9999" }
# from-spec-sha256 = "8e83a86b58a42b4e1651223cad2ef9e207d4b50645526dab5e441b82e6b02eee"


# ruff: noqa: E402

# %% [markdown]
# # Subject Tracking
# TODO: top level description

# %% [markdown]
# ## Imports

import os
from ecoscope_workflows_core.tasks.config import set_workflow_details
from ecoscope_workflows_core.tasks.io import set_connection
from ecoscope_workflows_core.tasks.groupby import set_groupers
from ecoscope_workflows_core.tasks.filter import set_time_range
from ecoscope_workflows_ext_ecoscope.tasks.io import get_subjectgroup_observations
from ecoscope_workflows_ext_ecoscope.tasks.preprocessing import process_relocations
from ecoscope_workflows_ext_ecoscope.tasks.transformation import classify_is_night
from ecoscope_workflows_ext_ecoscope.tasks.preprocessing import (
    relocations_to_trajectory,
)
from ecoscope_workflows_core.tasks.transformation import add_temporal_index
from ecoscope_workflows_core.tasks.groupby import split_groups
from ecoscope_workflows_ext_ecoscope.tasks.transformation import apply_classification
from ecoscope_workflows_ext_ecoscope.tasks.transformation import apply_color_map
from ecoscope_workflows_core.tasks.transformation import map_values_with_unit
from ecoscope_workflows_ext_ecoscope.tasks.results import create_polyline_layer
from ecoscope_workflows_ext_ecoscope.tasks.results import draw_ecomap
from ecoscope_workflows_core.tasks.io import persist_text
from ecoscope_workflows_core.tasks.results import create_map_widget_single_view
from ecoscope_workflows_core.tasks.results import merge_widget_views
from ecoscope_workflows_core.tasks.analysis import dataframe_column_mean
from ecoscope_workflows_core.tasks.transformation import with_unit
from ecoscope_workflows_core.tasks.results import create_single_value_widget_single_view
from ecoscope_workflows_core.tasks.analysis import dataframe_column_max
from ecoscope_workflows_core.tasks.analysis import dataframe_count
from ecoscope_workflows_ext_ecoscope.tasks.analysis import get_day_night_ratio
from ecoscope_workflows_core.tasks.analysis import dataframe_column_sum

# %% [markdown]
# ## Set Workflow Details

# %%
# parameters

workflow_details_params = dict(
    name=...,
    description=...,
    image_url=...,
)

# %%
# call the task


workflow_details = set_workflow_details.partial(**workflow_details_params).call()


# %% [markdown]
# ## Select EarthRanger Connection

# %%
# parameters

er_client_name_params = dict(
    name=...,
)

# %%
# call the task


er_client_name = set_connection.partial(**er_client_name_params).call()


# %% [markdown]
# ## Set Groupers

# %%
# parameters

groupers_params = dict(
    groupers=...,
)

# %%
# call the task


groupers = set_groupers.partial(**groupers_params).call()


# %% [markdown]
# ## Set Time Range Filters

# %%
# parameters

time_range_params = dict(
    since=...,
    until=...,
    time_format=...,
)

# %%
# call the task


time_range = set_time_range.partial(**time_range_params).call()


# %% [markdown]
# ## Get Subject Group Observations from EarthRanger

# %%
# parameters

subject_obs_params = dict(
    subject_group_name=...,
    include_inactive=...,
)

# %%
# call the task


subject_obs = get_subjectgroup_observations.partial(
    client=er_client_name, time_range=time_range, **subject_obs_params
).call()


# %% [markdown]
# ## Transform Observations to Relocations

# %%
# parameters

subject_reloc_params = dict()

# %%
# call the task


subject_reloc = process_relocations.partial(
    observations=subject_obs,
    relocs_columns=["groupby_col", "fixtime", "junk_status", "geometry"],
    filter_point_coords=[
        {"x": 180.0, "y": 90.0},
        {"x": 0.0, "y": 0.0},
        {"x": 1.0, "y": 1.0},
    ],
    **subject_reloc_params,
).call()


# %% [markdown]
# ## Apply Day/Night Labels to Relocations

# %%
# parameters

day_night_labels_params = dict()

# %%
# call the task


day_night_labels = classify_is_night.partial(
    relocations=subject_reloc, **day_night_labels_params
).call()


# %% [markdown]
# ## Transform Relocations to Trajectories

# %%
# parameters

subject_traj_params = dict(
    min_length_meters=...,
    max_length_meters=...,
    max_time_secs=...,
    min_time_secs=...,
    max_speed_kmhr=...,
    min_speed_kmhr=...,
)

# %%
# call the task


subject_traj = relocations_to_trajectory.partial(
    relocations=day_night_labels, **subject_traj_params
).call()


# %% [markdown]
# ## Add temporal index to Subject Trajectories

# %%
# parameters

traj_add_temporal_index_params = dict(
    cast_to_datetime=...,
    format=...,
)

# %%
# call the task


traj_add_temporal_index = add_temporal_index.partial(
    df=subject_traj,
    time_col="segment_start",
    groupers=groupers,
    **traj_add_temporal_index_params,
).call()


# %% [markdown]
# ## Split Subject Trajectories by Group

# %%
# parameters

split_subject_traj_groups_params = dict()

# %%
# call the task


split_subject_traj_groups = split_groups.partial(
    df=traj_add_temporal_index, groupers=groupers, **split_subject_traj_groups_params
).call()


# %% [markdown]
# ## Classify Trajectories By Speed

# %%
# parameters

classify_traj_speed_params = dict(
    labels=...,
)

# %%
# call the task


classify_traj_speed = apply_classification.partial(
    input_column_name="speed_kmhr",
    output_column_name="speed_bins",
    classification_options={"scheme": "equal_interval", "k": 6},
    **classify_traj_speed_params,
).mapvalues(argnames=["df"], argvalues=split_subject_traj_groups)


# %% [markdown]
# ## Apply Color to Trajectories By Speed

# %%
# parameters

colormap_traj_speed_params = dict()

# %%
# call the task


colormap_traj_speed = apply_color_map.partial(
    input_column_name="speed_bins",
    output_column_name="speed_bins_colormap",
    colormap=["#1a9850", "#91cf60", "#d9ef8b", "#fee08b", "#fc8d59", "#d73027"],
    **colormap_traj_speed_params,
).mapvalues(argnames=["df"], argvalues=classify_traj_speed)


# %% [markdown]
# ## Format Speedmap Legend Label

# %%
# parameters

speedmap_legend_with_unit_params = dict(
    decimal_places=...,
)

# %%
# call the task


speedmap_legend_with_unit = map_values_with_unit.partial(
    input_column_name="speed_bins",
    output_column_name="speed_bins_formatted",
    original_unit="km/h",
    new_unit="km/h",
    **speedmap_legend_with_unit_params,
).mapvalues(argnames=["df"], argvalues=colormap_traj_speed)


# %% [markdown]
# ## Create map layer for each trajectory group

# %%
# parameters

traj_map_layers_params = dict()

# %%
# call the task


traj_map_layers = create_polyline_layer.partial(
    layer_style={"color_column": "speed_bins_colormap"},
    legend={
        "label_column": "speed_bins_formatted",
        "color_column": "speed_bins_colormap",
    },
    **traj_map_layers_params,
).mapvalues(argnames=["geodataframe"], argvalues=speedmap_legend_with_unit)


# %% [markdown]
# ## Draw Ecomaps for each trajectory group

# %%
# parameters

traj_ecomap_params = dict(
    title=...,
)

# %%
# call the task


traj_ecomap = draw_ecomap.partial(
    tile_layers=[{"name": "TERRAIN"}, {"name": "SATELLITE", "opacity": 0.5}],
    north_arrow_style={"placement": "top-left"},
    legend_style={"placement": "bottom-right"},
    static=False,
    **traj_ecomap_params,
).mapvalues(argnames=["geo_layers"], argvalues=traj_map_layers)


# %% [markdown]
# ## Persist ecomap as Text

# %%
# parameters

ecomap_html_urls_params = dict(
    filename=...,
)

# %%
# call the task


ecomap_html_urls = persist_text.partial(
    root_path=os.environ["ECOSCOPE_WORKFLOWS_RESULTS"], **ecomap_html_urls_params
).mapvalues(argnames=["text"], argvalues=traj_ecomap)


# %% [markdown]
# ## Create Map Widgets for Trajectories

# %%
# parameters

traj_map_widgets_single_views_params = dict()

# %%
# call the task


traj_map_widgets_single_views = create_map_widget_single_view.partial(
    title="Subject Group Trajectory Map", **traj_map_widgets_single_views_params
).map(argnames=["view", "data"], argvalues=ecomap_html_urls)


# %% [markdown]
# ## Merge EcoMap Widget Views

# %%
# parameters

traj_grouped_map_widget_params = dict()

# %%
# call the task


traj_grouped_map_widget = merge_widget_views.partial(
    widgets=traj_map_widgets_single_views, **traj_grouped_map_widget_params
).call()


# %% [markdown]
# ## Apply Color to Trajectories By Day/Night

# %%
# parameters

colormap_traj_night_params = dict()

# %%
# call the task


colormap_traj_night = apply_color_map.partial(
    colormap=["#292965", "#e7a553"],
    input_column_name="extra__is_night",
    output_column_name="is_night_colors",
    **colormap_traj_night_params,
).mapvalues(argnames=["df"], argvalues=split_subject_traj_groups)


# %% [markdown]
# ## Create map layer for each trajectory group

# %%
# parameters

traj_map_night_layers_params = dict()

# %%
# call the task


traj_map_night_layers = create_polyline_layer.partial(
    layer_style={"color_column": "is_night_colors"},
    legend={"labels": ["Night", "Day"], "colors": ["#292965", "#e7a553"]},
    **traj_map_night_layers_params,
).mapvalues(argnames=["geodataframe"], argvalues=colormap_traj_night)


# %% [markdown]
# ## Draw Ecomaps for each trajectory group

# %%
# parameters

traj_daynight_ecomap_params = dict(
    title=...,
)

# %%
# call the task


traj_daynight_ecomap = draw_ecomap.partial(
    tile_layers=[{"name": "TERRAIN"}, {"name": "SATELLITE", "opacity": 0.5}],
    north_arrow_style={"placement": "top-left"},
    legend_style={"placement": "bottom-right"},
    static=False,
    **traj_daynight_ecomap_params,
).mapvalues(argnames=["geo_layers"], argvalues=traj_map_night_layers)


# %% [markdown]
# ## Persist ecomap as Text

# %%
# parameters

ecomap_daynight_html_urls_params = dict(
    filename=...,
)

# %%
# call the task


ecomap_daynight_html_urls = persist_text.partial(
    root_path=os.environ["ECOSCOPE_WORKFLOWS_RESULTS"],
    **ecomap_daynight_html_urls_params,
).mapvalues(argnames=["text"], argvalues=traj_daynight_ecomap)


# %% [markdown]
# ## Create Map Widgets for Trajectories

# %%
# parameters

traj_map_daynight_widgets_sv_params = dict()

# %%
# call the task


traj_map_daynight_widgets_sv = create_map_widget_single_view.partial(
    title="Subject Group Night/Day Map", **traj_map_daynight_widgets_sv_params
).map(argnames=["view", "data"], argvalues=ecomap_daynight_html_urls)


# %% [markdown]
# ## Merge EcoMap Widget Views

# %%
# parameters

traj_daynight_grouped_map_widget_params = dict()

# %%
# call the task


traj_daynight_grouped_map_widget = merge_widget_views.partial(
    widgets=traj_map_daynight_widgets_sv, **traj_daynight_grouped_map_widget_params
).call()


# %% [markdown]
# ## Calculate Mean Speed Per Group

# %%
# parameters

mean_speed_params = dict()

# %%
# call the task


mean_speed = dataframe_column_mean.partial(
    column_name="speed_kmhr", **mean_speed_params
).mapvalues(argnames=["df"], argvalues=split_subject_traj_groups)


# %% [markdown]
# ## Convert Average Speed units

# %%
# parameters

average_speed_converted_params = dict()

# %%
# call the task


average_speed_converted = with_unit.partial(
    original_unit="km/h", new_unit="km/h", **average_speed_converted_params
).mapvalues(argnames=["value"], argvalues=mean_speed)


# %% [markdown]
# ## Create Single Value Widgets for Mean Speed Per Group

# %%
# parameters

mean_speed_sv_widgets_params = dict(
    decimal_places=...,
)

# %%
# call the task


mean_speed_sv_widgets = create_single_value_widget_single_view.partial(
    title="Mean Speed", **mean_speed_sv_widgets_params
).map(argnames=["view", "data"], argvalues=average_speed_converted)


# %% [markdown]
# ## Merge per group Mean Speed SV widgets

# %%
# parameters

mean_speed_grouped_sv_widget_params = dict()

# %%
# call the task


mean_speed_grouped_sv_widget = merge_widget_views.partial(
    widgets=mean_speed_sv_widgets, **mean_speed_grouped_sv_widget_params
).call()


# %% [markdown]
# ## Calculate Max Speed Per Group

# %%
# parameters

max_speed_params = dict()

# %%
# call the task


max_speed = dataframe_column_max.partial(
    column_name="speed_kmhr", **max_speed_params
).mapvalues(argnames=["df"], argvalues=split_subject_traj_groups)


# %% [markdown]
# ## Convert Max Speed units

# %%
# parameters

max_speed_converted_params = dict()

# %%
# call the task


max_speed_converted = with_unit.partial(
    original_unit="km/h", new_unit="km/h", **max_speed_converted_params
).mapvalues(argnames=["value"], argvalues=max_speed)


# %% [markdown]
# ## Create Single Value Widgets for Max Speed Per Group

# %%
# parameters

max_speed_sv_widgets_params = dict(
    decimal_places=...,
)

# %%
# call the task


max_speed_sv_widgets = create_single_value_widget_single_view.partial(
    title="Max Speed", **max_speed_sv_widgets_params
).map(argnames=["view", "data"], argvalues=max_speed_converted)


# %% [markdown]
# ## Merge per group Max Speed SV widgets

# %%
# parameters

max_speed_grouped_sv_widget_params = dict()

# %%
# call the task


max_speed_grouped_sv_widget = merge_widget_views.partial(
    widgets=max_speed_sv_widgets, **max_speed_grouped_sv_widget_params
).call()


# %% [markdown]
# ## Calculate Number of Locations Per Group

# %%
# parameters

num_location_params = dict()

# %%
# call the task


num_location = dataframe_count.partial(**num_location_params).mapvalues(
    argnames=["df"], argvalues=split_subject_traj_groups
)


# %% [markdown]
# ## Create Single Value Widgets for Number of Location Per Group

# %%
# parameters

num_location_sv_widgets_params = dict(
    decimal_places=...,
)

# %%
# call the task


num_location_sv_widgets = create_single_value_widget_single_view.partial(
    title="Number of Locations", **num_location_sv_widgets_params
).map(argnames=["view", "data"], argvalues=num_location)


# %% [markdown]
# ## Merge per group Number of Locations SV widgets

# %%
# parameters

num_location_grouped_sv_widget_params = dict()

# %%
# call the task


num_location_grouped_sv_widget = merge_widget_views.partial(
    widgets=num_location_sv_widgets, **num_location_grouped_sv_widget_params
).call()


# %% [markdown]
# ## Calculate Day/Night Ratio Per Group

# %%
# parameters

daynight_ratio_params = dict()

# %%
# call the task


daynight_ratio = get_day_night_ratio.partial(**daynight_ratio_params).mapvalues(
    argnames=["df"], argvalues=split_subject_traj_groups
)


# %% [markdown]
# ## Create Single Value Widgets for Day/Night Ratio Per Group

# %%
# parameters

daynight_ratio_sv_widgets_params = dict(
    decimal_places=...,
)

# %%
# call the task


daynight_ratio_sv_widgets = create_single_value_widget_single_view.partial(
    title="Night/Day Ratio", **daynight_ratio_sv_widgets_params
).map(argnames=["view", "data"], argvalues=daynight_ratio)


# %% [markdown]
# ## Merge per group Day/Night Ratio SV widgets

# %%
# parameters

daynight_ratio_grouped_sv_widget_params = dict()

# %%
# call the task


daynight_ratio_grouped_sv_widget = merge_widget_views.partial(
    widgets=daynight_ratio_sv_widgets, **daynight_ratio_grouped_sv_widget_params
).call()


# %% [markdown]
# ## Calculate Total Distance Per Group

# %%
# parameters

total_distance_params = dict()

# %%
# call the task


total_distance = dataframe_column_sum.partial(
    column_name="dist_meters", **total_distance_params
).mapvalues(argnames=["df"], argvalues=split_subject_traj_groups)


# %% [markdown]
# ## Convert total distance units

# %%
# parameters

total_dist_converted_params = dict()

# %%
# call the task


total_dist_converted = with_unit.partial(
    original_unit="m", new_unit="km", **total_dist_converted_params
).mapvalues(argnames=["value"], argvalues=total_distance)


# %% [markdown]
# ## Create Single Value Widgets for Total Distance Per Group

# %%
# parameters

total_distance_sv_widgets_params = dict(
    decimal_places=...,
)

# %%
# call the task


total_distance_sv_widgets = create_single_value_widget_single_view.partial(
    title="Total Distance", **total_distance_sv_widgets_params
).map(argnames=["view", "data"], argvalues=total_dist_converted)
