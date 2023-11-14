import os
import sys

from fastcrc import crc16

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from ssp_config import SSPConfig

class SSP(SSPConfig):
    def __init__(_ssp):
        SSPConfig.__init__(_ssp)
        
        _ssp.sspERR_CODE = 0
        _ssp.sysERR_CODE = 0
        
        _ssp.ssp_errors = {
            "0":"SSP_NO_ERR",
            "1":"SSP_CRC_ERR",
            "2":"SSP_PARAMS_ERR",
            "3":"SSP_CMD_ERR",
            "4":"SSP_OTHER_ERR"
        }
        
        _ssp.sys_errors = {
            "0":"SSP_NO_ERR",
            "255":"SYS_FRAME_ERR_",
            "254":"SYS_DEST_ERR",
            "253":"SYS_PORT0_ERR",
            "252":"SYS_PORT1_ERR",
            "251":"SYS_TX_ERR",
            "250":"SYS_RX_ERR"
        }
        
        # dict for checking datalengths' of associated commands
        # key: cmd_id, value: data_length
        _ssp.params_check = {
            str(_ssp.cmdPING):0,
            str(_ssp.cmdGIMG):1,
            str(_ssp.cmdTEST):248
        }
        
        _ssp.FRAME =   [_ssp.FLAG,
                        0, # placeholder:dest_addr
                        0, # placeholder:src_addr
                        0, # placeholder:cmd_id
                        0, # placeholer:data_length
                    ]
        
        _ssp.allowed_DEST = [_ssp.addrRPI]
        _ssp.allowed_CMDS = [
                            _ssp.cmdTEST,
                            _ssp.cmdPING,
                            _ssp.cmdRCS,
                            _ssp.cmdGIMG,
                            _ssp.cmdTIMG,
                            _ssp.cmdDIMG,
                            _ssp.cmdCXT
                        ]
            
    def calc_crc(_crc,data):

        crc = crc16.mcrf4xx(bytes(data),0xFFFF).to_bytes(2,"little")
        return crc[0], crc[1] 
    
    def analyze_frame(_chk,frame,type='c'):
        try:
            crc_0 , crc_1 = _chk.calc_crc(frame[_chk.idxDEST_ADDR:_chk.idxCRC_0])
        
            assert frame[_chk.idxSTART_FLAG] == 0xC0 and frame[_chk.idxEND_FLAG] == 0xC0, _chk.errFRAME
            assert frame[_chk.idxCRC_0] == crc_0 and frame[_chk.idxCRC_1] == crc_1, _chk.errCRC
            if type == 'c':
                assert frame[_chk.idxDATA_LEN] == _chk.params_check[str(frame[_chk.idxCMD_ID])], _chk.errPARAMS
            else:
                pass
            _chk.sspERR_CODE = 0
            
            return _chk.sspERR_CODE
            
        except AssertionError as e:
            _chk.sspERR_CODE = e.args[0]
            return _chk.sspERR_CODE

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
    
    def depacketize(_dpkt,frame,type='c'):
    
        if _dpkt.analyze_frame(frame,type) != _dpkt.errNONE:
                return {
                "ssp_status":_dpkt.ssp_errors[str(_dpkt.sspERR_CODE)],
                "sys_status":_dpkt.sys_errors[str(_dpkt.sysERR_CODE)],
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