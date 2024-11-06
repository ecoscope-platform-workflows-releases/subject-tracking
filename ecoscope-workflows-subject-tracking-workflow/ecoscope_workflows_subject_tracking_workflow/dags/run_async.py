# [generated]
# by = { compiler = "ecoscope-workflows-core", version = "9999" }
# from-spec-sha256 = "ce99aa75b964ef05abbda6aaf04196155783e7be46b4194b23de1ec97f12a9ea"
import json
import os

from ecoscope_workflows_core.graph import DependsOn, DependsOnSequence, Graph, Node

from ecoscope_workflows_core.tasks.config import set_workflow_details
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
from ecoscope_workflows_ext_ecoscope.tasks.analysis import calculate_time_density
from ecoscope_workflows_ext_ecoscope.tasks.results import create_polygon_layer
from ecoscope_workflows_ext_ecoscope.tasks.results import draw_ecoplot
from ecoscope_workflows_core.tasks.results import create_plot_widget_single_view
from ecoscope_workflows_core.tasks.results import gather_dashboard

from ..params import Params


def main(params: Params):
    params_dict = json.loads(params.model_dump_json(exclude_unset=True))

    dependencies = {
        "workflow_details": [],
        "groupers": [],
        "time_range": [],
        "subject_obs": ["time_range"],
        "subject_reloc": ["subject_obs"],
        "day_night_labels": ["subject_reloc"],
        "subject_traj": ["day_night_labels"],
        "traj_add_temporal_index": ["subject_traj", "groupers"],
        "split_subject_traj_groups": ["traj_add_temporal_index", "groupers"],
        "classify_traj_speed": ["split_subject_traj_groups"],
        "colormap_traj_speed": ["classify_traj_speed"],
        "speedmap_legend_with_unit": ["colormap_traj_speed"],
        "traj_map_layers": ["speedmap_legend_with_unit"],
        "traj_ecomap": ["traj_map_layers"],
        "ecomap_html_urls": ["traj_ecomap"],
        "traj_map_widgets_single_views": ["ecomap_html_urls"],
        "traj_grouped_map_widget": ["traj_map_widgets_single_views"],
        "colormap_traj_night": ["split_subject_traj_groups"],
        "traj_map_night_layers": ["colormap_traj_night"],
        "traj_daynight_ecomap": ["traj_map_night_layers"],
        "ecomap_daynight_html_urls": ["traj_daynight_ecomap"],
        "traj_map_daynight_widgets_sv": ["ecomap_daynight_html_urls"],
        "traj_daynight_grouped_map_widget": ["traj_map_daynight_widgets_sv"],
        "mean_speed": ["split_subject_traj_groups"],
        "average_speed_converted": ["mean_speed"],
        "mean_speed_sv_widgets": ["average_speed_converted"],
        "mean_speed_grouped_sv_widget": ["mean_speed_sv_widgets"],
        "max_speed": ["split_subject_traj_groups"],
        "max_speed_converted": ["max_speed"],
        "max_speed_sv_widgets": ["max_speed_converted"],
        "max_speed_grouped_sv_widget": ["max_speed_sv_widgets"],
        "num_location": ["split_subject_traj_groups"],
        "num_location_sv_widgets": ["num_location"],
        "num_location_grouped_sv_widget": ["num_location_sv_widgets"],
        "daynight_ratio": ["split_subject_traj_groups"],
        "daynight_ratio_sv_widgets": ["daynight_ratio"],
        "daynight_ratio_grouped_sv_widget": ["daynight_ratio_sv_widgets"],
        "total_distance": ["split_subject_traj_groups"],
        "total_dist_converted": ["total_distance"],
        "total_distance_sv_widgets": ["total_dist_converted"],
        "total_dist_grouped_sv_widget": ["total_distance_sv_widgets"],
        "total_time": ["split_subject_traj_groups"],
        "total_time_converted": ["total_time"],
        "total_time_sv_widgets": ["total_time_converted"],
        "total_time_grouped_sv_widget": ["total_time_sv_widgets"],
        "td": ["split_subject_traj_groups"],
        "td_colormap": ["td"],
        "td_map_layer": ["td_colormap"],
        "td_ecomap": ["td_map_layer"],
        "td_ecomap_html_url": ["td_ecomap"],
        "td_map_widget": ["td_ecomap_html_url"],
        "td_grouped_map_widget": ["td_map_widget"],
        "nsd_chart": ["traj_add_temporal_index"],
        "nsd_chart_html_url": ["nsd_chart"],
        "nsd_chart_widget": ["nsd_chart_html_url"],
        "subject_tracking_dashboard": [
            "workflow_details",
            "traj_grouped_map_widget",
            "mean_speed_grouped_sv_widget",
            "max_speed_grouped_sv_widget",
            "num_location_grouped_sv_widget",
            "daynight_ratio_grouped_sv_widget",
            "total_dist_grouped_sv_widget",
            "total_time_grouped_sv_widget",
            "td_grouped_map_widget",
            "traj_daynight_grouped_map_widget",
            "nsd_chart_widget",
            "groupers",
            "time_range",
        ],
    }

    nodes = {
        "workflow_details": Node(
            async_task=set_workflow_details.validate().set_executor("lithops"),
            partial=(params_dict.get("workflow_details") or {}),
            method="call",
        ),
        "groupers": Node(
            async_task=set_groupers.validate().set_executor("lithops"),
            partial=(params_dict.get("groupers") or {}),
            method="call",
        ),
        "time_range": Node(
            async_task=set_time_range.validate().set_executor("lithops"),
            partial=(params_dict.get("time_range") or {}),
            method="call",
        ),
        "subject_obs": Node(
            async_task=get_subjectgroup_observations.validate().set_executor("lithops"),
            partial={
                "time_range": DependsOn("time_range"),
            }
            | (params_dict.get("subject_obs") or {}),
            method="call",
        ),
        "subject_reloc": Node(
            async_task=process_relocations.validate().set_executor("lithops"),
            partial={
                "observations": DependsOn("subject_obs"),
                "relocs_columns": ["groupby_col", "fixtime", "junk_status", "geometry"],
                "filter_point_coords": [
                    {"x": 180.0, "y": 90.0},
                    {"x": 0.0, "y": 0.0},
                    {"x": 1.0, "y": 1.0},
                ],
            }
            | (params_dict.get("subject_reloc") or {}),
            method="call",
        ),
        "day_night_labels": Node(
            async_task=classify_is_night.validate().set_executor("lithops"),
            partial={
                "relocations": DependsOn("subject_reloc"),
            }
            | (params_dict.get("day_night_labels") or {}),
            method="call",
        ),
        "subject_traj": Node(
            async_task=relocations_to_trajectory.validate().set_executor("lithops"),
            partial={
                "relocations": DependsOn("day_night_labels"),
            }
            | (params_dict.get("subject_traj") or {}),
            method="call",
        ),
        "traj_add_temporal_index": Node(
            async_task=add_temporal_index.validate().set_executor("lithops"),
            partial={
                "df": DependsOn("subject_traj"),
                "time_col": "segment_start",
                "groupers": DependsOn("groupers"),
            }
            | (params_dict.get("traj_add_temporal_index") or {}),
            method="call",
        ),
        "split_subject_traj_groups": Node(
            async_task=split_groups.validate().set_executor("lithops"),
            partial={
                "df": DependsOn("traj_add_temporal_index"),
                "groupers": DependsOn("groupers"),
            }
            | (params_dict.get("split_subject_traj_groups") or {}),
            method="call",
        ),
        "classify_traj_speed": Node(
            async_task=apply_classification.validate().set_executor("lithops"),
            partial=(params_dict.get("classify_traj_speed") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["df"],
                "argvalues": DependsOn("split_subject_traj_groups"),
            },
        ),
        "colormap_traj_speed": Node(
            async_task=apply_color_map.validate().set_executor("lithops"),
            partial={
                "colormap": [
                    "#1a9850",
                    "#91cf60",
                    "#d9ef8b",
                    "#fee08b",
                    "#fc8d59",
                    "#d73027",
                ],
            }
            | (params_dict.get("colormap_traj_speed") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["df"],
                "argvalues": DependsOn("classify_traj_speed"),
            },
        ),
        "speedmap_legend_with_unit": Node(
            async_task=map_values_with_unit.validate().set_executor("lithops"),
            partial=(params_dict.get("speedmap_legend_with_unit") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["df"],
                "argvalues": DependsOn("colormap_traj_speed"),
            },
        ),
        "traj_map_layers": Node(
            async_task=create_polyline_layer.validate().set_executor("lithops"),
            partial={
                "layer_style": {"color_column": "speed_bins_colormap"},
                "legend": {
                    "label_column": "speed_bins_formatted",
                    "color_column": "speed_bins_colormap",
                },
            }
            | (params_dict.get("traj_map_layers") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["geodataframe"],
                "argvalues": DependsOn("speedmap_legend_with_unit"),
            },
        ),
        "traj_ecomap": Node(
            async_task=draw_ecomap.validate().set_executor("lithops"),
            partial=(params_dict.get("traj_ecomap") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["geo_layers"],
                "argvalues": DependsOn("traj_map_layers"),
            },
        ),
        "ecomap_html_urls": Node(
            async_task=persist_text.validate().set_executor("lithops"),
            partial={
                "root_path": os.environ["ECOSCOPE_WORKFLOWS_RESULTS"],
            }
            | (params_dict.get("ecomap_html_urls") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["text"],
                "argvalues": DependsOn("traj_ecomap"),
            },
        ),
        "traj_map_widgets_single_views": Node(
            async_task=create_map_widget_single_view.validate().set_executor("lithops"),
            partial=(params_dict.get("traj_map_widgets_single_views") or {}),
            method="map",
            kwargs={
                "argnames": ["view", "data"],
                "argvalues": DependsOn("ecomap_html_urls"),
            },
        ),
        "traj_grouped_map_widget": Node(
            async_task=merge_widget_views.validate().set_executor("lithops"),
            partial={
                "widgets": DependsOn("traj_map_widgets_single_views"),
            }
            | (params_dict.get("traj_grouped_map_widget") or {}),
            method="call",
        ),
        "colormap_traj_night": Node(
            async_task=apply_color_map.validate().set_executor("lithops"),
            partial={
                "colormap": ["#292965", "#e7a553"],
            }
            | (params_dict.get("colormap_traj_night") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["df"],
                "argvalues": DependsOn("split_subject_traj_groups"),
            },
        ),
        "traj_map_night_layers": Node(
            async_task=create_polyline_layer.validate().set_executor("lithops"),
            partial={
                "layer_style": {"color_column": "is_night_colors"},
                "legend": {
                    "labels": ["Night", "Day"],
                    "colors": ["#292965", "#e7a553"],
                },
            }
            | (params_dict.get("traj_map_night_layers") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["geodataframe"],
                "argvalues": DependsOn("colormap_traj_night"),
            },
        ),
        "traj_daynight_ecomap": Node(
            async_task=draw_ecomap.validate().set_executor("lithops"),
            partial=(params_dict.get("traj_daynight_ecomap") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["geo_layers"],
                "argvalues": DependsOn("traj_map_night_layers"),
            },
        ),
        "ecomap_daynight_html_urls": Node(
            async_task=persist_text.validate().set_executor("lithops"),
            partial={
                "root_path": os.environ["ECOSCOPE_WORKFLOWS_RESULTS"],
            }
            | (params_dict.get("ecomap_daynight_html_urls") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["text"],
                "argvalues": DependsOn("traj_daynight_ecomap"),
            },
        ),
        "traj_map_daynight_widgets_sv": Node(
            async_task=create_map_widget_single_view.validate().set_executor("lithops"),
            partial=(params_dict.get("traj_map_daynight_widgets_sv") or {}),
            method="map",
            kwargs={
                "argnames": ["view", "data"],
                "argvalues": DependsOn("ecomap_daynight_html_urls"),
            },
        ),
        "traj_daynight_grouped_map_widget": Node(
            async_task=merge_widget_views.validate().set_executor("lithops"),
            partial={
                "widgets": DependsOn("traj_map_daynight_widgets_sv"),
            }
            | (params_dict.get("traj_daynight_grouped_map_widget") or {}),
            method="call",
        ),
        "mean_speed": Node(
            async_task=dataframe_column_mean.validate().set_executor("lithops"),
            partial=(params_dict.get("mean_speed") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["df"],
                "argvalues": DependsOn("split_subject_traj_groups"),
            },
        ),
        "average_speed_converted": Node(
            async_task=with_unit.validate().set_executor("lithops"),
            partial=(params_dict.get("average_speed_converted") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["value"],
                "argvalues": DependsOn("mean_speed"),
            },
        ),
        "mean_speed_sv_widgets": Node(
            async_task=create_single_value_widget_single_view.validate().set_executor(
                "lithops"
            ),
            partial=(params_dict.get("mean_speed_sv_widgets") or {}),
            method="map",
            kwargs={
                "argnames": ["view", "data"],
                "argvalues": DependsOn("average_speed_converted"),
            },
        ),
        "mean_speed_grouped_sv_widget": Node(
            async_task=merge_widget_views.validate().set_executor("lithops"),
            partial={
                "widgets": DependsOn("mean_speed_sv_widgets"),
            }
            | (params_dict.get("mean_speed_grouped_sv_widget") or {}),
            method="call",
        ),
        "max_speed": Node(
            async_task=dataframe_column_max.validate().set_executor("lithops"),
            partial=(params_dict.get("max_speed") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["df"],
                "argvalues": DependsOn("split_subject_traj_groups"),
            },
        ),
        "max_speed_converted": Node(
            async_task=with_unit.validate().set_executor("lithops"),
            partial=(params_dict.get("max_speed_converted") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["value"],
                "argvalues": DependsOn("max_speed"),
            },
        ),
        "max_speed_sv_widgets": Node(
            async_task=create_single_value_widget_single_view.validate().set_executor(
                "lithops"
            ),
            partial=(params_dict.get("max_speed_sv_widgets") or {}),
            method="map",
            kwargs={
                "argnames": ["view", "data"],
                "argvalues": DependsOn("max_speed_converted"),
            },
        ),
        "max_speed_grouped_sv_widget": Node(
            async_task=merge_widget_views.validate().set_executor("lithops"),
            partial={
                "widgets": DependsOn("max_speed_sv_widgets"),
            }
            | (params_dict.get("max_speed_grouped_sv_widget") or {}),
            method="call",
        ),
        "num_location": Node(
            async_task=dataframe_count.validate().set_executor("lithops"),
            partial=(params_dict.get("num_location") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["df"],
                "argvalues": DependsOn("split_subject_traj_groups"),
            },
        ),
        "num_location_sv_widgets": Node(
            async_task=create_single_value_widget_single_view.validate().set_executor(
                "lithops"
            ),
            partial=(params_dict.get("num_location_sv_widgets") or {}),
            method="map",
            kwargs={
                "argnames": ["view", "data"],
                "argvalues": DependsOn("num_location"),
            },
        ),
        "num_location_grouped_sv_widget": Node(
            async_task=merge_widget_views.validate().set_executor("lithops"),
            partial={
                "widgets": DependsOn("num_location_sv_widgets"),
            }
            | (params_dict.get("num_location_grouped_sv_widget") or {}),
            method="call",
        ),
        "daynight_ratio": Node(
            async_task=get_day_night_ratio.validate().set_executor("lithops"),
            partial=(params_dict.get("daynight_ratio") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["df"],
                "argvalues": DependsOn("split_subject_traj_groups"),
            },
        ),
        "daynight_ratio_sv_widgets": Node(
            async_task=create_single_value_widget_single_view.validate().set_executor(
                "lithops"
            ),
            partial=(params_dict.get("daynight_ratio_sv_widgets") or {}),
            method="map",
            kwargs={
                "argnames": ["view", "data"],
                "argvalues": DependsOn("daynight_ratio"),
            },
        ),
        "daynight_ratio_grouped_sv_widget": Node(
            async_task=merge_widget_views.validate().set_executor("lithops"),
            partial={
                "widgets": DependsOn("daynight_ratio_sv_widgets"),
            }
            | (params_dict.get("daynight_ratio_grouped_sv_widget") or {}),
            method="call",
        ),
        "total_distance": Node(
            async_task=dataframe_column_sum.validate().set_executor("lithops"),
            partial=(params_dict.get("total_distance") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["df"],
                "argvalues": DependsOn("split_subject_traj_groups"),
            },
        ),
        "total_dist_converted": Node(
            async_task=with_unit.validate().set_executor("lithops"),
            partial=(params_dict.get("total_dist_converted") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["value"],
                "argvalues": DependsOn("total_distance"),
            },
        ),
        "total_distance_sv_widgets": Node(
            async_task=create_single_value_widget_single_view.validate().set_executor(
                "lithops"
            ),
            partial=(params_dict.get("total_distance_sv_widgets") or {}),
            method="map",
            kwargs={
                "argnames": ["view", "data"],
                "argvalues": DependsOn("total_dist_converted"),
            },
        ),
        "total_dist_grouped_sv_widget": Node(
            async_task=merge_widget_views.validate().set_executor("lithops"),
            partial={
                "widgets": DependsOn("total_distance_sv_widgets"),
            }
            | (params_dict.get("total_dist_grouped_sv_widget") or {}),
            method="call",
        ),
        "total_time": Node(
            async_task=dataframe_column_sum.validate().set_executor("lithops"),
            partial=(params_dict.get("total_time") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["df"],
                "argvalues": DependsOn("split_subject_traj_groups"),
            },
        ),
        "total_time_converted": Node(
            async_task=with_unit.validate().set_executor("lithops"),
            partial=(params_dict.get("total_time_converted") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["value"],
                "argvalues": DependsOn("total_time"),
            },
        ),
        "total_time_sv_widgets": Node(
            async_task=create_single_value_widget_single_view.validate().set_executor(
                "lithops"
            ),
            partial=(params_dict.get("total_time_sv_widgets") or {}),
            method="map",
            kwargs={
                "argnames": ["view", "data"],
                "argvalues": DependsOn("total_time_converted"),
            },
        ),
        "total_time_grouped_sv_widget": Node(
            async_task=merge_widget_views.validate().set_executor("lithops"),
            partial={
                "widgets": DependsOn("total_time_sv_widgets"),
            }
            | (params_dict.get("total_time_grouped_sv_widget") or {}),
            method="call",
        ),
        "td": Node(
            async_task=calculate_time_density.validate().set_executor("lithops"),
            partial=(params_dict.get("td") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["trajectory_gdf"],
                "argvalues": DependsOn("split_subject_traj_groups"),
            },
        ),
        "td_colormap": Node(
            async_task=apply_color_map.validate().set_executor("lithops"),
            partial={
                "input_column_name": "percentile",
                "colormap": "RdYlGn_r",
                "output_column_name": "percentile_colormap",
            }
            | (params_dict.get("td_colormap") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["df"],
                "argvalues": DependsOn("td"),
            },
        ),
        "td_map_layer": Node(
            async_task=create_polygon_layer.validate().set_executor("lithops"),
            partial={
                "layer_style": {
                    "fill_color_column": "percentile_colormap",
                    "opacity": 0.7,
                    "get_line_width": 0,
                },
            }
            | (params_dict.get("td_map_layer") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["geodataframe"],
                "argvalues": DependsOn("td_colormap"),
            },
        ),
        "td_ecomap": Node(
            async_task=draw_ecomap.validate().set_executor("lithops"),
            partial=(params_dict.get("td_ecomap") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["geo_layers"],
                "argvalues": DependsOn("td_map_layer"),
            },
        ),
        "td_ecomap_html_url": Node(
            async_task=persist_text.validate().set_executor("lithops"),
            partial={
                "root_path": os.environ["ECOSCOPE_WORKFLOWS_RESULTS"],
            }
            | (params_dict.get("td_ecomap_html_url") or {}),
            method="mapvalues",
            kwargs={
                "argnames": ["text"],
                "argvalues": DependsOn("td_ecomap"),
            },
        ),
        "td_map_widget": Node(
            async_task=create_map_widget_single_view.validate().set_executor("lithops"),
            partial=(params_dict.get("td_map_widget") or {}),
            method="map",
            kwargs={
                "argnames": ["view", "data"],
                "argvalues": DependsOn("td_ecomap_html_url"),
            },
        ),
        "td_grouped_map_widget": Node(
            async_task=merge_widget_views.validate().set_executor("lithops"),
            partial={
                "widgets": DependsOn("td_map_widget"),
            }
            | (params_dict.get("td_grouped_map_widget") or {}),
            method="call",
        ),
        "nsd_chart": Node(
            async_task=draw_ecoplot.validate().set_executor("lithops"),
            partial={
                "dataframe": DependsOn("traj_add_temporal_index"),
            }
            | (params_dict.get("nsd_chart") or {}),
            method="call",
        ),
        "nsd_chart_html_url": Node(
            async_task=persist_text.validate().set_executor("lithops"),
            partial={
                "text": DependsOn("nsd_chart"),
                "root_path": os.environ["ECOSCOPE_WORKFLOWS_RESULTS"],
            }
            | (params_dict.get("nsd_chart_html_url") or {}),
            method="call",
        ),
        "nsd_chart_widget": Node(
            async_task=create_plot_widget_single_view.validate().set_executor(
                "lithops"
            ),
            partial={
                "data": DependsOn("nsd_chart_html_url"),
            }
            | (params_dict.get("nsd_chart_widget") or {}),
            method="call",
        ),
        "subject_tracking_dashboard": Node(
            async_task=gather_dashboard.validate().set_executor("lithops"),
            partial={
                "details": DependsOn("workflow_details"),
                "widgets": DependsOnSequence(
                    [
                        DependsOn("traj_grouped_map_widget"),
                        DependsOn("mean_speed_grouped_sv_widget"),
                        DependsOn("max_speed_grouped_sv_widget"),
                        DependsOn("num_location_grouped_sv_widget"),
                        DependsOn("daynight_ratio_grouped_sv_widget"),
                        DependsOn("total_dist_grouped_sv_widget"),
                        DependsOn("total_time_grouped_sv_widget"),
                        DependsOn("td_grouped_map_widget"),
                        DependsOn("traj_daynight_grouped_map_widget"),
                        DependsOn("nsd_chart_widget"),
                    ],
                ),
                "groupers": DependsOn("groupers"),
                "time_range": DependsOn("time_range"),
            }
            | (params_dict.get("subject_tracking_dashboard") or {}),
            method="call",
        ),
    }
    graph = Graph(dependencies=dependencies, nodes=nodes)
    results = graph.execute()
    return results
