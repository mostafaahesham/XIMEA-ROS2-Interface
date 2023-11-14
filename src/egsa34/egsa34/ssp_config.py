import json
import os

class SSPConfig:
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

        # Indices Configuration
        # This section defines the indices for different fields in SSP frames.
        _cfg.idxSTART_FLAG = ssp_config["indicies"]["start_flag"]
        _cfg.idxEND_FLAG = ssp_config["indicies"]["end_flag"]
        _cfg.idxDEST_ADDR = ssp_config["indicies"]["dest_addr"]
        _cfg.idxSRC_ADDR = ssp_config["indicies"]["src_addr"]
        _cfg.idxCMD_ID = ssp_config["indicies"]["cmd_id"]
        _cfg.idxDATA_LEN = ssp_config["indicies"]["data_len"]
        _cfg.idxDATA_START = ssp_config["indicies"]["data_start"]
        _cfg.idxCRC_0 = ssp_config["indicies"]["crc_0"]
        _cfg.idxCRC_1 = ssp_config["indicies"]["crc_1"]

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
        
        # Payload Commands
        _cfg.cmdRCS = ssp_config["commands"]["payload_commands"]["RCS"]
        _cfg.cmdGIMG = ssp_config["commands"]["payload_commands"]["GIMG"]
        _cfg.cmdTIMG = ssp_config["commands"]["payload_commands"]["TIMG"]
        _cfg.cmdDIMG = ssp_config["commands"]["payload_commands"]["DIMG"]
        _cfg.cmdCXT = ssp_config["commands"]["payload_commands"]["CXT"]
        
        _cfg.rplyACK = ssp_config["replies"]["generic_replies"]["ACK"]
        _cfg.rplyNACK = ssp_config["replies"]["generic_replies"]["NACK"]
        
        
        # SSP Errors (sspERR_CODE)
        _cfg.errNONE = ssp_config["ssp_errors"]["no_err"]
        _cfg.errCRC = ssp_config["ssp_errors"]["crc_err"]
        _cfg.errPARAMS = ssp_config["ssp_errors"]["params_err"]
        _cfg.errCMD = ssp_config["ssp_errors"]["cmd_err"]
        _cfg.errOTHER = ssp_config["ssp_errors"]["other_err"]
        
        # System Errors (sysERR_CODE)
        _cfg.errNONE = ssp_config["sys_errors"]["no_err"]
        _cfg.errFRAME = ssp_config["sys_errors"]["frame_err"]
        _cfg.errDEST = ssp_config["sys_errors"]["dest_err"]
        _cfg.errPORT0 = ssp_config["sys_errors"]["port0_error"]
        _cfg.errPORT1 = ssp_config["sys_errors"]["port1_error"]
        _cfg.errTX = ssp_config["sys_errors"]["transmit_error"]
        _cfg.errRX = ssp_config["sys_errors"]["recieve_error"]