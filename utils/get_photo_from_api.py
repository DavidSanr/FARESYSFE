


def savePic(_tipo_documento,_cedula,bith):
    tipo_documento = _tipo_documento;
    cedula = _cedula
    url = os.environ.get('URL_SIC')
    print(url)   
    response = http.request('GET',url)
    jeyjey = json.loads(response.data.decode('utf-8'))
    pic = jeyjey["UrlFoto"] 
    #downloadImages(url,jeyjey["Numero"]+'.png')
    if(response.status == 200): 
       r = http.request('GET',pic)
       while(r.data == b'Not Found'):
           response = http.request('GET',url)
           jeyjey = json.loads(response.data.decode('utf-8'))
           pic = jeyjey["UrlFoto"]
           r = http.request('GET',pic)
            
       downloadImages(r.data,jeyjey['Numero'],bith)
       