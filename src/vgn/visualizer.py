import numpy as np
from mayavi import mlab


cm = lambda s: tuple([float(1 - s), float(s), float(0)])


def clear():
    mlab.clf()


def scene_cloud(voxel_size, cloud):
    points = np.asarray(cloud.points)
    mlab.points3d(
        points[:, 0],
        points[:, 1],
        points[:, 2],
        scale_factor=voxel_size,
        scale_mode="none",
    )


def map_cloud(voxel_size, cloud):
    points = np.asarray(cloud.points)
    distances = np.asarray(cloud.colors)[:, 0]
    mlab.points3d(
        points[:, 0],
        points[:, 1],
        points[:, 2],
        distances,
        mode="cube",
        scale_factor=voxel_size,
        scale_mode="none",
    )


def grasp(grasp, quality, depth, radius=0.002):
    pose, w, d = grasp.pose, grasp.width, depth
    color = cm(quality)

    points = [[0, -w / 2, d], [0, -w / 2, 0], [0, w / 2, 0], [0, w / 2, d]]
    points = np.vstack([pose.apply(p) for p in points])
    mlab.plot3d(
        points[:, 0],
        points[:, 1],
        points[:, 2],
        color=color,
        tube_radius=radius,
    )

    points = [[0, 0, 0], [0, 0, -d]]
    points = np.vstack([pose.apply(p) for p in points])
    mlab.plot3d(
        points[:, 0],
        points[:, 1],
        points[:, 2],
        color=color,
        tube_radius=radius,
    )


def grasps(grasps, qualities, depth, max_grasps=None):
    if max_grasps and max_grasps < len(grasps):
        i = np.random.randint(len(grasps), size=max_grasps)
        grasps, qualities = grasps[i], qualities[i]
    for grasp_config, quality in zip(grasps, qualities):
        grasp(grasp_config, quality, depth)


def show():
    mlab.show()
