def caracter_function(args):
    Input = namedtuple('Input', ['requested', 'received', 'duration'])

    tentativa=0
    bem_sucedido = 0

    start_time = time() 

    while True:

        tempo_atual = time()
        tempo_decorrido = int(tempo_atual - start_time )

        if tempo_decorrido >= args.max_value:
            break  

        random_ascii = random.randint(97,122)
        random_caracter = chr(random_ascii)

        print(f"Digite: {random_caracter} : ") 
        ti = time()

        key = readkey()

        tf = time()
        duration = tf-ti
        input_ascii = ord(key)

        if input_ascii == 32:

            break

        elif key == random_caracter:
            print(Fore.GREEN + f"Correto" + Fore.WHITE + ", voce inseriu! " + Fore.GREEN + f"{key}" + Fore.WHITE)
            bem_sucedido += 1
        else:
            print(Fore.RED+"Incorreto" + Fore.WHITE + ". Tente novamente.")

        tentativa +=1
        input_record = Input( requested = random_caracter, received = key, duration = duration)    

    print(f"\nEm {tentativa} tentativas voce acertou em: {bem_sucedido}, em {tempo_decorrido} segundos.") 

    print(input_record.requested)  
    print(input_record.received)   
    print(input_record.duration)  