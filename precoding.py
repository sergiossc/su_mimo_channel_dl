# Define os metodos de precoding/combining
from numpy.linalg import inv
from numpy.linalg import svd
import numpy as np

def opt_precoding(h, tx_array, rx_array, num_tx_rf, num_rx_rf, num_stream, snr):
    """
    Obtem as matrizes de precoding/combining considerando a informacao de canal CSI existente na matriz h. Esta abordagem considera a existencia de CSI tanto no transmissor(CSIT), quanto no receptor(CSIR). Na pratica, no entanto, as caracteristiacas de mmWave ainda nao tornam possivel a obtencao da coerencia de canal entre transmissor e receptor, principalmente em modelos de sistema dinamicos.
    """

    # Realiza a decomposicao em valores singulares do canal para obter as matrizes de precoding/combining.
    u, s, vh = svd(h, full_matrices=True)
    #f_opt corresponde a matriz de precoding otima no transmissor.
    f_opt = u[:,num_stream]
    #w_opt: corresponde a matriz de combining otima no receptor. Utiliza o metodo de combiner mmse.
    w_opt = (inv((f_opt.conj().T * h.conj() * h.T * f_opt) + (snr * np.eye(num_stream)))) * f_opt.conj().T * h.conj() #combiner mmse
     
    return f_opt, w_opt

def spatially_sparse_precoding(h, tx_array, rx_array, num_tx_rf, num_rx_rf, num_stream, snr):
    f_hybrid = 0
    w_hybrid = 0

    return f_hybrid, w_hybrid


