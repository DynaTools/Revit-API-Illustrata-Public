---
title: View
classe: Autodesk.Revit.DB.View
namespace: Autodesk.Revit.DB
eredita: Autodesk.Revit.DB.Element
revit: "2025"
revitapi: "25.4.30.0"
stato: auto
verbo: leggere
membri_n: 140
---

# View

!!! note "Scheda automatica"
    La corrispondenza C#→Python è generata dalle 7 Regole. Descrizione, tranello ed esempio sono **da rivedere** — [contribuisci](https://github.com/DynaTools/Revit-API-Illustrata-Public).

## La classe

_(una frase: cos'è e a cosa serve)_

## La corrispondenza

| nella doc (C#) | in python | tipo |
|---|---|---|
| `ElementId AnalysisDisplayStyleId { get; set; }` | `view.AnalysisDisplayStyleId` | ElementId |
| `Boolean AreAnalyticalModelCategoriesHidden { get; set; }` | `view.AreAnalyticalModelCategoriesHidden` | Boolean |
| `Boolean AreAnnotationCategoriesHidden { get; set; }` | `view.AreAnnotationCategoriesHidden` | Boolean |
| `Boolean AreCoordinationModelHandlesHidden { get; set; }` | `view.AreCoordinationModelHandlesHidden` | Boolean |
| `Boolean AreImportCategoriesHidden { get; set; }` | `view.AreImportCategoriesHidden` | Boolean |
| `Boolean AreModelCategoriesHidden { get; set; }` | `view.AreModelCategoriesHidden` | Boolean |
| `Boolean ArePointCloudsHidden { get; set; }` | `view.ArePointCloudsHidden` | Boolean |
| `ElementId AssociatedAssemblyInstanceId { get; }` | `view.AssociatedAssemblyInstanceId` | ElementId |
| `Boolean CanBePrinted { get; }` | `view.CanBePrinted` | Boolean |
| `BoundingBoxXYZ CropBox { get; set; }` | `view.CropBox` | BoundingBoxXYZ |
| `Boolean CropBoxActive { get; set; }` | `view.CropBoxActive` | Boolean |
| `Boolean CropBoxVisible { get; set; }` | `view.CropBoxVisible` | Boolean |
| `ViewDetailLevel DetailLevel { get; set; }` | `view.DetailLevel` | ViewDetailLevel |
| `ViewDiscipline Discipline { get; set; }` | `view.Discipline` | ViewDiscipline |
| `DisplayStyle DisplayStyle { get; set; }` | `view.DisplayStyle` | DisplayStyle |
| `Level GenLevel { get; }` | `view.GenLevel` | Level |
| `Boolean IsAssemblyView { get; }` | `view.IsAssemblyView` | Boolean |
| `Boolean IsCallout { get; }` | `view.IsCallout` | Boolean |
| `Boolean IsTemplate { get; }` | `view.IsTemplate` | Boolean |
| `XYZ Origin { get; }` | `view.Origin` | XYZ |
| `BoundingBoxUV Outline { get; }` | `view.Outline` | BoundingBoxUV |
| `PartsVisibility PartsVisibility { get; set; }` | `view.PartsVisibility` | PartsVisibility |
| `Boolean RevealConstraintsMode { get; set; }` | `view.RevealConstraintsMode` | Boolean |
| `XYZ RightDirection { get; }` | `view.RightDirection` | XYZ |
| `Int32 Scale { get; set; }` | `view.Scale` | Int32 |
| `Int32 ShadowIntensity { get; set; }` | `view.ShadowIntensity` | Int32 |
| `SketchPlane SketchPlane { get; set; }` | `view.SketchPlane` | SketchPlane |
| `SunAndShadowSettings SunAndShadowSettings { get; }` | `view.SunAndShadowSettings` | SunAndShadowSettings |
| `Int32 SunlightIntensity { get; set; }` | `view.SunlightIntensity` | Int32 |
| `TemporaryViewModes TemporaryViewModes { get; }` | `view.TemporaryViewModes` | TemporaryViewModes |
| `String Title { get; }` | `view.Title` | String |
| `XYZ UpDirection { get; }` | `view.UpDirection` | XYZ |
| `XYZ ViewDirection { get; }` | `view.ViewDirection` | XYZ |
| `ElementId ViewTemplateId { get; set; }` | `view.ViewTemplateId` | ElementId |
| `ViewType ViewType { get; }` | `view.ViewType` | ViewType |
| `Void AddFilter(ElementId)` | `view.AddFilter(filterElementId)` | Void |
| `Boolean AllowsAnalysisDisplay()` | `view.AllowsAnalysisDisplay()` | Boolean |
| `Void ApplyViewTemplateParameters(View)` | `view.ApplyViewTemplateParameters(otherView)` | Void |
| `Boolean AreGraphicsOverridesAllowed()` | `view.AreGraphicsOverridesAllowed()` | Boolean |
| `Boolean CanApplyColorFillScheme(ElementId, ElementId)` | `view.CanApplyColorFillScheme(categoryId, schemeId)` | Boolean |
| `Boolean CanCategoryBeHidden(ElementId)` | `view.CanCategoryBeHidden(elementId)` | Boolean |
| `Boolean CanCategoryBeHiddenTemporary(ElementId)` | `view.CanCategoryBeHiddenTemporary(elementId)` | Boolean |
| `Boolean CanEnableTemporaryViewPropertiesMode()` | `view.CanEnableTemporaryViewPropertiesMode()` | Boolean |
| `Boolean CanModifyDetailLevel()` | `view.CanModifyDetailLevel()` | Boolean |
| `Boolean CanModifyDisplayStyle()` | `view.CanModifyDisplayStyle()` | Boolean |
| `Boolean CanModifyViewDiscipline()` | `view.CanModifyViewDiscipline()` | Boolean |
| `Boolean CanUseDepthCueing()` | `view.CanUseDepthCueing()` | Boolean |
| `Boolean CanUseTemporaryVisibilityModes()` | `view.CanUseTemporaryVisibilityModes()` | Boolean |
| `Boolean CanViewBeDuplicated(ViewDuplicateOption)` | `view.CanViewBeDuplicated(duplicateOption)` | Boolean |
| `Void ConvertTemporaryHideIsolateToPermanent()` | `view.ConvertTemporaryHideIsolateToPermanent()` | Void |
| `Void ConvertToIndependent()` | `view.ConvertToIndependent()` | Void |
| `View CreateViewTemplate()` | `view.CreateViewTemplate()` | View |
| `Void DisableTemporaryViewMode(TemporaryViewMode)` | `view.DisableTemporaryViewMode(mode)` | Void |
| `ElementId Duplicate(ViewDuplicateOption)` | `view.Duplicate(duplicateOption)` | ElementId |
| `Void EnableRevealHiddenMode()` | `view.EnableRevealHiddenMode()` | Void |
| `Boolean EnableTemporaryViewPropertiesMode(ElementId)` | `view.EnableTemporaryViewPropertiesMode(viewTemplateId)` | Boolean |
| `ViewDisplayBackground GetBackground()` | `view.GetBackground()` | ViewDisplayBackground |
| `ElementId GetCalloutParentId()` | `view.GetCalloutParentId()` | ElementId |
| `Boolean GetCategoryHidden(ElementId)` | `view.GetCategoryHidden(categoryId)` | Boolean |
| `OverrideGraphicSettings GetCategoryOverrides(ElementId)` | `view.GetCategoryOverrides(categoryId)` | OverrideGraphicSettings |
| `ElementId GetColorFillSchemeId(ElementId)` | `view.GetColorFillSchemeId(categoryId)` | ElementId |
| `ViewCropRegionShapeManager GetCropRegionShapeManager()` | `view.GetCropRegionShapeManager()` | ViewCropRegionShapeManager |
| `ViewCropRegionShapeManager GetCropRegionShapeManagerForReferenceCallout(Document, ElementId)` | `View.GetCropRegionShapeManagerForReferenceCallout(doc, callout)` | ViewCropRegionShapeManager |
| `ICollection<ElementId> GetDependentViewIds()` | `view.GetDependentViewIds()` | ICollection<ElementId> |
| `ViewDisplayDepthCueing GetDepthCueing()` | `view.GetDepthCueing()` | ViewDisplayDepthCueing |
| `DirectContext3DHandleOverrides GetDirectContext3DHandleOverrides()` | `view.GetDirectContext3DHandleOverrides()` | DirectContext3DHandleOverrides |
| `OverrideGraphicSettings GetElementOverrides(ElementId)` | `view.GetElementOverrides(elementId)` | OverrideGraphicSettings |
| `OverrideGraphicSettings GetFilterOverrides(ElementId)` | `view.GetFilterOverrides(filterElementId)` | OverrideGraphicSettings |
| `ICollection<ElementId> GetFilters()` | `view.GetFilters()` | ICollection<ElementId> |
| `Boolean GetFilterVisibility(ElementId)` | `view.GetFilterVisibility(filterElementId)` | Boolean |
| `Boolean GetIsFilterEnabled(ElementId)` | `view.GetIsFilterEnabled(filterElementId)` | Boolean |
| `RevitLinkGraphicsSettings GetLinkOverrides(ElementId)` | `view.GetLinkOverrides(linkId)` | RevitLinkGraphicsSettings |
| `IList<TransformWithBoundary> GetModelToProjectionTransforms()` | `view.GetModelToProjectionTransforms()` | IList<TransformWithBoundary> |
| `ICollection<ElementId> GetNonControlledTemplateParameterIds()` | `view.GetNonControlledTemplateParameterIds()` | ICollection<ElementId> |
| `IList<ElementId> GetOrderedFilters()` | `view.GetOrderedFilters()` | IList<ElementId> |
| `ViewPlacementOnSheetStatus GetPlacementOnSheetStatus()` | `view.GetPlacementOnSheetStatus()` | ViewPlacementOnSheetStatus |
| `PointCloudOverrides GetPointCloudOverrides()` | `view.GetPointCloudOverrides()` | PointCloudOverrides |
| `ElementId GetPrimaryViewId()` | `view.GetPrimaryViewId()` | ElementId |
| `ICollection<ElementId> GetReferenceCallouts()` | `view.GetReferenceCallouts()` | ICollection<ElementId> |
| `ICollection<ElementId> GetReferenceElevations()` | `view.GetReferenceElevations()` | ICollection<ElementId> |
| `ICollection<ElementId> GetReferenceSections()` | `view.GetReferenceSections()` | ICollection<ElementId> |
| `ViewDisplaySketchyLines GetSketchyLines()` | `view.GetSketchyLines()` | ViewDisplaySketchyLines |
| `IList<ElementId> GetTemplateParameterIds()` | `view.GetTemplateParameterIds()` | IList<ElementId> |
| `ElementId GetTemporaryViewPropertiesId()` | `view.GetTemporaryViewPropertiesId()` | ElementId |
| `String GetTemporaryViewPropertiesName()` | `view.GetTemporaryViewPropertiesName()` | String |
| `ViewDisplayModel GetViewDisplayModel()` | `view.GetViewDisplayModel()` | ViewDisplayModel |
| `WorksetVisibility GetWorksetVisibility(WorksetId)` | `view.GetWorksetVisibility(worksetId)` | WorksetVisibility |
| `WorksharingDisplayMode GetWorksharingDisplayMode()` | `view.GetWorksharingDisplayMode()` | WorksharingDisplayMode |
| `Boolean HasDetailLevel()` | `view.HasDetailLevel()` | Boolean |
| `Boolean HasDisplayStyle()` | `view.HasDisplayStyle()` | Boolean |
| `Boolean HasViewDiscipline()` | `view.HasViewDiscipline()` | Boolean |
| `Boolean HasViewTransforms()` | `view.HasViewTransforms()` | Boolean |
| `Void HideActiveWorkPlane()` | `view.HideActiveWorkPlane()` | Void |
| `Void HideCategoriesTemporary(ICollection<ElementId>)` | `view.HideCategoriesTemporary(elementIds)` | Void |
| `Void HideCategoryTemporary(ElementId)` | `view.HideCategoryTemporary(elementId)` | Void |
| `Void HideElements(ICollection<ElementId>)` | `view.HideElements(elementIdSet)` | Void |
| `Void HideElementsTemporary(ICollection<ElementId>)` | `view.HideElementsTemporary(elementIdSet)` | Void |
| `Void HideElementTemporary(ElementId)` | `view.HideElementTemporary(elementId)` | Void |
| `Boolean IsCategoryOverridable(ElementId)` | `view.IsCategoryOverridable(categoryId)` | Boolean |
| `Boolean IsElementVisibleInTemporaryViewMode(TemporaryViewMode, ElementId)` | `view.IsElementVisibleInTemporaryViewMode(mode, id)` | Boolean |
| `Boolean IsFilterApplied(ElementId)` | `view.IsFilterApplied(filterElementId)` | Boolean |
| `Boolean IsInTemporaryViewMode(TemporaryViewMode)` | `view.IsInTemporaryViewMode(mode)` | Boolean |
| `Void IsolateCategoriesTemporary(ICollection<ElementId>)` | `view.IsolateCategoriesTemporary(elementIds)` | Void |
| `Void IsolateCategoryTemporary(ElementId)` | `view.IsolateCategoryTemporary(elementId)` | Void |
| `Void IsolateElementsTemporary(ICollection<ElementId>)` | `view.IsolateElementsTemporary(elementIds)` | Void |
| `Void IsolateElementTemporary(ElementId)` | `view.IsolateElementTemporary(elementId)` | Void |
| `Boolean IsTemporaryHideIsolateActive()` | `view.IsTemporaryHideIsolateActive()` | Boolean |
| `Boolean IsTemporaryViewPropertiesModeEnabled()` | `view.IsTemporaryViewPropertiesModeEnabled()` | Boolean |
| `Boolean IsValidViewScale(Int32)` | `View.IsValidViewScale(viewScale)` | Boolean |
| `Boolean IsValidViewTemplate(ElementId)` | `view.IsValidViewTemplate(templateId)` | Boolean |
| `Boolean IsViewValidForTemplateCreation()` | `view.IsViewValidForTemplateCreation()` | Boolean |
| `Boolean IsWorksetVisible(WorksetId)` | `view.IsWorksetVisible(worksetId)` | Boolean |
| `Void Print(View)` | `view.Print(viewTemplate)` | Void |
| `Void Print()` | `view.Print()` | Void |
| `Void Print(View, Boolean)` | `view.Print(viewTemplate, useCurrentPrintSettings)` | Void |
| `Void Print(Boolean)` | `view.Print(useCurrentPrintSettings)` | Void |
| `Void RemoveCalloutParent()` | `view.RemoveCalloutParent()` | Void |
| `Void RemoveFilter(ElementId)` | `view.RemoveFilter(filterElementId)` | Void |
| `Void RemoveLinkOverrides(ElementId)` | `view.RemoveLinkOverrides(linkId)` | Void |
| `Void RestoreCalloutParent()` | `view.RestoreCalloutParent()` | Void |
| `Void SetBackground(ViewDisplayBackground)` | `view.SetBackground(background)` | Void |
| `Void SetCategoryHidden(ElementId, Boolean)` | `view.SetCategoryHidden(categoryId, hide)` | Void |
| `Void SetCategoryOverrides(ElementId, OverrideGraphicSettings)` | `view.SetCategoryOverrides(categoryId, overrideGraphicSettings)` | Void |
| `Void SetColorFillSchemeId(ElementId, ElementId)` | `view.SetColorFillSchemeId(categoryId, schemeId)` | Void |
| `Void SetDepthCueing(ViewDisplayDepthCueing)` | `view.SetDepthCueing(depthCueing)` | Void |
| `Void SetElementOverrides(ElementId, OverrideGraphicSettings)` | `view.SetElementOverrides(elementId, overrideGraphicSettings)` | Void |
| `Void SetFilterOverrides(ElementId, OverrideGraphicSettings)` | `view.SetFilterOverrides(filterElementId, overrideGraphicSettings)` | Void |
| `Void SetFilterVisibility(ElementId, Boolean)` | `view.SetFilterVisibility(filterElementId, visibility)` | Void |
| `Void SetIsFilterEnabled(ElementId, Boolean)` | `view.SetIsFilterEnabled(filterElementId, enable)` | Void |
| `Void SetLinkOverrides(ElementId, RevitLinkGraphicsSettings)` | `view.SetLinkOverrides(linkId, linkDisplaySettings)` | Void |
| `Void SetNonControlledTemplateParameterIds(ICollection<ElementId>)` | `view.SetNonControlledTemplateParameterIds(newSet)` | Void |
| `Void SetSketchyLines(ViewDisplaySketchyLines)` | `view.SetSketchyLines(sketchyLines)` | Void |
| `Void SetViewDisplayModel(ViewDisplayModel)` | `view.SetViewDisplayModel(viewDisplayModel)` | Void |
| `Void SetWorksetVisibility(WorksetId, WorksetVisibility)` | `view.SetWorksetVisibility(worksetId, visible)` | Void |
| `Void SetWorksharingDisplayMode(WorksharingDisplayMode)` | `view.SetWorksharingDisplayMode(displayMode)` | Void |
| `Void ShowActiveWorkPlane()` | `view.ShowActiveWorkPlane()` | Void |
| `ICollection<ElementId> SupportedColorFillCategoryIds()` | `view.SupportedColorFillCategoryIds()` | ICollection<ElementId> |
| `Boolean SupportsRevealConstraints()` | `view.SupportsRevealConstraints()` | Boolean |
| `Boolean SupportsWorksharingDisplayMode(WorksharingDisplayMode)` | `view.SupportsWorksharingDisplayMode(mode)` | Boolean |
| `Void UnhideElements(ICollection<ElementId>)` | `view.UnhideElements(elementIdSet)` | Void |

## Il tranello

_(ciò che la pagina non dice e ti farebbe sbagliare)_

## Lo script

```python
# esempio da completare
```
