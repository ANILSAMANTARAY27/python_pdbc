import mysql.connector

def get_all_product():
    cnx = mysql.connector.connect(user='root', password='a@#np',
                                  host='localhost',
                                  database='grocery_store')
    cursor = cnx.cursor()

    query=("SELECT * FROM grocery_store.uom;")

    cursor.execute(query)
    response=[]

    for(uom_ids,uom_name) in cursor:
        response.append({'uom_id':uom_ids,
                         'uom_name':uom_name})
    cnx.close()
    return response
if __name__=="__main__":
    print(get_all_product())

