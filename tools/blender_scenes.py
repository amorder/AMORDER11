#!/usr/bin/env python3
"""Deterministic original Blender 3D plates for public AMORDER educational shorts."""
import argparse, json, math, sys
from pathlib import Path
import bpy
from mathutils import Vector

NAVY=(.008,.018,.042,1); BLUE=(.035,.30,.72,1); CYAN=(.06,.76,.90,1)
ICE=(.58,.88,.98,1); AMBER=(1,.45,.16,1); WHITE=(.86,.94,1,1)

def mat(name, color):
    material = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    material.diffuse_color = color
    material.use_nodes = True
    shader = material.node_tree.nodes.get("Principled BSDF")
    if shader:
        shader.inputs["Base Color"].default_value = color
        shader.inputs["Metallic"].default_value = .58
        shader.inputs["Roughness"].default_value = .24
        if "ice" in name.lower() or "white" in name.lower():
            shader.inputs["Metallic"].default_value = .24
            shader.inputs["Roughness"].default_value = .19
        if "amber" in name.lower() or "cyan" in name.lower():
            shader.inputs["Metallic"].default_value = .42
            shader.inputs["Roughness"].default_value = .2
        if "Coat Weight" in shader.inputs:
            shader.inputs["Coat Weight"].default_value = .28
        if "Coat Roughness" in shader.inputs:
            shader.inputs["Coat Roughness"].default_value = .16
        if "cyan" in name.lower() or "amber" in name.lower() or "blue" in name.lower():
            emission_socket = shader.inputs.get("Emission Color") or shader.inputs.get("Emission")
            if emission_socket:
                emission_socket.default_value = color
            if "Emission Strength" in shader.inputs:
                shader.inputs["Emission Strength"].default_value = .16
        if "graphite" in name.lower():
            nodes = material.node_tree.nodes
            links = material.node_tree.links
            noise = nodes.new("ShaderNodeTexNoise")
            noise.inputs["Scale"].default_value = 145
            noise.inputs["Detail"].default_value = 2
            bump = nodes.new("ShaderNodeBump")
            bump.inputs["Strength"].default_value = .075
            bump.inputs["Distance"].default_value = .018
            links.new(noise.outputs["Fac"], bump.inputs["Height"])
            links.new(bump.outputs["Normal"], shader.inputs["Normal"])
    return material


def finish(obj, color, radius=.07):
    obj.data.materials.clear(); obj.data.materials.append(color); obj.color=color.diffuse_color
    if radius:
        b=obj.modifiers.new("Soft precision edges","BEVEL"); b.width=radius; b.segments=5
        obj.modifiers.new("Weighted normals","WEIGHTED_NORMAL")
    return obj

def box(name, loc, dims, color, radius=.07):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc)
    o=bpy.context.object; o.name=name; o.dimensions=dims
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    return finish(o,color,min(radius,min(dims)*.22) if radius else 0)

def ball(name, loc, radius, color):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=40, ring_count=20, radius=radius, location=loc)
    o=bpy.context.object; o.name=name
    for p in o.data.polygons: p.use_smooth=True
    return finish(o,color,0)

def ring(name, loc, major, minor, color, rotation=(math.pi/2,0,0)):
    bpy.ops.mesh.primitive_torus_add(major_segments=80, minor_segments=14, major_radius=major,
                                     minor_radius=minor, location=loc, rotation=rotation)
    o=bpy.context.object; o.name=name
    for p in o.data.polygons: p.use_smooth=True
    return finish(o,color,0)

def rod(name, a, b, radius, color):
    a,b=Vector(a),Vector(b); v=b-a
    bpy.ops.mesh.primitive_cylinder_add(vertices=48, radius=radius, depth=v.length, location=(a+b)/2)
    o=bpy.context.object; o.name=name; o.rotation_euler=v.to_track_quat("Z","Y").to_euler()
    return finish(o,color,radius*.25)

def shield(color):
    points=[(-1.18,1.0),(1.18,1.0),(1.0,-.2),(0,-1.30),(-1.0,-.2)]
    depth=.32; n=len(points)
    verts=[(x,y,z) for y in (-depth/2,depth/2) for x,z in points]
    faces=[tuple(range(n-1,-1,-1)),tuple(range(n,2*n))]
    for i in range(n): j=(i+1)%n; faces.append((i,j,j+n,i+n))
    mesh=bpy.data.meshes.new("Shield mesh"); mesh.from_pydata(verts,[],faces); mesh.materials.append(color)
    o=bpy.data.objects.new("Risk shield",mesh); bpy.context.collection.objects.link(o)
    b=o.modifiers.new("Soft shield edges","BEVEL"); b.width=.09; b.segments=5
    return o

def clear():
    bpy.ops.object.select_all(action="SELECT"); bpy.ops.object.delete(use_global=False)

def area_light(name, location, target, power, color, size):
    data = bpy.data.lights.new(name, "AREA")
    data.energy = power
    data.color = color
    data.shape = "DISK"
    data.size = size
    obj = bpy.data.objects.new(name, data)
    bpy.context.collection.objects.link(obj)
    obj.location = location
    obj.rotation_euler = (Vector(target) - obj.location).to_track_quat("-Z", "Y").to_euler()
    return obj


def setup(width=1080, height=1920):
    scene = bpy.context.scene
    engines = {item.identifier for item in scene.render.bl_rna.properties["engine"].enum_items}
    scene.render.engine = "BLENDER_EEVEE_NEXT" if "BLENDER_EEVEE_NEXT" in engines else "BLENDER_EEVEE"
    scene.render.resolution_x = width
    scene.render.resolution_y = height
    scene.render.resolution_percentage = 100
    scene.render.image_settings.file_format = "PNG"
    scene.render.image_settings.color_mode = "RGBA"
    scene.render.film_transparent = False
    scene.render.threads_mode = "FIXED"
    scene.render.threads = 4
    try:
        scene.view_settings.view_transform = "AgX"
        scene.view_settings.look = "AgX - Medium High Contrast"
    except Exception:
        pass

    world = bpy.data.worlds.get("World") or bpy.data.worlds.new("World")
    world.use_nodes = True
    world.node_tree.nodes["Background"].inputs["Color"].default_value = (.003, .006, .014, 1)
    world.node_tree.nodes["Background"].inputs["Strength"].default_value = .18
    scene.world = world

    # Physical graphite studio with carefully shaped softbox lighting.
    graphite = mat("Graphite set", (.009, .016, .027, 1))
    box("Seamless dark studio backdrop", (0, 3.4, 1.0), (36, .5, 34), graphite, 0)
    box("Graphite reflective floor", (0, 0, -.62), (36, 36, .34), graphite, .02)
    area_light("Large cool key softbox", (4.5, -7, 9), (0, 0, 2.5), 2600, (.72, .86, 1.0), 8)
    area_light("Warm edge softbox", (-6, 0, 5.8), (0, 0, 2.5), 1800, (1.0, .55, .32), 5)
    area_light("Cyan rim light", (1.5, 4.5, 7), (0, 0, 2.6), 3200, (.18, .68, 1.0), 5)
    area_light("Low fill", (0, -4, -.2), (0, 0, 2.3), 500, (.46, .62, .82), 7)
    area_light("Top edge softbox", (0, 1.5, 10), (0, 0, 2.4), 1500, (.58, .75, 1.0), 7)

    # Raised anodised display stage with a restrained cyan edge accent.
    stage_material = mat("Anodised graphite stage", (.014, .025, .042, 1))
    bpy.ops.mesh.primitive_cylinder_add(vertices=128, radius=4.15, depth=.18,
                                        location=(0, 0, -.34))
    stage = bpy.context.object
    stage.name = "Anodised circular presentation stage"
    finish(stage, stage_material, .08)
    ring("Stage perimeter cyan inlay", (0, 0, -.245), 4.02, .018,
         mat("Stage cyan accent", CYAN), rotation=(0, 0, 0))

    camera_data = bpy.data.cameras.new("Cinematic portrait camera")
    camera = bpy.data.objects.new("Cinematic portrait camera", camera_data)
    bpy.context.collection.objects.link(camera)
    camera.location = (.2, -19.5, 2.6)
    target = Vector((0, 0, 2.55))
    camera.rotation_euler = (target - camera.location).to_track_quat("-Z", "Y").to_euler()
    camera_data.type = "PERSP"
    camera_data.lens = 52
    camera_data.dof.use_dof = True
    focus = bpy.data.objects.new("Focus plane", None)
    bpy.context.collection.objects.link(focus)
    focus.location = target
    camera_data.dof.focus_object = focus
    camera_data.dof.aperture_fstop = 7.1
    scene.camera = camera

    # Skip version-specific compositor nodes; PBR lighting and FFmpeg finishing remain.
    return scene


def build(key):
    blue=mat("Cobalt",BLUE); cyan=mat("Cyan",CYAN); ice=mat("Ice",ICE)
    amber=mat("Amber",AMBER); white=mat("White",WHITE)
    if key=="idea":
        ring("Evidence lens",(0,0,2.8),1.62,.17,cyan); ring("Lens inner rim",(0,-.05,2.8),1.30,.04,ice)
        rod("Lens handle",(1.05,0,1.65),(2.05,0,.30),.18,amber); ball("Focus core",(-.35,-.25,2.9),.38,blue)
        for i,(x,z) in enumerate([(-2.1,.2),(-1,-.25),(.85,.25),(1.65,.95)]):
            box("Evidence tile "+str(i),(x,.25,z),(.56,.3,.56),ice if i%2==0 else blue,.08)
    elif key=="timestamp":
        ring("Clock bezel",(0,0,2.5),2,.16,cyan); ring("Clock track",(0,-.02,2.5),1.7,.035,ice)
        for i in range(12):
            a=math.tau*i/12; x,z=1.76*math.sin(a),2.5+1.76*math.cos(a)
            box("Clock marker "+str(i),(x,-.16,z),(.11,.18,.26 if i%3==0 else .15),ice,.03)
        ball("Clock pivot",(0,-.4,2.5),.17,amber)
        rod("Minute hand",(0,-.38,2.5),(.15,-.38,3.85),.075,ice)
        rod("Second hand",(0,-.43,2.5),(-1.02,-.43,2.12),.045,amber)
        box("Clock base",(0,.15,-.05),(2.7,.55,.28),blue,.10)
    elif key=="gaps":
        for row in range(3):
            for col in range(4):
                if (row,col)==(1,2): continue
                x=(col-1.5)*1.05; z=3.2-row
                box(f"Data block {row}-{col}",(x,0,z),(.82,.52,.72),
                    ice if (row+col)%3==0 else (cyan if col%2 else blue),.10)
        ring("Missing segment",(1.58,-.08,2.2),.33,.075,amber)
        rod("Gap left",(.82,.05,2.2),(1.10,.05,2.2),.045,amber)
        rod("Gap right",(2,.05,2.2),(2.30,.05,2.2),.045,amber)
    elif key=="source":
        for i,z in enumerate((4,2.65,1.3)):
            color=(ice,blue,cyan)[i]
            box("Source panel "+str(i),(-2.45,.1,z),(1.45,.45,.72),color,.12)
            for j in range(2):
                box(f"Panel detail {i}-{j}",(-2.45,-.19,z+.12-j*.23),(.78-j*.24,.055,.055),white,.02)
            rod("Source stream "+str(i),(-1.6,.1,z),(-.45,.1,2.65),.055,amber if i==1 else cyan)
        ring("Source gateway",(.62,0,2.65),.94,.14,amber); ball("Verified core",(.62,-.24,2.65),.38,ice)
        for i in range(3): ball("Output node "+str(i),(2.2+i*.48,0,2.65),.18,cyan)
    elif key=="stand_down":
        ring("Decision boundary",(0,.3,2.5),2,.09,blue); shield(ice)
        box("Pause bar left",(-.43,-.42,2.52),(.34,.23,1.35),cyan,.10)
        box("Pause bar right",(.43,-.42,2.52),(.34,.23,1.35),amber,.10)
        ball("Shield anchor",(0,-.45,1.4),.19,ice)
    elif key=="brand":
        ring("Brand orbital ring",(0,.1,2.7),2.25,.10,cyan,(math.radians(68),0,math.radians(-18)))
        ring("Brand inner orbit",(0,-.1,2.7),1.55,.055,amber,(math.radians(105),0,math.radians(24)))
        ball("Brand core",(0,-.1,2.7),.72,ice)
        for i,a in enumerate((.4,2.3,4.55)):
            ball("Brand satellite "+str(i),(2.25*math.cos(a),-.05,2.7+2.25*math.sin(a)),.16,amber if i==1 else cyan)
        box("Brand plinth",(0,.3,.15),(3.4,.8,.22),blue,.10)
    else:
        raise ValueError("Unsupported Blender visual: "+str(key))

def animate_scene(scene, visual, duration, fps):
    """Keyframe the camera and scene geometry in Blender (not a still-image zoom)."""
    frame_end = max(2, int(math.ceil(duration * fps)))
    scene.frame_start = 1
    scene.frame_end = frame_end
    scene.render.fps = fps

    camera = scene.camera
    focus = bpy.data.objects.get("Focus plane")
    if camera is None or focus is None:
        raise RuntimeError("Cinematic camera/focus rig was not created")

    base_camera = camera.location.copy()
    target = focus.location.copy()
    key_frames = sorted(set([1, max(2, frame_end // 4), max(2, frame_end // 2),
                             max(2, (frame_end * 3) // 4), frame_end]))
    for frame in key_frames:
        p = (frame - 1) / max(1, frame_end - 1)
        camera.location = base_camera + Vector((
            .34 * math.sin(math.tau * p),
            .10 * (1 - math.cos(math.tau * p)),
            .12 * math.sin(2 * math.tau * p)
        ))
        camera.rotation_euler = (target - camera.location).to_track_quat("-Z", "Y").to_euler()
        camera.keyframe_insert(data_path="location", frame=frame)
        camera.keyframe_insert(data_path="rotation_euler", frame=frame)

    pivot = None
    if visual == "timestamp":
        pivot = bpy.data.objects.new("Clockwork animation pivot", None)
        scene.collection.objects.link(pivot)
        pivot.location = (0, -.4, 2.5)
        for name in ("Minute hand", "Second hand"):
            obj = bpy.data.objects.get(name)
            if obj:
                world = obj.matrix_world.copy()
                obj.parent = pivot
                obj.matrix_parent_inverse = pivot.matrix_world.inverted()
                obj.matrix_world = world

    for obj_index, obj in enumerate(scene.objects):
        if obj.type != "MESH" or obj.name in {
            "Seamless dark studio backdrop", "Graphite reflective floor"
        }:
            continue
        if pivot and obj.parent == pivot:
            continue
        base_loc = obj.location.copy()
        base_rot = obj.rotation_euler.copy()
        base_scale = obj.scale.copy()
        token = sum(ord(ch) for ch in obj.name) + obj_index * 17
        phase = (token % 97) / 97 * math.tau
        name = obj.name.lower()

        for frame in key_frames:
            p = (frame - 1) / max(1, frame_end - 1)
            wave = math.sin(math.tau * p + phase)
            if "ring" in name or "orbit" in name or "bezel" in name or "track" in name:
                obj.rotation_euler = base_rot.copy()
                obj.rotation_euler[1] += math.tau * p
                obj.location = base_loc
            elif "satellite" in name or "output node" in name or "focus core" in name:
                obj.location = base_loc + Vector((
                    .10 * math.sin(math.tau * p + phase) - .10 * math.sin(phase),
                    0,
                    .12 * (math.cos(math.tau * p + phase) - math.cos(phase))
                ))
                pulse = 1 + .045 * (math.cos(math.tau * p + phase) - math.cos(phase))
                obj.scale = base_scale * pulse
            elif "clock marker" in name:
                pulse = 1 + .025 * math.sin(math.tau * p + phase)
                obj.scale = base_scale * pulse
            else:
                obj.location = base_loc + Vector((.025 * wave, 0, .065 * wave))
                obj.rotation_euler = base_rot.copy()
                obj.rotation_euler[2] += .025 * wave

            obj.keyframe_insert(data_path="location", frame=frame)
            obj.keyframe_insert(data_path="rotation_euler", frame=frame)
            obj.keyframe_insert(data_path="scale", frame=frame)

    if pivot:
        for frame in key_frames:
            p = (frame - 1) / max(1, frame_end - 1)
            pivot.rotation_euler = (0, -math.tau * p, 0)
            pivot.keyframe_insert(data_path="rotation_euler", frame=frame)
    scene.frame_set(1)


def configure_animation_output(scene, output, fps):
    scene.render.fps = fps
    scene.render.image_settings.file_format = "FFMPEG"
    scene.render.ffmpeg.format = "MPEG4"
    scene.render.ffmpeg.codec = "H264"
    scene.render.ffmpeg.constant_rate_factor = "HIGH"
    scene.render.ffmpeg.ffmpeg_preset = "GOOD"
    scene.render.ffmpeg.video_bitrate = 16000
    scene.render.ffmpeg.maxrate = 24000
    scene.render.ffmpeg.buffersize = 2000
    scene.render.ffmpeg.audio_codec = "NONE"
    scene.render.filepath = str(Path(output).resolve().with_suffix(""))
    scene.render.use_file_extension = True
    if hasattr(scene.render, "use_motion_blur"):
        scene.render.use_motion_blur = True
        if hasattr(scene.render, "motion_blur_shutter"):
            scene.render.motion_blur_shutter = .35


def main():
    if "--" not in sys.argv:
        raise SystemExit("Expected -- followed by --visual and --output")
    p = argparse.ArgumentParser()
    p.add_argument("--visual", required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--width", type=int, default=1080)
    p.add_argument("--height", type=int, default=1920)
    p.add_argument("--duration", type=float, default=0)
    p.add_argument("--fps", type=int, default=15)
    a = p.parse_args(sys.argv[sys.argv.index("--") + 1:])
    clear()
    scene = setup(a.width, a.height)
    build(a.visual)
    if a.duration > 0:
        animate_scene(scene, a.visual, a.duration, a.fps)
        configure_animation_output(scene, a.output, a.fps)
        bpy.ops.render.render(animation=True)
        output = Path(a.output).resolve()
        if not output.exists() or output.stat().st_size < 100000:
            raise RuntimeError("Blender animation export is missing or unexpectedly small")
        print("Rendered genuine Blender camera/object animation:", a.visual,
              a.width, a.height, a.duration, "seconds at", a.fps, "fps")
    else:
        scene.render.filepath = str(Path(a.output).resolve())
        bpy.ops.render.render(write_still=True)
        print("Rendered cinematic Blender still:", a.visual, a.width, a.height)


if __name__ == "__main__":
    main()
