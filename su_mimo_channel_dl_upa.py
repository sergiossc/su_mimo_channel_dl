"""
SU-MIMO DL Channel Model

O modelo de canal geometrico, NLOS com multipath, considera a existencia de uma BS @60GHz com Nt antenas transmissoras e um usuario Nr antenas receptoras. Considera-se ainda o modelo
de bandas estreitas (narrowband). 

"""
import numpy as np
from scipy.constants import c
from read_data import read_data
from phased import PartitionedArray
from channel import scatteringchnmtx
from precoding import opt_precoding, spatially_sparse_precoding



if __name__ == "__main__":
    print("MIMO UPA DL Model 3D")
   
    num_tx = 25  # numero de antenas no transmissor
    num_tx_rf = 4 # numero de cadeias de rf no transmissor
   
    num_rx = 16 # numero de antenas no receptor
    num_rx_rf = 4 # numero de cadeias de rf no receptor
   
    num_stream = 1

    fc = 60*(10**9) 
    wave_length = c/fc
    element_spacing = wave_length/2
    print("*****element_spacing: ", element_spacing)

    tx_array = PartitionedArray(num_tx, element_spacing, num_tx_rf, wave_length)
    rx_array = PartitionedArray(num_rx, element_spacing, num_rx_rf, wave_length)

    # Obtem os dados entre o transmissor e o receptor 1 (dentre os 10 existentes no banco de dados).
    rays = read_data(1)

    # Estima o canal
    h = scatteringchnmtx(rays, tx_array, num_tx, rx_array, num_rx)
    print(h.shape)
    
    snr = np.arange(-40,5,5)
    #se_opt: Spectral Efficiency Optimal
    #se_hybrid: Spectral Efficiency Hybrid
    f_opt, w_opt = opt_precoding(h, tx_array, rx_array, num_tx_rf, num_rx_rf, num_stream, snr[0])
    f_hybrid, w_hybrid = spatially_sparse_precoding(h, tx_array, rx_array, num_tx_rf, num_rx_rf, num_stream, snr[0])
