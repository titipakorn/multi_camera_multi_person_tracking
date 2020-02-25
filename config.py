# This config is tuned for the bundle of person-detection-retail-xxx and person-reidentification-retail-xxx
# models, but should be suitable for other well-trained detector and reid models
# Alse all tracking update intervals are set assumin input frequency about 30FPS

sct_config = dict(
    time_window=10,
    continue_time_thresh=2,
    track_clear_thresh=3000,
    match_threshold=0.475,
    merge_thresh=0.3,
    n_clusters=4,
    max_bbox_velocity=0.2,
    detection_occlusion_thresh=0.7,
    track_detection_iou_thresh=0.5
)

footfall_config=dict(
    p_in=[{"x":576,"y":718},{"x":586,"y":1},{"x":2,"y":0},{"x":4,"y":717},{"x":575,"y":718}],
    p_out=[{"x":584,"y":719},{"x":601,"y":0},{"x":1279,"y":2},{"x":1279,"y":717},{"x":585,"y":719}]
)