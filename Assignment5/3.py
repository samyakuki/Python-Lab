seq=[1,2,3,4,5,7,11,9]
min_value=min(seq)
max_value=max(seq)
full_range=set(range(min_value,max_value+1))
seq_set=set(seq)
missing_Set=full_range-seq_set
print(sorted(missing_Set))