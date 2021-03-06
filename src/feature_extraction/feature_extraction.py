from src.feature_extraction.advanced_statistics import advanced_statistics
from src.feature_extraction.graph_statistics import graph_statistics
from src.feature_extraction.non_points_features import non_points_features
from src.feature_extraction.points_features import points_features
from src.feature_extraction.simple_stats import simple_stats


def feature_extraction(data_frame):
    """
    :param data_frame: The loaded input file
    :return:
    """
    dict_list = list()
    feature_list = list()

    dict_list.extend(simple_stats(data_frame)[0])
    feature_list.extend(simple_stats(data_frame)[1])
    dict_list.extend(points_features(data_frame)[0])
    feature_list.extend(points_features(data_frame)[1])
    dict_list.extend(non_points_features(data_frame)[0])
    feature_list.extend(non_points_features(data_frame)[1])
    dict_list.extend(advanced_statistics(data_frame)[0])
    feature_list.extend(advanced_statistics(data_frame)[1])
    dict_list.extend(advanced_statistics(data_frame)[0])
    feature_list.extend(advanced_statistics(data_frame)[1])
    dict_list.extend(graph_statistics(data_frame)[0])
    feature_list.extend(graph_statistics(data_frame)[1])
    return dict_list, feature_list


def merge_dicts(data_frame):
    final_dict = dict()
    extraction = feature_extraction(data_frame)
    for d in extraction[0]:
        for key, value in d.items():
            final_dict.setdefault(key, []).append(value)
    return final_dict, extraction[1]
