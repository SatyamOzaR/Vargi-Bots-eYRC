
"use strict";

let VacuumGripperControl = require('./VacuumGripperControl.js')
let SubmitTray = require('./SubmitTray.js')
let PopulationControl = require('./PopulationControl.js')
let AGVControl = require('./AGVControl.js')
let GetMaterialLocations = require('./GetMaterialLocations.js')
let ConveyorBeltControl = require('./ConveyorBeltControl.js')

module.exports = {
  VacuumGripperControl: VacuumGripperControl,
  SubmitTray: SubmitTray,
  PopulationControl: PopulationControl,
  AGVControl: AGVControl,
  GetMaterialLocations: GetMaterialLocations,
  ConveyorBeltControl: ConveyorBeltControl,
};
