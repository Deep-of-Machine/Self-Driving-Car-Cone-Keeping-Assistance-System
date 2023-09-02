
"use strict";

let NavTIMEUTC = require('./NavTIMEUTC.js');
let NavHPPOSLLH = require('./NavHPPOSLLH.js');
let RxmRAWX = require('./RxmRAWX.js');
let NavSAT = require('./NavSAT.js');
let NavSTATUS = require('./NavSTATUS.js');
let MgaGAL = require('./MgaGAL.js');
let NavVELNED = require('./NavVELNED.js');
let CfgINF = require('./CfgINF.js');
let NavPVT7 = require('./NavPVT7.js');
let NavRELPOSNED = require('./NavRELPOSNED.js');
let TimTM2 = require('./TimTM2.js');
let UpdSOS = require('./UpdSOS.js');
let NavVELECEF = require('./NavVELECEF.js');
let NavSOL = require('./NavSOL.js');
let CfgANT = require('./CfgANT.js');
let NavTIMEGPS = require('./NavTIMEGPS.js');
let MonVER = require('./MonVER.js');
let Inf = require('./Inf.js');
let EsfRAW_Block = require('./EsfRAW_Block.js');
let MonHW6 = require('./MonHW6.js');
let NavSBAS = require('./NavSBAS.js');
let CfgDGNSS = require('./CfgDGNSS.js');
let EsfALG = require('./EsfALG.js');
let CfgCFG = require('./CfgCFG.js');
let CfgTMODE3 = require('./CfgTMODE3.js');
let CfgNAV5 = require('./CfgNAV5.js');
let RxmSVSI_SV = require('./RxmSVSI_SV.js');
let CfgNMEA = require('./CfgNMEA.js');
let EsfSTATUS_Sens = require('./EsfSTATUS_Sens.js');
let MonVER_Extension = require('./MonVER_Extension.js');
let CfgRATE = require('./CfgRATE.js');
let RxmSFRB = require('./RxmSFRB.js');
let NavATT = require('./NavATT.js');
let RxmRTCM = require('./RxmRTCM.js');
let CfgMSG = require('./CfgMSG.js');
let NavSVINFO_SV = require('./NavSVINFO_SV.js');
let RxmRAW = require('./RxmRAW.js');
let EsfRAW = require('./EsfRAW.js');
let NavSVIN = require('./NavSVIN.js');
let NavPOSLLH = require('./NavPOSLLH.js');
let NavSAT_SV = require('./NavSAT_SV.js');
let CfgGNSS = require('./CfgGNSS.js');
let NavPOSECEF = require('./NavPOSECEF.js');
let CfgNMEA7 = require('./CfgNMEA7.js');
let AidALM = require('./AidALM.js');
let CfgPRT = require('./CfgPRT.js');
let UpdSOS_Ack = require('./UpdSOS_Ack.js');
let NavCLOCK = require('./NavCLOCK.js');
let NavHPPOSECEF = require('./NavHPPOSECEF.js');
let EsfMEAS = require('./EsfMEAS.js');
let NavDGPS_SV = require('./NavDGPS_SV.js');
let CfgGNSS_Block = require('./CfgGNSS_Block.js');
let EsfSTATUS = require('./EsfSTATUS.js');
let CfgUSB = require('./CfgUSB.js');
let RxmSFRBX = require('./RxmSFRBX.js');
let NavDGPS = require('./NavDGPS.js');
let CfgSBAS = require('./CfgSBAS.js');
let CfgNAVX5 = require('./CfgNAVX5.js');
let NavSBAS_SV = require('./NavSBAS_SV.js');
let RxmSVSI = require('./RxmSVSI.js');
let CfgRST = require('./CfgRST.js');
let CfgHNR = require('./CfgHNR.js');
let Ack = require('./Ack.js');
let NavDOP = require('./NavDOP.js');
let NavRELPOSNED9 = require('./NavRELPOSNED9.js');
let RxmRAW_SV = require('./RxmRAW_SV.js');
let MonHW = require('./MonHW.js');
let AidEPH = require('./AidEPH.js');
let CfgDAT = require('./CfgDAT.js');
let CfgNMEA6 = require('./CfgNMEA6.js');
let RxmRAWX_Meas = require('./RxmRAWX_Meas.js');
let HnrPVT = require('./HnrPVT.js');
let NavPVT = require('./NavPVT.js');
let RxmEPH = require('./RxmEPH.js');
let RxmALM = require('./RxmALM.js');
let AidHUI = require('./AidHUI.js');
let MonGNSS = require('./MonGNSS.js');
let NavSVINFO = require('./NavSVINFO.js');
let EsfINS = require('./EsfINS.js');
let CfgINF_Block = require('./CfgINF_Block.js');

module.exports = {
  NavTIMEUTC: NavTIMEUTC,
  NavHPPOSLLH: NavHPPOSLLH,
  RxmRAWX: RxmRAWX,
  NavSAT: NavSAT,
  NavSTATUS: NavSTATUS,
  MgaGAL: MgaGAL,
  NavVELNED: NavVELNED,
  CfgINF: CfgINF,
  NavPVT7: NavPVT7,
  NavRELPOSNED: NavRELPOSNED,
  TimTM2: TimTM2,
  UpdSOS: UpdSOS,
  NavVELECEF: NavVELECEF,
  NavSOL: NavSOL,
  CfgANT: CfgANT,
  NavTIMEGPS: NavTIMEGPS,
  MonVER: MonVER,
  Inf: Inf,
  EsfRAW_Block: EsfRAW_Block,
  MonHW6: MonHW6,
  NavSBAS: NavSBAS,
  CfgDGNSS: CfgDGNSS,
  EsfALG: EsfALG,
  CfgCFG: CfgCFG,
  CfgTMODE3: CfgTMODE3,
  CfgNAV5: CfgNAV5,
  RxmSVSI_SV: RxmSVSI_SV,
  CfgNMEA: CfgNMEA,
  EsfSTATUS_Sens: EsfSTATUS_Sens,
  MonVER_Extension: MonVER_Extension,
  CfgRATE: CfgRATE,
  RxmSFRB: RxmSFRB,
  NavATT: NavATT,
  RxmRTCM: RxmRTCM,
  CfgMSG: CfgMSG,
  NavSVINFO_SV: NavSVINFO_SV,
  RxmRAW: RxmRAW,
  EsfRAW: EsfRAW,
  NavSVIN: NavSVIN,
  NavPOSLLH: NavPOSLLH,
  NavSAT_SV: NavSAT_SV,
  CfgGNSS: CfgGNSS,
  NavPOSECEF: NavPOSECEF,
  CfgNMEA7: CfgNMEA7,
  AidALM: AidALM,
  CfgPRT: CfgPRT,
  UpdSOS_Ack: UpdSOS_Ack,
  NavCLOCK: NavCLOCK,
  NavHPPOSECEF: NavHPPOSECEF,
  EsfMEAS: EsfMEAS,
  NavDGPS_SV: NavDGPS_SV,
  CfgGNSS_Block: CfgGNSS_Block,
  EsfSTATUS: EsfSTATUS,
  CfgUSB: CfgUSB,
  RxmSFRBX: RxmSFRBX,
  NavDGPS: NavDGPS,
  CfgSBAS: CfgSBAS,
  CfgNAVX5: CfgNAVX5,
  NavSBAS_SV: NavSBAS_SV,
  RxmSVSI: RxmSVSI,
  CfgRST: CfgRST,
  CfgHNR: CfgHNR,
  Ack: Ack,
  NavDOP: NavDOP,
  NavRELPOSNED9: NavRELPOSNED9,
  RxmRAW_SV: RxmRAW_SV,
  MonHW: MonHW,
  AidEPH: AidEPH,
  CfgDAT: CfgDAT,
  CfgNMEA6: CfgNMEA6,
  RxmRAWX_Meas: RxmRAWX_Meas,
  HnrPVT: HnrPVT,
  NavPVT: NavPVT,
  RxmEPH: RxmEPH,
  RxmALM: RxmALM,
  AidHUI: AidHUI,
  MonGNSS: MonGNSS,
  NavSVINFO: NavSVINFO,
  EsfINS: EsfINS,
  CfgINF_Block: CfgINF_Block,
};
