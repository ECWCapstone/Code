# -*- coding: utf-8 -*-
"""This module communicates with Emotiv's DLL"""
## @package PyEpoc
# This is a Python wrapper for Emotiv's dynamic link libraries.

## @mainpage PyEpoc
# @summary This module enables Python to communicate with the Emotiv Epoc head-set and Emotiv's EmoComposer, using Emotiv's dynamic link libraries. Although some functions return data in a way that differs from the Emotiv SDK, PyEpoc functions should be familiar to those using the Emotiv SDK.\n\n
# \b Classes:\n
# \li EpocHandler
#
# \b Structs:\n
# \li InputSensorDescriptor
#
# \b Dictionaries:\n
# \li #ERRCODE
# \li #EVENT
# \li #SUITE
# \li #SIGNALSTRENGTH
# \li #AFFECTIVALGO
# \li #EXPEVENT
# \li #EXPRESSIVALGO
# \li #EXPRTHRESHOLD
# \li #EXPRTRAININGCONTROL
# \li #EXPRSIGNATURE
# \li #COGACTION
# \li #COGTRAININGCONTROL
# \li #COGEVENT
# \li #INPUTCHANNELS
# \li #CONTACTQUALITY
#
# 
# @version \b PyEpoc 1.2
# @copyright Copyright 2009 Morten André Steinsland. \n\n
# @author Morten André Steinsland \n
# @contact morten.a.steinsland@gmail.com \n
# @contact http://www.mortenblog.net \n
#
# @note \li This module requires <a href="http://www.emotiv.com">Emotiv</a>'s SDK - Copyright 2009 , Emotiv Systems, Inc.
# \li This module requires <a href="http://www.python.org/download/releases/2.6.4/">Python 2.6.4</a> (or later) - Copyright 1990-2009 , Python Software Foundation.\n

import ctypes
#import time
#import decimal

## Emotiv Engine's Return Codes.
#
# This dictionary contains the EmoEngine return codes.
#
# EDK_OK                             : \b 0x0000 \n
# EDK_UNKNOWN_ERROR                  : \b 0x0001 \n
# EDK_INVALID_PROFILE_ARCHIVE        : \b 0x0101 \n
# EDK_NO_USER_FOR_BASEPROFILE        : \b 0x0102 \n
# EDK_CANNOT_ACQUIRE_DATA            : \b 0x0200 \n
# EDK_BUFFER_TOO_SMALL               : \b 0x0300 \n
# EDK_OUT_OF_RANGE                   : \b 0x0301 \n
# EDK_INVALID_PARAMETER              : \b 0x0302 \n
# EDK_PARAMETER_LOCKED               : \b 0x0303 \n
# EDK_COG_INVALID_TRAINING_ACTION    : \b 0x0304 \n
# EDK_COG_INVALID_TRAINING_CONTROL   : \b 0x0305 \n
# EDK_COG_INVALID_ACTIVE_ACTION      : \b 0x0306 \n
# EDK_COG_EXCESS_MAX_ACTIONS         : \b 0x0307 \n
# EDK_EXP_NO_SIG_AVAILABLE           : \b 0x0308 \n
# EDK_FILESYSTEM_ERROR               : \b 0x0309 \n
# EDK_INVALID_USER_ID                : \b 0x0400 \n
# EDK_EMOENGINE_UNINITIALIZED        : \b 0x0500 \n
# EDK_EMOENGINE_DISCONNECTED         : \b 0x0501 \n
# EDK_EMOENGINE_PROXY_ERROR          : \b 0x0502 \n
# EDK_NO_EVENT                       : \b 0x0600 \n
# EDK_GYRO_NOT_CALIBRATED            : \b 0x0700 \n
# EDK_OPTIMIZATION_IS_ON             : \b 0x0800 \n
# EDK_RESERVED1                      : \b 0x0900 \n
# @see edkErrorCode.h
ERRCODE = {'EDK_OK'                             : 0x0000,
           'EDK_UNKNOWN_ERROR'                  : 0x0001,
           'EDK_INVALID_PROFILE_ARCHIVE'        : 0x0101,
           'EDK_NO_USER_FOR_BASEPROFILE'        : 0x0102,
           'EDK_CANNOT_ACQUIRE_DATA'            : 0x0200,
           'EDK_BUFFER_TOO_SMALL'               : 0x0300,
           'EDK_OUT_OF_RANGE'                   : 0x0301,
           'EDK_INVALID_PARAMETER'              : 0x0302,
           'EDK_PARAMETER_LOCKED'               : 0x0303,
           'EDK_COG_INVALID_TRAINING_ACTION'    : 0x0304,
           'EDK_COG_INVALID_TRAINING_CONTROL'   : 0x0305,
           'EDK_COG_INVALID_ACTIVE_ACTION'      : 0x0306,
           'EDK_COG_EXCESS_MAX_ACTIONS'         : 0x0307,
           'EDK_EXP_NO_SIG_AVAILABLE'           : 0x0308,
           'EDK_FILESYSTEM_ERROR'               : 0x0309,
           'EDK_INVALID_USER_ID'                : 0x0400,
           'EDK_EMOENGINE_UNINITIALIZED'        : 0x0500,
           'EDK_EMOENGINE_DISCONNECTED'         : 0x0501,
           'EDK_EMOENGINE_PROXY_ERROR'          : 0x0502,
           'EDK_NO_EVENT'                       : 0x0600,
           'EDK_GYRO_NOT_CALIBRATED'            : 0x0700,
           'EDK_OPTIMIZATION_IS_ON'             : 0x0800,
           'EDK_RESERVED1'                      : 0x0900}

## Emotiv Events.
#
# This dictionary contains EmoEngine event types.
#
# EE_UnknownEvent          : \b 0x0000 \n
# EE_EmulatorError         : \b 0x0001 \n
# EE_ReservedEvent         : \b 0x0002 \n
# EE_UserAdded             : \b 0x0010 \n
# EE_UserRemoved           : \b 0x0020 \n
# EE_EmoStateUpdated       : \b 0x0040 \n
# EE_ProfileEvent          : \b 0x0080 \n
# EE_CognitivEvent         : \b 0x0100 \n
# EE_ExpressivEvent        : \b 0x0200 \n
# EE_InternalStateChanged  : \b 0x0400 \n
# @see EE_Event_enum (edk.h)
EVENT = {'EE_UnknownEvent'          : 0x0000,
         'EE_EmulatorError'         : 0x0001,
         'EE_ReservedEvent'         : 0x0002,
         'EE_UserAdded'             : 0x0010,
         'EE_UserRemoved'           : 0x0020,
         'EE_EmoStateUpdated'       : 0x0040,
         'EE_ProfileEvent'          : 0x0080,
         'EE_CognitivEvent'         : 0x0100,
         'EE_ExpressivEvent'        : 0x0200,
         'EE_InternalStateChanged'  : 0x0400}

## Emotiv Detection Suites.
#
# This dictionary contains the detection suite types.
#
# EE_EXPRESSIV   : \b 0 \n
# EE_AFFECTIV    : \b 1 \n
# EE_COGNITIV    : \b 2 \n
# @see EE_EmotivSuite_enum (EmoStateDLL.h)
SUITE = {'EE_EXPRESSIV' :0,
         'EE_AFFECTIV'  :1,
         'EE_COGNITIV'  :2}

## Wireless Signal Strength.
#
# This dictionary contains the wireless signal strength levels.
#
# NO_SIGNAL    : \b 0 \n
# BAD_SIGNAL   : \b 1 \n
# GOOD_SIGNAL  : \b 2 \n
# @see EE_SignalStrength_enum (EmoStateDLL.h)
SIGNALSTRENGTH = {'NO_SIGNAL'   : 0,
                  'BAD_SIGNAL'  : 1,
                  'GOOD_SIGNAL' : 2}

## Affectiv Algorithms.
#
# This dictionary contains the affectiv emotional types.
#
# AFF_EXCITEMENT         : \b 0x0001 \n
# AFF_MEDITATION         : \b 0x0002 \n
# AFF_FRUSTRATION        : \b 0x0004 \n
# AFF_ENGAGEMENT_BOREDOM : \b 0x0008 \n
# @see EE_AffectivAlgo_enum (EmoStateDLL.h)
AFFECTIVALGO = {'AFF_EXCITEMENT'        : 0x0001,
                'AFF_MEDITATION'        : 0x0002,
                'AFF_FRUSTRATION'       : 0x0004,
                'AFF_ENGAGEMENT_BOREDOM': 0x0008}

## Expressiv Events.
#
# Expressiv specific event types.
#
# EE_ExpressivNoEvent            : \b 0 \n
# EE_ExpressivTrainingStarted    : \b 1 \n
# EE_ExpressivTrainingSucceeded  : \b 2 \n
# EE_ExpressivTrainingFailed     : \b 3 \n 
# EE_ExpressivTrainingCompleted  : \b 4 \n
# EE_ExpressivTrainingDataErased : \b 5 \n
# EE_ExpressivTrainingRejected   : \b 6 \n
# EE_ExpressivTrainingReset      : \b 7 \n
# @see EE_ExpressivEvent_enum (edk.h)
EXPEVENT = {'EE_ExpressivNoEvent': 0,
            'EE_ExpressivTrainingStarted': 1,
            'EE_ExpressivTrainingSucceeded' : 2,
            'EE_ExpressivTrainingFailed':3,
            'EE_ExpressivTrainingCompleted':4,
            'EE_ExpressivTrainingDataErased':5,
            'EE_ExpressivTrainingRejected': 6,
            'EE_ExpressivTrainingReset': 7}

## Expressiv Facial Expression.
#
# This dictionary contains the expressiv facial expression types.
#
# EXP_NEUTRAL     : \b 0x0001 \n
# EXP_BLINK       : \b 0x0002 \n
# EXP_WINK_LEFT   : \b 0x0004 \n
# EXP_WINK_RIGHT  : \b 0x0008 \n
# EXP_HORIEYE     : \b 0x0010 \n
# EXP_EYEBROW     : \b 0x0020 \n
# EXP_FURROW      : \b 0x0040 \n
# EXP_SMILE       : \b 0x0080 \n
# EXP_CLENCH      : \b 0x0100 \n
# EXP_LAUGH       : \b 0x0200 \n
# EXP_SMIRK_LEFT  : \b 0x0400 \n
# EXP_SMIRK_RIGHT : \b 0x0800 \n
# @see EE_ExpressivAlgo_enum (EmoStateDLL.h)
EXPRESSIVALGO = {'EXP_NEUTRAL'      : 0x0001,
                 'EXP_BLINK'        : 0x0002,
                 'EXP_WINK_LEFT'    : 0x0004,
                 'EXP_WINK_RIGHT'   : 0x0008,
                 'EXP_HORIEYE'      : 0x0010,
                 'EXP_EYEBROW'      : 0x0020,
                 'EXP_FURROW'       : 0x0040,
                 'EXP_SMILE'        : 0x0080,
                 'EXP_CLENCH'       : 0x0100,
                 'EXP_LAUGH'        : 0x0200,
                 'EXP_SMIRK_LEFT'   : 0x0400,
                 'EXP_SMIRK_RIGHT'  : 0x0800}

## Expressiv Threshold.
#
# Expressiv Suite sensitivity threshold.
#
# EXP_SENSITIVITY : \b 0 \n
# @see EE_ExpressivThreshold_enum (edk.h)
EXPRTHRESHOLD = {'EXP_SENSITIVITY': 0}

## Expressiv Training Control.
#
# Expressiv Suite training controls.
#
# EXP_NONE    : \b 0 \n
# EXP_START   : \b 1 \n
# EXP_ACCEPT  : \b 2 \n
# EXP_REJECT  : \b 3 \n
# EXP_ERASE   : \b 4 \n
# EXP_RESET   : \b 5 \n
# @see EE_ExpressivTrainingControl_enum (edk.h)
EXPRTRAININGCONTROL = {'EXP_NONE'  : 0,
                       'EXP_START' : 1,
                       'EXP_ACCEPT': 2,
                       'EXP_REJECT': 3,
                       'EXP_ERASE' : 4,
                       'EXP_RESET' : 5}

## Expressiv Signature.
#
# Expressiv Suite signature types.
#
# EXP_SIG_UNIVERSAL  : \b 0 \n
# EXP_SIG_TRAINED    : \b 1 \n
# @see EE_ExpressivSignature_enum (edk.h)
EXPRSIGNATURE = {'EXP_SIG_UNIVERSAL': 0,
                 'EXP_SIG_TRAINED'  : 1}

## Cognitiv Actions.
#
# Cognitiv action types.
#
# COG_NEUTRAL                  : \b 0x0001 \n
# COG_PUSH                     : \b 0x0002 \n
# COG_PULL                     : \b 0x0004 \n
# COG_LIFT                     : \b 0x0008 \n
# COG_DROP                     : \b 0x0010 \n
# COG_LEFT                     : \b 0x0020 \n
# COG_RIGHT                    : \b 0x0040 \n
# COG_ROTATE_LEFT              : \b 0x0080 \n
# COG_ROTATE_RIGHT             : \b 0x0100 \n
# COG_ROTATE_CLOCKWISE         : \b 0x0200 \n
# COG_ROTATE_COUNTER_CLOCKWISE : \b 0x0400 \n
# COG_ROTATE_FORWARDS          : \b 0x0800 \n
# COG_ROTATE_REVERSE           : \b 0x1000 \n
# COG_DISAPPEAR                : \b 0x2000 \n
# @see EE_CognitivAction_enum (EmoStateDLL.h)
COGACTION = {'COG_NEUTRAL'                 : 0x0001,
             'COG_PUSH'                    : 0x0002,
             'COG_PULL'                    : 0x0004,
             'COG_LIFT'                    : 0x0008,
             'COG_DROP'                    : 0x0010,
             'COG_LEFT'                    : 0x0020,
             'COG_RIGHT'                   : 0x0040,
             'COG_ROTATE_LEFT'             : 0x0080,
             'COG_ROTATE_RIGHT'            : 0x0100,
             'COG_ROTATE_CLOCKWISE'        : 0x0200,
             'COG_ROTATE_COUNTER_CLOCKWISE': 0x0400,
             'COG_ROTATE_FORWARDS'         : 0x0800,
             'COG_ROTATE_REVERSE'          : 0x1000,
             'COG_DISAPPEAR'               : 0x2000}


## Cognitiv Training Control.
#
# Cognitiv Suite training controls.
#
# COG_NONE     : \b 0 \n
# COG_START    : \b 1 \n
# COG_ACCEPT   : \b 2 \n
# COG_REJECT   : \b 3 \n
# COG_ERASE    : \b 4 \n
# COG_RESET    : \b 5 \n
## @see EE_CognitivTrainingControl_enum (edk.h)
COGTRAININGCONTROL = {'COG_NONE'    : 0,
                      'COG_START'   : 1,
                      'COG_ACCEPT'  : 2,
                      'COG_REJECT'  : 3,
                      'COG_ERASE'   : 4,
                      'COG_RESET'   : 5}

## Cognitiv Events.
#
# Cognitiv-specific event types.
#
# EE_CognitivNoEvent                      : \b 0 \n
# EE_CognitivTrainingStarted              : \b 1 \n
# EE_CognitivTrainingSucceeded            : \b 2 \n
# EE_CognitivTrainingFailed               : \b 3 \n
# EE_CognitivTrainingCompleted            : \b 4 \n
# EE_CognitivTrainingDataErased           : \b 5 \n
# EE_CognitivTrainingRejected             : \b 6 \n
# EE_CognitivTrainingReset                : \b 7 \n
# EE_CognitivAutoSamplingNeutralCompleted : \b 8 \n
# EE_CognitivSignatureUpdated             : \b 9 \n 
# @see EE_CognitivEvent_enum (edk.h)
COGEVENT = {'EE_CognitivNoEvent'                        : 0,
            'EE_CognitivTrainingStarted'                : 1,
            'EE_CognitivTrainingSucceeded'              : 2,
            'EE_CognitivTrainingFailed'                 : 3,
            'EE_CognitivTrainingCompleted'              : 4,
            'EE_CognitivTrainingDataErased'             : 5,
            'EE_CognitivTrainingRejected'               : 6,
            'EE_CognitivTrainingReset'                  : 7,
            'EE_CognitivAutoSamplingNeutralCompleted'   : 8,
            'EE_CognitivSignatureUpdated'               : 9}

## Input Channels.
#
# Headset Input Channels.
#
# EE_CHAN_CMS : \b 0 \n
# EE_CHAN_DRL : \b 1 \n
# EE_CHAN_FP1 : \b 2 \n
# EE_CHAN_AF3 : \b 3 \n
# EE_CHAN_F7  : \b 4 \n
# EE_CHAN_F3  : \b 5 \n
# EE_CHAN_FC5 : \b 6 \n
# EE_CHAN_T7  : \b 7 \n
# EE_CHAN_P7  : \b 8 \n
# EE_CHAN_O1  : \b 9 \n
# EE_CHAN_O2  : \b 10 \n
# EE_CHAN_P8  : \b 11 \n
# EE_CHAN_T8  : \b 12 \n
# EE_CHAN_FC6 : \b 13 \n
# EE_CHAN_F4  : \b 14 \n
# EE_CHAN_F8  : \b 15 \n
# EE_CHAN_AF4 : \b 16 \n
# EE_CHAN_FP2 : \b 17 \n
# @see EE_InputChannels_enum (EmoStateDLL.h)
INPUTCHANNELS = {'EE_CHAN_CMS'  : 0,
                 'EE_CHAN_DRL'  : 1,
                 'EE_CHAN_FP1'  : 2,
                 'EE_CHAN_AF3'  : 3,
                 'EE_CHAN_F7'   : 4,
                 'EE_CHAN_F3'   : 5,
                 'EE_CHAN_FC5'  : 6,
                 'EE_CHAN_T7'   : 7,
                 'EE_CHAN_P7'   : 8,
                 'EE_CHAN_O1'   : 9,
                 'EE_CHAN_O2'   : 10,
                 'EE_CHAN_P8'   : 11,
                 'EE_CHAN_T8'   : 12,
                 'EE_CHAN_FC6'  : 13,
                 'EE_CHAN_F4'   : 14,
                 'EE_CHAN_F8'   : 15,
                 'EE_CHAN_AF4'  : 16,
                 'EE_CHAN_FP2'  : 17}

## EEG Sensor Contact Quality.
#
# EEG Electrode Contact Quality enumeration. Used to characterize the EEG signal reception
# or electrode contact for a sensor on the headset.
#
# EEG_CQ_NO_SIGNAL : \b 0 \n
# EEG_CQ_VERY_BAD : \b 1 \n
# EEG_CQ_POOR : \b 3 \n
# EEG_CQ_FAIR : \b 4 \n
# EEG_CQ_GOOD : \b 5 \n
# @note This differs from the wireless signal strength (#SIGNALSTRENGTH), which refers to the radio
# communication between the headset transmitter and USB dongle receiver.
# @see EE_EEG_ContactQuality_enum (EmoStateDLL.h)
CONTACTQUALITY = {'EEG_CQ_NO_SIGNAL'    : 0,
                  'EEG_CQ_VERY_BAD'     : 1,
                  'EEG_CQ_POOR'         : 3,
                  'EEG_CQ_FAIR'         : 4,
                  'EEG_CQ_GOOD'         : 5}

## @struct InputSensorDescriptor
# \brief Input sensor description struct.
#
# A struct to hold input sensor descriptions
# @sa #INPUTCHANNELS
class InputSensorDescriptor(ctypes.Structure):
    """.ChannelId    - logical channel id
    .Exist        - does this sensor exist
    .Label        - sensor label
    .xLoc         - x coordinate from center of head towards nose
    .yLoc         - y coordinate from center of head towards ears
    .zLoc         - z coordinate from center of head toward top of skull"""
    
    _fields_ = [("ChannelId", ctypes.c_int), ## logical channel id
                ("Exist", ctypes.c_int), ## does this sensor exist on this headset model
                ("Label", ctypes.c_char_p), ## text label identifying this sensor
                ("xLoc", ctypes.c_double), ## x coordinate from center of head towards nose
                ("yLoc", ctypes.c_double), ## y coordinate from center of head towards ears
                ("zLoc", ctypes.c_double)]  ## z coordinate from center of head toward top of skull

## @class EpocHandler
# \brief The wrapper class.
#
# This class creates a link to Emotiv's DLL and it's functions.
class EpocHandler:
    ## \internal
    def __init__(self):
        self.EmotivEngineDLL = ctypes.CDLL("~/EmotivEducation_2.0.0.20/lib/libedk.so")  # link the edk.dll
        
    ## Initializes a connection to EmoEngine.
    #
    # This function should be called at the beginning of programs.
    # @return #ERRCODE
    # @sa EpocHandler::EE_EngineRemoteConnect()
    # @see edkErrorCode.h
    def EE_EngineConnect(self):
        return self.EmotivEngineDLL.EE_EngineConnect(ctypes.c_char_p(b'Emotiv Systems-5'))  ####### Editted 2-5-2015

    ## Initializes a connection to EmoComposer.
    #
    # This function should be called at the beginning of programs.
    # @param ip str, IP address of the host
    # @param port int, the port of the host
    # @return #ERRCODE
    # @sa EpocHandler::EE_EngineConnect()
    # @see edkErrorCode.h
    # @note For Emotiv Control Panel use port 3008. For EmoComposer use port 1726.
    def EE_EngineRemoteConnect(self, ip, port):
        return self.EmotivEngineDLL.EE_EngineRemoteConnect(ip, port)
    
    ## Ends the connection to EmoEngine.
    #
    # Closes the connection to EmoEngine. This function should be called at the end of programs.
    # @return #ERRCODE    
    # @see edkErrorCode.h
    def EE_EngineDisconnect(self):
        return self.EmotivEngineDLL.EE_EngineDisconnect()
    
    ## Enables diagnostics logging.
    #
    # @param emotivlogfile str, filepath
    # @param enabled int, 1 enable / 0 disable 
    # @warning This should only be enabled if instructed to do so by Emotiv developer support for
    # the purposes of collecting diagnostic information.
    # @return #ERRCODE
    # @see edkErrorCode.h
    def EE_EnableDiagnostics(self, emotivlogfile, enabled):
        if (enabled != 0):
            emotivlogfile = """logs\emotiv.log""" # set the default log file
            return self.EmotivEngineDLL.EE_EnableDiagnostics(emotivlogfile, 1)
        else:
            return self.EmotivEngineDLL.EE_EnableDiagnostics(emotivlogfile, 0)
    
    ## Create a handle for EmoEngine event.
    #
    # This handle can be reused by the caller to retrieve events.
    # @return handle, EmoEngineEventHandle
    def EE_EmoEngineEventCreate(self):        
        return self.EmotivEngineDLL.EE_EmoEngineEventCreate()
    
    ## Create a handle to EmoEngine profile event.
    #
    # details Returns a handle to memory that can hold a profile byte stream.
    # This handle can be reused by the caller to retrieve subsequent profile bytes.
    # @return handle, EmoEngineEventHandle
    def EE_ProfileEventCreate(self):
        return self.EmotivEngineDLL.EE_ProfileEventCreate()
    
    ## Free an event handle.
    # 
    # This frees memory referenced by event handle.
    # @param emoengineeventhandle handle, created by EE_EmoEngineEventCreate()
    def EE_EmoEngineEventFree(self, emoengineeventhandle):
        self.EmotivEngineDLL.EE_EmoEngineEventFree(emoengineeventhandle)
    
    ## Create a handle to EmoState.
    #
    # Returns a handle to memory that can store an EmoState.
    # This handle can be reused by the caller to retrieve subsequent EmoStates.
    # @return handle
    def EE_EmoStateCreate(self):
        return self.EmotivEngineDLL.EE_EmoStateCreate()
    
    ## Free EmoState.
    #
    # Frees memory referenced by an EmoState handle.
    # @param emostatehandle handle, created by EE_EmoStateCreate()
    def EE_EmoStateFree(self, emostatehandle):
        self.EmotivEngineDLL.EE_EmoStateFree(emostatehandle)
        
    ## Get EmoEngine event type.
    #
    # Returns the event type for an event already retrieved using EE_EngineGetNextEvent.
    # @param emoengineeventhandle handle
    # @return #EVENT
    def EE_EmoEngineEventGetType(self, emoengineeventhandle):
         return self.EmotivEngineDLL.EE_EmoEngineEventGetType(emoengineeventhandle)
    
    ## Get Cognitiv event type.
    #
    # Returns the Cognitiv-specific event type for an EE_CognitivEvent event already
    # retrieved using EE_EngineGetNextEvent. \n 
    # @param emoengineeventhandle handle, created by EE_EmoEngineEventCreate()
    # @return #COGEVENT
    def EE_CognitivEventGetType(self, emoengineeventhandle):
        return self.EmotivEngineDLL.EE_CognitivEventGetType(emoengineeventhandle)
    
    ## Get Expressiv event type.
    #
    # Returns the Expressiv-specific event type for an EE_ExpressivEvent event already
    # retrieved using EE_EngineGetNextEvent.
    # @param emoengineeventhandle handle, created by EE_EmoEngineEventCreate()
    # @return #EXPEVENT
    def EE_ExpressivEventGetType(self, emoengineeventhandle):
        return self.EmotivEngineDLL.EE_ExpressivEventGetType(emoengineeventhandle)
    
    ## Get user ID.
    #
    # Retrieves the user ID for EE_UserAdded and EE_UserRemoved events.
    # @param emoengineeventhandle handle
    # @return (#ERRCODE, userID)
    def EE_EmoEngineEventGetUserId(self, emoengineeventhandle):
        userid = ctypes.c_int()
        code = self.EmotivEngineDLL.EE_EmoEngineEventGetUserId(emoengineeventhandle, ctypes.byref(userid))
        returnid = userid.value
        del userid
        return (code, returnid)

    ## Get EmoState.
    #
    # Copies an EmoState returned with a EE_EmoStateUpdate event to memory referenced by an EmoStateHandle.
    # @param emoengineeventhandle handle, returned by EE_EmoEngineEventCreate() and populated with EE_EmoEngineGetNextEvent()
    # @param emostatehandle handle, returned by EE_EmoStateCreate()
    # @return #ERRCODE    
    def EE_EmoEngineEventGetEmoState(self, emoengineeventhandle, emostatehandle):
        return self.EmotivEngineDLL.EE_EmoEngineEventGetEmoState(emoengineeventhandle, emostatehandle)
    
    ## Retrieves the next EmoEngine event.
    #
    # Non-blocking call.
    # @note ERRCODE['EDK_OK'] if a new event has been retrieved.
    # ERRCODE['EDK_NO_EVENT'] if no new events have been generated by EmoEngine.
    # @param emoengineeventhandle handle created by EE_EmoEngineEventCreate()
    # @return #ERRCODE
    def EE_EngineGetNextEvent(self, emoengineeventhandle):
        return self.EmotivEngineDLL.EE_EngineGetNextEvent(emoengineeventhandle)
    
    ## Clear EmoEngine event.
    #
    # Clear a specific EmoEngine event type or all events currently inside the event queue.
    # Event flags can be combined together as one argument except EE_UnknownEvent and EE_EmulatorError.\n
    # @note ERRCODE['EDK_OK'] if the events have been cleared from the queue.\n
    # ERRCODE['EDK_INVALID_PARAMETER'] if input event types are invalid.\n
    # @param eventtypes list, EmoEngine event types (#EVENT)
    # @return #ERRCODE
    def EE_EngineClearEventQueue(self, eventtypes):    
        return self.EmotivEngineDLL.EE_EngineClearEventQueue(eventtypes)
    
    ## Get number of users.
    #
    # Retrieves the number of users on the engine.
    # @return (#ERRCODE, numberofusers)
    def EE_EngineGetNumUser(self):
        numusers = ctypes.c_int()
        code = self.EmotivEngineDLL.EE_EngineGetNumUser(ctypes.byref(numusers))
        returnnum = numusers.value
        del numusers
        return (code, returnnum)
    
    ## Set Player number on display.
    #
    # Sets the player number displayed on the physical input device (currently the USB Dongle)
    # that corresponds to the specified user.
    # @param userid int, EmoEngine user ID
    # @param playernum int, application assigned player number displayed on input device hardware (must be in the range 1-4)
    # @return #ERRCODE
    def EE_SetHardwarePlayerDisplay(self, userid, playernum):
        return self.EmotivEngineDLL.EE_SetHardwarePlayerDisplay(userid, playernum)

    ## Set User Profile.
    #
    # Loads an EmoEngine profile for the specified user.
    # @param userid int, User ID
    # @param profilebuffer pointer, to buffer containing a serialized user profile previously returned from EmoEngine.
    # @param length int, buffer size (number of bytes)
    # @todo Make it work!!  
    def EE_SetUserProfile(self, userid, profilebuffer, length):
        buffer = ctypes.create_string_buffer(length)
        buffer.value = profilebuffer
        code = self.EmotivEngineDLL.EE_SetUserProfile(userid, buffer, length)
        return code
        

    ## Get User Profile.
    #
    # Returns user profile data in a synchronous manner. Fills in the event referred to by emoengineeventhandle
    # with an EE_ProfileEvent event that contains the profile data for the specified user.
    # @param userid int, User ID
    # @param emoengineeventhan handle,returned by EE_EmoEngineEventCreate()
    # @return #ERRCODE
    def EE_GetUserProfile(self, userid, emoengineeventhandle):
        return self.EmotivEngineDLL.EE_GetUserProfile(userid, emoengineeventhandle)
    
    ## Get Base Profile.
    #
    # Returns a serialized user profile for a default user in a synchronous manner. Fills in the event referred
    # to by emoengineeventhandle with an EE_ProfileEvent event that contains the profile data for the default user
    # @param emoengineeventhandle handle, returned by EE_EmoEngineEventCreate()
    # @return #ERRCODE 
    def EE_GetBaseProfile(self, emoengineeventhandle):
        return self.EmotivEngineDLL.EE_GetBaseProfile(emoengineeventhandle)
    
    ## Get User Profile Size.
    #
    # Retrieves the number of bytes required to store a serialized version of the requested user profile.
    # @param emoengineeventhandle handle, returned by EE_EmoEngineEventCreate()
    # @return (#ERRCODE, int sizeinbytes)
    # @todo figure out why it gives EDK_INVALID_PARAMETER
    def EE_GetUserProfileSize(self, emoengineeventhandle):        
        profilesizeout = ctypes.c_uint()
        code = self.EmotivEngineDLL.EE_GetUserProfileSize(emoengineeventhandle, ctypes.byref(profilesizeout))
        sizeinbytes = profilesizeout.value
        del profilesizeout
        return (code, int(sizeinbytes))
    
    ## Get User Profile Bytes.
    #
    # Returns a serialized version of the requested user profile.
    # @param emoengineeventhandle handle, something something
    # @param bufferlength int, size of buffer in bytes
    # @todo make it work!!
    # @sa EpocHandler::EE_GetUserProfileSize()
    def EE_GetUserProfileBytes(self, emoengineeventhandle, bufferlength):
        buffer = ctypes.create_string_buffer(bufferlength)        
        code = self.EmotivEngineDLL.EE_GetUserProfileBytes(emoengineeventhandle, ctypes.byref(buffer), bufferlength)
        returnbuffer = buffer.raw
        del buffer
        return (code, returnbuffer)
    
    ## Load User Profile.
    #
    # Loads a user profile from disk and assigns it to the specified user.
    # @param userid int, User ID
    # @param inputfilename str, filepath
    # @return #ERRCODE
    # @sa EpocHandler::EE_SaveUserProfile()
    def EE_LoadUserProfile(self, userid, inputfilename):
        return self.EmotivEngineDLL.EE_LoadUserProfile(userid, inputfilename)
    
    ## Save User Profile.
    #
    # Saves a user profile for specified user to disk.
    # @param userid int, User ID
    # @param outputfilename str, filepath
    # @return #ERRCODE
    # @sa EpocHandler::EE_LoadUserProfile()
    def EE_SaveUserProfile(self, userid, outputfilename):
        return self.EmotivEngineDLL.EE_SaveUserProfile(userid, outputfilename)
    
    ## Set Expressiv Alghorithms Threshold.
    #
    # Set threshold for Expressiv algorithms.
    # @param userid int, User ID
    # @param expressivalgoname #EXPRESSIVALGO
    # @param thresholdname #EXPRTHRESHOLD
    # @param value int, threshold value (min: 0 max: 1000)
    # @return #ERRCODE 
    def EE_ExpressivSetThreshold(self, userid, expressivalgoname, thresholdname, value):
        return self.EmotivEngineDLL.EE_ExpressivSetThreshold(userid, expressivalgoname, thresholdname, value)
    
    ## Get Expressiv Threshold.
    #
    # Get threshold from Expressiv algorithms.
    # @param userid int, User ID
    # @param expressivalgoname #EXPRESSIVALGO
    # @param thresholdname #EXPRTHRESHOLD
    # @return (#ERRCODE , int value)
    def EE_ExpressivGetThreshold(self, userid, expressivalgoname, thresholdname):
        valueout = ctypes.c_int()
        code = self.EmotivEngineDLL.EE_ExpressivGetThreshold(userid, expressivalgoname, thresholdname, ctypes.byref(valueout))
        returnvalue = valueout.value
        del valueout
        return (code, returnvalue)
    
    ## Set Expressiv Training Action.
    #
    # Set the current facial expression for Expressiv training.
    # @param userid int, User ID
    # @param expressivalgoname #EXPRESSIVALGO
    # @return #ERRCODE
    def EE_ExpressivSetTrainingAction(self, userid, expressivalgoname):
        return self.EmotivEngineDLL.EE_ExpressivSetTrainingAction(userid, expressivalgoname)
    
    ## Set Expressiv Training Control.
    #
    # Set the control flag for Expressiv training. Blocking call.
    # @param int, User ID
    # @param control #EXPRTRAININGCONTROL
    # @return #ERRCODE - current status of EmoEngine. If the query is successful, returns EDK_OK.
    def EE_ExpressivSetTrainingControl(self, userid, control):
        return self.EmotivEngineDLL.EE_ExpressivSetTrainingControl(userid, control)
    
    ## Get Expressiv Training Action.
    #
    # Gets the facial expression currently selected for Expressiv training. Blocking call.
    # @param userid int, User ID
    # @return (#ERRCODE, int action)
    # @see #EXPRESSIVALGO
    # @todo check return value [1]
    def EE_ExpressivGetTrainingAction(self, userid):
        actionout = ctypes.c_int()
        code = self.EmotivEngineDLL.EE_ExpressivGetTrainingAction(userid, ctypes.byref(actionout))
        returnaction = actionout.value
        del actionout
        return (code, returnaction)
    
    ## Get Expressiv Training Time.
    #
    # Return the duration of a Expressiv training session in ms.
    # @param userid int, User ID
    # @return (#ERRCODE, int time)
    def EE_ExpressivGetTrainingTime(self, userid):
        timeout = ctypes.c_int()
        code = self.EmotivEngineDLL.EE_ExpressivGetTrainingTime(userid, ctypes.byref(timeout))
        returntime = timeout.value
        del timeout
        return (code, returntime)

    ## Get Expressiv Trained Signature Actions
    #
    # Gets a list of the actions that have been trained by the user.
    # @param userid int, User ID
    # @return (#ERRCODE , bitvector trainedactions)
    # @todo make it work!! figure out bitvector 
    def EE_ExpressivGetTrainedSignatureActions(self, userid):
        trainedactionsout = ctypes.c_ulong()
        code = self.EmotivEngineDLL.EE_ExpressivGetTrainedSignatureActions(userid, ctypes.byref(trainedactionsout))
        returntrainedactions = trainedactionsout.value
        del trainedactionsout
        return (code, returntrainedactions)
    
    ## Get Expressiv Trained Signature Available Flag.
    #
    # Gets a flag indicating if the user has trained sufficient actions to activate a trained
    # signature. return[1] will be set to 1 if the user has trained EXP_NEUTRAL and at least
    # one other Expressiv action. Otherwise, return[1] = 0.
    # @param userid int, User ID
    # @return (#ERRCODE , int flag)
    # @see #EXPRESSIVALGO
    def EE_ExpressivGetTrainedSignatureAvailable(self, userid):
        availableout = ctypes.c_int()
        code = self.EmotivEngineDLL.EE_ExpressivGetTrainedSignatureAvailable(userid, ctypes.byref(availableout))
        returnavailable = availableout.value
        del availableout
        return (code, returnavailable)
    
    ## Set Expressiv Signature Type.
    #
    # Configures the Expressiv suite to use either the built-in, universal signature or a personal, trained
    # signature. Note: Expressiv defaults to use its universal signature. This function will fail if
    # EE_ExpressivGetTrainedSignatureAvailable() returns false. Blocking call
    # @param userid int, User ID
    # @param expsigtype #EXPRSIGNATURE
    # @return #ERRCODE
    def EE_ExpressivSetSignatureType(self, userid, expsigtype):
        return self.EmotivEngineDLL.EE_ExpressivSetSignatureType(userid, expsigtype)
    
    ## Get Expressiv Signature Type.
    #
    # Indicates whether the Expressiv suite is currently using either the built-in, universal signature or
    # a trained signature. Blocking call
    # @param userid int, User ID
    # @return (#ERRCODE , int sigtype)
    # @see #ERRCODE
    # @see #EXPRSIGNATURE
    def EE_ExpressivGetSignatureType(self, userid):
        sigtypeout = ctypes.c_int()
        code = self.EmotivEngineDLL.EE_ExpressivGetSignatureType(userid, ctypes.byref(sigtypeout))
        returnsigtype = sigtypeout.value
        del sigtypeout
        return (code, returnsigtype)
    
    ## Set Cognitiv Active Actions
    #
    # Set the current Cognitiv active action types.
    # @param userid int, User ID
    # @param activeactions  bitvector, a bit vector composed of #COGACTION contants
    # @todo Make it work! Find out what bitvectors are.
    def EE_CognitivSetActiveActions(self, userid, activeactions):
        #return self.EmotivEngineDLL.EE_CognitivSetActiveActions(userid, activeactions)
        pass
    
    ## Get Cognitiv Active Actions
    #
    # Get the current Cognitiv active action types.
    # @param userid int, User ID
    # @return (#ERRCODE, ulong activeactions)
    # @todo Find out what bitvectors are.
    # @test Test it!
    # @see #COGACTION
    def EE_CognitivGetActiveActions(self, userid):
        activeactionsout = ctypes.c_ulong()
        code = self.EmotivEngineDLL.EE_CognitivGetActiveActions(userid, ctypes.byref(activeactionsout))
        returnactions = activeactionsout.value
        del activeactionsout
        return (code, returnactions)
    
    ## Get Cognitiv Training Time
    #
    # Return the duration of a Cognitiv training session in ms.
    # @param userid int, User ID
    # @return (#ERRCODE, int trainingms)
    # @see #ERRCODE
    def EE_CognitivGetTrainingTime(self, userid):
        trainingtimeout = ctypes.c_int()
        code = self.EmotivEngineDLL.EE_CognitivGetTrainingTime(userid, ctypes.byref(trainingtimeout))
        returntrainingtime = trainingtimeout.value
        del trainingtimeout
        return (code, returntrainingtime)
    
    ## Set Cognitiv Training Control
    #
    # Set the training control flag for Cognitiv training.
    # @param userid int, User ID
    # @return  #ERRCODE
    # @see #COGTRAININGCONTROL
    def EE_CognitivSetTrainingControl(self, userid, trainingcontrol):
        return self.EmotivEngineDLL.EE_CognitivSetTrainingControl(userid, trainingcontrol)
    
    ## Set Cognitiv Training Action
    #
    # Set the type of Cognitiv action to be trained.
    # @param userid int, User ID
    # @param action int, #COGACTION
    # @return #ERRCODE
    def EE_CognitivSetTrainingAction(self, userid, action):
        return self.EmotivEngineDLL.EE_CognitivSetTrainingAction(userid, action)
    
    ## Get Cognitiv Training Action
    #
    # Get the type of Cognitiv action currently selected for training.
    # @param userid int, User ID
    # @return (#ERRCODE, #COGACTION)
    def EE_CognitivGetTrainingAction(self, userid):
        trainingactionout = ctypes.c_int()
        code = self.EmotivEngineDLL.EE_CognitivGetTrainingAction(userid, ctypes.byref(trainingactionout))
        returntrainingaction = trainingactionout.value
        del trainingactionout
        return (code, returntrainingaction)
    
    ## Get Cognitiv Trained Signature Actions
    #
    # Gets a list of the Cognitiv actions that have been trained by the user.\nBlocking call
    # @param userid int, User ID
    # @return (#ERRCODE, ulong trainedactions)
    # @see #COGACTION
    # @test Test it!
    def EE_CognitivGetTrainedSignatureActions(self, userid):
        trainedactionsout = ctypes.c_ulong()
        code = self.EmotivEngineDLL.EE_CognitivGetTrainedSignatureActions(userid, ctypes.byref(trainedactionsout))
        returntrainedactions = trainedactionsout.value
        del trainedactionsout
        return (code, returntrainedactions)
    
    ## Get Overall Cognitiv Skill Rating
    #
    # Gets the current overall skill rating of the user in Cognitiv.
    # @param userid int, User ID
    # @return (#ERRCODE, float overallskillrating)
    # @note Representation error (0.70 in EmoComposer returned 0.69999998807907104)
    def EE_CognitivGetOverallSkillRating(self, userid):
        skillratingout = ctypes.c_float()
        code = self.EmotivEngineDLL.EE_CognitivGetOverallSkillRating(userid, ctypes.byref(skillratingout))
        returnoverallskillrating = skillratingout.value
        del skillratingout
        return (code, returnoverallskillrating)
    
    ## Get Cognitiv Action Skill Rating
    #
    # Gets the current skill rating for particular Cognitiv actions of the user. Blocking call.
    # @param userid int, User ID
    # @param action int, #COGACTION
    # @return (#ERRCODE, float skillrating)
    def EE_CognitivGetActionSkillRating(self, userid, action):
        skillratingout = ctypes.c_float()
        code = self.EmotivEngineDLL.EE_CognitivGetActionSkillRating(userid, action, ctypes.byref(skillratingout))
        returnskillrating = skillratingout.value
        del skillratingout
        return (code, returnskillrating)
    
    ## Set Cognitiv Activation Level
    #
    # Set the overall sensitivity for all Cognitiv actions (lowest 1 - highest 7)
    # @param userid int, User ID
    # @param level int, sensitivity level 1-7
    # @return #ERRCODE
    # @sa EpocHandler::EE_CognitivGetActivationLevel()
    def EE_CognitivSetActivationLevel(self, userid, level):
        return self.EmotivEngineDLL.EE_CognitivSetActivationLevel(userid, level)
    
    ## Set Cognitiv Action Sensitivity
    #
    # Set the sensitivity of Cognitiv actions (lowest 1 - highest 10)
    # @param userid int, User ID
    # @param action1sens int, sensitivity of action 1
    # @param action2sens int, sensitivity of action 2
    # @param action3sens int, sensitivity of action 3
    # @param action4sens int, sensitivity of action 4
    # @return #ERRCODE
    # @test Test it!
    # @todo Find out what this does.
    # @sa EpocHandler::EE_CognitivGetActionSensitivity()
    def EE_CognitivSetActionSensitivity(self, userid, action1sens, action2sens, action3sens, action4sens):
        return self.EmotivEngineDLL.EE_CognitivSetActionSensitivity(userid, action1sens, action2sens, action3sens, action4sens)
    
    ## Get Cognitiv Activation Level
    #
    # Get the overall sensitivity for all Cognitiv actions (Min 1 Max 10)
    # @param userid int, User ID
    # @return (#ERRCODE, int level)
    # @sa EpocHandler::EE_CognitivSetActivationLevel()
    def EE_CognitivGetActivationLevel(self, userid):
        levelout = ctypes.c_int()
        code = self.EmotivEngineDLL.EE_CognitivGetActivationLevel(userid, ctypes.byref(levelout))
        returnlevel = levelout.value
        del levelout
        return (code, returnlevel)
    
    ## Get Cognitiv Action Sensitivity
    #
    # Query the sensitivity of Cognitiv actions.
    # @param userid int, User ID
    # @return (#ERRCODE, action1sens, action2sens, action3sens, action4sens)
    # @sa EpocHandler::EE_CognitivSetActionSensitivity()
    def EE_CognitivGetActionSensitivity(self, userid):
        action1sensout = ctypes.c_int()
        action2sensout = ctypes.c_int()
        action3sensout = ctypes.c_int()
        action4sensout = ctypes.c_int()
        code = self.EmotivEngineDLL.EE_CognitivGetActionSensitivity(userid, ctypes.byref(action1sensout), ctypes.byref(action2sensout), ctypes.byref(action3sensout), ctypes.byref(action4sensout))
        action1sens = action1sensout.value
        action2sens = action2sensout.value
        action3sens = action3sensout.value
        action4sens = action4sensout.value
        del action1sensout, action2sensout, action3sensout, action4sensout
        return (code, action1sens, action2sens, action3sens, action4sens)
    
    ## Start Sampling Cognitiv Neutral
    #
    # Start the sampling of Neutral state in Cognitiv.
    # @param userid int, User ID
    # @return #ERRCODE
    # @sa EpocHandler::EE_CognitivStopSamplingNeutral()
    def EE_CognitivStartSamplingNeutral(self, userid):
        return self.EmotivEngineDLL.EE_CognitivStartSamplingNeutral(userid)
    
    ## Stop Sampling Cognitiv Neutral
    #
    # Stop the sampling of Neutral state in Cognitiv.
    # @param userid int, User ID
    # @return #ERRCODE
    # @sa EpocHandler::EE_CognitivStartSamplingNeutral()
    def EE_CognitivStopSamplingNeutral(self, userid):
        return self.EmotivEngineDLL.EE_CognitivStopSamplingNeutral(userid)
    
    ## Set Cognitiv Signature Caching
    #
    # Enable or disable signature caching in Cognitiv (1 enable/0 disable)
    # @param userid int, User ID
    # @param enable int, 1/0
    # @return #ERRCODE
    # @sa EpocHandler::EE_CognitivGetSignatureCaching()
    def EE_CognitivSetSignatureCaching(self, userid, enable):
        return self.EmotivEngineDLL.EE_CognitivSetSignatureCaching(userid, enable)
    
    ## Get Cognitiv Signature Caching
    #
    # Get the status of signature caching in Cognitiv
    # @param userid int, User ID
    # @return (#ERRCODE, int flag)
    # @sa EpocHandler::EE_CognitivSetSignatureCaching()
    def EE_CognitivGetSignatureCaching(self, userid):
        flag = ctypes.c_int()
        code = self.EmotivEngineDLL.EE_CognitivGetSignatureCaching(userid, ctypes.byref(flag))
        returnflag = flag.value
        del flag
        return (code, returnflag)
    
    ## Set Cognitiv Signature Cache Size
    #
    # Set the cache size for the signature caching in Cognitiv
    # @param userid int, User ID
    # @param size int, number of signatures to keep in cache (0 = unlimited)
    # @return #ERRCODE
    # @sa EpocHandler::EE_CognitivGetSignatureCacheSize()
    def EE_CognitivSetSignatureCacheSize(self, userid, size):
        return self.EmotivEngineDLL.EE_CognitivSetSignatureCacheSize(userid, size)
    
    ## Get Cognitiv Signature Cache Size
    #
    # Get the current cache size for the signature caching in Cognitiv (0 = unlimited)
    # @param userid int, User ID
    # @return (#ERRCODE, int size)
    # @sa EpocHandler::EE_CognitivSetSignatureCacheSize()
    def EE_CognitivGetSignatureCacheSize(self, userid):
        sizeout = ctypes.c_int()
        code = self.EmotivEngineDLL.EE_CognitivGetSignatureCacheSize(userid, ctypes.byref(sizeout))
        returnsize = sizeout.value
        del sizeout
        return (code, returnsize)
    
    ## Get Headset Sensor Details
    #
    # Returns a struct containing details about the specified EEG channel's headset.
    # @param channelid int, #INPUTCHANNELS
    # @return ( #ERRCODE, InputSensorDescriptor )
    # @sa http://docs.python.org/library/ctypes.html#structured-data-types
    def EE_HeadsetGetSensorDetails(self, channelid):
        inputsensordescriptor = InputSensorDescriptor()
        code = self.EmotivEngineDLL.EE_HeadsetGetSensorDetails(channelid, ctypes.byref(inputsensordescriptor))
        return (code, inputsensordescriptor)
    
    ## Get Emotiv hardware versions.
    #
    # This returns the Emotiv hardware version numbers (as hex)
    # @param userid int, user ID
    # @return (#ERRCODE, (headsetversion,dongleversion))
    # @todo Get rid if the "invalid literal for int() with base 10" error that occurs when trying to int() the versions.
    def EE_HardwareGetVersion(self, userid):
        versionout = ctypes.c_ulong()
        code = self.EmotivEngineDLL.EE_HardwareGetVersion(userid, ctypes.byref(versionout))
        version = hex(versionout.value)
        # Get hibyte and lowbyte version numbers
        version = str(version).replace("0x", "0").strip("L")
        versionheadset = list(version[:4])
        versiondongle = list(version[4:])
        versionheadset.insert(1, "x")
        versiondongle.insert(1, "x")
        versionheadset = "".join(versionheadset)
        versiondongle = "".join(versiondongle)        
        return (code, (hex(int(versionheadset, 16)), hex(int(versiondongle, 16))))
    
    ## Get Software Version
    #
    # Returns the current version of the Emotiv SDK software. X.X.X.X
    # @return (#ERRCODE, version, buildnr)
    def EE_SoftwareGetVersion(self):
        versionout = ctypes.create_string_buffer(16)
        versionchars = ctypes.sizeof(versionout)
        buildnrout = ctypes.c_ulong()
        code = self.EmotivEngineDLL.EE_SoftwareGetVersion(ctypes.byref(versionout), versionchars, ctypes.byref(buildnrout))
        returnversion = versionout.value
        returnbuildnr = buildnrout.value
        del versionout, buildnrout
        return (code, returnversion, returnbuildnr)
    
    ## Get Headset Gyro Delta
    #
    # Returns the delta of the movement of the gyro since the previous call for a particular user.
    # @param userid int, User ID
    # @return (#ERRCODE, (xpos, ypos))
    # @sa EpocHandler::EE_HeadsetGyroRezero()
    def EE_HeadsetGetGyroDelta(self, userid):
        xposout = ctypes.c_int()
        yposout = ctypes.c_int()
        code = self.EmotivEngineDLL.EE_HeadsetGetGyroDelta(userid, ctypes.byref(xposout), ctypes.byref(yposout))
        returnxpos = xposout.value
        returnypos = yposout.value
        del xposout , yposout
        return (code, (returnxpos, returnypos))
    
    ## Rezero Headset Gyro
    #
    # Re-zero the gyro for a particular user.
    # @param userid int, User ID
    # @return #ERRCODE
    # @sa EpocHandler::EE_HeadsetGetGyroDelta() 
    def EE_HeadsetGyroRezero(self, userid):
        code = self.EmotivEngineDLL.EE_HeadsetGyroRezero(userid)
        return code
    
    ## Create Optimization Parameter Handle
    #
    # Creates a handle to memory that can hold an optimization parameter which is used to configure the behaviour of optimization.
    # @return optparam handle, Optimization parameter handle
    # @sa EpocHandler::EE_OptimizationParamFree()
    def EE_OptimizationParamCreate(self):
        return self.EmotivEngineDLL.EE_OptimizationParamCreate()
    
    ## Free Optimization Parameter Handle
    #
    # Frees memory referenced by an optimization parameter handle.
    # @param optparamhandle handle, Handle created by EpocHandler::EE_OptimizationParamCreate()
    def EE_OptimizationParamFree(self, optimizationparamhandle):
        self.EmotivEngineDLL.EE_OptimizationParamFree(optimizationparamhandle)
    
    ## Enable Optimization
    #
    # Enable optimization. EmoEngine will try to optimize its performance according to the information
    # passed in with optimization parameter. EmoEngine guarantees the correctness of the results of vital
    # algorithms. For algorithms that are not vital, results are undefined.
    # @param optparamhandle handle, Handle created by EpocHandler::EE_OptimizationParamCreate()
    # @return #ERRCODE
    def EE_OptimizationEnable(self, optimizationparamhandle):
        code = self.EmotivEngineDLL.EE_OptimizationEnable(optimizationparamhandle)
        return code
    
    ## Is Optimization Enabled
    #
    # Determine whether optimization is on or not.
    # @return (#ERRCODE , enabled)
    # @todo check that it can become True
    def EE_OptimizationIsEnabled(self):        
        enabledout = ctypes.c_bool()
        code = self.EmotivEngineDLL.EE_OptimizationIsEnabled(ctypes.byref(enabledout))
        returnenabled = enabledout.value
        del enabledout
        return (code, returnenabled)
    
    ## Disable Optimization
    #
    # Disable optimization.
    # @return #ERRCODE
    def EE_OptimizationDisable(self):
        return self.EmotivEngineDLL.EE_OptimizationDisable()
    
    ## Get Optimization Parameter
    #
    # Get optimization parameter. If optimization is not enabled (this can be checked with\n
    # EpocHandler::EE_OptimmizationIsEnabled()) then the results attached to the hParam parameter are undefined.
    # @param optparamhandle handle, Handle returned by EpocHandler::EE_OptimizationParamCreate()
    # @return #ERRCODE
    def EE_OptimizationGetParam(self, optimizationparamhandle):
        return self.EmotivEngineDLL.EE_OptimizationGetParam(optimizationparamhandle)
    
    ## Get Vital Optimization Algorithm
    #
    # Get a list of vital algorithms of specific suite from optimization parameter\n
    # Returns #ERRCODE and a list of vital algorithm composed of #EXPRESSIVALGO,\n
    # #AFFECTIVALGO or #COGACTION depending on the suite parameter.
    # @return (#ERRCODE, algbitvector)
    # @todo make sure it works!!
    def EE_OptimizationGetVitalAlgorithm(self, optimizationparamhandle, suite):        
        alghorithbitvectorout = ctypes.c_uint()
        code = self.EmotivEngineDLL.EE_OptimizationGetVitalAlgorithm(optimizationparamhandle, suite, ctypes.byref(alghorithbitvectorout))
        returnalgbitvector = alghorithbitvectorout.value
        del alghorithbitvectorout
        return (code, returnalgbitvector)
    
    ## Set Vital Optimization Algorithm
    #
    # Set a list of vital algorithms of specific suite to optimization parameter.
    # @param param optparamhandle handle, Handle returned by EpocHandler::EE_OptimizationParamCreate()
    # @param suite int, #SUITE
    # @param algbitvector bitvector, a list of vital algorithm composed of #EXPRESSIVALGO, #AFFECTIVALGO or #COGACTION depending on the suite parameter passed in.
    # @return #ERRCODE
    # @todo make sure it works!!
    def EE_OptimizationSetVitalAlgorithm(self, optimizationparamhandle, suite, algbitvector):        
        code = self.EmotivEngineDLL.EE_OptimizationSetVitalAlgorithm(optimizationparamhandle, suite, algbitvector)
        return code
    
    ## Reset Detection
    #
    # Resets all settings and user-specific profile data for the specified detection suite.
    # @param userid int, User ID
    # @param suite int, #SUITE
    # @param detectionbivector bitvector, identifies specific detections. Set to zero for all detections.
    # @return #ERRCODE
    # @todo make sure it works!!
    def EE_ResetDetection(self, userid, suite, detectionbitvector):
        code = self.EmotivEngineDLL.EE_ResetDetection(userid, suite, detectionbitvector)
        return code
    
    ##################################[ EmoState ]########################################
    # EmoStates are generated by the Emotiv detection engine (EmoEngine) and
    # represent the emotional status of the user at a given time.
    # EmoStateHandle is an opaque reference to an internal EmoState structure
    # None of the EmoState interface functions are thread-safe.
    ######################################################################################
    
    ## Get Time From Start
    #
    # Return the time since EmoEngine has been successfully connected to the headset.
    # If the headset is disconnected from EmoEngine due to low battery or weak wireless signal,\n
    # the time will be reset to zero.
    # @param  emostatehandle
    # @return float seconds
    # @sa EpocHandler::EE_EmoStateCreate()
    # @bug It will start returning "nan"
    def ES_GetTimeFromStart(self, emostatehandle):
        return self.EmotivEngineDLL.ES_GetTimeFromStart(emostatehandle)
    
    ## Get Headset On/Off
    #
    # Return whether the headset has been put on correctly or not. If the headset cannot not be
    # detected on the head, then signal quality will not report any results for all the channels
    # @param emostatehandle
    # @return 1/0 (on or off)
    # @sa EpocHandler::EE_EmoStateCreate()
    def ES_GetHeadsetOn(self, emostatehandle):
        return self.EmotivEngineDLL.ES_GetHeadsetOn(emostatehandle)
    
    ## Get Number Of Channels With Contact Quality Data
    #
    # Get the number of channels with available sensor contact quality data.
    # @param emostatehandle 
    # @return int, number of channels with contact quality data available.
    # @sa EpocHandler::EE_EmoStateCreate()
    def ES_GetNumContactQualityChannels(self, emostatehandle):
        return self.EmotivEngineDLL.ES_GetNumContactQualityChannels(emostatehandle)
    
    ## Get Contact Quality
    #
    # Get the contact quality of a specific sensor.
    # @param emostatehandle
    # @param sensorid int, id of the sensor to check
    # @return #CONTACTQUALITY
    def ES_GetContactQuality(self, emostatehandle, sensorid):
        return self.EmotivEngineDLL.ES_GetContactQuality(emostatehandle, sensorid)
    
    ## Get Contact Quality From All Channels
    #
    # Query the contact quality of all the electrodes in one single call.
    # @note The contact quality will be stored in the array, contactQuality, passed to the function. The value stored in contactQuality[0] is identical to the result returned by ES_GetContactQuality(state, 0) The value stored in contactQuality[1] is identical to the result returned by ES_GetContactQuality(state, 1). etc. The ordering of the array is consistent with the ordering of the logical input channels in PyEpoc::INPUTCHANNELS .
    # @todo Make it work!
    def ES_GetContactQualityFromAllChannels(self, emostatehandle):
        pass
    
    ## Expression Blinking
    #
    # Query whether the user is blinking at the time the EmoState is captured.
    # @param emostatehandle
    # @return 1/0 (blink/no blink)
    # @sa EpocHandler::ES_ExpressivIsLeftWink() , EpocHandler::ES_ExpressivIsRightWink() , EpocHandler::ES_ExpressivIsEyesOpen()
    def ES_ExpressivIsBlink(self, emostatehandle):
        return self.EmotivEngineDLL.ES_ExpressivIsBlink(emostatehandle)
    
    ## Expression Left Winking
    #
    # Query whether the user is winking left at the time the EmoState is captured.
    # @param emostatehandle
    # @return 1/0 (left wink/no left wink)
    # @sa EpocHandler::ES_ExpressivIsRightWink() , EpocHandler::ES_ExpressivIsEyesOpen() , EpocHandler::ES_ExpressivIsBlink()
    def ES_ExpressivIsLeftWink(self, emostatehandle):
        return self.EmotivEngineDLL.ES_ExpressivIsLeftWink(emostatehandle)
    
    ## Expression Right Winking
    #
    # Query whether the user is winking right at the time the EmoState is captured.
    # @param emostatehandle
    # @return 1/0 (right wink/no right wink)
    # @sa EpocHandler::ES_ExpressivIsLeftWink() , EpocHandler::ES_ExpressivIsBlink() , EpocHandler::ES_ExpressivIsEyesOpen()
    def ES_ExpressivIsRightWink(self, emostatehandle):        
        return self.EmotivEngineDLL.ES_ExpressivIsRightWink(emostatehandle)
    
    ## Expression Eyes Open
    #
    # Query whether the eyes of the user are opened at the time the EmoState is captured.
    # @param emostatehandle
    # @return 1/0 (eyes open/closed)
    # @sa EpocHandler::ES_ExpressivIsRightWink() , EpocHandler::ES_ExpressivIsLeftWink() , EpocHandler::ES_ExpressivIsBlink()
    def ES_ExpressivIsEyesOpen(self, emostatehandle):
        return self.EmotivEngineDLL.ES_ExpressivIsEyesOpen(emostatehandle)
    
    ## Expression Looking Up
    #
    # Query whether the user is looking up at the time the EmoState is captured. 
    # @param emostatehandle
    # @return 1/0 (looking up/not looking up)
    # @sa EpocHandler::ES_ExpressivIsRightWink() , EpocHandler::ES_ExpressivIsLeftWink() , EpocHandler::ES_ExpressivIsBlink() , EpocHandler::ES_ExpressivIsEyesOpen()
    def ES_ExpressivIsLookingUp(self, emostatehandle):
        return self.EmotivEngineDLL.ES_ExpressivIsLookingUp(emostatehandle)
    
    ## Expression Looking Down
    #
    # Query whether the user is looking down at the time the EmoState is captured.
    # @param emostatehandle
    # @return 1/0 (looking down/not looking down)
    # @sa EpocHandler::ES_ExpressivIsRightWink() , EpocHandler::ES_ExpressivIsLeftWink() , EpocHandler::ES_ExpressivIsBlink() , EpocHandler::ES_ExpressivIsEyesOpen() , EpocHandler::ES_ExpressivIsLookingUp()
    def ES_ExpressivIsLookingDown(self, emostatehandle):
        return self.EmotivEngineDLL.ES_ExpressivIsLookingDown(emostatehandle)
    
    ## Expression Looking Left
    #
    # Query whether the user is looking left at the time the EmoState is captured.
    # @param emostatehandle
    # @return 1/0 (looking left/not looking left)
    # @sa EpocHandler::ES_ExpressivIsRightWink() , EpocHandler::ES_ExpressivIsLeftWink() , EpocHandler::ES_ExpressivIsBlink() , EpocHandler::ES_ExpressivIsEyesOpen() , EpocHandler::ES_ExpressivIsLookingUp() , EpocHandler::ES_ExpressivIsLookingDown()
    def ES_ExpressivIsLookingLeft(self, emostatehandle):
        return self.EmotivEngineDLL.ES_ExpressivIsLookingLeft(emostatehandle)
    
    ## Expression Looking Right
    #
    # Query whether the user is looking right at the time the EmoState is captured.
    # @param emostatehandle
    # @return 1/0 (looking right/not looking right)
    # @sa EpocHandler::ES_ExpressivIsRightWink() , EpocHandler::ES_ExpressivIsLeftWink() , EpocHandler::ES_ExpressivIsBlink() , EpocHandler::ES_ExpressivIsEyesOpen() , EpocHandler::ES_ExpressivIsLookingUp() , EpocHandler::ES_ExpressivIsLookingDown() , EpocHandler::ES_ExpressivIsLookingLeft()
    def ES_ExpressivIsLookingRight(self, emostatehandle):
        return self.EmotivEngineDLL.ES_ExpressivIsLookingRight(emostatehandle)
    
    ## Get Eyelid State
    #
    # Query the eyelids state of the user.
    # @note The left and right eyelid state are stored in the parameter leftEye and rightEye respectively. They are floating point values ranging from 0.0 to 1.0. 0.0 indicates that the eyelid is fully opened while 1.0 indicates that the eyelid is fully closed.
    # @param emostatehandle
    # @return (float lefteye , float righteye)
    # @sa EpocHandler::ES_ExpressivIsRightWink() , EpocHandler::ES_ExpressivIsLeftWink() , EpocHandler::ES_ExpressivIsBlink() , EpocHandler::ES_ExpressivIsEyesOpen() , EpocHandler::ES_ExpressivIsLookingUp() , EpocHandler::ES_ExpressivIsLookingDown() , EpocHandler::ES_ExpressivIsLookingLeft() , Epochandler:: ES_ExpressivIsLookingRight()
    def ES_ExpressivGetEyelidState(self, emostatehandle):
        lefteye = ctypes.c_float()
        righteye = ctypes.c_float()
        self.EmotivEngineDLL.ES_ExpressivGetEyelidState(emostatehandle, ctypes.byref(lefteye), ctypes.byref(righteye))
        lefteyereturn , righteyereturn = lefteye.value , righteye.value
        del lefteye, righteye
        return (lefteyereturn, righteyereturn)
    
    ## Get Eye Location
    #
    # Query the eyes position of the user.
    # The horizontal and vertical position of the eyes are stored in the parameter x and y respectively. They are floating point values ranging from -1.0 to 1.0.
    # For horizontal position, -1.0 indicates that the user is looking left while 1.0 indicates that the user is looking right.
    # For vertical position, -1.0 indicates that the user is looking down while 1.0 indicatest that the user is looking up.
    # @note This function assumes that both eyes have the same horizontal or vertical positions. (i.e. no crossed eyes)
    # @param emostatehandle
    # @return (float x , float y) - (horizontal position / vertical position)
    # @sa EpocHandler::ES_ExpressivIsRightWink() , EpocHandler::ES_ExpressivIsLeftWink() , EpocHandler::ES_ExpressivIsBlink() , EpocHandler::ES_ExpressivIsEyesOpen() , EpocHandler::ES_ExpressivIsLookingUp() , EpocHandler::ES_ExpressivIsLookingDown() , EpocHandler::ES_ExpressivIsLookingLeft() , Epochandler:: ES_ExpressivIsLookingRight() , EpocHandler::ES_ExpressivGetEyelidState()
    def ES_ExpressivGetEyeLocation(self, emostatehandle):
        x = ctypes.c_float()
        y = ctypes.c_float()
        self.EmotivEngineDLL.ES_ExpressivGetEyeLocation(emostatehandle, ctypes.byref(x), ctypes.byref(y))
        xreturn , yreturn = x.value , y.value
        del x, y
        return (xreturn, yreturn)
    
    ## Get Eyebrow Extent
    #
    # Returns the eyebrow extent of the user (Obsolete function).
    # @param emostatehandle
    # @return extent float, eyebrow extent value (0.0 to 1.0)  
    # @sa EpocHandler::ES_ExpressivGetUpperFaceAction(), EpocHandler::ES_ExpressivGetUpperFaceActionPower()
    def ES_ExpressivGetEyebrowExtent(self,emostatehandle):
        return self.EmotivEngineDLL.ES_ExpressivGetEyebrowExtent(emostatehandle)
    
    ## Get Smile Extent
    #
    # Returns the smile extent of the user (Obsolete function).
    # @param emostatehandle
    # @return extent float, smile extent value (0.0 to 1.0)
    # @sa EpocHandler::ES_ExpressivGetUpperFaceAction(), EpocHandler::ES_ExpressivGetUpperFaceActionPower()
    def ES_ExpressivGetSmileExtent(self,emostatehandle):
        return self.EmotivEngineDLL(emostatehandle)
    
    ## Get Clench Extent
    #
    # Returns the clench extent of the user (obsolete)
    # @param emostatehandle
    # @return extent float, clench extent value (0.0 to 1.0)
    # @sa EpocHandler::ES_ExpressivGetUpperFaceAction(), EpocHandler::ES_ExpressivGetUpperFaceActionPower()
    def ES_ExpressivGetClenchExtent(self, emostatehandle):
        return self.EmotivEngineDLL.ES_ExpressivGetClenchExtent(emostatehandle)

    ## Get Upper Face Action
    #
    # Returns the detected upper face Expressiv action of the user.
    # @param emostatehandle
    # @return #EXPRESSIVALGO
    # @sa EpocHandler::ES_ExpressivGetUpperFaceActionPower()
    def ES_ExpressivGetUpperFaceAction(self, emostatehandle):
        return self.EmotivEngineDLL.ES_ExpressivGetUpperFaceAction(emostatehandle)
    
    ## Get Upper Face Action Power
    #
    # Return the power of the upper face action of the user.
    # @param emostatehandle
    # @return power float, power of the action (0.0 to 1.0)
    # @sa EpocHandler::ES_ExpressivGetUpperFaceAction()
    def ES_ExpressivGetUpperFaceActionPower(self, emostatehandle):
        return self.EmotivEngineDLL.ES_ExpressivGetUpperFaceActionPower(emostatehandle)
    
    ## Get Lower Face Action
    #
    # Returns the detected lower face Expressiv action of the user.
    # @param emostatehandle
    # @return #EXPRESSIVALGO
    # @sa EpocHandler::ES_ExpressivGetLowerFaceActionPower() , EpocHandler::ES_ExpressivGetUpperFaceAction()
    def ES_ExpressivGetLowerFaceAction(self, emostatehandle):
        return self.EmotivEngineDLL.ES_ExpressivGetLowerFaceAction(emostatehandle)
    
    ## Get Lower Face Action Power
    #
    # Returns the detected lower face Expressiv action power of the user.
    # @param emostatehandle
    # @return power float, action power (0.0 to 1.0)
    # @sa EpocHandler::ES_ExpressivGetLowerFaceAction()
    def ES_ExpressivGetLowerFaceActionPower(self, emostatehandle):
        return self.EmotivEngineDLL.ES_ExpressivGetLowerFaceActionPower(emostatehandle)
    
    ## Is Expressiv Active
    #
    # Query whether the signal is too noisy for Expressiv detection to be active.
    # @param emostatehandle
    # @param #EXPRESSIVALGO , expression type
    # @return 1/0, (active / not active)
    def ES_ExpressivIsActive(self, emostatehandle, type):
        return self.EmotivEngineDLL.ES_ExpressivIsActive(emostatehandle, type)
    
    ## Get Long Term Affectiv Excitement Score
    #
    # Returns the long term excitement level of the user.
    # @param emostatehandle
    # @return score float, (0.0 to 1.0)
    # @sa EpocHandler::ES_AffectivGetExcitementShortTermScore()
    def ES_AffectivGetExcitementLongTermScore(self, emostatehandle):
        return self.EmotivEngineDLL.ES_AffectivGetExcitementLongTermScore(emostatehandle)
    
    ## Get Short Term Affectiv Excitement Score
    #
    # Returns the short term excitement level of the user.
    # @param emostatehandle
    # @return score float, (0.0 to 1.0)
    # @sa EpocHandler::ES_AffectivGetExcitementLongTermScore()
    def ES_AffectivGetExcitementShortTermScore(self, emostatehandle):
        score = ctypes.c_float
        score.value = self.EmotivEngineDLL.ES_AffectivGetExcitementShortTermScore(emostatehandle)
        return score.value
    
    ## Is Affectiv Active
    #
    # Query whether the signal is too noisy for Affectiv detection to be active.
    # @param emostatehandle
    # @param #AFFECTIVALGO , affectiv type
    # @return 1/0, (active / not active)
    def ES_AffectivIsActive(self, emostatehandle, type):
        return self.EmotivEngineDLL.ES_AffectivIsActive(emostatehandle, type)
    
    ## Get Affectiv Meditation Score
    #
    # Return the meditation score of the user.
    # @param emostatehandle
    # @return score float, (0.0 to 1.0)
    def ES_AffectivGetMeditationScore(self, emostatehandle):
        return self.EmotivEngineDLL.ES_AffectivGetMeditationScore(emostatehandle)
    
    ## Get Affectiv Frustration Score
    #
    # Return the frustration score of the user.
    # @param emostatehandle
    # @return score float, (0.0 to 1.0) 
    def ES_AffectivGetFrustrationScore(self,emostatehandle):
        return self.EmotivEngineDLL.ES_AffectivGetFrustrationScore(emostatehandle)
    
    ## Get Affectiv Engagement/Boredom Score
    #
    # Return the engangement/boredom score of the user.
    # @param emostatehandle
    # @return score float, (0.0 to 1.0) 
    def ES_AffectivGetEngagementBoredomScore(self, emostatehandle):
        return self.EmotivEngineDLL.ES_AffectivGetEngagementBoredomScore(emostatehandle)
    
    ## Get Current Cognitiv Action
    #
    # Returns the detected Cognitiv action of the user.
    # @param emostatehandle
    # @return type , #COGACTION
    # @sa EpocHandler::ES_CognitivGetCurrentActionPower()
    def ES_CognitivGetCurrentAction(self, emostatehandle):
        return self.EmotivEngineDLL.ES_CognitivGetCurrentAction(emostatehandle)
    
    ## Get Current Cognitiv Action Power
    #
    # Returns the detected action power of the user.
    # @param emostatehandle
    # @return value float, (0.0 to 1.0)
    # @sa EpocHandler::ES_CognitivGetCurrentAction()
    def ES_CognitivGetCurrentActionPower(self, emostatehandle):
        return self.EmotivEngineDLL.ES_CognitivGetCurrentActionPower(emostatehandle)
    
    ## Is Cognitiv Active
    #
    # Query whether the signal is too noisy for Cognitiv detection to be active.
    # @param emostatehandle 
    # @param 1/0 , (active / not active) 
    def ES_CognitivIsActive(self, emostatehandle):
        return self.EmotivEngineDLL.ES_CognitivIsActive(emostatehandle)
    
    ## Get Wireless Signal Status
    #
    # Get the current wireless signal strength.
    # @param emostatehandle
    # @return signalstrength, #SIGNALSTRENGTH
    def ES_GetWirelessSignalStatus(self, emostatehandle):
        return self.EmotivEngineDLL.ES_GetWirelessSignalStatus(emostatehandle)
    
    ## Clone EmoStateHandle
    #
    # Copy srcemostatehandle to destemostatehandle
    # @param destemostatehandle handle , Destination EmoState handle
    # @param srcemostatehandle handle , Source EmoState handle
    # @sa EpocHandler::EE_EmoStateCreate()
    def ES_Copy(self, destemostatehandle, srcemostatehandle): 
        self.EmotivEngineDLL.ES_Copy(destemostatehandle, srcemostatehandle)
        return
    
    ## Is Affectiv EmoStates Equal
    #
    # Check whether handle A are identical with B 'emotiv' state.
    # @param emostatehandle, Emostate handle A
    # @param emostatehandle, Emostate handle B
    # @return 1/0 , (equal / no equal)
    # @sa EpocHandler::ES_ExpressivEqual(), EpocHandler::ES_CognitivEqual(), EpocHandler::ES_EmoEngineEqual(), EpocHandler::ES_Equal() 
    def ES_AffectivEqual(self, handlea, handleb):
        return self.EmotivEngineDLL.ES_AffectivEqual(handlea, handleb)
    
    ## Is Expressiv EmoStates Equal
    #
    # Check whether two states are with identical Expressiv state, i.e. are both state representing the same facial expression.
    # @param emostatehandle, Emostate handle A
    # @param emostatehandle, Emostate handle B
    # @return 1/0 , (equal / no equal)
    # @sa EpocHandler::ES_AffectivEqual(), EpocHandler::ES_CognitivEqual(), EpocHandler::ES_EmoEngineEqual(), EpocHandler::ES_Equal() 
    def ES_ExpressivEqual(self, handlea, handleb):
        return self.EmotivEngineDLL.ES_ExpressivEqual(handlea, handleb)
    
    ## Is Cognitiv EmoStates Equal
    #
    # Check whether two states are with identical Cognitiv state.
    # @param emostatehandle, Emostate handle A
    # @param emostatehandle, Emostate handle B
    # @return 1/0 , (equal / no equal)
    # @sa EpocHandler::ES_AffectivEqual(), EpocHandler::ES_ExpressivEqual(), EpocHandler::ES_EmoEngineEqual(), EpocHandler::ES_Equal() 
    def ES_CognitivEqual(self, handlea, handleb):
        return self.EmotivEngineDLL.ES_CognitivEqual(handlea, handleb)
    
    ## Is EmoEngine States Equal
    #
    # Check whether two states are with identical EmoEngine state.
    # This function is comparing the time since EmoEngine start, the wireless signal strength and the signal quality of different channels.
    # \param emostatehandle, Emostate handle A
    # \param emostatehandle, Emostate handle B
    # \return 1/0 , (equal / no equal)
    # \sa EpocHandler::ES_AffectivEqual(), EpocHandler::ES_ExpressivEqual(), EpocHandler::ES_CognitivEqual(), EpocHandler::ES_Equal() 
    def ES_EmoEngineEqual(self, handlea, handleb):
        return self.EmotivEngineDLL.ES_EmoEngineEqual(handlea, handleb)
    
    ## Is EmoStateHandles Identical
    #
    # Check whether two EmoStateHandles are identical.
    # \param emostatehandle, Emostate handle A
    # \param emostatehandle, Emostate handle B
    # \return 1/0 , (equal / no equal)
    # \sa EpocHandler::ES_AffectivEqual(), EpocHandler::ES_ExpressivEqual(), EpocHandler::ES_EmoEngineEqual()
    def ES_Equal(self, handlea, handleb):
        return self.EmotivEngineDLL.ES_Equal(handlea, handleb)
    
    ## Get Battery Charge Level
    #
    # Get the level of charge remaining in the headset battery.
    # \param emostatehandle 
    # \return (chargelevel, maxchargelevel) - (the current level of charge in the headset battery / the maximum level of charge in the battery)
    def ES_GetBatteryChargeLevel(self,emostatehandle):
        chrglvl     = ctypes.c_int()
        maxchrglvl  = ctypes.c_int()
        self.EmotivEngineDLL.ES_GetBatteryChargeLevel(emostatehandle,ctypes.byref(chrglvl),ctypes.byref(maxchrglvl))
        returnchrglvl, returnmaxlvl = chrglvl.value , maxchrglvl.value
        return (returnchrglvl, returnmaxlvl)
    
    ## Initialize Emo State
    #
    # Initialize the EmoState into neutral state.
    # \param emostatehandle
    def ES_Init(self,emostatehandle):
        self.EmotivEngineDLL.ES_Init(emostatehandle)