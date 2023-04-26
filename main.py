import open3d as o3d


source = o3d.io.read_point_cloud("test0.pcd")  # 换成自己的路径
o3d.visualization.draw_geometries([source])

