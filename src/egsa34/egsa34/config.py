import json
import os

class Config:
    def __init__(_cfg):

        # Load configuration data from 'ssp_config.json' file and set class attributes based on the data.
        file = open(f'{os.getcwd()}/src/egsa34/config/ssp_config.json')
        ssp_config = json.load(file)

        # Configuration related to SSP (Simple Serial Protocol)
        # This section defines various configuration parameters for SSP.
        _cfg.FLAG = ssp_config["flag"]
        _cfg.maxFrame_SIZE = ssp_config["max_frame_size"]
        _cfg.maxDATA_SIZE = ssp_config["max_data_size"]
        
        # Configuration related to SSP Frame Types (Simple Serial Protocol)
        # This section defines various Frame & Frame fields types for SSP.
        _cfg.typeDIRECT_CMD = ssp_config["frame_types"]["type_direct_cmd"]
        _cfg.typeTT_CMD = ssp_config["frame_types"]["type_time_tagged_cmd"]
        _cfg.typeCMD_FRAME = ssp_config["frame_types"]["type_cmd_frame"]
        _cfg.typeREPLY_FRAME = ssp_config["frame_types"]["type_reply_frame"]

        # SSP Frame Indices Configuration
        # This section defines the indices for different fields in SSP frames.
        _cfg.idxSTART_FLAG = ssp_config["ssp_indicies"]["start_flag"]
        _cfg.idxEND_FLAG = ssp_config["ssp_indicies"]["end_flag"]
        _cfg.idxDEST_ADDR = ssp_config["ssp_indicies"]["dest_addr"]
        _cfg.idxSRC_ADDR = ssp_config["ssp_indicies"]["src_addr"]
        _cfg.idxCMD_ID = ssp_config["ssp_indicies"]["cmd_id"]
        _cfg.idxDATA_LEN = ssp_config["ssp_indicies"]["data_len"]
        _cfg.idxDATA_START = ssp_config["ssp_indicies"]["data_start"]
        _cfg.idxCRC_0 = ssp_config["ssp_indicies"]["crc_0"]
        _cfg.idxCRC_1 = ssp_config["ssp_indicies"]["crc_1"]
        
        # Payload Frame Indices Configuration
        # This section defines the indices for different fields in Payload frames.
        _cfg.idxCAM_ID = ssp_config["payload_indicies"]["cam_id"]
        _cfg.idxTIME_ON = ssp_config["payload_indicies"]["time_on"]
        _cfg.idxTIME_SNAP = ssp_config["payload_indicies"]["time_snap"]
        _cfg.idxTIME_OFF = ssp_config["payload_indicies"]["time_off"]
        _cfg.idxFPS = ssp_config["payload_indicies"]["fps"]
        _cfg.idxEXP_TIME = ssp_config["payload_indicies"]["exp_time"]
        _cfg.idxGAIN = ssp_config["payload_indicies"]["gain"]
        _cfg.idxCOMPRESSION = ssp_config["payload_indicies"]["compression"]
        
        # Subsystems Configuration
        # This section defines subsystem identifiers for SSP.
        _cfg.addrOBC = ssp_config["addresses"]["subsystems_addr"]["OBC"]
        _cfg.addrEPS = ssp_config["addresses"]["subsystems_addr"]["EPS"]
        _cfg.addrCCU = ssp_config["addresses"]["subsystems_addr"]["CCU"]
        _cfg.addrADCS = ssp_config["addresses"]["subsystems_addr"]["ADCS"]
        _cfg.addrPL = ssp_config["addresses"]["subsystems_addr"]["PL"]

        # Modules Configuration
        # This section defines module identifiers for SSP.
        _cfg.addrUHF_1 = ssp_config["addresses"]["modules_addr"]["UHF_1"]
        _cfg.addrUHF_2 = ssp_config["addresses"]["modules_addr"]["UHF_2"]
        _cfg.addrXIMEA_PAN = ssp_config["addresses"]["modules_addr"]["XIMEA_PAN"]
        _cfg.addrXIMEA_LS = ssp_config["addresses"]["modules_addr"]["XIMEA_LS"]
        _cfg.addrXIMEA_SS = ssp_config["addresses"]["modules_addr"]["XIMEA_SS"]
        _cfg.addrXBAND = ssp_config["addresses"]["modules_addr"]["XBAND"]
        _cfg.addrRPI = ssp_config["addresses"]["modules_addr"]["RPI"]

        # GCSS (Ground Control Stations) Configuration
        # This section defines configuration related to GCSS.
        _cfg.addrGCS = ssp_config["addresses"]["gcss_addr"]["GCS"]

        # Multicast Configuration
        # This section defines multicast and broadcast identifiers.
        _cfg.addrMULTICAST = ssp_config["addresses"]["multicast_addr"]["multicast"]
        _cfg.addrBROADCAST = ssp_config["addresses"]["multicast_addr"]["broadcast"]
        
        # Generic Commands
        _cfg.cmdPING = ssp_config["commands"]["generic_commands"]["PING"]
        _cfg.cmdWD = ssp_config["commands"]["generic_commands"]["WD"]
        _cfg.cmdSM = ssp_config["commands"]["generic_commands"]["SM"]
        _cfg.cmdGM = ssp_config["commands"]["generic_commands"]["GM"]
        _cfg.cmdGSC = ssp_config["commands"]["generic_commands"]["GSC"]
        _cfg.cmdSSC = ssp_config["commands"]["generic_commands"]["SSC"]
        
        # Payload Commands
        _cfg.cmdRCS = ssp_config["commands"]["payload_commands"]["RCS"]
        _cfg.cmdGIMG = ssp_config["commands"]["payload_commands"]["GIMG"]
        _cfg.cmdTIMG = ssp_config["commands"]["payload_commands"]["TIMG"]
        _cfg.cmdDIMG = ssp_config["commands"]["payload_commands"]["DIMG"]
        _cfg.cmdCXT = ssp_config["commands"]["payload_commands"]["CXT"]
        
        # Replies
        _cfg.rplyACK = ssp_config["replies"]["generic_replies"]["ACK"]
        _cfg.rplyNACK = ssp_config["replies"]["generic_replies"]["NACK"]
        
        # SAT Modes
        _cfg.modeINIT = ssp_config["modes"]["INIT"]
        _cfg.modeDTMBL = ssp_config["modes"]["DTMBL"]
        _cfg.modeNORM = ssp_config["modes"]["NORM"]
        _cfg.modeCOMM = ssp_config["modes"]["COMM"]
        _cfg.modePL = ssp_config["modes"]["PL"]
        _cfg.modeDWNLD = ssp_config["modes"]["DWNLD"]
        _cfg.modeSAFE = ssp_config["modes"]["SAFE"]
        _cfg.modeEMRGNC = ssp_config["modes"]["EMRGNC"]
        _cfg.modeMMCST = ssp_config["modes"]["MMCST"]
        
        # Errors (errCODE)
        _cfg.errNONE = ssp_config["errors"]["no_err"]
        _cfg.errCRC = ssp_config["errors"]["crc_err"]
        _cfg.errPARAMS = ssp_config["errors"]["params_err"]
        _cfg.errCMD = ssp_config["errors"]["cmd_err"]
        _cfg.errOTHER = ssp_config["errors"]["other_err"]
        _cfg.errFRAME = ssp_config["errors"]["frame_err"]
        _cfg.errDEST = ssp_config["errors"]["dest_err"]
        _cfg.errPORT0 = ssp_config["errors"]["port0_error"]
        _cfg.errPORT1 = ssp_config["errors"]["port1_error"]
        _cfg.errTX = ssp_config["errors"]["transmit_error"]
        _cfg.errRX = ssp_config["errors"]["recieve_error"]
        
        _cfg.satMODEs = list(ssp_config["modes"].values())
        _cfg.sysERRs = list(ssp_config["sys_errors"].values())