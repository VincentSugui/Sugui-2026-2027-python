1. create app 'clients'
2. clients model: user,
                attributes
                avatar: image field   default path
3. user/avatar/'
- birth_date: datefield
- gender: charfield

4. handle user serializers.py with create and update method to has the password
5. handle user views.py using the standards
        A. POST  Get(ALL)
        B. GET (Retrive)  PATCH DELETE

6. expose the API in urls.py with our said standard

7. test all exposed API's
