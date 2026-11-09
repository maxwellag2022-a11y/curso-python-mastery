def configurar(host,port,/, timeout=30, *, debug = False):
    '''
     Host y port: solo posicionales, estos nos e pueden cambiar
    timeout: posicional o nombrado
    debug "solo nombrado despues del *"
    '''

    print(host,port,timeout,debug)

configurar("localhost",8000)
configurar("localhost",8080,timeout=60, debug=True)
