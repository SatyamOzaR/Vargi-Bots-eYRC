// Auto-generated. Do not edit!

// (in-package pkg_task1.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class msgTurtleFeedback {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.cur_x = null;
      this.cur_y = null;
      this.cur_theta = null;
    }
    else {
      if (initObj.hasOwnProperty('cur_x')) {
        this.cur_x = initObj.cur_x
      }
      else {
        this.cur_x = 0;
      }
      if (initObj.hasOwnProperty('cur_y')) {
        this.cur_y = initObj.cur_y
      }
      else {
        this.cur_y = 0;
      }
      if (initObj.hasOwnProperty('cur_theta')) {
        this.cur_theta = initObj.cur_theta
      }
      else {
        this.cur_theta = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type msgTurtleFeedback
    // Serialize message field [cur_x]
    bufferOffset = _serializer.int8(obj.cur_x, buffer, bufferOffset);
    // Serialize message field [cur_y]
    bufferOffset = _serializer.int8(obj.cur_y, buffer, bufferOffset);
    // Serialize message field [cur_theta]
    bufferOffset = _serializer.int8(obj.cur_theta, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type msgTurtleFeedback
    let len;
    let data = new msgTurtleFeedback(null);
    // Deserialize message field [cur_x]
    data.cur_x = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [cur_y]
    data.cur_y = _deserializer.int8(buffer, bufferOffset);
    // Deserialize message field [cur_theta]
    data.cur_theta = _deserializer.int8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 3;
  }

  static datatype() {
    // Returns string type for a message object
    return 'pkg_task1/msgTurtleFeedback';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '0a9172acbd2d788295bb9e44c2e2758a';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
    
    int8 cur_x
    int8 cur_y
    int8 cur_theta
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new msgTurtleFeedback(null);
    if (msg.cur_x !== undefined) {
      resolved.cur_x = msg.cur_x;
    }
    else {
      resolved.cur_x = 0
    }

    if (msg.cur_y !== undefined) {
      resolved.cur_y = msg.cur_y;
    }
    else {
      resolved.cur_y = 0
    }

    if (msg.cur_theta !== undefined) {
      resolved.cur_theta = msg.cur_theta;
    }
    else {
      resolved.cur_theta = 0
    }

    return resolved;
    }
};

module.exports = msgTurtleFeedback;
