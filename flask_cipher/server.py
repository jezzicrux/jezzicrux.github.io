from cipher import app ##FROM THE FOLDER, IMPORT YOUR APP

if __name__ == '__main__': ##RUN THE APP
    app.run(debug = True, host='localhost', port=5555)
    ## FOR DEBUG: debug = True
    ## HOST IS LOCAL HOST, WHICH IS YOUR LOCAL COMPUTER
    ## TO CHOOSE A PORT NUMBER: port= 5555
    #*** HOST AND PORT ARE CASE SENSITIVE
