---
title: Document
classe: Autodesk.Revit.Creation.Document
namespace: Autodesk.Revit.Creation
eredita: Autodesk.Revit.Creation.ItemFactoryBase
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 57
---

# Document

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `Area NewArea(ViewPlan, UV)` | `document.NewArea(areaView, point)` | Area |
| `BoundaryConditions NewAreaBoundaryConditions(Element, TranslationRotationValue, Double, TranslationRotationValue, Double, TranslationRotationValue, Double)` | `document.NewAreaBoundaryConditions(hostElement, X_Translation, X_TranslationSpringModulus, Y_Translation, Y_TranslationSpringModulus, Z_Translation, Z_TranslationSpringModulus)` | BoundaryConditions |
| `BoundaryConditions NewAreaBoundaryConditions(Reference, TranslationRotationValue, Double, TranslationRotationValue, Double, TranslationRotationValue, Double)` | `document.NewAreaBoundaryConditions(reference, X_Translation, X_TranslationSpringModulus, Y_Translation, Y_TranslationSpringModulus, Z_Translation, Z_TranslationSpringModulus)` | BoundaryConditions |
| `ModelCurve NewAreaBoundaryLine(SketchPlane, Curve, ViewPlan)` | `document.NewAreaBoundaryLine(sketchPlane, geometryCurve, areaView)` | ModelCurve |
| `ElementSet NewAreas(List<AreaCreationData>)` | `document.NewAreas(dataList)` | ElementSet |
| `AreaTag NewAreaTag(ViewPlan, Area, UV)` | `document.NewAreaTag(areaView, room, point)` | AreaTag |
| `FamilyInstance NewCrossFitting(Connector, Connector, Connector, Connector)` | `document.NewCrossFitting(connector1, connector2, connector3, connector4)` | FamilyInstance |
| `CurtainSystem NewCurtainSystem(FaceArray, CurtainSystemType)` | `document.NewCurtainSystem(faces, curtainSystemType)` | CurtainSystem |
| `ICollection<ElementId> NewCurtainSystem2(ReferenceArray, CurtainSystemType)` | `document.NewCurtainSystem2(faces, curtainSystemType)` | ICollection<ElementId> |
| `FamilyInstance NewElbowFitting(Connector, Connector)` | `document.NewElbowFitting(connector1, connector2)` | FamilyInstance |
| `ExtrusionRoof NewExtrusionRoof(CurveArray, ReferencePlane, Level, RoofType, Double, Double)` | `document.NewExtrusionRoof(profile, refPlane, level, roofType, extrusionStart, extrusionEnd)` | ExtrusionRoof |
| `FamilyInstance NewFamilyInstance(Curve, FamilySymbol, Level, StructuralType)` | `document.NewFamilyInstance(curve, symbol, level, structuralType)` | FamilyInstance |
| `FamilyInstance NewFamilyInstance(XYZ, FamilySymbol, Element, Level, StructuralType)` | `document.NewFamilyInstance(location, symbol, host, level, structuralType)` | FamilyInstance |
| `Fascia NewFascia(FasciaType, Reference)` | `document.NewFascia(FasciaType, reference)` | Fascia |
| `Fascia NewFascia(FasciaType, ReferenceArray)` | `document.NewFascia(FasciaType, references)` | Fascia |
| `FlexDuct NewFlexDuct(Connector, Connector, FlexDuctType)` | `document.NewFlexDuct(connector1, connector2, ductType)` | FlexDuct |
| `FlexDuct NewFlexDuct(Connector, IList<XYZ>, FlexDuctType)` | `document.NewFlexDuct(connector, points, ductType)` | FlexDuct |
| `FlexDuct NewFlexDuct(IList<XYZ>, FlexDuctType)` | `document.NewFlexDuct(points, ductType)` | FlexDuct |
| `FlexPipe NewFlexPipe(Connector, Connector, FlexPipeType)` | `document.NewFlexPipe(connector1, connector2, pipeType)` | FlexPipe |
| `FlexPipe NewFlexPipe(Connector, IList<XYZ>, FlexPipeType)` | `document.NewFlexPipe(connector, points, pipeType)` | FlexPipe |
| `FlexPipe NewFlexPipe(IList<XYZ>, FlexPipeType)` | `document.NewFlexPipe(points, pipeType)` | FlexPipe |
| `FootPrintRoof NewFootPrintRoof(CurveArray, Level, RoofType, ModelCurveArray&)` | `document.NewFootPrintRoof(footPrint, level, roofType, footPrintToModelCurvesMapping)` | FootPrintRoof |
| `Gutter NewGutter(GutterType, Reference)` | `document.NewGutter(GutterType, reference)` | Gutter |
| `Gutter NewGutter(GutterType, ReferenceArray)` | `document.NewGutter(GutterType, references)` | Gutter |
| `BoundaryConditions NewLineBoundaryConditions(Element, TranslationRotationValue, Double, TranslationRotationValue, Double, TranslationRotationValue, Double, TranslationRotationValue, Double)` | `document.NewLineBoundaryConditions(hostElement, X_Translation, X_TranslationSpringModulus, Y_Translation, Y_TranslationSpringModulus, Z_Translation, Z_TranslationSpringModulus, X_Rotation, X_RotationSpringModulus)` | BoundaryConditions |
| `BoundaryConditions NewLineBoundaryConditions(Reference, TranslationRotationValue, Double, TranslationRotationValue, Double, TranslationRotationValue, Double, TranslationRotationValue, Double)` | `document.NewLineBoundaryConditions(reference, X_Translation, X_TranslationSpringModulus, Y_Translation, Y_TranslationSpringModulus, Z_Translation, Z_TranslationSpringModulus, X_Rotation, X_RotationSpringModulus)` | BoundaryConditions |
| `MechanicalSystem NewMechanicalSystem(Connector, ConnectorSet, DuctSystemType)` | `document.NewMechanicalSystem(baseEquipmentConnector, connectors, ductSystemType)` | MechanicalSystem |
| `Opening NewOpening(Element, CurveArray, Boolean)` | `document.NewOpening(hostElement, profile, bPerpendicularFace)` | Opening |
| `Opening NewOpening(Wall, XYZ, XYZ)` | `document.NewOpening(wall, pntStart, pntEnd)` | Opening |
| `Opening NewOpening(Level, Level, CurveArray)` | `document.NewOpening(bottomLevel, topLevel, profile)` | Opening |
| `Opening NewOpening(Element, CurveArray, eRefFace)` | `document.NewOpening(famInstElement, profile, iFace)` | Opening |
| `PipingSystem NewPipingSystem(Connector, ConnectorSet, PipeSystemType)` | `document.NewPipingSystem(baseEquipmentConnector, connectors, pipingSystemType)` | PipingSystem |
| `BoundaryConditions NewPointBoundaryConditions(Reference, TranslationRotationValue, Double, TranslationRotationValue, Double, TranslationRotationValue, Double, TranslationRotationValue, Double, TranslationRotationValue, Double, TranslationRotationValue, Double)` | `document.NewPointBoundaryConditions(reference, X_Translation, X_TranslationSpringModulus, Y_Translation, Y_TranslationSpringModulus, Z_Translation, Z_TranslationSpringModulus, X_Rotation, X_RotationSpringModulus, Y_Rotation, Y_RotationSpringModulus, Z_Rotation, Z_RotationSpringModulus)` | BoundaryConditions |
| `Room NewRoom(Room, PlanCircuit)` | `document.NewRoom(room, circuit)` | Room |
| `Room NewRoom(Phase)` | `document.NewRoom(phase)` | Room |
| `Room NewRoom(Level, UV)` | `document.NewRoom(level, point)` | Room |
| `ModelCurveArray NewRoomBoundaryLines(SketchPlane, CurveArray, View)` | `document.NewRoomBoundaryLines(sketchPlane, curves, view)` | ModelCurveArray |
| `ICollection<ElementId> NewRooms2(Phase, Int32)` | `document.NewRooms2(phase, count)` | ICollection<ElementId> |
| `ICollection<ElementId> NewRooms2(Level, Phase)` | `document.NewRooms2(level, phase)` | ICollection<ElementId> |
| `ICollection<ElementId> NewRooms2(Level)` | `document.NewRooms2(level)` | ICollection<ElementId> |
| `RoomTag NewRoomTag(LinkElementId, UV, ElementId)` | `document.NewRoomTag(roomId, point, viewId)` | RoomTag |
| `SlabEdge NewSlabEdge(SlabEdgeType, Reference)` | `document.NewSlabEdge(SlabEdgeType, reference)` | SlabEdge |
| `SlabEdge NewSlabEdge(SlabEdgeType, ReferenceArray)` | `document.NewSlabEdge(SlabEdgeType, references)` | SlabEdge |
| `Space NewSpace(Level, Phase, UV)` | `document.NewSpace(level, phase, point)` | Space |
| `Space NewSpace(Level, UV)` | `document.NewSpace(level, point)` | Space |
| `Space NewSpace(Phase)` | `document.NewSpace(phase)` | Space |
| `ModelCurveArray NewSpaceBoundaryLines(SketchPlane, CurveArray, View)` | `document.NewSpaceBoundaryLines(sketchPlane, curves, view)` | ModelCurveArray |
| `ICollection<ElementId> NewSpaces2(Phase, Int32)` | `document.NewSpaces2(phase, count)` | ICollection<ElementId> |
| `ICollection<ElementId> NewSpaces2(Level, Phase, View)` | `document.NewSpaces2(level, phase, view)` | ICollection<ElementId> |
| `SpaceTag NewSpaceTag(Space, UV, View)` | `document.NewSpaceTag(space, point, view)` | SpaceTag |
| `SpotDimension NewSpotCoordinate(View, Reference, XYZ, XYZ, XYZ, XYZ, Boolean)` | `document.NewSpotCoordinate(view, reference, origin, bend, end, refPt, hasLeader)` | SpotDimension |
| `SpotDimension NewSpotElevation(View, Reference, XYZ, XYZ, XYZ, XYZ, Boolean)` | `document.NewSpotElevation(view, reference, origin, bend, end, refPt, hasLeader)` | SpotDimension |
| `FamilyInstance NewTakeoffFitting(Connector, MEPCurve)` | `document.NewTakeoffFitting(connector, curve)` | FamilyInstance |
| `FamilyInstance NewTeeFitting(Connector, Connector, Connector)` | `document.NewTeeFitting(connector1, connector2, connector3)` | FamilyInstance |
| `FamilyInstance NewTransitionFitting(Connector, Connector)` | `document.NewTransitionFitting(connector1, connector2)` | FamilyInstance |
| `FamilyInstance NewUnionFitting(Connector, Connector)` | `document.NewUnionFitting(connector1, connector2)` | FamilyInstance |
| `Zone NewZone(Level, Phase)` | `document.NewZone(level, phase)` | Zone |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
