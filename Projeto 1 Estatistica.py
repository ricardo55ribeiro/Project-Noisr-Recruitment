#Projeto 1 Estatística
import matplotlib.pyplot as plt

def read_txt_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read().replace('\n', '')
        return data.strip()
    except FileNotFoundError:
        return "File not found."

def convert_to_string(data):
    lines = data.split('\n')
    binary_string = ''.join(lines)
    return binary_string

teste = read_txt_file("seq1.txt")

def plot_histogram(int_list):
    plt.hist(int_list, bins=max(int_list)-min(int_list)+1, \
             align='left', edgecolor='black')
    plt.xlabel('Integers')
    plt.ylabel('Frequency')
    plt.title('Histogram of Integers')
    plt.grid(True)
    plt.show()


int_list = []
for i in range(0, len(teste), 6):
    grupo_de_seis = teste[i:i+6]
    binario_para_inteiro = int(grupo_de_seis, 2)
    int_list.append(binario_para_inteiro)

plot_histogram(int_list)

# O enviesamento é que em cada grupo de seis bits, estão
# três 0 e três 1, o que não é característico de um número
# aleatório. Por esta razão, o número mínimo possível a cada
# seis bits é o 000111, que é o 7, como vemos no gráfico.