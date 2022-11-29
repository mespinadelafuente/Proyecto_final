def importe_total_carro(request):
    total=0
    if request.user.is_authenticated:
        for keys, value in request.session['carro'].items():
            total=total+(float(value["precio"]))
    else:
        total="Debes logearte para conocer el total"
    
    return {"importe_total_carro":total}

