from fastapi import FastAPI, Path, HTTPException, status
import scraper 
import time
import validators
from mangum import Mangum
import uvicorn


app = FastAPI()
handler = Mangum(app)



@app.get("/")
def home():
    return {
        "author": "Shine Barbhuiya",
        "status" : "active",
        "description" : "Unofficial Walmart API written in Python using FastAPI. Search for products, get product details and more! Read the docs for all the API endpoints"
    }




@app.get("/product")
def get_product_details(url: str):

    # Check if the url is an valid url
    if not validators.url(url):
        
        return {
            'error' : 'Invalid url!',
        }
    
    if "https://www.walmart.com" not in url:
        return {
            'message' : 'Paste valid walmart address',
            'status' : 'error'
        }
    

    start_time = time.time()
    prod_details = scraper.product_details(url)

    
    


    print(prod_details['status'])
    if prod_details['status'] != 'success':
        return {
            'message' : 'Sorry, there was some kind of error! Please try again.',
            'status' : 'error',
            'reason' : prod_details['status'],
            
        }
    

    return {
        'author' : 'Shine Barbhuiya',
        'execution_time' : time.time() - start_time,
        'status' : 'success',
        'product_details' : prod_details,    
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    


     
     