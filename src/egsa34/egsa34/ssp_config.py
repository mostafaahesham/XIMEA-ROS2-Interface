import json
import os

class SSPConfig:
    def __init__(_cfg):

        # Load configuration data from 'ssp_config.json' file and set class attributes based on the data.
        file = open(f'{os.getcwd()}/src/egsa34/config/ssp_config.json')
        ssp_config = json.load(file)
        
        # _cfg.FRAME =   [_cfg.FLAG,
        #                 0, # placeholder:dest_addr
        #                 0, # placeholder:src_addr
        #                 0, # placeholder:cmd_id
        #                 0, # placeholer:data_length
        #             ]
        
        # # Error Codes dict for logging purposes
        # _cfg.errors = {
        #     "0":"NO_ERR",
        #     "1":"CRC_ERR",
        #     "2":"PARAMS_ERR",
        #     "3":"DEST_ERR",
        #     "4":"CMD_ERR",
        #     "5":"OTHER_ERR"
        # }
        
        # # dict for checking datalengths' of associated commands
        # # key: cmd_id, value: data_length
        # _cfg.params_check = {
        #     str(_cfg.cmdPING):0
        # }
        
        # _cfg.allowed_DEST = [_cfg.addrRPI]
        # _cfg.allowed_CMDS = [_cfg.cmdPING]

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
        
        _cfg.cmdPING = ssp_config["commands"]["generic_commands"]["PING"]
        
        _cfg.rplyACK = ssp_config["replies"]["generic_replies"]["ACK"]
        _cfg.rplyNACK = ssp_config["replies"]["generic_replies"]["NACK"]
        
        _cfg.errCRC = ssp_config["errors"]["crc_err"]
        _cfg.errPARAMS = ssp_config["errors"]["params_err"]
        _cfg.errCMD = ssp_config["errors"]["cmd_err"]
        _cfg.errOTHER = ssp_config["errors"]["other_err"]
        
        # custom errors
        _cfg.errDEST = ssp_config["errors"]["dest_err"]