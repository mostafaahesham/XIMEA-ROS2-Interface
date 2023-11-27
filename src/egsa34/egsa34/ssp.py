import os
import sys

from fastcrc import crc16

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from config import Config

class SSP(Config):
    def __init__(_ssp):
        Config.__init__(_ssp)
        
        _ssp.errCODE = 0
        
        _ssp.errors = {
            "0":"NO_ERR",
            "1":"CRC_ERR",
            "2":"PARAMS_ERR",
            "3":"CMD_ERR",
            "4":"OTHER_ERR",
            "5":"FRAME_ERR",
            "6":"DEST_ERR",
            "7":"PORT0_ERR",
            "8":"PORT1_ERR",
            "9":"TX_ERR",
            "10":"RX_ERR"
        }
        
        # dict for checking datalengths' of associated commands
        # key: cmd_id, value: data_length
        _ssp.params_check = {
            str(_ssp.cmdPING):0,
            str(_ssp.cmdWD):248,
            str(_ssp.cmdSM):1,
            str(_ssp.cmdGM):0,
            str(_ssp.cmdGSC):0,
            str(_ssp.cmdSSC):8,
            str(_ssp.cmdRCS):31,
            str(_ssp.cmdGIMG):1
        }
        
        _ssp.FRAME =   [_ssp.FLAG,
                        0, # placeholder:dest_addr
                        0, # placeholder:src_addr
                        0, # placeholder:cmd_id
                        0, # placeholer:data_length
                    ]
        
        _ssp.allowed_DEST = [_ssp.addrRPI]
        _ssp.allowed_CMDS = [
                            _ssp.cmdPING,
                            _ssp.cmdWD,
                            _ssp.cmdSM,
                            _ssp.cmdGM,
                            _ssp.cmdGSC,
                            _ssp.cmdSSC,
                            _ssp.cmdRCS,
                            _ssp.cmdGIMG,
                            _ssp.cmdTIMG,
                            _ssp.cmdDIMG,
                            _ssp.cmdCXT
                        ]
        
        _ssp.syncCOUNTER = 0
        _ssp.satMODE = 0
            
    def calc_crc(_crc,data):

        crc = crc16.mcrf4xx(bytes(data),0xFFFF).to_bytes(2,"little")
        return crc[0], crc[1] 
    
    def analyze_frame(_chk,frame):
        try:
            crc_0 , crc_1 = _chk.calc_crc(frame[_chk.idxDEST_ADDR:_chk.idxCRC_0])
        
            assert frame[_chk.idxSTART_FLAG] == 0xC0 and frame[_chk.idxEND_FLAG] == 0xC0, _chk.errFRAME
            assert frame[_chk.idxCRC_0] == crc_0 and frame[_chk.idxCRC_1] == crc_1, _chk.errCRC
            assert frame[_chk.idxCMD_ID] in _chk.allowed_CMDS, _chk.errCMD
            assert frame[_chk.idxDATA_LEN] == _chk.params_check[str(frame[_chk.idxCMD_ID])], _chk.errPARAMS
            
            _chk.errCODE = 0
            
            return _chk.errCODE
            
        except AssertionError as e:
            _chk.errCODE = e.args[0]
            return _chk.errCODE

    def packetize(_pkt,dest,src,cmd,data):
        
        _pkt.FRAME =   [_pkt.FLAG,
                        0, # placeholder:dest_addr
                        0, # placeholder:src_addr
                        0, # placeholder:cmd_id
                        0, # placeholer:data_length
                    ]

        _pkt.FRAME[_pkt.idxDEST_ADDR] = dest
        _pkt.FRAME[_pkt.idxSRC_ADDR] = src
        _pkt.FRAME[_pkt.idxCMD_ID] = cmd
        _pkt.FRAME[_pkt.idxDATA_LEN] = len(data)
        _pkt.FRAME[_pkt.idxDATA_START:_pkt.idxDATA_START] = data
        
        crc_0, crc_1 = _pkt.calc_crc(_pkt.FRAME[_pkt.idxDEST_ADDR:])
        
        _pkt.FRAME.extend([crc_0,crc_1,_pkt.FLAG])
        
        return _pkt.FRAME
    
    def depacketize(_dpkt,frame):
    
        if _dpkt.analyze_frame(frame) in _dpkt.sysERRs:
                return {
                "err_status":_dpkt.errors[str(_dpkt.errCODE)],
            }
        else:
            data_len = frame[_dpkt.idxDATA_LEN]
            return {
                "flag_s":frame[_dpkt.idxSTART_FLAG],
                "dest":frame[_dpkt.idxDEST_ADDR],
                "src":frame[_dpkt.idxSRC_ADDR],
                "cmd":frame[_dpkt.idxCMD_ID],
                "data_len":frame[_dpkt.idxDATA_LEN],
                "data":frame[_dpkt.idxDATA_START:_dpkt.idxDATA_START + data_len],
                "crc_0":frame[_dpkt.idxCRC_0],
                "crc_1":frame[_dpkt.idxCRC_1],
                "flag_e":frame[_dpkt.idxEND_FLAG],
            }