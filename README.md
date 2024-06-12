# Sistema de Pedido de Pastéis

Este é um script em Python que simula um sistema de pedidos de pastéis sem interface gráfica. Ele solicita ao usuário informações básicas de cadastro, 
exibe um cardápio de pastéis com diferentes sabores e preços, e permite que o usuário selecione e adicione itens ao seu carrinho. 
Ao final, o usuário pode confirmar o pedido ou remover itens antes da confirmação final.

## Funcionalidades

- **Cadastro do Cliente**: Solicita nome e endereço do cliente.
- **Exibição de Cardápio**: Mostra uma imagem do cardápio com os diferentes sabores e preços dos pastéis.
- **Adição de Itens ao Carrinho**: Permite que o usuário selecione sabores e quantidades de pastéis para adicionar ao carrinho.
- **Confirmação do Pedido**: O usuário pode confirmar o pedido ou remover itens do carrinho antes da confirmação final.
- **Remoção de Itens do Carrinho**: Caso o usuário não confirme o pedido inicialmente, ele pode remover itens do carrinho.

## Como Usar

1. **Instale as Dependências**:
   Certifique-se de ter a biblioteca `Pillow` instalada para manipulação de imagens:
   ```bash
   pip install Pillow
