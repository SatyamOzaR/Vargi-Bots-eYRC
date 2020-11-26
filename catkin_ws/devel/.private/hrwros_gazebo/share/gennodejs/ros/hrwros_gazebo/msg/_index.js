
"use strict";

let VacuumGripperState = require('./VacuumGripperState.js');
let PopulationState = require('./PopulationState.js');
let LogicalCameraImage = require('./LogicalCameraImage.js');
let ConveyorBeltState = require('./ConveyorBeltState.js');
let KitObject = require('./KitObject.js');
let DetectedObject = require('./DetectedObject.js');
let StorageUnit = require('./StorageUnit.js');
let Kit = require('./Kit.js');
let KitTray = require('./KitTray.js');
let Proximity = require('./Proximity.js');
let Order = require('./Order.js');
let Model = require('./Model.js');
let TrayContents = require('./TrayContents.js');

module.exports = {
  VacuumGripperState: VacuumGripperState,
  PopulationState: PopulationState,
  LogicalCameraImage: LogicalCameraImage,
  ConveyorBeltState: ConveyorBeltState,
  KitObject: KitObject,
  DetectedObject: DetectedObject,
  StorageUnit: StorageUnit,
  Kit: Kit,
  KitTray: KitTray,
  Proximity: Proximity,
  Order: Order,
  Model: Model,
  TrayContents: TrayContents,
};
