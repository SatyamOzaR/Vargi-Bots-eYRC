// Auto-generated. Do not edit!

// (in-package gazebo_conveyor.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class ConveyorBeltControlRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.power = null;
    }
    else {
      if (initObj.hasOwnProperty('power')) {
        this.power = initObj.power
      }
      else {
        this.power = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ConveyorBeltControlRequest
    // Serialize message field [power]
    bufferOffset = _serializer.float64(obj.power, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ConveyorBeltControlRequest
    let len;
    let data = new ConveyorBeltControlRequest(null);
    // Deserialize message field [power]
    data.power = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'gazebo_conveyor/ConveyorBeltControlRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'b61bda1d4e0075084b2082bebb59ea34';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # Conveyor belt control
    
    # desired conveyor belt power
    float64 power
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ConveyorBeltControlRequest(null);
    if (msg.power !== undefined) {
      resolved.power = msg.power;
    }
    else {
      resolved.power = 0.0
    }

    return resolved;
    }
};

class ConveyorBeltControlResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.success = null;
    }
    else {
      if (initObj.hasOwnProperty('success')) {
        this.success = initObj.success
      }
      else {
        this.success = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ConveyorBeltControlResponse
    // Serialize message field [success]
    bufferOffset = _serializer.bool(obj.success, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ConveyorBeltControlResponse
    let len;
    let data = new ConveyorBeltControlResponse(null);
    // Deserialize message field [success]
    data.success = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'gazebo_conveyor/ConveyorBeltControlResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '358e233cde0c8a8bcfea4ce193f8fc15';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool success
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ConveyorBeltControlResponse(null);
    if (msg.success !== undefined) {
      resolved.success = msg.success;
    }
    else {
      resolved.success = false
    }

    return resolved;
    }
};

module.exports = {
  Request: ConveyorBeltControlRequest,
  Response: ConveyorBeltControlResponse,
  md5sum() { return '8b0e8e2d213d4fc4d0fcb5152aec2d9d'; },
  datatype() { return 'gazebo_conveyor/ConveyorBeltControl'; }
};
