# Define o modelo de canal a ser utilizado
import numpy as np
def scatteringchnmtx(rays, tx_array, num_tx, rx_array, num_rx):
    """
    Estima o canal ataves atraves do modelo geometrico narrowband utilizando os dados de ray-tracing, utilizando angulo de elevacao e azimute. Retorna a matriz de canal.
    """
    h = np.zeros(num_tx * num_rx).reshape(num_rx, num_tx)
    
    for n in range(len(rays)):
        departure_omega_x = 2 * np.pi * tx_array.element_spacing * np.sin(rays[n].departure_theta) * np.cos(rays[n].departure_phi)
        departure_omega_y = 2 * np.pi * tx_array.element_spacing * np.sin(rays[n].departure_theta) * np.sin(rays[n].departure_phi)

        arrival_omega_x = 2 * np.pi * rx_array.element_spacing * np.sin(rays[n].arrival_theta) * np.cos(rays[n].arrival_phi)
        arrival_omega_y = 2 * np.pi * rx_array.element_spacing * np.sin(rays[n].arrival_theta) * np.sin(rays[n].arrival_phi)
        
        factor_departure = (1/np.sqrt(num_tx)) 
        factor_arrival = (1/np.sqrt(num_rx)) 
        factor = (np.sqrt(num_rx * num_tx)) * rays[n].received_power
        
        #departure
        departure_vec = np.zeros((1, num_tx)) 
        for m in range(len(tx_array.ura)):
            vecx = np.exp(1j * departure_omega_x * np.arange(len(tx_array.ura[m,:])))
            vecy = np.exp(1j * departure_omega_y * np.arange(len(tx_array.ura[:,m])))
            departure_vec = factor_departure *np.matrix(np.kron(vecy, vecx)) 

        #arrival
        arrival_vec = np.zeros((1, num_rx)) 
        for m in range(len(rx_array.ura)):
            vecx = np.exp(1j * arrival_omega_x * np.arange(len(rx_array.ura[m,:])))
            vecy = np.exp(1j * arrival_omega_y * np.arange(len(rx_array.ura[:,m])))
            arrival_vec = factor_arrival * np.matrix(np.kron(vecy, vecx))
      
        h = h + factor * (arrival_vec.conj().T * departure_vec) 

    return h.T
