# Define os arrays de antenas
import numpy as np

#class PartitionedArray:
class PartitionedArray:
    """
    Define a arquitetura de antenas tanto transmissoras quanto receptoras.
    """
    def __init__(self, size, element_spacing, num_rf, wave_length):
        """
        size: quantidade de elementos de recepcao ou transmissao.
        element_spacing: corresponde a distancia entre elementos na antena, deve ser menor que lambda/2
        wave_length: comprimento de onda, lambda = c/fc
        """

        #Uniform Regular Array (URA). Define regularmente a posicao de cada elemento do array.
        self.ura = np.ones((int(np.sqrt(size)), int(np.sqrt(size))))

        #Atribuicao do element_spacing
        self.element_spacing = element_spacing
        
        #Elementos do subarray. Na arquitetura de beamforming hibrido, cada elemento do array possui um conjunto de subarrays. Equivale a dizer que cada elemento possui um setup de elementos de RF.
        self.subarray_selection = np.ones((size, num_rf))
        
        #Atribuicao do comprimento de onda
        self.wave_length = wave_length


