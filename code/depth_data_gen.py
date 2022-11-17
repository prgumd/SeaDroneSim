import bpy
import numpy as np
import math
from Utils import render_img

def randomize_scene(mesh_names):
    mesh_names = []
    scene_size_x = 50
    scene_Size_y = 50
    z_val = 0.02
    for mesh_name in cluster_mesh_names:
            obj=bpy.context.scene.objects[mesh_name]

            # Set oyster location in x and y randomly
            rn=random.random()
            obj.location.x=rn*scene_size_x
            rn=random.random() 
            bpy.context.object.location.y=rn*scene_Size_y
            bpy.context.object.location.z=z_val

            # [Roll, Pitch, Yaw] = [(random.randint(-180, 180)) * pi / 180 for x in range(3)]
            # bpy.ops.transform.rotate(value=Roll, orient_axis='X')
            # bpy.ops.transform.rotate(value=Pitch, orient_axis='Y')
            # bpy.ops.transform.rotate(value=Yaw, orient_axis='Z')
    cam = bpy.context.scene.objects['BlueROV']
    del_pitch = random.random(-10,10) * np.pi / 180
    obj.rotation_euler.x = del_pitch + obj.rotation_euler.x 


def main():
    base_dir_path = script_path.split('code')[0]

    mesh_names=[]
    N_IMAGES = 5
    bluerov_model_path = base_dir_path + "//data//blender_data//blueROV//BlueRov2.dae"
    out_dir = base_dir_path + "//data//output//"

     # if output dir not present, make one
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    # if render output dir not present, make one
    render_out_dir = os.path.join(out_dir, "render_output")
    if not os.path.exists(render_out_dir):
        os.makedirs(render_out_dir)
    
    # if front camera render output dir not present, make one
    front_cam_dir = os.path.join(render_out_dir, "front_cam")
    if not os.path.exists(front_cam_dir):
        os.makedirs(front_cam_dir)
    
    # collection objects to randomize in scene
    collections = ['grass','corals','rocks','hills','misc']
    for collection in collections:
        col = bpy.data.collections[collection]
        for obj in col.objects:
            mesh_names.append(obj)
        


    bluerov_location = (-0.85, -0.65, 7.45)
    bluerov_orientation = (1.57, 0, 1.57)
    # import blueROV 3d model 
    front_cam, bottom_cam = add_bluerov(bluerov_model_path, bluerov_location)

    for frame_count in range(N_IMAGES):
        randomize_scene(mesh_names)
        render_img(front_cam_dir, frame_count, front_cam, save_both=True)

if __name__=="__main__":
    main()
