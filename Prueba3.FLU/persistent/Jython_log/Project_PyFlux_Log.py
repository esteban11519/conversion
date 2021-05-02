#! Flux2D 21.0
#! Sun May 02 13:52:02 COT 2021 loadProject('G:/Mi unidad/UNIVERSIDAD/Octavo Semestre/Conversion electromagnetica/SIMULACION PROYECTO FINAL/Prueba3.FLU')

Material(name='FLU_COPPER_1', propertyBH=PropertyBhLinear(mur='1.0'), thermalConductivity=KtIsotropic(k='394.0'), specificHeat=RhoCpConstant(rhoCp='3518000.0'), propertyJE=PropertyJeTLinearFunction(slope='0.00427', rhoConstant='1.564E-8', referenceTemperature=Temperature(temperature='0.0'), temperature=Temperature(temperature='20.0')))

Material['FLU_COPPER_1'].delete()

exportCircuit(filename='Prueba3_log1.xcir')

storeCircuitLinks()

DeleteElectricCircuit(deleteStrandedConductor='YES')

importCircuit(filename='Prueba3_log1.xcir',
              importValue=1,
              ImportFELink=1)


restoreCircuitLinks()

exportCircuit(filename='Prueba3_log2.xcir')

storeCircuitLinks()

DeleteElectricCircuit(deleteStrandedConductor='YES')

importCircuit(filename='Prueba3_log2.xcir',
              importValue=1,
              ImportFELink=1)


restoreCircuitLinks()

saveProject()

exportCircuit(filename='Prueba3_log3.xcir')

storeCircuitLinks()

DeleteElectricCircuit(deleteStrandedConductor='YES')

importCircuit(filename='Prueba3_log3.xcir',
              importValue=1,
              ImportFELink=1)


restoreCircuitLinks()

exportCircuit(filename='Prueba3_log4.xcir')

storeCircuitLinks()

DeleteElectricCircuit(deleteStrandedConductor='YES')

importCircuit(filename='Prueba3_log4.xcir',
              importValue=1,
              ImportFELink=1)


restoreCircuitLinks()

RegionFace['PHASE_NEG_1'].magneticTransient2D=MagneticTransient2DFaceCoilConductor(coilConductor=CoilConductor2DNegative(turnNumber='66',
                                                                                                                         seriesParallel=AllInSeries(),
                                                                                                                         electricComponent=CoilConductor['COILCONDUCTOR_1']),
                                                                                   material=Material['FLU_COPPER'])


RegionFace['PHASE_NEG_2'].magneticTransient2D=MagneticTransient2DFaceCoilConductor(coilConductor=CoilConductor2DNegative(turnNumber='66',
                                                                                                                         seriesParallel=AllInSeries(),
                                                                                                                         electricComponent=CoilConductor['COILCONDUCTOR_2']),
                                                                                   material=Material['FLU_COPPER'])


RegionFace['PHASE_NEG_3'].magneticTransient2D=MagneticTransient2DFaceCoilConductor(coilConductor=CoilConductor2DNegative(turnNumber='66',
                                                                                                                         seriesParallel=AllInSeries(),
                                                                                                                         electricComponent=CoilConductor['COILCONDUCTOR_3']),
                                                                                   material=Material['FLU_COPPER'])


RegionFace['PHASE_POS_1'].magneticTransient2D=MagneticTransient2DFaceCoilConductor(coilConductor=CoilConductor2DPositive(turnNumber='66',
                                                                                                                         seriesParallel=AllInSeries(),
                                                                                                                         electricComponent=CoilConductor['COILCONDUCTOR_1']),
                                                                                   material=Material['FLU_COPPER'])


RegionFace['PHASE_POS_2'].magneticTransient2D=MagneticTransient2DFaceCoilConductor(coilConductor=CoilConductor2DPositive(turnNumber='66',
                                                                                                                         seriesParallel=AllInSeries(),
                                                                                                                         electricComponent=CoilConductor['COILCONDUCTOR_1']),
                                                                                   material=Material['FLU_COPPER'])


RegionFace['PHASE_POS_2'].magneticTransient2D=MagneticTransient2DFaceCoilConductor(coilConductor=CoilConductor2DPositive(turnNumber='66',
                                                                                                                         seriesParallel=AllInSeries(),
                                                                                                                         electricComponent=CoilConductor['COILCONDUCTOR_2']),
                                                                                   material=Material['FLU_COPPER'])


RegionFace['PHASE_POS_3'].magneticTransient2D=MagneticTransient2DFaceCoilConductor(coilConductor=CoilConductor2DPositive(turnNumber='66',
                                                                                                                         seriesParallel=AllInSeries(),
                                                                                                                         electricComponent=CoilConductor['COILCONDUCTOR_3']),
                                                                                   material=Material['FLU_COPPER'])


Scenario(name='Scenario_1')

startMacroTransaction()

Scenario['Scenario_1'].addPilot(pilot=MultiValues(parameter=VariationParameter['ANGPOS_ROTOR'],
                                                  intervals=[IntervalLogStepNumber(minValue=1.0E-7,
                                                                                   maxValue=1.0,
                                                                                   stepNumber=30)]))

endMacroTransaction()

Scenario['SCENARIO_1'].solve(projectName='G:/Mi unidad/UNIVERSIDAD/Octavo Semestre/Conversion electromagnetica/SIMULACION PROYECTO FINAL/Prueba3.FLU')

DeleteAllResults(deletePostprocessingResults='yes')

checkMesh()

checkCircuit()

result = checkGeometry()

result = checkPhysic()

saveProject()

