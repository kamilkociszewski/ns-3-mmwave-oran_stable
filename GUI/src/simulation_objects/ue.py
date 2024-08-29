from dataclasses import dataclass
from typing import Optional


@dataclass
class Ue:
    ue_id: int
    x_position: float
    y_position: float
    type: str
    connected_to: int
    ErrTotalNbrDl: Optional[float] = None
    DRB_BufferSize_Qos: Optional[float] = None
    RRU_PrbUsedDl: Optional[float] = None
    DRB_UEThpDlPdcpBased: Optional[float] = None
    DRB_UEThpDl: Optional[float] = None
    QosFlow_PdcpPduVolumeDl: Optional[float] = None
    TotNbrDlInitial: Optional[float] = None
    TotNbrDlInitial_16Qam: Optional[float] = None
    TotNbrDlInitial_64Qam: Optional[float] = None
    TotNbrDlInitial_Qpsk: Optional[float] = None
    TotNbrDl: Optional[float] = None
    PDCP_PDU_Volume: Optional[float] = None
    Cell_PDCP_Latency: Optional[float] = None
    Qos_PDCP_PDU: Optional[float] = None
    PDCP_PDU: Optional[float] = None
    PDCP_Throughput: Optional[float] = None
    Tx_Bytes: Optional[float] = None
    L3servingSINR: Optional[float] = None
    L3servingSINR_CellID: Optional[float] = None
    L3neighSINR: Optional[float] = None
    L3neighSINR_CellId: Optional[float] = None
    DRB_Estab_Succ_5QI: Optional[float] = None
