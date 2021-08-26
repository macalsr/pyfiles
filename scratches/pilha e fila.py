from collections import deque
pilha = deque(['A', 'E', 'I', 'O'])
print(pilha) # Saída: ['A', 'E', 'I', 'O']
pilha.append('U') # Adicionar no topo da lista
print(pilha) # Saída: ['A', 'E', 'I', 'O', 'U']
pilha.pop() # Remover 'U' do topo da lista
pilha.pop() # Remover 'O' do topo da lista
pilha.pop() # Remover 'I' do topo da lista
pilha.pop() # Remover 'E' do topo da lista
pilha.pop() # Remover 'A' do topo da lista
pilha.pop()

fila = []
print(fila) # Saída: []
fila.append('1') # Adicionar no fim da fila
fila.append('2') # Adicionar no fim da fila
fila.append('3') # Adicionar no fim da fila
fila.append('4') # Adicionar no fim da fila
fila.append('5') # Adicionar no fim da fila
print(fila) # Saída: ['1', '2', '3', '4', '5']
fila.pop(0) # Remover '1' do início da fila
fila.pop(0) # Remover '2' do início da fila
fila.pop(0) # Remover '3' do início da fila
fila.pop(0) # Remover '4' do início da fila
fila.pop(0) # Remover '5' do início da fila
fila.pop()

from collections import deque
fila = deque()
print(fila) # Saída: []
fila.append('1') # Adicionar no fim da fila
fila.append('2') # Adicionar no fim da fila
fila.append('3') # Adicionar no fim da fila
fila.append('4') # Adicionar no fim da fila
fila.append('5') # Adicionar no fim da fila
print(fila) # Saída: ['1', '2', '3', '4', '5']
fila.popleft() # Remover '1' do início da fila
fila.popleft() # Remover '2' do início da fila
fila.popleft() # Remover '3' do início da fila
fila.popleft() # Remover '4' do início da fila
fila.popleft() # Remover '5' do início da fila
fila.popleft()