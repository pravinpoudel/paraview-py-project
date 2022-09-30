# trace generated using paraview version 5.10.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 10

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# load plugin
LoadPlugin('C:/Program Files/ParaView 5.10.1-Windows-Python3.9-msvc2017-AMD64/bin/paraview-5.10/plugins/TopologyToolKit/TopologyToolKit.dll', remote=False, ns=globals())

# create a new 'STL Reader'
elev500blur2stl = STLReader(registrationName='elev500blur2.stl', FileNames=['./resources/terrain_400.stl'])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
elev500blur2stlDisplay = Show(elev500blur2stl, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
elev500blur2stlDisplay.Representation = 'Surface'

# reset view to fit data
renderView1.ResetCamera(False)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'TTK GeometrySmoother'
tTKGeometrySmoother1 = TTKGeometrySmoother(registrationName='TTKGeometrySmoother1', Input=elev500blur2stl)

# Properties modified on tTKGeometrySmoother1
tTKGeometrySmoother1.IterationNumber = 3
tTKGeometrySmoother1.InputMaskField = ['POINTS', '']

# show data in view
tTKGeometrySmoother1Display = Show(tTKGeometrySmoother1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
tTKGeometrySmoother1Display.Representation = 'Surface'

# hide data in view
Hide(elev500blur2stl, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Elevation'
elevation1 = Elevation(registrationName='Elevation1', Input=tTKGeometrySmoother1)

tTKGeometrySmoother1.UpdatePipeline()
di = tTKGeometrySmoother1.GetDataInformation()
bounds = di.DataInformation.GetBounds()

# Properties modified on elevation1
elevation1.ScalarRange = [0.0, 100.0]
elevation1.LowPoint = [0.0, 0.0, bounds[4]]
elevation1.HighPoint = [0.0, 0.0, bounds[5]]

# show data in view
elevation1Display = Show(elevation1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
elevation1Display.Representation = 'Surface'

# hide data in view
Hide(tTKGeometrySmoother1, renderView1)

# show color bar/color legend
elevation1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get color transfer function/color map for 'Elevation'
elevationLUT = GetColorTransferFunction('Elevation')

# get opacity transfer function/opacity map for 'Elevation'
elevationPWF = GetOpacityTransferFunction('Elevation')

# get layout
layout1 = GetLayout()

# split cell
layout1.SplitHorizontal(0, 0.5)

# set active view
SetActiveView(None)

# create a new 'TTK PersistenceCurve'
tTKPersistenceCurve1 = TTKPersistenceCurve(registrationName='TTKPersistenceCurve1', Input=elevation1)

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')

# show data in view
tTKPersistenceCurve1Display = Show(tTKPersistenceCurve1, lineChartView1, 'XYChartRepresentation')

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=2)

# show data in view
tTKPersistenceCurve1Display_1 = Show(OutputPort(tTKPersistenceCurve1, 1), lineChartView1, 'XYChartRepresentation')

# show data in view
tTKPersistenceCurve1Display_2 = Show(OutputPort(tTKPersistenceCurve1, 2), lineChartView1, 'XYChartRepresentation')

# show data in view
tTKPersistenceCurve1Display_3 = Show(OutputPort(tTKPersistenceCurve1, 3), lineChartView1, 'XYChartRepresentation')

# update the view to ensure updated data information
lineChartView1.Update()

# set active source
SetActiveSource(tTKPersistenceCurve1)

# Properties modified on lineChartView1
lineChartView1.BottomAxisTitle = 'Number of Pairs'

# Properties modified on lineChartView1
lineChartView1.BottomAxisUseCustomRange = 0

# Properties modified on lineChartView1
lineChartView1.BottomAxisLogScale = 1

# Properties modified on lineChartView1
lineChartView1.BottomAxisUseCustomRange = 1

# Properties modified on lineChartView1
lineChartView1.BottomAxisUseCustomRange = 0

# Properties modified on lineChartView1
lineChartView1.BottomAxisUseCustomRange = 1

# Properties modified on lineChartView1
lineChartView1.BottomAxisTitle = 'Persistance'

# Properties modified on lineChartView1
lineChartView1.LeftAxisTitle = 'Number of Pairs'

# Properties modified on lineChartView1
lineChartView1.LeftAxisLogScale = 1

# Properties modified on lineChartView1
lineChartView1.LeftAxisUseCustomRange = 0

# Properties modified on lineChartView1
lineChartView1.LeftAxisUseCustomRange = 1

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(elevation1)

# set active source
SetActiveSource(tTKPersistenceCurve1)

# set active source
SetActiveSource(tTKPersistenceCurve1)

# set active source
SetActiveSource(tTKPersistenceCurve1)

# set active source
SetActiveSource(tTKPersistenceCurve1)

# set active source
SetActiveSource(elevation1)

# set active view
SetActiveView(lineChartView1)

# set active source
SetActiveSource(tTKPersistenceCurve1)

# set active source
SetActiveSource(tTKPersistenceCurve1)

# hide data in view
Hide(OutputPort(tTKPersistenceCurve1, 2), lineChartView1)

# hide data in view
Hide(OutputPort(tTKPersistenceCurve1, 1), lineChartView1)

# hide data in view
Hide(tTKPersistenceCurve1, lineChartView1)

# Properties modified on tTKPersistenceCurve1Display_3
tTKPersistenceCurve1Display_3.SeriesVisibility = ['Number Of Pairs (all pairs)']

# Properties modified on lineChartView1
lineChartView1.LeftAxisUseCustomRange = 0

# Properties modified on lineChartView1
lineChartView1.LeftAxisUseCustomRange = 1

# Properties modified on lineChartView1
lineChartView1.BottomAxisUseCustomRange = 0

# Properties modified on lineChartView1
lineChartView1.BottomAxisUseCustomRange = 0

# Properties modified on lineChartView1
lineChartView1.BottomAxisUseCustomRange = 1

# split cell
layout1.SplitVertical(2, 0.5)

# set active view
SetActiveView(None)

# set active source
SetActiveSource(elevation1)

# create a new 'TTK PersistenceDiagram'
tTKPersistenceDiagram1 = TTKPersistenceDiagram(registrationName='TTKPersistenceDiagram1', Input=elevation1)

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraFocalDisk = 1.0
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.OSPRayMaterialLibrary = materialLibrary1

# show data in view
tTKPersistenceDiagram1Display = Show(tTKPersistenceDiagram1, renderView2, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
tTKPersistenceDiagram1Display.Representation = 'Surface'

# add view to a layout so it's visible in UI
AssignViewToLayout(view=renderView2, layout=layout1, hint=6)

# reset view to fit data
renderView2.ResetCamera(False)

#changing interaction mode based on data extents
renderView2.InteractionMode = '2D'
renderView2.CameraPosition = [49.0662841796875, 50.0, 10000.0]
renderView2.CameraFocalPoint = [49.0662841796875, 50.0, 0.0]

# update the view to ensure updated data information
renderView2.Update()

# Properties modified on renderView2.AxesGrid
renderView2.AxesGrid.XTitle = 'Birth'
renderView2.AxesGrid.YTitle = 'Death'

# Properties modified on renderView2.AxesGrid
renderView2.AxesGrid.Visibility = 1

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=tTKPersistenceDiagram1)

# Properties modified on threshold1
threshold1.Scalars = ['CELLS', 'PairIdentifier']
threshold1.LowerThreshold = -1.0
threshold1.UpperThreshold = -0.1

# show data in view
threshold1Display = Show(threshold1, renderView2, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold1Display.Representation = 'Surface'

# hide data in view
Hide(tTKPersistenceDiagram1, renderView2)

# update the view to ensure updated data information
renderView2.Update()

# create a new 'Extract Surface'
extractSurface1 = ExtractSurface(registrationName='ExtractSurface1', Input=threshold1)

# show data in view
extractSurface1Display = Show(extractSurface1, renderView2, 'GeometryRepresentation')

# trace defaults for the display properties.
extractSurface1Display.Representation = 'Surface'

# hide data in view
Hide(threshold1, renderView2)

# update the view to ensure updated data information
renderView2.Update()

# create a new 'Tube'
tube1 = Tube(registrationName='Tube1', Input=extractSurface1)

# show data in view
tube1Display = Show(tube1, renderView2, 'GeometryRepresentation')

# trace defaults for the display properties.
tube1Display.Representation = 'Surface'

# hide data in view
Hide(extractSurface1, renderView2)

# update the view to ensure updated data information
renderView2.Update()

# Properties modified on tube1
tube1.Radius = 0.6

# update the view to ensure updated data information
renderView2.Update()

# set active source
SetActiveSource(threshold1)

# set active source
SetActiveSource(tTKPersistenceDiagram1)

# create a new 'Threshold'
threshold2 = Threshold(registrationName='Threshold2', Input=tTKPersistenceDiagram1)

# Properties modified on threshold2
threshold2.Scalars = ['CELLS', 'PairIdentifier']
threshold2.LowerThreshold = -0.1
threshold2.UpperThreshold = 9255.0

# show data in view
threshold2Display = Show(threshold2, renderView2, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold2Display.Representation = 'Surface'

# hide data in view
Hide(tTKPersistenceDiagram1, renderView2)

# update the view to ensure updated data information
renderView2.Update()

# Properties modified on threshold2
threshold2.UpperThreshold = 100.0

# update the view to ensure updated data information
renderView2.Update()

# Properties modified on threshold2
threshold2.UpperThreshold = 1000.0

# update the view to ensure updated data information
renderView2.Update()

# Properties modified on threshold2
threshold2.UpperThreshold = 9255.0

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# create a new 'Threshold'
threshold3 = Threshold(registrationName='Threshold3', Input=threshold2)

# Properties modified on threshold3
threshold3.Scalars = ['CELLS', 'Persistence']
threshold3.LowerThreshold = 10.0
threshold3.UpperThreshold = 100.0

# show data in view
threshold3Display = Show(threshold3, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold3Display.Representation = 'Surface'

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# set active source
SetActiveSource(threshold2)

# set active view
SetActiveView(renderView2)

# set active source
SetActiveSource(threshold3)

# set active source
SetActiveSource(threshold2)

# hide data in view
Hide(threshold3, renderView1)

# destroy threshold3
Delete(threshold3)
del threshold3

# set active view
SetActiveView(renderView1)

# set active view
SetActiveView(renderView2)

# create a new 'Threshold'
threshold3 = Threshold(registrationName='Threshold3', Input=threshold2)

# Properties modified on threshold3
threshold3.Scalars = ['CELLS', 'Persistence']
threshold3.LowerThreshold = 10.0
threshold3.UpperThreshold = 100.0

# show data in view
threshold3Display = Show(threshold3, renderView2, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold3Display.Representation = 'Surface'

# hide data in view
Hide(threshold2, renderView2)

# update the view to ensure updated data information
renderView2.Update()

# Properties modified on threshold3
threshold3.LowerThreshold = 20.0

# update the view to ensure updated data information
renderView2.Update()

# set active view
SetActiveView(renderView1)

# set active source
SetActiveSource(elevation1)

# set active source
SetActiveSource(tTKGeometrySmoother1)

# set active source
SetActiveSource(elevation1)

# set active source
SetActiveSource(threshold2)

# rename source object
RenameSource('Persistance Threshold', threshold2)

# rename source object
RenameSource('Persistance', threshold2)

# set active source
SetActiveSource(threshold3)

# set active source
SetActiveSource(threshold2)

# rename source object
RenameSource('Persistance pAIR', threshold2)

# rename source object
RenameSource('Persistance Pair', threshold2)

# set active source
SetActiveSource(threshold3)

# rename source object
RenameSource('PersistanceThreshold', threshold3)

# set active source
SetActiveSource(threshold2)

# rename source object
RenameSource('PersistancePair', threshold2)

# set active source
SetActiveSource(elevation1)

# create a new 'TTK TopologicalSimplification'
tTKTopologicalSimplification1 = TTKTopologicalSimplification(registrationName='TTKTopologicalSimplification1', Domain=elevation1,
    Constraints=threshold3)

# show data in view
tTKTopologicalSimplification1Display = Show(tTKTopologicalSimplification1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
tTKTopologicalSimplification1Display.Representation = 'Surface'

# hide data in view
Hide(elevation1, renderView1)

# show color bar/color legend
tTKTopologicalSimplification1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# update the view to ensure updated data information
renderView2.Update()

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints1 = TTKIcospheresFromPoints(registrationName='TTKIcospheresFromPoints1', Input=tTKTopologicalSimplification1)

# show data in view
tTKIcospheresFromPoints1Display = Show(tTKIcospheresFromPoints1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
tTKIcospheresFromPoints1Display.Representation = 'Surface'

# show color bar/color legend
tTKIcospheresFromPoints1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# save data
SaveData('C:/work/paraview Projs/exports/terrain.pvd', proxy=tTKIcospheresFromPoints1, PointDataArrays=['Elevation', 'Elevation_Order', 'Normals'])

# set active source
SetActiveSource(tTKTopologicalSimplification1)

# set active source
SetActiveSource(threshold2)

# set active source
SetActiveSource(tTKTopologicalSimplification1)

# create a new 'TTK ScalarFieldCriticalPoints'
tTKScalarFieldCriticalPoints1 = TTKScalarFieldCriticalPoints(registrationName='TTKScalarFieldCriticalPoints1', Input=tTKTopologicalSimplification1)

# show data in view
tTKScalarFieldCriticalPoints1Display = Show(tTKScalarFieldCriticalPoints1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
tTKScalarFieldCriticalPoints1Display.Representation = 'Surface'

# show color bar/color legend
tTKScalarFieldCriticalPoints1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'TTK IcospheresFromPoints'
tTKIcospheresFromPoints2 = TTKIcospheresFromPoints(registrationName='TTKIcospheresFromPoints2', Input=tTKScalarFieldCriticalPoints1)

# show data in view
tTKIcospheresFromPoints2Display = Show(tTKIcospheresFromPoints2, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
tTKIcospheresFromPoints2Display.Representation = 'Surface'

# show color bar/color legend
tTKIcospheresFromPoints2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on tTKIcospheresFromPoints2
tTKIcospheresFromPoints2.Radius = 2.0

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on tTKIcospheresFromPoints2
tTKIcospheresFromPoints2.Radius = 22.0

# update the view to ensure updated data information
renderView1.Update()

# split cell
layout1.SplitVertical(1, 0.5)

# set active view
SetActiveView(None)

# set active source
SetActiveSource(tTKTopologicalSimplification1)

# Create a new 'Render View'
renderView3 = CreateView('RenderView')
renderView3.AxesGrid = 'GridAxes3DActor'
renderView3.StereoType = 'Crystal Eyes'
renderView3.CameraFocalDisk = 1.0
renderView3.BackEnd = 'OSPRay raycaster'
renderView3.OSPRayMaterialLibrary = materialLibrary1

# assign view to a particular cell in the layout
AssignViewToLayout(view=renderView3, layout=layout1, hint=4)

# set active source
SetActiveSource(tTKTopologicalSimplification1)

# show data in view
tTKTopologicalSimplification1Display_1 = Show(tTKTopologicalSimplification1, renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
tTKTopologicalSimplification1Display_1.Representation = 'Surface'

# show color bar/color legend
tTKTopologicalSimplification1Display_1.SetScalarBarVisibility(renderView3, True)

# reset view to fit data
renderView3.ResetCamera(False)

# link cameras in two views
AddCameraLink(renderView3, renderView1, 'CameraLink0')

# set active view
SetActiveView(renderView1)

# set active view
SetActiveView(renderView3)

# set active source
SetActiveSource(tTKTopologicalSimplification1)

# create a new 'TTK Merge and Contour Tree (FTM)'
tTKMergeandContourTreeFTM1 = TTKMergeandContourTreeFTM(registrationName='TTKMergeandContourTreeFTM1', Input=tTKTopologicalSimplification1)

# show data in view
tTKMergeandContourTreeFTM1Display = Show(tTKMergeandContourTreeFTM1, renderView3, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
tTKMergeandContourTreeFTM1Display.Representation = 'Surface'

# hide data in view
Hide(tTKTopologicalSimplification1, renderView3)

# show color bar/color legend
tTKMergeandContourTreeFTM1Display.SetScalarBarVisibility(renderView3, True)

# show data in view
tTKMergeandContourTreeFTM1Display_1 = Show(OutputPort(tTKMergeandContourTreeFTM1, 1), renderView3, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
tTKMergeandContourTreeFTM1Display_1.Representation = 'Surface'

# hide data in view
Hide(tTKTopologicalSimplification1, renderView3)

# show color bar/color legend
tTKMergeandContourTreeFTM1Display_1.SetScalarBarVisibility(renderView3, True)

# show data in view
tTKMergeandContourTreeFTM1Display_2 = Show(OutputPort(tTKMergeandContourTreeFTM1, 2), renderView3, 'GeometryRepresentation')

# trace defaults for the display properties.
tTKMergeandContourTreeFTM1Display_2.Representation = 'Surface'

# hide data in view
Hide(tTKTopologicalSimplification1, renderView3)

# show color bar/color legend
tTKMergeandContourTreeFTM1Display_2.SetScalarBarVisibility(renderView3, True)

# update the view to ensure updated data information
renderView3.Update()

# get color transfer function/color map for 'CriticalType'
criticalTypeLUT = GetColorTransferFunction('CriticalType')

# get opacity transfer function/opacity map for 'CriticalType'
criticalTypePWF = GetOpacityTransferFunction('CriticalType')

# hide data in view
Hide(tTKMergeandContourTreeFTM1, renderView3)

# hide data in view
Hide(tTKMergeandContourTreeFTM1, renderView3)

# set active source
SetActiveSource(tTKMergeandContourTreeFTM1)

# show data in view
tTKMergeandContourTreeFTM1Display = Show(tTKMergeandContourTreeFTM1, renderView3, 'UnstructuredGridRepresentation')

# show color bar/color legend
tTKMergeandContourTreeFTM1Display.SetScalarBarVisibility(renderView3, True)

# show data in view
tTKMergeandContourTreeFTM1Display = Show(tTKMergeandContourTreeFTM1, renderView3, 'UnstructuredGridRepresentation')

# show color bar/color legend
tTKMergeandContourTreeFTM1Display.SetScalarBarVisibility(renderView3, True)

# hide data in view
Hide(tTKMergeandContourTreeFTM1, renderView3)

# show data in view
tTKMergeandContourTreeFTM1Display = Show(tTKMergeandContourTreeFTM1, renderView3, 'UnstructuredGridRepresentation')

# show color bar/color legend
tTKMergeandContourTreeFTM1Display.SetScalarBarVisibility(renderView3, True)

# hide data in view
Hide(OutputPort(tTKMergeandContourTreeFTM1, 1), renderView3)

# hide data in view
Hide(tTKMergeandContourTreeFTM1, renderView3)

# set active source
SetActiveSource(tTKMergeandContourTreeFTM1)

# get color transfer function/color map for 'SegmentationId'
segmentationIdLUT = GetColorTransferFunction('SegmentationId')

# get opacity transfer function/opacity map for 'SegmentationId'
segmentationIdPWF = GetOpacityTransferFunction('SegmentationId')

# get active source.
tTKMergeandContourTreeFTM1_1 = GetActiveSource()

# save data
SaveData('./exports/terrain.pvd', proxy=OutputPort(tTKMergeandContourTreeFTM1_1, 2), PointDataArrays=['Elevation', 'Elevation_Order', 'RegionSize', 'RegionSpan', 'RegionType', 'SegmentationId'])

# layout/tab size in pixels
layout1.SetSize(1307, 1089)

# current camera placement for renderView1
renderView1.CameraPosition = [1120.9096028346419, 3183.877937528499, 4547.697923083958]
renderView1.CameraFocalPoint = [2051.499999999999, 927.499999999998, 254.16547060012843]
renderView1.CameraViewUp = [0.2366772438153094, -0.8379904923636894, 0.49168670611279514]
renderView1.CameraParallelScale = 2264.5036630197

# current camera placement for renderView2
renderView2.InteractionMode = '2D'
renderView2.CameraPosition = [49.0662841796875, 50.0, 10000.0]
renderView2.CameraFocalPoint = [49.0662841796875, 50.0, 0.0]
renderView2.CameraParallelScale = 70.05355268080164

# current camera placement for renderView3
renderView3.CameraPosition = [1120.9096028346419, 3183.877937528499, 4547.697923083958]
renderView3.CameraFocalPoint = [2051.499999999999, 927.499999999998, 254.16547060012843]
renderView3.CameraViewUp = [0.2366772438153094, -0.8379904923636894, 0.49168670611279514]
renderView3.CameraParallelScale = 2264.5036630197

# save extracts
SaveExtracts(ExtractsOutputDirectory='extracts',
    GenerateCinemaSpecification=0)

# export view
ExportView('./exports/terrain.gltf', view=renderView3, InlineData=1,
    SaveNormal=1,
    SaveBatchId=1)

# export view
ExportView('./exports/terrain.vtkjs', view=renderView3, ParaViewGlanceHTML='')

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1307, 819)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [1120.9096028346419, 3183.877937528499, 4547.697923083958]
renderView1.CameraFocalPoint = [2051.499999999999, 927.499999999998, 254.16547060012843]
renderView1.CameraViewUp = [0.2366772438153094, -0.8379904923636894, 0.49168670611279514]
renderView1.CameraParallelScale = 2264.5036630197

# current camera placement for renderView2
renderView2.InteractionMode = '2D'
renderView2.CameraPosition = [49.0662841796875, 50.0, 10000.0]
renderView2.CameraFocalPoint = [49.0662841796875, 50.0, 0.0]
renderView2.CameraParallelScale = 70.05355268080164

# current camera placement for renderView3
renderView3.CameraPosition = [1120.9096028346419, 3183.877937528499, 4547.697923083958]
renderView3.CameraFocalPoint = [2051.499999999999, 927.499999999998, 254.16547060012843]
renderView3.CameraViewUp = [0.2366772438153094, -0.8379904923636894, 0.49168670611279514]
renderView3.CameraParallelScale = 2264.5036630197

#--------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).