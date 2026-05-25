produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]

print(f"{'PRODUTO':<20} | {'2019':<10} | {'2020':<10} | {'CRESCIMENTO'}")
print("-" * 60)

# O enumerate nos dá o índice (i) e o item (produto) ao mesmo tempo
for i, produto in enumerate(produtos):
    venda19 = vendas2019[i]
    venda20 = vendas2020[i]
    
    # Critério: apenas produtos que venderam MAIS em 2020 do que em 2019
    if venda20 > venda19:
        # Cálculo do percentual de crescimento
        crescimento = (venda20 / venda19) - 1
        
        # Exibição formatada:
        # :<20 (alinha à esquerda com 20 espaços)
        # :>10 (alinha à direita com 10 espaços)
        # :.1% (formata como porcentagem com 1 casa decimal)
        print(f"{produto:<20} | {venda19:>10} | {venda20:>10} | {crescimento:,.1%}")