import requests


#def build_book():

#       titulo = input("Digite el titulo del libro: ")
#       descripccion = input("Digite la descripccion del libro": )
#       autor = input ("Digite el autor del libro:" )
#       book = {
#               'title':titulo, 'description':descripccion, 'author':autor
#       }
#       return book

def getall_request():
        url ='http://192.168.60.3:5000/books'
        response = requests.get(url)

        if response.status_code == 200:
                response_json = response.json()
                print(response_json)

def get_request():
        url ='http://192.168.60.3:5000/books/2'
        response = requests.get(url)

        if response.status_code == 200:
                response_json = response.json()
                print(response_json)

def post_request():
        url = 'http://192.168.60.3:5000/books'
        payload = {'title':'Historia de dos ciudades', 'description':'situada en la revolucion francesa', 'author':'Charles Dickens'}
        headers = {'Content-Type': 'application/json'}

        #json post se encarga de serializar los datos
        response = requests.post (url, json=payload, headers=headers)

        if response.status_code ==200:
                print(response.content)

def put_request():
        url = 'http://192.168.60.3:5000/books/4'
        payload = {'title':'Bueno', 'description':'Buenisimo', 'author':'niidea'}
        headers = {'Content-Type': 'application/json'}
        #json post se encarga de serializar los datos       
        response = requests.put (url, json=payload, headers=headers)

        if response.status_code ==200:
                print(response.content)

def delete_request():
        url = 'http://192.168.60.3:5000/books/4'
        #json post se encarga de serializar los datos
        response = requests.delete (url)

        if response.status_code ==200:
                print(response.content)

def main():

        metodo= int(input("Digite el metodo que desea realizar GETALL(1),GET(2),POST(3),PUT(4) OR DELETE(5): "))
        if metodo == 1:
                getall_request()
        else:
                if metodo == 2:
                        get_request()
                else:
                        if metodo == 3:
                                #book = build_book()
                                #post_request(book)
                                post_request()
                        else:
                                if metodo == 4:
                                        put_request()
                                else:
                                        if metodo == 5:
                                                delete_request()



if __name__ == '__main__':
         main()