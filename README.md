# Stock Market Api

## Stack:
- FastAPI
- MongoDB + Beanie (ODM)


## Features
* 

## TODO:
- [X] Calculation balance by account
- [X] Calculation total cost of all shares by account
- [X] Calculation profitability by formula  TODO: fix this
- [ ] Autorization support, getting info of autorizated user "GET /getme"
- [ ] buy shares and write transactions "POST /buy?account_id={}&"


## Screenshots
Endpoints:
WARNING: The schema may be out of date!

[![image.png](https://i.postimg.cc/P5NwFJN2/image.png)]


## How to use
1. Rename ".env example" to ".env" 
2. Create mongodb database instance on localhost
2. Run main.py




## Response examples
Get Account information by ID
```
{
  "full_name": "Alexey Petrov",
  "email": "a.valny@gg.com",
  "hashed_password": "hashed_password",
  "registration_date": "2010-09-23",
  "balance": 235.60000000000036              # Free money to buy shares
  "deposited_usd": 3000,
  "share_list": [
    {
      "_id": "BABA",
      "count": 5,
      "avg_price": 113.1,
      "total": 565.5
    },
    {
      "_id": "TAL",
      "count": 230,
      "avg_price": 4.3,
      "total": 989
    },
    {
      "_id": "TSLA",
      "count": 10,
      "avg_price": 120.99,
      "total": 1209.8999999999999
    }
  ],
  "profitability": 7.853333333333346
}
```

