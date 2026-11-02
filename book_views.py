from mysql import connector

class Dbconnect:
    def get_connection(self):
        try:
            self.connection = connector.connect(
                host='localhost',
                user='root',
                password='vishnu@191004',
                database='book_db'
            )
            return self.connection
        except Exception as e:
            return None
class LibraryManager(Dbconnect):
    def get(self):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from book_details"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            #print(records)
            #for data in records:
                #print(data)
            return records



        except Exception as e:
            print(e)
            return[]


    def post(self, **kwargs):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "INSERT INTO book_details( book_name, author_name, price, type, published_year) VALUES (%s, %s, %s, %s, %s)"

            values = [v for v in kwargs.values()]
            self.cursor.execute(query, values)
            self.connect.commit()
            print("New book added successfully...!")
        except Exception as e:
            print(e)

    def get_object(self,id=None):
        try:
            self.cursor = self.connect.cursor()

            query ="select *from book_details where id =%s"
            values=(id,)
            self.cursor.execute(query,values)
            record = self.cursor.fetchone()
            return record
            self.cursor = super().get_connection()

        except Exception as e:
            print(e)

    def retrive(self,id=None):
        try:
            record = self.get_object(id=id)
            if record == None:
                print("Book not found...!")
            print(record)
        except Exception as e:
            print(e)
    def delete(self,id=None):
        try:
            record=self.get_object(id=id)
            values=(id,)

            if record !=None:
                query = "delete from book_details where id =%s"
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Book deleted successfully...!")
            else:
                print("Book not found...!")
        except Exception as e:
            print(e)

    def put(self, id=None, **kwargs):
        try:
            record = self.get_object(id=id)
            if record != None:
                self.cursor = self.connection.cursor()
                placeholder = ""

                for k in kwargs.keys():
                    placeholder += k + "=%s,"
                    placeholder = placeholder.rstrip(",")
                    query = f"update book_details set{placeholder}where id=%s"
                    values = [v for v in kwargs.values()]
                    values.append(id)
                    self.cursor.execute(query, values)
                    self.connection.commit()
                    print("Book Updated Successfully....!")

            else:
                print("Book not found....!")

        except Exception as e:
            print(e)

connection_instance = Dbconnect()
print(connection_instance.get_connection())
book_instance = LibraryManager()
#book_instance.post(book_name="The Shining",author_name="Stephen King",price=450,type="Horror",published_year=1977)

