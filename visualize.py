from d3blocks import D3Blocks


d3 = D3Blocks(verbose='info', chart='tree', frame=False)

df = d3.import_example('energy')

print(df)

#d3.set_node_properties(df)
