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
            "0":"NO_ERR",
            "1":"CRC_ERR",
            "2":"PARAMS_ERR",
            "3":"DEST_ERR",
            "4":"CMD_ERR",
            "5":"OTHER_ERR"
        }
        
        _ssp.FRAME =   [_ssp.FLAG,
                        0, # placeholder:dest_addr
                        0, # placeholder:src_addr
                        0, # placeholder:cmd_id
                        0, # placeholer:data_length
                    ]
        
        _ssp.allowed_DEST = [_ssp.addrRPI]
        _ssp.allowed_CMDS = [_ssp.cmdPING]
        
    def get_member_variables(self):
        attributes = [attr for attr in dir(self) if not callable(getattr(self, attr)) and not attr.startswith("__")]
        for attr in attributes:
            value = getattr(self, attr)
            print(f"{attr}: {value}")
            
    def calc_crc(_crc,data):

        crc = crc16.mcrf4xx(bytes(data),0xFFFF).to_bytes(2,"big")
        return crc[0], crc[1] 
    
    def check_frame(_chk,frame):
        data_len = frame[_chk.idxDATA_LEN]
        crc_0 , crc_1 = _chk.calc_crc(frame[_chk.idxDEST_ADDR:_chk.idxCRC_0])
        
        try:
            assert frame[_chk.idxSTART_FLAG] == 0xC0 and frame[_chk.idxEND_FLAG] == 0xC0, _chk.errOTHER
            assert frame[_chk.idxCRC_0] == crc_0 and frame[_chk.idxCRC_1] == crc_1, _chk.errCRC
            assert frame[_chk.idxDEST_ADDR] in _chk.allowed_DEST, _chk.errDEST
            assert frame[_chk.idxCMD_ID] in _chk.allowed_CMDS, _chk.errCMD
            
            _chk.errCODE = 0
            
            return
            
        except AssertionError as e:
            _chk.errCODE = e.args[0]
            return

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
    
            _dpkt.check_frame(frame)
            data_len = frame[_dpkt.idxDATA_LEN]
            return {
                # "flag_s":frame[_dpkt.idxSTART_FLAG],
                "dest":frame[_dpkt.idxDEST_ADDR],
                "src":frame[_dpkt.idxSRC_ADDR],
                "cmd":frame[_dpkt.idxCMD_ID],
                "data_len":frame[_dpkt.idxDATA_LEN],
                "data":frame[_dpkt.idxDATA_START:_dpkt.idxDATA_START + data_len],
                "crc_0":frame[_dpkt.idxCRC_0],
                "crc_1":frame[_dpkt.idxCRC_1],
                # "flag_e":frame[_dpkt.idxEND_FLAG],
            }