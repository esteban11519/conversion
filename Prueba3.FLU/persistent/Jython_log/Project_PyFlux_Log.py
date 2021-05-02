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

