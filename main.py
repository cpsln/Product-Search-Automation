from app import app

# import allcategory
import categoryData
import filterData


if __name__ == '__main__':
    
    app.secret_key = 'some secret key'
    app.debug = True
    # app.run(port=5001)
    
    app.run(host='0.0.0.0', port=5001)