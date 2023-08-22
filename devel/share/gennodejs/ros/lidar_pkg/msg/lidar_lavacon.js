// Auto-generated. Do not edit!

// (in-package lidar_pkg.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class lidar_lavacon {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.lidar_mid_X = null;
      this.lidar_mid_y = null;
      this.lidar_mid_z = null;
      this.lidar_con_name = null;
      this.lidar_con_color = null;
    }
    else {
      if (initObj.hasOwnProperty('lidar_mid_X')) {
        this.lidar_mid_X = initObj.lidar_mid_X
      }
      else {
        this.lidar_mid_X = 0.0;
      }
      if (initObj.hasOwnProperty('lidar_mid_y')) {
        this.lidar_mid_y = initObj.lidar_mid_y
      }
      else {
        this.lidar_mid_y = 0.0;
      }
      if (initObj.hasOwnProperty('lidar_mid_z')) {
        this.lidar_mid_z = initObj.lidar_mid_z
      }
      else {
        this.lidar_mid_z = 0.0;
      }
      if (initObj.hasOwnProperty('lidar_con_name')) {
        this.lidar_con_name = initObj.lidar_con_name
      }
      else {
        this.lidar_con_name = '';
      }
      if (initObj.hasOwnProperty('lidar_con_color')) {
        this.lidar_con_color = initObj.lidar_con_color
      }
      else {
        this.lidar_con_color = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type lidar_lavacon
    // Serialize message field [lidar_mid_X]
    bufferOffset = _serializer.float64(obj.lidar_mid_X, buffer, bufferOffset);
    // Serialize message field [lidar_mid_y]
    bufferOffset = _serializer.float64(obj.lidar_mid_y, buffer, bufferOffset);
    // Serialize message field [lidar_mid_z]
    bufferOffset = _serializer.float64(obj.lidar_mid_z, buffer, bufferOffset);
    // Serialize message field [lidar_con_name]
    bufferOffset = _serializer.string(obj.lidar_con_name, buffer, bufferOffset);
    // Serialize message field [lidar_con_color]
    bufferOffset = _serializer.string(obj.lidar_con_color, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type lidar_lavacon
    let len;
    let data = new lidar_lavacon(null);
    // Deserialize message field [lidar_mid_X]
    data.lidar_mid_X = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [lidar_mid_y]
    data.lidar_mid_y = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [lidar_mid_z]
    data.lidar_mid_z = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [lidar_con_name]
    data.lidar_con_name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [lidar_con_color]
    data.lidar_con_color = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.lidar_con_name);
    length += _getByteLength(object.lidar_con_color);
    return length + 32;
  }

  static datatype() {
    // Returns string type for a message object
    return 'lidar_pkg/lidar_lavacon';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '8869dac3714f40275d5d1c09afbfd6f5';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 lidar_mid_X
    float64 lidar_mid_y
    float64 lidar_mid_z
    string lidar_con_name
    string lidar_con_color
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new lidar_lavacon(null);
    if (msg.lidar_mid_X !== undefined) {
      resolved.lidar_mid_X = msg.lidar_mid_X;
    }
    else {
      resolved.lidar_mid_X = 0.0
    }

    if (msg.lidar_mid_y !== undefined) {
      resolved.lidar_mid_y = msg.lidar_mid_y;
    }
    else {
      resolved.lidar_mid_y = 0.0
    }

    if (msg.lidar_mid_z !== undefined) {
      resolved.lidar_mid_z = msg.lidar_mid_z;
    }
    else {
      resolved.lidar_mid_z = 0.0
    }

    if (msg.lidar_con_name !== undefined) {
      resolved.lidar_con_name = msg.lidar_con_name;
    }
    else {
      resolved.lidar_con_name = ''
    }

    if (msg.lidar_con_color !== undefined) {
      resolved.lidar_con_color = msg.lidar_con_color;
    }
    else {
      resolved.lidar_con_color = ''
    }

    return resolved;
    }
};

module.exports = lidar_lavacon;
