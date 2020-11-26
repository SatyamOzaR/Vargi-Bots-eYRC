// Auto-generated. Do not edit!

// (in-package gazebo_conveyor.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class ConveyorBeltState {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.power = null;
      this.enabled = null;
    }
    else {
      if (initObj.hasOwnProperty('power')) {
        this.power = initObj.power
      }
      else {
        this.power = 0.0;
      }
      if (initObj.hasOwnProperty('enabled')) {
        this.enabled = initObj.enabled
      }
      else {
        this.enabled = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ConveyorBeltState
    // Serialize message field [power]
    bufferOffset = _serializer.float64(obj.power, buffer, bufferOffset);
    // Serialize message field [enabled]
    bufferOffset = _serializer.bool(obj.enabled, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ConveyorBeltState
    let len;
    let data = new ConveyorBeltState(null);
    // Deserialize message field [power]
    data.power = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [enabled]
    data.enabled = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 9;
  }

  static datatype() {
    // Returns string type for a message object
    return 'gazebo_conveyor/ConveyorBeltState';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c0b232b8dd148cb7c71d4df1ea72012c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # Conveyor belt state message
    float64 power  # power of the belt (percentage, in +Y direction of belt frame)
    bool enabled  # true if the power of the belt can be modified; false if the belt is stopped
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ConveyorBeltState(null);
    if (msg.power !== undefined) {
      resolved.power = msg.power;
    }
    else {
      resolved.power = 0.0
    }

    if (msg.enabled !== undefined) {
      resolved.enabled = msg.enabled;
    }
    else {
      resolved.enabled = false
    }

    return resolved;
    }
};

module.exports = ConveyorBeltState;
