try:
    def mapper(param):  
        import pandas as pd
        df=pd.read_csv("MAPPER/MAPPING.csv")

        CHECK_POINTS=df['CHECK_POINTS']
        X=df['X']
        Y=df['Y']
        CHECK_POINTS_LIST=CHECK_POINTS.tolist()
        X_LIST=X.tolist()
        Y_LIST=Y.tolist()

        if(param in CHECK_POINTS_LIST):
            indexer=CHECK_POINTS_LIST.index(param)
            
            X_DATA=X_LIST[indexer]
            Y_DATA=Y_LIST[indexer]

            return(X_DATA,Y_DATA)

except:
    print("[ERROR in mapper")

