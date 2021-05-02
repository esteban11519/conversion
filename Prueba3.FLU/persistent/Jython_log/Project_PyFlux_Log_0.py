#! Flux2D 21.0
newProject()

SketcherOption[1].magnetizationGrid=MagnetizationGrid(gridActivation='OUI',lengthGridCell=10.0,cellSubdivision=10,subdivisionPoint=10)

openSketcher2dContext()

loadOverlay(name='Brushless_Permanent_Magnet_Outer_Rotor_Motors_V11.1.PFO')

lastInstance = MotorBPMExtRot(name='MotorBPMExtRot_140',
               lengthUnit='Millimeter',
               mesh_factor=0.5,
               GAP=0.6,
               excentricity=ExcentricityNo(periodicity='Yes',
                                           bdr='1_layer_airgap'),
               rotor=RotorExtPll(RadSH=100.0,
                                 Rad1=85.6,
                                 POLES=8,
                                 Nmbp=1,
                                 LM=3.5,
                                 rotorAng=0.0,
                                 BetaM=135.0,
                                 R_rpf=85.6,
                                 magnetType=RotorExtPllNot()),
               stator=InStatorFlared(Rad3=40.0,
                                     NSLOTS=24,
                                     statorAng=0.0,
                                     SD=30.0,
                                     TWS=7.2,
                                     SO=8.5,
                                     TGD=3.0,
                                     SOANG=60.0,
                                     SWIT=9.0,
                                     filSO=0.0,
                                     filSB=0.0,
                                     airgapShape=AirgapShapeSimple()),
               infiniteBox=InfiniteDisc(rInt=105.0,
                                        rExt=140.0),
               winding=ClassicalWinding(layers_position='superimposed',
                                        nPhases=3,
                                        windingType=ConcentricWinding(windingThrow=8,
                                                                      cpp=1)))

MotorBPMExtRot['MotorBPMExtRot_140'].excentricity=ExcentricityNo(periodicity='No',
                                                                 bdr='1_layer_airgap')


MotorBPMExtRot['MotorBPMExtRot_140'].stator=InStatorPllSquare(Rad3=40.0,
                                                              NSLOTS=24,
                                                              statorAng=0.0,
                                                              SD=30.0,
                                                              SWID=11.1,
                                                              SO=7.2,
                                                              TGD=3.0,
                                                              SOANG=60.0,
                                                              airgapShape=AirgapShapeSimple())

MotorBPMExtRot['MotorBPMExtRot_140'].winding=ClassicalWinding(layers_position='adjacent',
                                                              nPhases=3,
                                                              windingType=LapWinding(windingThrow=1,
                                                                                     cpp=1))


MotorBPMExtRot['MotorBPMExtRot_140'].winding=ClassicalWinding(layers_position='adjacent',
                                                              nPhases=3,
                                                              windingType=ConcentricWinding(windingThrow=1,
                                                                                            cpp=1))


leaveOverlay()
closeSketcher2dContext()

buildFaces()

meshDomain()

lastInstance = ApplicationMagneticTransient2D(domain2D=Domain2DPlane(lengthUnit=LengthUnit['MILLIMETER'],
                                                      depth='63'),
                               coilCoefficient=CoilCoefficientAutomatic(),
                               transientInitialization=TransientInitializationZeroInitialSolution())

Material(name='Cogent_M270_35A_50Hz : AC Curve 50 Hz - Magsoft 11-27-13', propertyBH=PropertyBhNonlinearSpline(splinePoints=[BHPoint(h=0.0, b=0.0), BHPoint(h=26.375800811465094, b=0.5542453884496874), BHPoint(h=50.27887029685533, b=0.7932457282512432), BHPoint(h=100.55774059371066, b=1.0413790461856718), BHPoint(h=152.0729765536034, b=1.1653798787285532), BHPoint(h=216.46702150346937, b=1.2526024627952799), BHPoint(h=296.9595776908018, b=1.3164607428059398), BHPoint(h=397.5752729249673, b=1.3648107594964283), BHPoint(h=523.3448919676742, b=1.4026007679786716), BHPoint(h=680.5569157710579, b=1.4331470586060477), BHPoint(h=877.0719455252874, b=1.4588045063560051), BHPoint(h=1122.7157327180744, b=1.4813464195631727), BHPoint(h=1429.7704667090582, b=1.5021953757078763), BHPoint(h=1813.5888841977878, b=1.5225741352263291), BHPoint(h=2293.3619060587, b=1.543612769755432), BHPoint(h=2893.07818338484, b=1.5664322436521476), BHPoint(h=3642.723530042515, b=1.5922166756843776), BHPoint(h=4579.780213364609, b=1.6222823840784122), BHPoint(h=5751.1010675172265, b=1.6581497374002823), BHPoint(h=7215.252135207998, b=1.7016188693305998), BHPoint(h=9045.440969821462, b=1.7504878853271493), BHPoint(h=11333.177013088292, b=1.8007862770631304), BHPoint(h=14192.847067171831, b=1.851071142297314), BHPoint(h=17767.434634776255, b=1.8997687017550717), BHPoint(h=22235.669094281784, b=1.9452929178152862), BHPoint(h=27820.962168663693, b=1.9861524420879992), BHPoint(h=34802.57851164108, b=2.0210222667408715), BHPoint(h=43529.59894036281, b=2.0487662869186134), BHPoint(h=54438.37447626499, b=2.0684092789312016), BHPoint(h=59882.21192389149, b=2.0752502068243217)], equivalentHarmonicCurve=EquivalentBhUnmodified()), propertyJE=PropertyJeLinear(rho='5.2E-7'), volumicMass='7650')

Material(name='CY_N35_20DEG : 80C_SinteredNdFebMagnet', propertyBH=PropertyBhMagnetOneDirection(br='1.21', mur='1.052'), propertyJE=PropertyJeLinear(rho='1.6E-6'), volumicMass='7400')

lastInstance = MechanicalSetRotation1Axis(name='Rotor',
                           kinematics=RotatingImposedSpeed(velocity='1/6',
                                                           initialPosition='0'),
                           rotationAxis=RotationZAxis(coordSys=CoordSys['XY1'],
                                                      pivot=['0',
                                                             '0']))

lastInstance = MechanicalSetFixed(name='Stator')

startMacroTransaction()
RegionFace['MAGNET_1_POLE_1','MAGNET_1_POLE_2','MAGNET_1_POLE_3','MAGNET_1_POLE_4','MAGNET_1_POLE_5','MAGNET_1_POLE_6','MAGNET_1_POLE_7','MAGNET_1_POLE_8'].mechanicalSet=MechanicalSet['ROTOR']

RegionFace['MAGNET_1_POLE_1'].magneticTransient2D=MagneticTransient2DFaceMagnetic(material=Material['CY_N35_20DEG'])

RegionFace['MAGNET_1_POLE_2'].magneticTransient2D=MagneticTransient2DFaceMagnetic(material=Material['CY_N35_20DEG'])

RegionFace['MAGNET_1_POLE_3'].magneticTransient2D=MagneticTransient2DFaceMagnetic(material=Material['CY_N35_20DEG'])

RegionFace['MAGNET_1_POLE_4'].magneticTransient2D=MagneticTransient2DFaceMagnetic(material=Material['CY_N35_20DEG'])

RegionFace['MAGNET_1_POLE_5'].magneticTransient2D=MagneticTransient2DFaceMagnetic(material=Material['CY_N35_20DEG'])

RegionFace['MAGNET_1_POLE_6'].magneticTransient2D=MagneticTransient2DFaceMagnetic(material=Material['CY_N35_20DEG'])

RegionFace['MAGNET_1_POLE_7'].magneticTransient2D=MagneticTransient2DFaceMagnetic(material=Material['CY_N35_20DEG'])

RegionFace['MAGNET_1_POLE_8'].magneticTransient2D=MagneticTransient2DFaceMagnetic(material=Material['CY_N35_20DEG'])

endMacroTransaction()

startMacroTransaction()
RegionFace['PHASE_NEG_1','PHASE_NEG_2','PHASE_NEG_3','PHASE_POS_2','PHASE_POS_1','PHASE_POS_3'].mechanicalSet=MechanicalSet['STATOR']

RegionFace['PHASE_NEG_1'].magneticTransient2D=MagneticTransient2DFaceVacuum()

RegionFace['PHASE_NEG_2'].magneticTransient2D=MagneticTransient2DFaceVacuum()

RegionFace['PHASE_NEG_3'].magneticTransient2D=MagneticTransient2DFaceVacuum()

RegionFace['PHASE_POS_2'].magneticTransient2D=MagneticTransient2DFaceVacuum()

RegionFace['PHASE_POS_1'].magneticTransient2D=MagneticTransient2DFaceVacuum()

RegionFace['PHASE_POS_3'].magneticTransient2D=MagneticTransient2DFaceVacuum()

endMacroTransaction()

startMacroTransaction()
RegionFace['INFINITE','WEDGE','STATOR_AIR','ROTATING_AIRGAP'].mechanicalSet=MechanicalSet['STATOR']

RegionFace['INFINITE'].magneticTransient2D=MagneticTransient2DFaceVacuum()

RegionFace['WEDGE'].magneticTransient2D=MagneticTransient2DFaceVacuum()

RegionFace['STATOR_AIR'].magneticTransient2D=MagneticTransient2DFaceVacuum()

RegionFace['ROTATING_AIRGAP'].magneticTransient2D=MagneticTransient2DFaceVacuum()

endMacroTransaction()

startMacroTransaction()
RegionFace['SHAFT','ROTOR_AIR'].mechanicalSet=MechanicalSet['ROTOR']

RegionFace['SHAFT'].magneticTransient2D=MagneticTransient2DFaceVacuum()

RegionFace['ROTOR_AIR'].magneticTransient2D=MagneticTransient2DFaceVacuum()

endMacroTransaction()

startMacroTransaction()
RegionFace['ROTOR'].magneticTransient2D=MagneticTransient2DFaceMagnetic(material=Material['COGENT_M270_35A_50HZ'])

RegionFace['ROTOR'].mechanicalSet=MechanicalSet['ROTOR']

endMacroTransaction()

startMacroTransaction()
RegionFace['STATOR'].magneticTransient2D=MagneticTransient2DFaceMagnetic(material=Material['COGENT_M270_35A_50HZ'])

RegionFace['STATOR'].mechanicalSet=MechanicalSet['STATOR']

endMacroTransaction()

orientRegSurfMaterial(region=RegionFace['MAGNET_1_POLE_1'],coordSys=CoordSys['ROTOR_COORD'],orientation='Direction',angle='22.5')
orientRegSurfMaterial(region=RegionFace['MAGNET_1_POLE_2'],coordSys=CoordSys['ROTOR_COORD'],orientation='Direction',angle='67.5')
orientRegSurfMaterial(region=RegionFace['MAGNET_1_POLE_3'],coordSys=CoordSys['ROTOR_COORD'],orientation='Direction',angle='112.5')
orientRegSurfMaterial(region=RegionFace['MAGNET_1_POLE_4'],coordSys=CoordSys['ROTOR_COORD'],orientation='Direction',angle='157.5')
orientRegSurfMaterial(region=RegionFace['MAGNET_1_POLE_5'],coordSys=CoordSys['ROTOR_COORD'],orientation='Direction',angle='-157.5')
orientRegSurfMaterial(region=RegionFace['MAGNET_1_POLE_6'],coordSys=CoordSys['ROTOR_COORD'],orientation='Direction',angle='-112.5')
orientRegSurfMaterial(region=RegionFace['MAGNET_1_POLE_7'],coordSys=CoordSys['ROTOR_COORD'],orientation='Direction',angle='-67.5')
orientRegSurfMaterial(region=RegionFace['MAGNET_1_POLE_8'],coordSys=CoordSys['ROTOR_COORD'],orientation='Direction',angle='-22.5')
result = checkPhysic()

Scenario(name='Scenario_1')

startMacroTransaction()

Scenario['Scenario_1'].addPilot(pilot=MultiValues(parameter=VariationParameter['ANGPOS_ROTOR'],
                                                  intervals=[IntervalStepValue(minValue=0.0,
                                                                               maxValue=7.5,
                                                                               stepValue=0.1875)]))

endMacroTransaction()

