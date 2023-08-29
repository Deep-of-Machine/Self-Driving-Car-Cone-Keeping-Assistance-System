// Auto-generated. Do not edit!

// (in-package iahrs_driver.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class euler_angle_initRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type euler_angle_initRequest
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type euler_angle_initRequest
    let len;
    let data = new euler_angle_initRequest(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a service object
    return 'iahrs_driver/euler_angle_initRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd41d8cd98f00b204e9800998ecf8427e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    #This message is used to send command to IAHRS(IMU)
    #Euler_angle_init command
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new euler_angle_initRequest(null);
    return resolved;
    }
};

class euler_angle_initResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.command_Result = null;
    }
    else {
      if (initObj.hasOwnProperty('command_Result')) {
        this.command_Result = initObj.command_Result
      }
      else {
        this.command_Result = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type euler_angle_initResponse
    // Serialize message field [command_Result]
    bufferOffset = _serializer.bool(obj.command_Result, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type euler_angle_initResponse
    let len;
    let data = new euler_angle_initResponse(null);
    // Deserialize message field [command_Result]
    data.command_Result = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'iahrs_driver/euler_angle_initResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '6b370111df6d9d8116fbdd43bd394a52';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool command_Result
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new euler_angle_initResponse(null);
    if (msg.command_Result !== undefined) {
      resolved.command_Result = msg.command_Result;
    }
    else {
      resolved.command_Result = false
    }

    return resolved;
    }
};

module.exports = {
  Request: euler_angle_initRequest,
  Response: euler_angle_initResponse,
  md5sum() { return '6b370111df6d9d8116fbdd43bd394a52'; },
  datatype() { return 'iahrs_driver/euler_angle_init'; }
};
