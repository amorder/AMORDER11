#!/usr/bin/env python3
"""Deterministic original Blender 3D plates for public AMORDER educational shorts."""
import argparse, json, math, sys
from pathlib import Path
import bpy
from mathutils import Vector

NAVY=(.008,.018,.042,1); BLUE=(.035,.30,.72,1); CYAN=(.06,.76,.90,1)
ICE=(.58,.88,.98,1); AMBER=(1,.45,.16,1); WHITE=(.86,.94,1,1)

def mat(name, color):
    m=bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.diffuse_color=color
    return m

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

def setup():
    s=bpy.context.scene; s.render.engine="BLENDER_WORKBENCH"
    s.render.resolution_x=1080; s.render.resolution_y=1920; s.render.resolution_percentage=100
    s.render.image_settings.file_format="PNG"; s.render.image_settings.color_mode="RGBA"
    s.render.threads_mode="FIXED"; s.render.threads=2
    sh=s.display.shading; sh.light="STUDIO"; sh.color_type="MATERIAL"
    sh.background_type="WORLD"; sh.show_shadows=True; sh.show_cavity=True; sh.cavity_type="WORLD"
    try: sh.studio_light="paint.sl"
    except Exception: sh.studio_light="rim.sl"
    w=bpy.data.worlds.get("World") or bpy.data.worlds.new("World"); s.world=w
    w.color=(.008,.016,.034)
    cd=bpy.data.cameras.new("Portrait camera"); cam=bpy.data.objects.new("Portrait camera",cd)
    bpy.context.collection.objects.link(cam); cam.location=(0,-24,.2)
    cam.rotation_euler=(math.pi/2,0,0); cd.type="ORTHO"; cd.ortho_scale=17.8; s.camera=cam
    box("Midnight stage",(0,2.8,0),(30,.45,36),mat("Midnight",NAVY),0)
    for i,(x,z) in enumerate([(-4.1,5.8),(3.9,5.2),(-4.2,-2),(4.25,-3.6),(3.4,6.6)]):
        ball("Ambient point "+str(i),(x,1.8,z),.045,mat("Ambient "+str(i),CYAN))
    return s

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

def main():
    if "--" not in sys.argv: raise SystemExit("Expected -- followed by --input and --output-dir")
    p=argparse.ArgumentParser(); p.add_argument("--input",required=True); p.add_argument("--output-dir",required=True)
    a=p.parse_args(sys.argv[sys.argv.index("--")+1:])
    story=json.loads(Path(a.input).read_text(encoding="utf-8")); scenes=story.get("scenes",[])
    if story.get("language")!="en" or not scenes: raise SystemExit("English storyboard required")
    out=Path(a.output_dir); out.mkdir(parents=True,exist_ok=True)
    for i,item in enumerate(scenes,1):
        clear(); scene=setup(); build(item.get("visual"))
        scene.render.filepath=str(out/f"{i:02d}.png"); bpy.ops.render.render(write_still=True)
        print(f"Rendered Blender scene {i}/{len(scenes)}")
if __name__=="__main__": main()
