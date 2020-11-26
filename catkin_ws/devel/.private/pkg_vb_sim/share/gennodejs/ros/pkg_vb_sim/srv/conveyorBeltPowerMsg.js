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

class conveyorBeltPowerMsgRequest {
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
        this.power = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type conveyorBeltPowerMsgRequest
    // Serialize message field [power]
    bufferOffset = _serializer.int8(obj.power, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type conveyorBeltPowerMsgRequest
    let len;
    let data = new conveyorBeltPowerMsgRequest(null);
    // Deserialize message field [power]
    data.power = _deserializer.int8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'pkg_vb_sim/conveyorBeltPowerMsgRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'cb865fe69e245bdfa52dafc5c79743f2';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int8 power
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new conveyorBeltPowerMsgRequest(null);
    if (msg.power !== undefined) {
      resolved.power = msg.power;
    }
    else {
      resolved.power = 0
    }

    return resolved;
    }
};

class conveyorBeltPowerMsgResponse {
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
    // Serializes a message object of type conveyorBeltPowerMsgResponse
    // Serialize message field [result]
    bufferOffset = _serializer.bool(obj.result, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type conveyorBeltPowerMsgResponse
    let len;
    let data = new conveyorBeltPowerMsgResponse(null);
    // Deserialize message field [result]
    data.result = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'pkg_vb_sim/conveyorBeltPowerMsgResponse';
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
    const resolved = new conveyorBeltPowerMsgResponse(null);
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
  Request: conveyorBeltPowerMsgRequest,
  Response: conveyorBeltPowerMsgResponse,
  md5sum() { return '734278aaf6d621cbe98c5cbee4553347'; },
  datatype() { return 'pkg_vb_sim/conveyorBeltPowerMsg'; }
};
