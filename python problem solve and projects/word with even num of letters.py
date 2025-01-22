st='print every word in this sentence that has an even number of letters'
a=st.split()
for i in a:
    if len(i)%2==0:
        print(f'even {i}')
