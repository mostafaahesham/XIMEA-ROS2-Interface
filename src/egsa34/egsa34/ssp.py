import os
import sys

from fastcrc import crc16

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from ssp_config import SSPConfig

class SSP(SSPConfig):
    def __init__(_ssp):
        SSPConfig.__init__(_ssp)
        
        _ssp.errCODE = 0
        
        _ssp.errors = {
            "0":"NO_ERR_SSP",
            "1":"CRC_ERR_SSP",
            "2":"PARAMS_ERR_SSP",
            "3":"CMD_ERR_SSP",
            "4":"OTHER_ERR_SSP",
            "5":"DEST_ERR_RPI",
            "6":"FRAME_ERR_RPI"
        }
        
        # dict for checking datalengths' of associated commands
        # key: cmd_id, value: data_length
        _ssp.params_check = {
            str(_ssp.cmdPING):0,
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
                            _ssp.cmdRCS,
                            _ssp.cmdGIMG,
                            _ssp.cmdTIMG,
                            _ssp.cmdDIMG,
                            _ssp.cmdCXT
                        ]
        
    def get_member_variables(self):
        attributes = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
        for attr in attributes:
            value = getattr(self, attr)
            print(f"{attr}: {value}")
            
    def calc_crc(_crc,data):

        crc = crc16.mcrf4xx(bytes(data),0xFFFF).to_bytes(2,"little")
        return crc[0], crc[1] 
    
    def analyze_frame(_chk,frame):
        data_len = frame[_chk.idxDATA_LEN]
        crc_0 , crc_1 = _chk.calc_crc(frame[_chk.idxDEST_ADDR:_chk.idxCRC_0])
        
        try:
            assert frame[_chk.idxSTART_FLAG] == 0xC0 and frame[_chk.idxEND_FLAG] == 0xC0, _chk.errFRAME
            assert frame[_chk.idxCRC_0] == crc_0 and frame[_chk.idxCRC_1] == crc_1, _chk.errCRC
            assert frame[_chk.idxDEST_ADDR] in _chk.allowed_DEST, _chk.errDEST
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
    
        if _dpkt.analyze_frame(frame) == _dpkt.errDEST:
                return {
                "status":_dpkt.errors[str(_dpkt.errCODE)]
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