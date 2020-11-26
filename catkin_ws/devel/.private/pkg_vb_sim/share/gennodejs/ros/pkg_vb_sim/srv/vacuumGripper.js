// Auto-generated. Do not edit!

// (in-package pkg_vb_sim.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class vacuumGripperRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.activate_vacuum_gripper = null;
    }
    else {
      if (initObj.hasOwnProperty('activate_vacuum_gripper')) {
        this.activate_vacuum_gripper = initObj.activate_vacuum_gripper
      }
      else {
        this.activate_vacuum_gripper = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type vacuumGripperRequest
    // Serialize message field [activate_vacuum_gripper]
    bufferOffset = _serializer.bool(obj.activate_vacuum_gripper, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type vacuumGripperRequest
    let len;
    let data = new vacuumGripperRequest(null);
    // Deserialize message field [activate_vacuum_gripper]
    data.activate_vacuum_gripper = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'pkg_vb_sim/vacuumGripperRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '751b0bcd7e7e984c5083f65904bb71f9';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool activate_vacuum_gripper
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new vacuumGripperRequest(null);
    if (msg.activate_vacuum_gripper !== undefined) {
      resolved.activate_vacuum_gripper = msg.activate_vacuum_gripper;
    }
    else {
      resolved.activate_vacuum_gripper = false
    }

    return resolved;
    }
};

class vacuumGripperResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.result = null;
    }
    else {
      if (initObj.hasOwnProperty('result')) {
        this.result = initObj.result
      }
      else {
        this.result = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type vacuumGripperResponse
    // Serialize message field [result]
    bufferOffset = _serializer.bool(obj.result, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type vacuumGripperResponse
    let len;
    let data = new vacuumGripperResponse(null);
    // Deserialize message field [result]
    data.result = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'pkg_vb_sim/vacuumGripperResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'eb13ac1f1354ccecb7941ee8fa2192e8';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool result
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new vacuumGripperResponse(null);
    if (msg.result !== undefined) {
      resolved.result = msg.result;
    }
    else {
      resolved.result = false
    }

    return resolved;
    }
};

module.exports = {
  Request: vacuumGripperRequest,
  Response: vacuumGripperResponse,
  md5sum() { return '22dce99b1d1e31fc9ba6b2faee126298'; },
  datatype() { return 'pkg_vb_sim/vacuumGripper'; }
};
