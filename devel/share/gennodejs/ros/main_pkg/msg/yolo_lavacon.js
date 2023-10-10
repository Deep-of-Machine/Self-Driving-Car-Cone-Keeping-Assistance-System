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

class yolo_lavacon {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.yolo_mid_X = null;
      this.yolo_mid_y = null;
      this.yolo_con_name = null;
      this.yolo_con_color = null;
    }
    else {
      if (initObj.hasOwnProperty('yolo_mid_X')) {
        this.yolo_mid_X = initObj.yolo_mid_X
      }
      else {
        this.yolo_mid_X = 0.0;
      }
      if (initObj.hasOwnProperty('yolo_mid_y')) {
        this.yolo_mid_y = initObj.yolo_mid_y
      }
      else {
        this.yolo_mid_y = 0.0;
      }
      if (initObj.hasOwnProperty('yolo_con_name')) {
        this.yolo_con_name = initObj.yolo_con_name
      }
      else {
        this.yolo_con_name = '';
      }
      if (initObj.hasOwnProperty('yolo_con_color')) {
        this.yolo_con_color = initObj.yolo_con_color
      }
      else {
        this.yolo_con_color = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type yolo_lavacon
    // Serialize message field [yolo_mid_X]
    bufferOffset = _serializer.float64(obj.yolo_mid_X, buffer, bufferOffset);
    // Serialize message field [yolo_mid_y]
    bufferOffset = _serializer.float64(obj.yolo_mid_y, buffer, bufferOffset);
    // Serialize message field [yolo_con_name]
    bufferOffset = _serializer.string(obj.yolo_con_name, buffer, bufferOffset);
    // Serialize message field [yolo_con_color]
    bufferOffset = _serializer.string(obj.yolo_con_color, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type yolo_lavacon
    let len;
    let data = new yolo_lavacon(null);
    // Deserialize message field [yolo_mid_X]
    data.yolo_mid_X = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [yolo_mid_y]
    data.yolo_mid_y = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [yolo_con_name]
    data.yolo_con_name = _deserializer.string(buffer, bufferOffset);
    // Deserialize message field [yolo_con_color]
    data.yolo_con_color = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += _getByteLength(object.yolo_con_name);
    length += _getByteLength(object.yolo_con_color);
    return length + 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'main_pkg/yolo_lavacon';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'da269e966072bed82c14a04982ff80e5';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 yolo_mid_X
    float64 yolo_mid_y
    string yolo_con_name
    string yolo_con_color
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new yolo_lavacon(null);
    if (msg.yolo_mid_X !== undefined) {
      resolved.yolo_mid_X = msg.yolo_mid_X;
    }
    else {
      resolved.yolo_mid_X = 0.0
    }

    if (msg.yolo_mid_y !== undefined) {
      resolved.yolo_mid_y = msg.yolo_mid_y;
    }
    else {
      resolved.yolo_mid_y = 0.0
    }

    if (msg.yolo_con_name !== undefined) {
      resolved.yolo_con_name = msg.yolo_con_name;
    }
    else {
      resolved.yolo_con_name = ''
    }

    if (msg.yolo_con_color !== undefined) {
      resolved.yolo_con_color = msg.yolo_con_color;
    }
    else {
      resolved.yolo_con_color = ''
    }

    return resolved;
    }
};

module.exports = yolo_lavacon;
