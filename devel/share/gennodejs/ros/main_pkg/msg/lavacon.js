// Auto-generated. Do not edit!

// (in-package main_pkg.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class lavacon {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.con_mid_X = null;
      this.con_mid_y = null;
      this.con_mid_z = null;
      this.con_name = null;
      this.con_color = null;
    }
    else {
      if (initObj.hasOwnProperty('con_mid_X')) {
        this.con_mid_X = initObj.con_mid_X
      }
      else {
        this.con_mid_X = 0.0;
      }
      if (initObj.hasOwnProperty('con_mid_y')) {
        this.con_mid_y = initObj.con_mid_y
      }
      else {
        this.con_mid_y = 0.0;
      }
      if (initObj.hasOwnProperty('con_mid_z')) {
        this.con_mid_z = initObj.con_mid_z
      }
      else {
        this.con_mid_z = 0.0;
      }
      if (initObj.hasOwnProperty('con_name')) {
        this.con_name = initObj.con_name
      }
      else {
        this.con_name = '';
      }
      if (initObj.hasOwnProperty('con_color')) {
        this.con_color = initObj.con_color
      }
      else {
        this.con_color = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type lavacon
    // Serialize message field [con_mid_X]
    bufferOffset = _serializer.float64(obj.con_mid_X, buffer, bufferOffset);
    // Serialize message field [con_mid_y]
    bufferOffset = _serializer.float64(obj.con_mid_y, buffer, bufferOffset);
    // Serialize message field [con_mid_z]
    bufferOffset = _serializer.float64(obj.con_mid_z, buffer, bufferOffset);
    // Serialize message field [con_name]
    bufferOffset = _serializer.string(obj.con_name, buffer, bufferOffset);
    // Serialize message field [con_color]
    bufferOffset = _serializer.string(obj.con_color, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type lavacon
    let len;
    let data = new lavacon(null);
    // Deserialize message field [con_mid_X]
    data.con_mid_X = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [con_mid_y]
    data.con_mid_y = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [con_mid_z]
    data.con_mid_z = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [con_name]
    data.con_name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [con_color]
    data.con_color = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.con_name);
    length += _getByteLength(object.con_color);
    return length + 32;
  }

  static datatype() {
    // Returns string type for a message object
    return 'main_pkg/lavacon';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd7d5d863398db1715dabc8c59e13dbfe';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 con_mid_X
    float64 con_mid_y
    float64 con_mid_z
    string con_name
    string con_color
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new lavacon(null);
    if (msg.con_mid_X !== undefined) {
      resolved.con_mid_X = msg.con_mid_X;
    }
    else {
      resolved.con_mid_X = 0.0
    }

    if (msg.con_mid_y !== undefined) {
      resolved.con_mid_y = msg.con_mid_y;
    }
    else {
      resolved.con_mid_y = 0.0
    }

    if (msg.con_mid_z !== undefined) {
      resolved.con_mid_z = msg.con_mid_z;
    }
    else {
      resolved.con_mid_z = 0.0
    }

    if (msg.con_name !== undefined) {
      resolved.con_name = msg.con_name;
    }
    else {
      resolved.con_name = ''
    }

    if (msg.con_color !== undefined) {
      resolved.con_color = msg.con_color;
    }
    else {
      resolved.con_color = ''
    }

    return resolved;
    }
};

module.exports = lavacon;
