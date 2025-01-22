with open('output1.txt', 'w') as output:
    with open('input1.txt', 'r') as input:
        lines=input.read().splitlines()
        assignments=int(lines[0])
        lines=lines[1:]
        main_array=[]        
        for i in lines:
            temp=i.split()
            temp=list(map(int, temp))
            main_array.append(temp)

        main_array.sort(key=lambda x: x[1])
        result=[]
        count=0        
        start_index=0
        end_index=1        
        result.append(main_array[0])
        count=count+1
        end_time=result[0][end_index]       
        main_array=main_array[1:]        
        for _, j in enumerate(main_array):
            if j[start_index]>=end_time:
                result.append(j)
                count=count+1
                end_time=j[1]
                
        output.write(str(count)+"\n")        
        last_result=result.pop()
        for i in result:
            output.write(str(i[0])+" "+str(i[1])+"\n")            
        output.write(str(last_result[0])+" "+str(last_result[1]))