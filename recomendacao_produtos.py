# Suponha que você tenha um DataFrame "df" que representa as vendas.
# Substitua "df" pelo nome real do seu DataFrame.

# Substitua 'cliente_id' pelo ID do cliente desejado
cliente_id = 1
historico_cliente = df[df['ClienteID'] == cliente_id]
produtos_comprados = historico_cliente['Produto'].unique()

# Recomendação de produtos com base nos produtos comprados pelo cliente
produtos_recomendados = df[~df['Produto'].isin(produtos_comprados)]
produtos_recomendados = produtos_recomendados.groupby('Produto')['Total Vendas'].sum().reset_index()
produtos_recomendados = produtos_recomendados.sort_values(by='Total Vendas', ascending=False)
