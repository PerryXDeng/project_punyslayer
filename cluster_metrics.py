from unicode_info.database import download_and_parse_unicode_clusters


def calculate_mean_coverage(predicted_codepoints_clusters_map: dict,
                            predicted_clusters_codepoints_map: dict) -> float:
  """
  "coverage", suited for comparing consortium clusters with predicted clusters on entire unicode
  :param predicted_clusters_codepoints_map: mapping of cluster ids to lists of codepoints
  :param predicted_codepoints_clusters_map: mapping of codepoints to cluster id
  :return:
  """
  unicode_clusters_codepoints_map = download_and_parse_unicode_clusters()
  unicode_clusters_coverage = [_best_coverage(cluster, predicted_codepoints_clusters_map,
                                              predicted_clusters_codepoints_map)
                               for cluster in unicode_clusters_codepoints_map.values()]
  return sum(unicode_clusters_coverage) / len(unicode_clusters_coverage)


def calculate_mean_iou(predicted_codepoints_clusters_map: dict,
                       predicted_clusters_codepoints_map: dict) -> float:
  """
  mean Intersection Over Union, suited for comparing consortium clusters with clusters on just the consortium homoglyphs
  :param predicted_clusters_codepoints_map: mapping of cluster ids to lists of codepoints
  :param predicted_codepoints_clusters_map: mapping of codepoints to cluster id
  :return:
  """
  unicode_clusters_codepoints_map = download_and_parse_unicode_clusters()
  unicode_clusters_iou = [_best_iou(cluster, predicted_codepoints_clusters_map,
                                    predicted_clusters_codepoints_map)
                          for cluster in unicode_clusters_codepoints_map.values()]
  return sum(unicode_clusters_iou) / len(unicode_clusters_iou)


def _best_coverage(cluster_of_codepoints: list, predicted_codepoints_clusters_map: dict,
                   predicted_clusters_codepoints_map: dict) -> float:
  actual_codepoints = set(cluster_of_codepoints)
  predicted_cluster_ids = set([predicted_codepoints_clusters_map[codepoint] for codepoint in cluster_of_codepoints])
  predicted_cluster_codepoints = [set(predicted_clusters_codepoints_map[cluster_id])
                                  for cluster_id in predicted_cluster_ids]
  set_size = len(actual_codepoints)
  coverage = [len(actual_codepoints.intersection(cluster)) / set_size for cluster in predicted_cluster_codepoints]
  return max(coverage)


def _best_iou(cluster_of_codepoints: list, predicted_codepoints_clusters_map: dict,
              predicted_clusters_codepoints_map: dict) -> float:
  actual_codepoints = set(cluster_of_codepoints)
  predicted_cluster_ids = set([predicted_codepoints_clusters_map[codepoint] for codepoint in cluster_of_codepoints])
  predicted_cluster_codepoints = [set(predicted_clusters_codepoints_map[cluster_id])
                                  for cluster_id in predicted_cluster_ids]
  iou = [len(actual_codepoints.intersection(cluster)) / len(actual_codepoints.union(cluster))
         for cluster in predicted_cluster_codepoints]
  return max(iou)
