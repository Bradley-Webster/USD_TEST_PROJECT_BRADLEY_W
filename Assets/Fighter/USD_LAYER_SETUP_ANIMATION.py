from pxr import Usd, UsdGeom, Gf, Sdf


def setupTimecode(path):
    stage = Usd.Stage.CreateNew(path)
    stage.SetStartTimeCode(0)
    stage.SetEndTimeCode(500)
    return stage

def AddReferenceToGeometry(stage, path):
    geom = UsdGeom.Xform.Define(stage, path)
    geom.GetPrim().GetReferences().AddReference('./Fighter_Scene_Geom_HD.usd')
    return geom


def AddRotateX(Fighter_Scene):
    spin = Fighter_Scene.AddRotateXOp(opSuffix='spin')
    # Frame 0
    spin.Set(time=0, value=0)

    # Frame 28
    spin.Set(time=28, value=10)

	# Frame 71
    spin.Set(time=71, value=22)

    # Frame 160
    spin.Set(time=160, value=-23)

	# Frame 302
    spin.Set(time=302, value=20)

    # Frame 400
    spin.Set(time=400, value=-12)

    # Frame 500 (End Loop)
    spin.Set(time=500, value=0)


def FighterAnim_X_Rotate():
    stage = setupTimecode('Fighter_Scene_Geom_HD_Anim_X_Rotate.usda')
    stage.SetMetadata('comment', 'Adding Rotate X animation')
    Fighter_Scene = AddReferenceToGeometry(stage, '/Fighter_Scene')
    AddRotateX(Fighter_Scene)
    stage.Save()


def AddTranslateY(Fighter_Scene):
    spin = Fighter_Scene.AddTranslateOp(opSuffix='Translate_Y')
    # Frame 0
    spin.Set(time=0, value=(0,0,0))

    # Frame 28
    spin.Set(time=28, value=(0,0.119,0))

	# Frame 71
    spin.Set(time=71, value=(0,0.428,0))

    # Frame 160
    spin.Set(time=160, value=(0,0.677,0))

	# Frame 302
    spin.Set(time=302, value=(0,0.773,0))

    # Frame 400
    spin.Set(time=400, value=(0,-0.773,0))

    # Frame 500 (End Loop)
    spin.Set(time=500, value=(0,0,0))


def FighterAnim_Y_Translate():
    stage = setupTimecode('Fighter_Scene_Geom_HD_Anim_Y_Translate.usda')
    stage.SetMetadata('comment', 'Adding Translate Y animation')
    Fighter_Scene = AddReferenceToGeometry(stage, '/Fighter_Scene')
    AddTranslateY(Fighter_Scene)
    stage.Save()

def AddTranslateZ(Fighter_Scene):
    spin = Fighter_Scene.AddTranslateOp(opSuffix='Translate_Z')
    # Frame 0
    spin.Set(time=0, value=(0,0,0))

    # Frame 28
    spin.Set(time=28, value=(0,0,-2.269))

	# Frame 71
    spin.Set(time=71, value=(0,0,-4.756))

    # Frame 160
    spin.Set(time=160, value=(0,0,3.343))

	# Frame 302
    spin.Set(time=302, value=(0,0,-2.991))

    # Frame 400
    spin.Set(time=400, value=(0,0,2.953))

    # Frame 500 (End Loop)
    spin.Set(time=500, value=(0,0,0))


def FighterAnim_Z_Translate():
    stage = setupTimecode('Fighter_Scene_Geom_HD_Anim_Z_Translate.usda')
    stage.SetMetadata('comment', 'Adding Translate Z animation')
    Fighter_Scene = AddReferenceToGeometry(stage, '/Fighter_Scene')
    AddTranslateZ(Fighter_Scene)
    stage.Save()

def FighterAnim_Combined():
    stage = setupTimecode('Fighter_Scene_Geom_HD_Anim_Combined.usda')
    stage.SetMetadata('comment', 'Combine all Transforms together')
    Fighter_Scene = AddReferenceToGeometry(stage, '/Fighter_Scene') 

    AddRotateX(Fighter_Scene)

    AddTranslateY(Fighter_Scene)
    AddTranslateZ(Fighter_Scene)

    stage.Save()



# Create sepatate Translate/Rotate USD files for optional editing
FighterAnim_X_Rotate()
# Combine Translations
FighterAnim_Y_Translate()
FighterAnim_Z_Translate()


FighterAnim_Combined()